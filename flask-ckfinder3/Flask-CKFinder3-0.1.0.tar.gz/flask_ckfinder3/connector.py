from flask import abort, json, redirect, request, safe_join, send_file, send_from_directory, url_for
from os import listdir, mkdir, rename, stat, unlink, walk
from os.path import dirname, isdir, isfile, join
from shutil import copyfile, rmtree
from datetime import datetime
from PIL import Image
from itertools import count
from tempfile import NamedTemporaryFile
from dataclasses import asdict
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
    uploadckeckimages = False

    #: Thumbnails sizes
    thumbs = ()

    #· Thumbnail cache directory
    thumbnail_dir = None

    #: Thumbnail cache size
    thumbnail_maxfiles = None

    #: Thumbnail gc threshold
    thumbnail_threshold = None

    #: ThumbnailMapper instance
    thumbnail_mapper = None

    def __init__(self, resource_types=dict(), **kwargs):
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

    def get_arg(self, name):
        """
        Renvoie la valeur de request.arg['name']
        Échoue avec un statut 400 si name est absent.
        """
        value = request.args.get(name, None)
        if value is None:
            abort(400)
        return value

    def get_files(self):
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
            CHARS = '123456789ABCDEFGHJKLMNPQRSTUVWXYZ'
            pos = CHARS.find(self.license_key[2]) % 5
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
        ret = dict(enabled=True,
                   s=ln,
                   c=lc,
                   thumbs=self.thumbs,
                   images={
                       "max": "",
                       "sizes": {}
                   },
                   uploadMaxSize=self.uploadmaxsize,
                   uploadCheckImages=self.uploadckeckimages,
                   resourceTypes=[asdict(x) for x in self.resource_types.values()])
        return ret

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
            return "Directory already exists.", 400
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
        file_name = self.get_arg('fileName')
        size = self.get_arg('size')
        try:
            width, height = map(int, size.split('x'))
        except ValueError:
            abort(400)
        source = safe_join(resource.abs_path(current_folder), file_name)
        if self.thumbnail_mapper:
            thumbnail = self.thumbnail_mapper.create_thumbnail(source, width, height)
            if self.thumbnail_mapper.has(thumbnail.filename):
                st = stat(thumbnail.absfilename)
                make = st.st_mtime < stat(source).st_mtime
            else:
                make = True
            if make:
                thumbnail.make()
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
    def command_GetResizedImages(self, resource, current_folder):
        file_name = self.get_arg('fileName')
        absfname = safe_join(resource.abs_path(current_folder), file_name)
        if not isfile(absfname):
            abort(404)
        img = Image.open(absfname)
        original_size = '{}x{}'.format(*img.size)
        img.close()
        ret = dict(resourceType=resource.name,
                   currentFolder=resource.folder(current_folder),
                   originalSize=original_size,
                   resized={})
        return ret
