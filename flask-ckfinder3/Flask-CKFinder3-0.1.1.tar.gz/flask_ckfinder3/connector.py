from flask import abort, json, redirect, request, safe_join, send_file, send_from_directory, url_for
from os import listdir, mkdir, rename, stat, unlink, walk
from os.path import dirname, isdir, isfile, join, splitext
from shutil import copyfile, rmtree
from datetime import datetime
from PIL import Image, UnidentifiedImageError
from itertools import count
from tempfile import NamedTemporaryFile
from dataclasses import asdict
import re
import base64
from mimetypes import guess_extension
from .acl import CKFAcl
from .thumbnail import Thumbnail, ThumbnailMapper


def ckf_command(method, acl=None):
    """
    Decorateur pour les commandes CKFConnector

    Recherche la ressource dans l'attribut resource_types de l'instance.
    Passe les paramètres de request resource et currentFolder à la fonction décorée.

    :param method: request.method à contrôler.
    :param acl: optionnel, flags à contrôler sur resource.acl
    """

    def decorator(func):

        def inner(instance):
            if request.method != method:
                abort(405)
            current_folder = request.args.get('currentFolder', None)
            if not current_folder:
                abort(400)
            hash = request.args.get('hash', None)
            if not hash:
                """
                En l'absence de hash, recherche le paramètre type.
                La commande RenameFolder ne fournit pas hash, ce qui pose un problème si 2
                ressources ont le même attribut name.
                Pour prévenir cela, CKFinder lèvera une exception.
                """
                resource_type = request.args.get('type', None)
                if not resource_type:
                    abort(400)
                for res in instance.resource_types.values():
                    if res.name == resource_type:
                        hash = res.hash
                        break
            resource = instance.resource_types.get(hash, None)
            if not resource:
                abort(404)
            if acl and resource.acl & acl != acl:
                abort(403)
            if not isdir(resource.abs_path(current_folder)):
                abort(404)
            return func(instance, resource, current_folder)

        return inner

    return decorator


class CKFConnector():
    """
    Conteneur pour les commandes CKFinder
    """

    #: CKFinder license name
    license_name = ''

    #: CKFinder license key
    license_key = ''

    #: Quick upload directory
    quickupload_dir = None

    #: Quick upload route name
    quickupload_endpoint = None

    #: CKFinder config uploadMaxSize
    uploadmaxsize = 0

    #: CKFinder config uploadCheckImages
    uploadcheckimages = False

    #: Thumbnails sizes
    thumbs = ()

    #: Resize presets
    images_sizes = dict()

    #: Thumbnail cache directory
    thumbnail_dir = None

    #: Thumbnail cache size
    thumbnail_maxfiles = None

    #: Thumbnail gc threshold
    thumbnail_threshold = None

    #: ThumbnailMapper instance
    thumbnail_mapper = None

    def __init__(self, resource_types=None, **kwargs):
        """
        Creates thumbnail_mapper if thumbnail_dir is set.
        """
        self.resource_types = resource_types
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
            else:
                print('CKFConnector : unknown option {!r}'.format(key))
        if self.thumbnail_dir:
            self.thumbnail_mapper = ThumbnailMapper(self.thumbnail_dir, self.thumbnail_maxfiles,
                                                    self.thumbnail_threshold)

    def __call__(self):
        """
        Dispatcher
        """
        command = self.get_arg('command')
        cmd = getattr(self, 'command_{}'.format(command), None)
        if not cmd:
            abort(404)
        return cmd()

    @staticmethod
    def get_arg(name):
        """
        Renvoie la valeur de request.arg['name']
        Échoue avec un statut 400 si name est absent.
        """
        value = request.args.get(name, None)
        if value is None:
            abort(400)
        return value

    @staticmethod
    def get_files():
        """
        Liste de noms de fichiers dans request body
        encodée en json (requiert request.method = POST)
        """
        text = request.form.get('jsonData', None)
        if not text:
            abort(400)
        data = json.loads(text)
        files = data.get('files', None)
        if not files:
            abort(400)
        return files

    def upload(self):
        """
        Quick upload view
        """
        f = request.files.get('upload', None)
        if not f:
            abort(400)
        f.save(safe_join(self.quickupload_dir, f.filename))
        return dict(url=url_for(self.quickupload_endpoint, filename=f.filename), uploaded=True)

    def command_Init(self):
        if request.method != 'GET':
            abort(405)
        ln = ''
        try:
            chars = '123456789ABCDEFGHJKLMNPQRSTUVWXYZ'
            pos = chars.find(self.license_key[2]) % 5
            if pos > -1 and pos % 5 in (1, 2):
                ln = self.license_name
        except IndexError:
            pass
        lc = ''
        try:
            cat = self.license_key.replace('-', '')
            lc = ''.join([cat[x] for x in (1, 8, 17, 22, 3, 13, 11, 20, 5, 24, 27)])
        except IndexError:
            pass
        return dict(s=ln,
                    c=lc,
                    thumbs=self.thumbs,
                    images=dict(sizes=self.images_sizes),
                    uploadMaxSize=self.uploadmaxsize,
                    uploadCheckImages=self.uploadcheckimages,
                    resourceTypes=[asdict(x) for x in self.resource_types.values()])

    @ckf_command('GET')
    def command_GetFolders(self, resource, current_folder):
        ret = dict(resourceType=resource.name, currentFolder=resource.folder(current_folder), folders=list())
        if resource.acl & CKFAcl.FOLDER_VIEW:
            root = resource.abs_path(current_folder)
            _, dirs, _ = next(walk(root))
            for dname in dirs:
                _, subdirs, _ = next(walk(join(root, dname)))
                ret['folders'].append(dict(name=dname, acl=resource.acl, hasChildren=bool(subdirs)))
        return ret

    @ckf_command('GET')
    def command_GetFiles(self, resource, current_folder):
        dname = resource.abs_path(current_folder)
        if not isdir(dname):
            abort(404)
        ret = dict(resourceType=resource.name, currentFolder=resource.folder(current_folder), files=list())
        for fname in listdir(dname):
            absfname = join(dname, fname)
            if isfile(absfname):
                st = stat(absfname)
                ret['files'].append(
                    dict(name=fname,
                         size=int(st.st_size / 102.4) / 10,
                         date=datetime.fromtimestamp(st.st_mtime).strftime('%Y%m%d%H%M')))
        return ret

    @ckf_command('POST', CKFAcl.FILE_CREATE)
    def command_FileUpload(self, resource, current_folder):
        f = request.files.get('upload')
        if not f:
            abort(400)
        absfname = safe_join(resource.abs_path(current_folder), f.filename)
        f.save(absfname)
        return dict(resourceType=resource.name,
                    currentFolder=resource.folder(current_folder),
                    fileName=f.filename,
                    uploaded=1)

    @ckf_command('POST', CKFAcl.FILE_DELETE)
    def command_DeleteFiles(self, resource, current_folder):
        files = self.get_files()
        for num, file in enumerate(files):
            unlink(safe_join(resource.abs_path(current_folder), file['name']))
        return dict(resourceType=resource.name, currentFolder=resource.folder(current_folder), deleted=num + 1)

    @ckf_command('POST', CKFAcl.FOLDER_CREATE)
    def command_CreateFolder(self, resource, current_folder):
        new_folder_name = self.get_arg('newFolderName')
        try:
            mkdir(safe_join(resource.abs_path(current_folder), new_folder_name))
        except FileExistsError:
            return dict(error={'message': 'Directory already exists.'})
        return dict(resourceType=resource.name,
                    currentFolder=resource.folder(current_folder),
                    newFolder=new_folder_name,
                    created=1)

    @ckf_command('POST', CKFAcl.FOLDER_DELETE)
    def command_DeleteFolder(self, resource, current_folder):
        rmtree(resource.abs_path(current_folder))
        return dict(resourceType=resource.name, currentFolder=resource.folder(current_folder), deleted=1)

    @ckf_command('POST', CKFAcl.FOLDER_RENAME)
    def command_RenameFolder(self, resource, current_folder):
        new_folder_name = self.get_arg('newFolderName')
        new_abs_path = resource.abs_path(safe_join(dirname(current_folder.rstrip('/')), new_folder_name))
        rename(resource.abs_path(current_folder), new_abs_path)
        new_path = '/'.join((current_folder.rsplit('/', 1)[0], new_folder_name))
        return dict(resourceType=resource.name,
                    currentFolder=resource.folder(current_folder),
                    newPath=new_path,
                    newName=new_folder_name,
                    renamed=1)

    @ckf_command('POST', CKFAcl.FILE_RENAME)
    def command_RenameFile(self, resource, current_folder):
        file_name = self.get_arg('fileName')
        new_file_name = self.get_arg('newFileName')
        abs_path = resource.abs_path(current_folder)
        rename(safe_join(abs_path, file_name), safe_join(abs_path, new_file_name))
        return dict(resourceType=resource.name,
                    currentFolder=resource.folder(current_folder),
                    name=file_name,
                    newName=new_file_name,
                    renamed=1)

    @ckf_command('GET', CKFAcl.FILE_VIEW)
    def command_ImagePreview(self, resource, current_folder):
        file_name = self.get_arg('fileName')
        return send_from_directory(resource.abs_path(current_folder), file_name)

    @ckf_command('POST', CKFAcl.FILE_CREATE)
    def command_CopyFiles(self, resource, current_folder):
        files = self.get_files()
        cnt = count()
        num = next(cnt)
        for item in files:
            src_res = None
            for res in self.resource_types.values():
                if res.name == item['type']:
                    src_res = res
                    break
            if src_res is None:
                abort(404)
            src = safe_join(src_res.abs_path(item['folder']), item['name'])
            dst = safe_join(resource.abs_path(current_folder), item['name'])
            if src != dst:
                num = next(cnt)
                copyfile(src, dst)
        return dict(resourceType=resource.name, currentFolder=resource.folder(current_folder), copied=num)

    @ckf_command('POST', CKFAcl.FILE_CREATE)
    def command_MoveFiles(self, resource, current_folder):
        files = self.get_files()
        cnt = count()
        num = next(cnt)
        for item in files:
            src_res = None
            for res in self.resource_types.values():
                if res.name == item['type']:
                    src_res = res
                    break
            if src_res is None:
                abort(404)
            src = safe_join(src_res.abs_path(item['folder']), item['name'])
            dst = safe_join(resource.abs_path(current_folder), item['name'])
            if src != dst:
                num = next(cnt)
                rename(src, dst)
        return dict(resourceType=resource.name, currentFolder=resource.folder(current_folder), moved=num)

    @ckf_command('GET', CKFAcl.FILE_VIEW)
    def command_DownloadFile(self, resource, current_folder):
        file_name = self.get_arg('fileName')
        return send_from_directory(resource.abs_path(current_folder), file_name, as_attachment=True)

    @ckf_command('GET')
    def command_Thumbnail(self, resource, current_folder):
        """
        If request parameter 'size' is omitted, creates a 150x150 thumbnail.
        """
        file_name = self.get_arg('fileName')
        size = request.args.get('size', '')
        try:
            width, height = map(int, size.split('x'))
        except ValueError:
            width, height = 150, 150
        source = safe_join(resource.abs_path(current_folder), file_name)
        if self.thumbnail_mapper:
            thumbnail = self.thumbnail_mapper.create_thumbnail(source, width, height)
            if self.thumbnail_mapper.has(thumbnail.filename):
                st = stat(thumbnail.absfilename)
                make = st.st_mtime < stat(source).st_mtime
            else:
                make = True
            if make:
                try:
                    thumbnail.make()
                except Exception:
                    abort(500)
                st = stat(thumbnail.absfilename)
            url = url_for('ckfinder.thumbnail', filename=thumbnail.filename, t=st.st_mtime)
            return redirect(url), 301
        else:
            temp = NamedTemporaryFile()
            thumbnail = Thumbnail(source, width, height)
            thumbnail.filename = temp.name
            thumbnail.make()
            return send_file(temp.name, mimetype='image/jpeg')  # test: , cache_timeout=-1

    @ckf_command('GET')
    def command_ImageInfo(self, resource, current_folder):
        file_name = self.get_arg('fileName')
        absfname = safe_join(resource.abs_path(current_folder), file_name)
        with Image.open(absfname) as img:
            width, height = img.size
        return dict(resourceType=resource.name,
                    currentFolder=resource.folder(current_folder),
                    width=width,
                    height=height)

    @ckf_command('GET')
    def command_GetResizedImages(self, resource, current_folder):
        file_name = self.get_arg('fileName')
        absfname = safe_join(resource.abs_path(current_folder), file_name)
        if not isfile(absfname):
            abort(404)
        try:
            img = Image.open(absfname)
            original_size = '{}x{}'.format(*img.size)
            img.close()
        except UnidentifiedImageError:
            """
            Workaround to allow deletion of invalid files.
            CKFinder wants an original_size before displaying the menu.
            """
            original_size = '0x0'
        return dict(resourceType=resource.name,
                    currentFolder=resource.folder(current_folder),
                    originalSize=original_size,
                    resized={})

    @ckf_command('POST')
    def command_ImageResize(self, resource, current_folder):
        file_name = self.get_arg('fileName')
        size = self.get_arg('size')
        try:
            width, height = map(int, size.split('x'))
        except ValueError:
            abort(400)
        absfname = safe_join(resource.abs_path(current_folder), file_name)
        basename, ext = splitext(file_name)
        img = Image.open(absfname)
        if (width, height) == img.size:
            url = url_for(resource.endpoint, filename=file_name)
        else:
            m = re.match('(.*)__\d+x\d+$', basename)
            if m:
                basename = m.group(1)
            output_img = img.resize((width, height))
            output = '{}__{}x{}{}'.format(basename, width, height, ext)
            output_path = join(current_folder, output)
            output_img.save(resource.abs_path(output_path))
            url = url_for(resource.endpoint, filename=output_path)
        img.close()
        return dict(resourceType=resource.name, currentFolder=resource.folder(current_folder), url=url)

    @ckf_command('POST')
    def command_SaveImage(self, resource, current_folder):
        file_name = self.get_arg('fileName')
        content = request.form.get('content', None)
        if content is None:
            abort(400)
        meta, boby = content.split(',', 1)
        m = re.match('data:(.+);base64', meta)
        if not m:
            abort(400)
        temp = NamedTemporaryFile(suffix=guess_extension(m.group(1)))
        temp.write(base64.decodebytes(boby.encode('ascii')))
        basename, ext = splitext(file_name)
        absfname = safe_join(resource.abs_path(current_folder), basename + ext)
        img = Image.open(temp.name)
        temp.close()
        if ext in ('.jpeg', '.jpg'):
            rgb_img = img.convert('RGB')
            rgb_img.save(absfname, 'JPEG', optimize=True, quality='web_high')
        elif ext == '.png':
            img.save(absfname, optimize=True, compress_level=9)
        else:
            img.save(absfname)
        img.close()
        st = stat(absfname)
        return dict(resourceType=resource.name,
                    currentFolder=resource.folder(current_folder),
                    date=datetime.fromtimestamp(st.st_mtime).strftime('%Y%m%d%H%M'),
                    size=int(st.st_size / 102.4) / 10,
                    saved=1)
