from flask import abort, request, send_from_directory, url_for
from werkzeug.utils import secure_filename
from os.path import join
from .resource_type import CKFResourceType
from .connector import CKFConnector
from .acl import CKFAcl


class CKFinder():
    """
    CKFinder flask extension
    """

    def __init__(self, app=None, url_prefix='/ckfinder', connector_class=CKFConnector, view_decorator=None):
        """
        CKFinder constructor

        :parameter app: Flask instance
        :parameter url_prefix: string to preprend to routes
        :parameter connector_class: connector class
        :parameter view_decorator: decorator for view functions
        """
        self.url_prefix = url_prefix.rstrip('/')
        self.connector_url = self.url_prefix + '/connector'
        self.upload_url = self.url_prefix + '/upload'
        self.connector_class = connector_class
        self.view_decorator = view_decorator
        if not app is None:
            self.init_app(app)

    def init_app(self, app):
        """
        Application setup

        Loads resource_types from app.config.
        Adds ckfinder routes.
        """
        self.app = app
        self.app.config.setdefault('CKFINDER_DEFAULT_ACL', 255)  # 1023 pour redimensionner les images
        self.app.config.setdefault('CKFINDER_THUMBS', ("150x150", "300x300", "500x500"))
        self.app.config.setdefault('CKFINDER_THUMBNAIL_MAXFILES', 200)
        self.app.config.setdefault('CKFINDER_THUMBNAIL_THRESHOLD', 1 / 20)
        """
        La commande RenameFolder transmet 'type' au lieu de 'hash',
        et MoveFiles et CopyFiles utilisent l'attribut name, ce qui peut provoquer une collision.
        -> On interdit les ressources avec le même 'name'.
        """
        name_seen = set()
        resource_types = dict()
        for res in self.app.config['CKFINDER_RESOURCE_TYPES']:
            if res['name'] in name_seen:
                raise RuntimeError('Resource name must be unique.')
            name_seen.add(res['name'])
            res.setdefault('maxSize', self.app.config['MAX_CONTENT_LENGTH'])
            res.setdefault('acl', self.app.config['CKFINDER_DEFAULT_ACL'])
            obj = CKFResourceType(**res)
            resource_types[obj.hash] = obj
        options = dict()
        for key in ('LICENSE_NAME', 'LICENSE_KEY', 'THUMBS', 'QUICKUPLOAD_DIR', 'QUICKUPLOAD_ENDPOINT', 'UPLOADMAXSIZE',
                    'UPLOADCKECKIMAGES', 'THUMBNAIL_DIR', 'THUMBNAIL_MAXFILES', 'THUMBNAIL_THRESHOLD'):
            value = self.app.config.get('CKFINDER_{}'.format(key), None)
            if value:
                options[key.lower()] = value
        self.connector = self.connector_class(resource_types, **options)
        if self.view_decorator:
            connector_func = self.view_decorator(self.connector)
            upload_func = self.view_decorator(self.connector.upload)
        else:
            connector_func = self.connector
            upload_func = self.connector.upload
        self.app.add_url_rule(self.connector_url,
                              view_func=connector_func,
                              endpoint='ckfinder.connector',
                              methods=('GET', 'POST'))
        self.app.add_url_rule(self.upload_url, view_func=upload_func, endpoint='ckfinder.upload', methods=('POST',))
        if self.connector.thumbnail_dir:
            thumbnail_view = lambda filename: send_from_directory(
                self.connector.thumbnail_dir, filename, mimetype='image/jpeg')
            self.app.add_url_rule('{}/thumbnail/<path:filename>'.format(self.url_prefix),
                                  view_func=thumbnail_view,
                                  endpoint='ckfinder.thumbnail',
                                  methods=('GET',))
