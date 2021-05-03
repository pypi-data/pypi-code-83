# -*- coding: UTF-8 -*-#
import collections
import os
import pickle
import re
import sys
import uuid
import weakref
import itertools

ROOT_PATH = os.path.dirname(__file__)
if ROOT_PATH.strip() == '':
    ROOT_PATH = os.getcwd()
for i in range(4):
    if os.path.basename(ROOT_PATH) == 'lib':
        ROOT_PATH = os.path.dirname(ROOT_PATH)
        break
    ROOT_PATH = os.path.dirname(ROOT_PATH)
if ROOT_PATH not in sys.path:
    sys.path.append(ROOT_PATH)


class llDict(collections.OrderedDict):
    """
    llDict stands for link list dict
    This is a normal dict but an order is given by the special elements llDictElement which contains a link to the next
    element.
    The extension of the dict contains ordered iterations controlled by this next element
    """
    VERSION = 2
    NO_REF = 1
    INCL_REF = 2
    ONLY_REF = 3
    ROOT_TAG = '.'
    STRUCT_TAG = 'STRUCTURE:'

    # subclasses
    class RefFlag(object):
        """
        Enumeration Flag used as method parameter
        determines the usage of references in the methods
        """
        EXCL = 1  # Exclude referenced items from operation (use only normal items)
        BOTH = 2  # Use both normal and referenced items in operation
        ONLY = 3  # Use only referenced items in operation

    class _SpecialItem(object):
        def __init__(self, is_ref=False):
            self.is_ref = is_ref
            self.is_llDict = True  # Needed for compatibility
            self.parent = llDict._Parent()
            self.is_SpecialItem = True  # Needed for identification

        def get_file_repr(self, _indentation=''):
            if self.is_ref:
                return _indentation + 'ref_item()'

        def create_lldict(self, parent, load_refs):
            _ = parent
            _ = load_refs
            return self

        def __repr__(self):
            if self.is_ref:
                return 'llDict._SpecialItem(is_ref=True)'

    class _WeakRef(weakref.ref):
        """
        Extended weak reference for llDict references
        """

        def __init__(self, lldict_item):
            """
            Extended weak reference for llDict references

            :param lldict_item: item to which the weakreference is linked to
            """
            if isinstance(lldict_item, llDict._WeakRef):
                # go back to org item
                lldict_item = lldict_item()
            if not hasattr(lldict_item, 'is_llDict'):
                raise TypeError('Error: Expect lldict as value item!')
            super().__init__(lldict_item)
            # data extension:
            self.parent = llDict._Parent()
            self.is_ref = True
            self.is_WeakRef = True
            self.is_llDict = True  # for faster value tests

    class _Reference(object):
        """
        sub class containing reference information of llDict
        """

        def __init__(self, key_path=None, file_path=None, ref_dict=None):
            """
            sub class containing reference information of llDict

            :param key_path: key to the referenced object in the referenced dict
            :param file_path: file_path to the file where the refrence is stored in (external reference)
            :param ref_dict: reference dict containing the original dict of a reference (external) or
                             the weakref to the internal part of llDict
                             normally this is set in the _load_reference method of llDict
            """
            if key_path is None and file_path is not None:
                key_path = [llDict.ROOT_TAG]
            self.key_path = key_path
            self.file_path = file_path
            self.ref_dict = ref_dict
            self.covered_items = {}
            self.is_Reference = True

        def __repr__(self):
            if self.key_path is None:
                return 'llDict.Reference()'
            else:
                if self.file_path is None:
                    return 'llDict.Reference(key_path=%s)' % (repr(self.key_path))
                else:
                    return 'llDict.Reference(key_path=%s,file_path=%s)' % (repr(self.key_path), repr(self.file_path))

        def __eq__(self, other):
            """
            equal check used by == operator
            :param other: other object against the check is performed
            :return:
            """
            if id(self) == id(other):
                return True
            if not hasattr(other, 'is_Reference'):
                return False
            if self.key_path != other.key_path:
                return False
            if self.file_path != other.file_path:
                return False
            return True

        def is_internal(self):
            """
            checks for internal reference (links to another element in the local llDict
            :return: True - is internal
                     False - is external
            :rtype: boolean
            """
            if self.ref_dict is None:
                # no reference set
                return None
            return isinstance(self.ref_dict, weakref.ref)

        def is_external(self):
            """
            checks for external reference (links to element in the external (other file) llDict)
            :return: True - is external
                     False - is internal
            :rtype: boolean
            """
            return not self.is_internal()

        def get_ref_dict(self):
            """
            gives the ref_dict stored in this object
            HINT: For internal references (weakref) it gives the llDict object not the weakref back
            :return:
            """
            if self.ref_dict is None:
                # no reference set
                return None
            if isinstance(self.ref_dict, weakref.ref):
                return self.ref_dict()
            return self.ref_dict

        def is_key_in_ref(self, key):
            """
            Search for key in the referenced dict
            :param key: key to be searched for
            :return: True - key is in
                     False - key not found
            :rtype: boolean
            """
            if self.ref_dict is None:
                # no reference set
                return False
            if isinstance(self.ref_dict, weakref.ref):
                return key in self.ref_dict()
            return key in self.ref_dict

    class _Parent(object):
        """
        data object containing the parent information of the llDict object
        """

        def __init__(self, weakref_parent=None, child_key=None):
            """
            data object containing the parent information of the llDict object

            :param weakref_parent: weak-reference to the parent object
            :param child_key: key of the llDict object in this parent
            """
            self.weakref_parent = weakref_parent
            self.child_key = child_key
            self.is_Parent = True

        def get_root(self, item):
            """
            recursive search for the highest parent in the llDict tree
            HINT: If an llDict._WeakRef is given the root of this references will be searched too
            :param item: llDict object which root should been found
            :return: root_parent
            :rtype: llDict
            """
            if item.parent.weakref_parent is None:
                return item
            parent_dict = item.parent.weakref_parent()
            return self.get_root(parent_dict)

    class ExchangeDataList(list):
        """
        small object containing only data no function for serialized data exchange and files
        """

        def __init__(self, lldict, include_ref=False):
            """
            small object containing only data no function for serialized data exchange and files
            The llDict is represented in this object as a list of tuples (key,value)
            The llDict is stripped from all functional overhead and only the data needed for recreation is stored in
            this object
            This object is used for file-storage (pickle) and for data transfer via network

            :param lldict: lldict which data is used to build exchangeDataList
            :param include_ref: include the reference dicts (not tested yet)
            """
            if not hasattr(lldict, 'is_llDict'):
                raise TypeError('Error: Parameter lldict must be of type llDict!')
            self.include_ref = include_ref
            self.data = lldict.data
            self.ref = None
            self.is_exchangeDataList = True
            self.cover_items_keys = []

            if lldict.ref.key_path is not None:
                if include_ref:
                    if lldict.ref.is_external:
                        # the rebuild of this is untested!
                        self.ref = llDict._Reference(key_path=lldict.ref.key_path,
                                                     file_path=lldict.ref.file_path,
                                                     ref_dict=llDict.ExchangeDataList(lldict.ref.ref_dict))
                        self.ref.covered_items = lldict.ref.coveritems
                    else:  # internal references will be rebuild
                        self.ref = llDict._Reference(key_path=lldict.ref.key_path,
                                                     file_path=lldict.ref.file_path)
                else:
                    self.ref = llDict._Reference(key_path=lldict.ref.key_path,
                                                 file_path=lldict.ref.file_path)

            super().__init__()
            if lldict.has_children():
                super().extend([lldict.is_ref_child(key) and
                                (key,llDict._SpecialItem(is_ref=True)) or
                                (key,llDict.ExchangeDataList(value, include_ref=include_ref))
                             for key, value in lldict.items()])
            self.cover_items_keys=[key for key, in lldict.ref.covered_items.keys()]
                

        def create_lldict(self, parent=None, load_refs=True):
            """
            recreate the lldict
            :return:
            """
            new_lldict = llDict(data=self.data, load_refs=load_refs)
            if parent is not None:
                new_lldict.parent = parent
            for key, value in self:
                new_parent = llDict._Parent(new_lldict._weakref, key)
                new_value = value.create_lldict(new_parent, load_refs=load_refs)
                if not load_refs:
                    if isinstance(new_value, llDict._SpecialItem):
                        continue
                new_lldict[key] = new_value
            if self.ref is not None:
                if self.ref.ref_dict is None:
                    new_lldict.set_reference(self.ref.key_path, self.ref.file_path)
            if hasattr(self, 'cover_items_keys'):
                (new_lldict.cover(key) for key in self.cover_items_keys)
            return new_lldict

        def get_file_repr(self, _indentation=''):
            """
            Structure string that shows the content in the stored files (Debugging feature)
            :param _indentation: helper for recursive execution (do not set)
            :return: string containing the structural information
            """
            out_str = []
            if self.data != {}:
                out_str.append(_indentation)
                out_str.append('data=%s\n' % repr(self.data))
            if self.ref is not None:
                out_str.append(_indentation)
                out_str.append('ref_key_path=%s\n' % repr(self.ref.key_path))
                out_str.append(_indentation)
                out_str.append('ref_file_path=%s\n' % repr(self.ref.file_path))
            if len(self) > 0:
                out_str.append(_indentation)
                out_str.append('substeps:\n')
            _indentation = _indentation + '  '
            for key, value in self:
                out_str.append( _indentation + key + ':')
                out_str.append(value.get_file_repr(_indentation=_indentation))
            return ''.join(out_str)

        @staticmethod
        def get_version():
            """
            get version of the  (same as source llDict)
            :return:
            """
            return llDict.VERSION

        def __repr__(self):
            """
            build the representation str is slow because lldict must be instanced
            :return:
            """
            out_str = 'llDict.exchangeDataList('
            out_str = out_str + 'lldict=%s' % repr(self.create_lldict())
            out_str = out_str + 'include_ref=%s' % repr(self.include_ref)
            out_str = out_str + ')'
            return out_str

        def copy(self):
            """
            shallow copy of this object
            :return:
            """
            return self.__class__(self)

    class exchangeDict(ExchangeDataList):
        pass

    class StructuralError(Exception):
        """
        Special llDict exception
        """

    def __init__(self, sub_dict=None, data=None, ref_key_path=None, ref_file_path=None, load_refs=True):
        """
        Init the llDict object given parameters can be given to build the dict
        HINT: We expect the arguments in the following way:

        :param sub_dict: llDict that is integrated as a sub tree into this lldict
        :type: sub_dict: llDict
        :param data: data object that can be stored in the tree item
        :type: data: object
        :param ref_key_path: keypath of a reference to be "linked" in the tree
        :type: ref_key_path: string
        :param ref_file_path: file_path of a external reference to be "linked" in the tree
        :type: ref_file_path: string
        :param load_refs: We can stop loading references during load if parameter is set to False
                          True (default) - references are loaded
                          False - references not loaded
        :type load_refs: boolean
        """
        self.ref = llDict._Reference(ref_key_path, ref_file_path)
        self.parent = llDict._Parent()
        # the is_ref parameter is changed depending on the context it is used
        # to be sure to have a functional reference use is_ref_child method
        self.is_ref = False
        self.is_llDict = True

        self.data = data

        self._weakref = weakref.ref(self)  # used in parents
        self._source_file = None

        if sub_dict is not None:
            super(llDict, self).__init__(**sub_dict)
            for key, value in self.items():
                value.parent = llDict._Parent(self._weakref, key)
        else:
            super(llDict, self).__init__()
        self.load_references_active = load_refs
        self.__load_references(_init=True)

    # main class methods:

    def __delitem__(self, key):
        """
        overload original dict delitem method
        :param key:
        :return:
        """
        ref_dict = self.ref.ref_dict
        value = None
        if ref_dict is not None:
            # check if a referenced item must replace the to be deleted item
            if isinstance(ref_dict, weakref.ref):  # internal reference
                ref_dict = ref_dict()
            value = ref_dict.get(key)
        if value is not None:
            # replace with referenced value
            super(llDict, self).__setitem__(key, llDict._WeakRef(value))
        else:
            super(llDict, self).__delitem__(key)

    def __setitem__(self, key, value):
        """
        overload dict setitem method

        :param key: item key
        :param value: item value
        :return:
        """
        if not hasattr(value, 'is_llDict'):
            raise TypeError('Error: Value (%s:%s) must been an llDict object!' % (repr(key), repr(value)))
        parent=value.parent
        parent.weakref_parent = self._weakref
        parent.child_key = key
        super(llDict, self).__setitem__(key, value)

    def __getitem__(self, key):
        value = super(llDict, self).__getitem__(key)
        if isinstance(value, llDict._WeakRef):
            return value()
        return value

    def __repr__(self):
        """
        create string representation of the object
        :return: string representation
        """
        out_str = 'llDict('
        if len(self) > 0:
            sub_dict_str = str(super(llDict, self).__repr__())
            out_str = out_str + 'sub_dict=%s,' % sub_dict_str
        if self.data is not None:
            out_str = out_str + ' data=%s,' % repr(self.data)
        if self.ref is not None:
            out_str = out_str + ' ref_key_path=%s,' % repr(self.ref.key_path)
            out_str = out_str + ' ref_file_path=%s,' % repr(self.ref.file_path)
        out_str = out_str[:-1] + ' )'
        return out_str

    def __eq__(self, other):
        """
        Test equal (operator =)

        :status: tested

        :rtype: boolean
        :return: True - equal; false - not equal
        """
        if not hasattr(other, 'is_llDict'):
            return False
        if id(self) == id(other):
            return True
        if self.data != other.data:
            return False
        if self.ref != other.ref:
            return False
        if len(self) != len(other):
            return False
        for (key, value), (key_o, value_o) in zip(self.items(), other.items()):
            if key != key_o:
                return False
            if value != value_o:  # This operation is recursive!
                return False
        return True

    def __ne__(self, other):
        """
        Test not equal (operator =)

        :status: tested

        :rtype: boolean
        :return: True - not equal; False - equal
        """
        return not (self == other)

    # dict manipulations:

    def __insert_after_item(self, after_item_key, new_key, value):
        """
        helper method that inserts a item in the given position
        :param after_item_key: key that marks the position of the insertion (insert after this item)
        :param new_key: key of the new item
        :param value: value of the new item
        :type value: llDict
        """
        self[new_key] = value
        # resort
        sort_list = []
        add = False
        iterator=itertools.dropwhile(lambda k: k!=after_item_key,list(self.keys()))
        try:
            next(iterator) # take first item out
        except StopIteration:
            return
        for k in iterator:
            if k==new_key:
                break
            super(llDict, self).move_to_end(k)
        return
        for k in self.keys():
            if k == after_item_key:
                add = True
                continue
            if add:
                sort_list.append(k)
        # move others to the end:
        ( super(llDict, self).move_to_end(k) for k in sort_list[:-1] )


    def __inherit_ref_dict(self, ref_dict):
        """
        helper method for inheritance of a reference dict
        (mixes the local elements with the inherited elements
        :param ref_dict: reference dict which should be inherited
        """
        last_match = None
        for key, value in ref_dict.items():
            # prepare ref value
            ref_value = llDict._WeakRef(value)
            ref_value.parent.weakref_parent = self._weakref
            ref_value.parent.child_key = key
            if key not in self:
                if last_match is None:
                    # prepend
                    self[key] = ref_value
                    super(llDict, self).move_to_end(key, last=False)
                    last_match = key
                else:
                    # insert
                    self.__insert_after_item(last_match, key, ref_value)
                    last_match = key
            else:
                if self.is_ref_child(key):
                    self[key] = ref_value
                last_match = key
        # check if a referenced key is deleted:
        del_keys = []
        for key, value in self.items():
            if isinstance(value, llDict._SpecialItem):
                del_keys.append(key)
        for key in del_keys:
            super(llDict, self).__delitem__(key)

    def __load_references(self, _init=False):
        def clean_all_references():
            pop_list = []
            (isinstance(value, llDict._WeakRef) and pop_list.append(key) for key, value in super(llDict, self).items())
            (super(llDict, self).__delitem__(key) for key in pop_list)


        def load_external_reference():
            # We expect here in the first case relative path to the application root!
            file_path = self.ref.file_path
            # 1. check abs path:
            if not os.path.exists(file_path):
                # 2. check rel path
                file_base_name = os.path.basename(file_path)
                if self._source_file is not None:
                    file_path = os.path.join(os.path.dirname(self._source_file), file_base_name)
                else:
                    source_file = None
                    parent = self
                    while (True):
                        parent = parent.parent
                        if parent is None:
                            break
                        if parent.weakref_parent is None:
                            break
                        parent_ref = parent.weakref_parent()
                        parent = parent_ref
                        if parent_ref is None:
                            break
                        source_file = parent_ref._source_file
                        if source_file is not None:
                            break
                        parent = parent_ref
                    if source_file is None:
                        file_path = "./" + file_base_name
                    else:
                        file_path = os.path.join(os.path.dirname(source_file), self.ref.file_path)
                if not os.path.exists(file_path):
                    # 3. check rel path to main app path
                    file_path = os.path.join(ROOT_PATH, os.path.basename(file_base_name))
                    if not os.path.exists(file_path):
                        file_path = os.path.join(ROOT_PATH, self.ref.file_path)
            if not os.path.exists(file_path):
                raise AttributeError(
                    'Error: Wrong "file_path" given (file=%s does not exists)!' % repr(
                        os.path.abspath(self.ref.file_path)))
            root_ref_dict = self.create_from_file(file_path)
            if self.ref.key_path == [llDict.ROOT_TAG]:
                ref_dict = root_ref_dict
            else:
                # store only subpart
                ref_dict = root_ref_dict.get_deep(self.ref.key_path)
            # store file reference as real dict in the object
            if ref_dict is None:
                out_str = 'Error: "key_path"=%s not found (referenced external dict %s )!' % (
                    repr(self.ref.key_path), repr(ref_dict))
                print(out_str)
                return out_str
            self.ref.ref_dict = ref_dict
            return ref_dict

        def load_internal_reference():
            # protect cyclic reference for root (higher level cycles not detect)
            if self.ref.key_path == [llDict.ROOT_TAG]:
                raise SyntaxError(
                    'Error: "key_path" links to root this leads into cyclic merge!')
            # We need the correct parents definition for the following steps!
            # Search for the highest parent of this llDict
            root_parent = self.parent.get_root(self)
            if root_parent is None:
                # internal error somehow the parent is not set correct!
                raise SyntaxError('Error: Internal error no parent found for item %s' % repr(self))
            # try to find the key:
            ref_dict = root_parent.get_deep(self.ref.key_path)
            if ref_dict is None:
                raise SyntaxError(
                    'Error: key_path=%s not found (in the root_Parent of this dict %s )!' % (
                        repr(self.ref.key_path), repr((root_parent, self))))
            self.ref.ref_dict = weakref.ref(ref_dict)
            return ref_dict

        if not self.load_references_active:
            return
        if not _init:
            clean_all_references()
        self.ref.ref_dict = None
        # watch for reference definition
        if self.ref.key_path is None:
            # nothing to do
            return None
        if self.ref.file_path is not None:
            ref_dict = load_external_reference()
        else:
            ref_dict = load_internal_reference()
        # build inheritance structure
        self.__inherit_ref_dict(ref_dict)

    # boolean questions

    def has_children(self):
        """
        gives back if this llDict has child llDicts
        :return: True - child llDicts exists
                 False - no child llDicts in this llDict
        """
        return super(llDict, self).__len__() > 0

    # reference handling

    def is_ref_child(self, child_key):
        """
        Search in the children an check if child is a reference or a local item

        :return: True - is reference; a merged element
                 False - is local element
        :rtype: boolean

        """
        if child_key not in self:
            # unknown child!
            raise KeyError('Error: Unknown key=%s' % repr(key))
        value = super(llDict, self).__getitem__(child_key)
        if isinstance(value, llDict._WeakRef) or isinstance(value, llDict._SpecialItem):
            return True
        return False

    def update_reference(self, force=False):
        """
        Reload the external and internal references!
        """
        if force:
            self.load_references_active = True
        self.__load_references()
        for v in self.values():
            v.update_reference(force)

    def clear_reference(self):
        """
        Delete the references of this element
        :return:
        """
        self.set_reference(None, None)

    def set_reference(self, key_path=None, file_path=None, load=True):
        """
        Method that sets an internal (same llDict) or external reference (other file)
        that should been merged into the local tree

        :param key_path: list of keys to the element
                         if key_path is '.' only for external references the whole tree will be merged!
        :type key_path: list of string
        :param file_path: string containing the path to the file (can be relative)
        :type file_path: string
        :param load: True - set and load the reference
                     False - set but do not load the reference
        :type load: boolean

        """
        if key_path is None:
            if self.ref is None:
                # nothing to do
                return
            # clear reference
            self.ref.key_path = None
            self.ref.file_path = None
            if load:
                self.__load_references()
        if self.ref is None:
            self.ref = llDict._Reference(key_path, file_path)
        else:
            self.ref.key_path = key_path
            self.ref.file_path = file_path
        if load:
            self.__load_references()
            (value.__load_references() for value in self.values_deep())


    def _set_source_file_path(self, source_file_path):
        '''
        store path in case the lldict is loaded from file
        :param source_file_path: abs path to source file create_from_file() command
        :return:
        '''

        self._source_file = source_file_path

    def _get_source_file_path(self):
        '''
        gives the abs path of the file the lldict is created from
        :return: absolute source file path
        '''
        return self._source_file

    def gen_key(self, pre_str='', post_str=''):
        """
        Append id to the given pre_key/post_key str

        :status: tested

        :param pre_str: pre_key string to which the id information will be added
        :type pre_str: string
        :param post_str: suffix to the key
        :type post_str: string
        :rtype: string
        :return: pre_key+'_IDxxxx' build key
        """
        new_id = 0
        for key in self.keys():
            numbers = re.findall(r'\d+', key)
            for number in numbers:
                n = int(number)
                if n > new_id:
                    new_id = n
        while True:
            new_id += 1
            seq = (str(pre_str), str(new_id), str(post_str))
            key = ''.join(seq)
            if key not in self:
                break
        return key

    @staticmethod
    def gen_uid_key(prefix='', suffix=''):
        """
        Append id to the given pre_key str

        :status: tested

        :param prefix: pre_key string to which the id information will be added
        :type prefix: string
        :param suffix: suffix to the key
        :type suffix: string
        :rtype: string
        :return: prefix+'_IDxxxx' build key
        """
        id_code = uuid.uuid4()
        seq = (str(prefix), str(id_code), str(suffix))
        key = ''.join(seq)
        return key

    # item operations

    def append(self, key, lldict_item):
        """
        Append an element to the ordered link_list at the end
        Hint1: For unique key generation use gen_key() method
        Hint2:
        Appending an existing local elements means replacing the local element
        Appending an existing referenced elements is not possible
        Hint3:
        Currently it's not possible to test if the this method is executed on a referenced item.
        (We have no access to the parent of the selection, only to the referenced parent)
        It must be ensured by the editor that we are on a local element when executing this function!

        :param key: key of the new element
        :type key: string
        :param lldict_item: llDict object that should been added
        :type lldict_item: llDict
        :return: llDict item prepended
        :rtype: string
        """
        if key in self:
            if self.is_ref_child(key):
                raise llDict.StructuralError('Error: Cannot append an element on a existing referenced item!')
            # In case of a non existent or local element we append at the end or overwrite and move to the end!
            self.__setitem__(key, lldict_item)
            self.move_to_end(key)
        else:
            self.__setitem__(key,lldict_item)
        return lldict_item

    def prepend(self, key, lldict_item):
        """
        Prepend an element to the ordered link_list at the beginning
        Hint1: For unique key generation use gen_key() method
        Hint2:
        Prepending an existing local elements means replacing the local element
        Prepending an existing referenced elements is not possible
        (The order of the referenced elements can not be changed here) -> Exception

        :param key: key of the new element
        :type key: string
        :param lldict_item: llDict object that should been added
        :type lldict_item: llDict
        :return: llDict item prepended
        :rtype: string
            """
        if key in self:
            if self.is_ref_child(key):
                raise llDict.StructuralError('Error: Cannot prepend an element on a existing referenced item!')
        # In case of a non existent or local element we append at the end or overwrite and move to the end!
        self.__setitem__(key, lldict_item)
        if len(self) != 1:
            self.move_to_end(key, False)
        return lldict_item

    def insert(self, insert_after_key, new_key, lldict_item):
        """
        Append an element to the ordered link_list after the given ident_key
        Hint1: For unique key generation use gen_key() method
        Hint2:
        Prepending an existing local elements means replacing the local element
        Prepending an existing referenced elements is not possible
        (The order of the referenced elements can not be changed here) -> Exception

        :param insert_after_key: key of the pre element after which the new should been inserted
        :type insert_after_key: string
        :param new_key: key of the new element
        :type new_key: string
        :param lldict_item: llDict obejct that should been added
        :type lldict_item: llDict
        :return: llDict item prepended
        :rtype: string
        """
        if new_key in self:
            if self.is_ref_child(new_key):
                raise llDict.StructuralError('Error: Cannot prepend an element on a existing referenced item!')
        # In case of a non existent or local element we append at the end or overwrite and move to the end!
        self.__insert_after_item(insert_after_key, new_key, lldict_item)
        return lldict_item

    def replace(self, key, lldict_item):
        """
        Replace an existing element
        IMPORTANT: We cannot ensure that the parent is local already
        This must been ensured by the editor,
        if this is not not the case we will loose the item after save and reload

        :param key: key of the element that should been overloaded
        :type key: string
        :param lldict_item: llDict object that should been placed in the llDict
        :type lldict_item: llDict
        :return: replaced element
        :rtype: llDict
        """
        if not hasattr(lldict_item, 'is_llDict'):
            raise AttributeError('Error: "value_item" must be of type llDict!')
        if key not in self:
            raise SyntaxError('Error: The to be replaced item (key=%s) not found!' % repr(key))
        back = self.__getitem__(key)
        self.__setitem__(key, lldict_item)
        return back

    def replace_key(self, keys_list, new_key):
        """
        Replace the key of the element found at path 'keys_list' with the supplied 'new_key'. The action is performed
        only if the element is found and if no other element at the same level has the key 'new_key'.

        :param keys_list: list of keys representing the ancestors path to the element, starting from root
        :type keys_list: list
        :param new_key: new name of the key
        :type new_key: string
        :return: the element at which the key has been replaced.
        :type: llDict
        """
        target_key = keys_list[-1] if keys_list else " "

        target_subitem = self.get_deep(keys_list)
        if target_subitem is None:
            raise KeyError("Old key '{}' not found, cannot replace key.".format(target_key))

        parent_item = target_subitem.get_parent()
        if new_key in parent_item.keys():
            raise KeyError("New key '{}' is already used, cannot replace key.".format(new_key))

        pre_key = parent_item.get_pre_key(target_key)
        parent_item.pop(target_key)

        if pre_key:
            parent_item.insert(pre_key, new_key, target_subitem)
        else:
            parent_item.prepend(new_key, target_subitem)

        return target_subitem

    def make_local(self, key):
        """
        Replace an existing referenced element with a local one
        but take over the whole content (per copy)
        IMPORTANT: We cannot ensure that the parent is local already
        This must been ensured by the editor,
        if this is not not the case we will loose the item after save and reload

        :param key: key of the element which should be transferred
        :type key: string
        """
        if key not in self:
            raise SyntaxError('Error: The to item to be made local (key=%s) not found!' % repr(key))
        if not self.is_ref_child(key):
            raise SyntaxError('Error: The original element (%s) is no reference!' % repr(key))
        value = self[key]
        new_lldict = llDict(data=value.data)
        # create weakrefs for one level deeper
        for k, v in value.items():
            new_lldict.__setitem__(k,llDict._WeakRef(v))
        self.__setitem__(key, new_lldict)
        return new_lldict

    def move_to_end(self, key, last=True):
        if self.is_ref_child(key):
            raise SyntaxError('Error: Cannot move referenced items!')
        super(llDict, self).move_to_end(key, last)

    def sort(self, reverse=False, sort_method=None):
        """
        Sorts the items in the llDict like sorting of a list
        (normally alphanumerical sort)

        :param reverse: reverse sort result
        :type reverse: boolean
        :param sort_method: sorting method (see list sort mechanism)
        :type sort_method: method
        """
        sorted_keys = []
        for k in super(llDict, self).keys():
            if self.is_ref_child(k):
                raise SyntaxError('Error: Sort a dict with refrenced items!')
            sorted_keys.append(k)
        sorted_keys.sort(key=sort_method, reverse=reverse)
        for k in sorted_keys:
            super(llDict, self).move_to_end(k, last=True)

    def cover(self, key):
        """
        Cover a referenced element

        :param key: key of the element that should been covered
        :type key: string
        :return: replaced element
        :rtype: llDict
        """
        if key not in self:
            raise llDict.StructuralError('Error: key=%s not found in llDict!' % (repr(key)))
        value = self[key]
        if not self.is_ref_child(key):
            raise llDict.StructuralError('Error: To be covered item (key=%s) is no reference!' % (repr(key)))
        self.ref.covered_items[key] = value
        super(llDict, self).__delitem__(key)
        return value

    def pop(self, key, default=None):
        """
        Deletes an element by key returns it

        :param key: key of the element that should be popped
        :type key: string
        :param default: value to return if the key does not exist
        :type default:
        :return: deleted element
        :rtype: llDict
        """
        if key in self:
            node = self.__getitem__(key)
            self.__delitem__(key)
            return node
        else:
            return default

    def pop_deep(self, key_list, default=None):
        """
        Deletes an element by key list returns it

        :param key_list: list of keys representing the ancestors path to the element, starting from root
        :type key_list: list
        :param default: value to return if the key_list does not exist
        :type default:
        :return: deleted element
        :rtype: llDict
        """
        if key_list is not None:
            parent_node = self.get_deep(key_list[:-1])
            if parent_node is not None and key_list[-1] in parent_node:
                node = parent_node[key_list[-1]]
                del parent_node[key_list[-1]]
                return node
        else:
            return default

    def swap(self, first_key, second_key):
        """
         Swaps element first_key with second_key

         :param first_key:
         :type first_key: string
         :param second_key:
         :type second_key: string
         """
        first_node = self.get(first_key)
        second_node = self.get(second_key)
        if first_node is not None and second_node is not None:
            pre_first_key = self.get_pre_key(first_key)
            if pre_first_key == second_key:
                pre_first_key = first_key
            else:
                self.pop(first_key)
                self.insert(second_key, first_key, first_node)
            self.pop(second_key)
            self.insert(pre_first_key, second_key, second_node)

    def _iter_items(self, deep=False, refs=INCL_REF, keep_ref=False, _key_list=None, _is_ref=False):
        """
        main iterator method (internal)

        :param deep: deep iteration switch
                     True - deep iteration over all subitems too (key id given a s a key_list
                     False - iteration only over children
        :param refs: reference flag (include/exclude reference subitems
                    llDict.RefFlag.BOTH - all items
                    llDict.RefFlag.ONLY - only referenced items
                    llDict.RefFlag.EXCL - only local items
        :param keep_ref: keep flag for reference
                         True - llDict.WeakRef objects will be given back as values in case of references
                         False - Conversion of llDict.WeakRef objects into the linked llDict objects
        :type keep_ref: boolean
        :param _key_list: internal parameter for recursive execution
        :return:
        """
        # iteration over OrderedDict Superclass:
        # We like to catch the weakrefs too!

        if _key_list is None:
            _key_list = []
        for key, i_value in super(llDict, self).items():
            real_value = i_value
            is_ref = False
            if isinstance(i_value, llDict._WeakRef):
                # transform weak into real reference
                real_value = i_value()
                is_ref = True
            if _is_ref:
                # we are already in a referenced tree:
                is_ref = True
            if is_ref:
                real_value.is_ref = True
                i_value.is_ref = True
                if refs == llDict.RefFlag.EXCL:
                    continue
            else:
                if refs == llDict.RefFlag.ONLY:
                    continue
            if deep:
                key_list = _key_list + [key]
                if keep_ref:
                    yield key_list, i_value
                else:
                    yield key_list, real_value
                for sub_key, sub_i_value in real_value._iter_items(deep=deep, refs=refs, _key_list=key_list,
                                                                   keep_ref=keep_ref,
                                                                   _is_ref=is_ref):
                    yield sub_key, sub_i_value
            else:
                if keep_ref:
                    yield key, i_value
                else:
                    yield key, real_value

    def items(self, deep=False, refs=INCL_REF, keep_ref=False):
        """
        iterator for items
        :param deep: deep iteration switch
                     True - deep iteration over all subitems too (key id given a s a key_list
                     False - iteration only over children
        :param refs: reference flag (include/exclude reference subitems
                    llDict.RefFlag.BOTH - all items
                    llDict.RefFlag.ONLY - only referenced items
                    llDict.RefFlag.EXCL - only local items
        :param keep_ref: keep flag for reference
                         True - llDict.WeakRef objects will be given back as values in case of references
                         False - Conversion of llDict.WeakRef objects into the linked llDict objects
        :type keep_ref: boolean
        :return: item iterator
        """
        for key, value in self._iter_items(deep=deep, refs=refs, keep_ref=keep_ref):
            yield key, value

    def values(self, deep=False, refs=INCL_REF, keep_ref=False):
        """
        value iterator
        :param deep: deep iteration switch
                     True - deep iteration over all subitems too (key id given a s a key_list
                     False - iteration only over children
        :param refs: reference flag (include/exclude reference subitems
                    llDict.RefFlag.BOTH - all items
                    llDict.RefFlag.ONLY - only referenced items
                    llDict.RefFlag.EXCL - only local items
        :param keep_ref: keep flag for reference
                         True - llDict.WeakRef objects will be given back as values in case of references
                         False - Conversion of llDict.WeakRef objects into the linked llDict objects
        :type keep_ref: boolean
        :return: value iterator
        """
        for key, value in self._iter_items(deep=deep, refs=refs, keep_ref=keep_ref):
            yield value

    def keys(self, deep=False, refs=INCL_REF):
        """
        key iterator
        :param deep: deep iteration switch
                     True - deep iteration over all subitems too (key id given a s a key_list
                     False - iteration only over children
        :param refs: reference flag (include/exclude reference subitems
                    llDict.RefFlag.BOTH - all items
                    llDict.RefFlag.ONLY - only referenced items
                    llDict.RefFlag.EXCL - only local items
        :return: key iterator
        """
        for key, value in self._iter_items(deep=deep, refs=refs):
            yield key

    def items_deep(self, refs=INCL_REF, keep_ref=False):
        """
        item iterator for deep iterations (subitems)

        :param refs: reference flag (include/exclude reference subitems
                    llDict.RefFlag.BOTH - all items
                    llDict.RefFlag.ONLY - only referenced items
                    llDict.RefFlag.EXCL - only local items
        :param keep_ref: Keep the references
        :type: boolean
        :return: item iterator (key/value) key is given as key_list
        """
        for key, value in self._iter_items(deep=True, refs=refs, keep_ref=keep_ref):
            yield key, value

    def values_deep(self, refs=INCL_REF, keep_ref=False):
        """
        value iterator for deep iterations (subitems)

        :param refs: reference flag (include/exclude reference subitems
                    llDict.RefFlag.BOTH - all items
                    llDict.RefFlag.ONLY - only referenced items
                    llDict.RefFlag.EXCL - only local items
        :param keep_ref: Keep the references
        :type: boolean
        :return: value iterator
        """
        for key, value in self._iter_items(deep=True, refs=refs, keep_ref=keep_ref):
            yield value

    def keys_deep(self, refs=INCL_REF):
        """
        key iterator for deep iterations (subitems)

        :param refs: reference flag (include/exclude reference subitems
                    llDict.RefFlag.BOTH - all items
                    llDict.RefFlag.ONLY - only referenced items
                    llDict.RefFlag.EXCL - only local items
        :return: key iterator - key is given as key_list
        """
        for key, value in self._iter_items(deep=True, refs=refs):
            yield key

    # getters

    def get_data(self):
        """
        Delivers the data object of the element

        :status: tested

        :return: data object
        :rtype: object

        """
        return self.data

    def get_parent(self):
        """
        Delivers parent llDict of the current object
        HINT: referenced parents are converted to llDict

        :return: parent llDict
        :rtype: llDict

        """
        if self.parent.weakref_parent is not None:
            return self.parent.weakref_parent()
        else:
            return None

    def get(self, key, default=None, keep_ref=False):
        """
        Get key related value data

        :param key: item key
        :param default: default value that is given back
        :param keep_ref: if item is llDict._WeakRef the value is given back as this object
        :return: item value
        :rtype: llDict
        """
        if key not in self:
            return default
        value = self[key]
        if value is None:
            return value
        if self.is_ref_child(key):
            if keep_ref:
                return super(llDict, self).__getitem__(key)
            value.is_ref = True
        return value

    def get_deep(self, key_list, default=None, keep_ref=False, _is_ref=False):
        """
        Deep get key_list related value data

        :param key_list: item key_list
        :type key_list: list
        :param default: default value that is given back
        :param keep_ref: if item is llDict._WeakRef the value is given back as this object
        :param _is_ref: internal parameter for recursive execution
        :return: item value
        :rtype: llDict
        """
        if (type(key_list) is str) or not hasattr(key_list,'__iter__'):
            raise SyntaxError('Error: The value of parameter key_list (%s) must be of type list or tuple or at least an iterable' % repr(key_list))
        length = len(key_list)
        if length == 0:
            return default
        if not key_list[0] in self:
            return default
        i_value = super(llDict, self).__getitem__(key_list[0])
        real_value = i_value
        is_ref = False
        if isinstance(i_value, llDict._WeakRef):
            real_value = i_value()
            is_ref = True
        if _is_ref:
            is_ref = True
        if length == 1:
            if keep_ref:
                i_value.is_ref = is_ref
                return i_value
            else:
                real_value.is_ref = is_ref
                return real_value
        else:
            value = real_value.get_deep(key_list[1:], default=default, keep_ref=keep_ref, _is_ref=is_ref)
        return value

    # key getters:

    def get_self_key(self):
        """
        Delivers key in the parent llDict of the current object

        :return: parent llDict
        :rtype: llDict
        """
        return self.parent.child_key

    def get_first_key(self):
        """
        Delivers first key of the linked list

        :return: key_string
        :rtype: string
        """
        try:
            i=iter(super(llDict, self).keys()).__next__()
        except StopIteration:
            return None
        return i

    def get_last_key(self):
        """
        Delivers last key of the linked list

        :return: key_string
        :rtype: string
        """
        keys_iterator = super(llDict, self).keys()
        keys_list = list(keys_iterator)
        return keys_list[-1] if len(keys_list) != 0 else None

    def get_pre_key(self, key):
        """
        Delivers pre key before the given key of the linked list

        Returns None if key is first element

        :return: key_string
        :rtype: string/None
        """
        last = None
        for k in super(llDict, self).keys():
            if k == key:
                break
            last = k
        return last

    def get_post_key(self, key):
        """
        Delivers next key after the given key of the linked list

        Returns None if key is last element

        :return: key_string
        :rtype: string/None
        """
        next_key = None
        stop = False
        for k in super(llDict, self).keys():
            if k == key:
                stop = True
                continue
            if stop:
                next_key = k
                break
        return next_key

    # get relative items:
    def get_pre_item(self):
        """
        Delivers pre item relative to this item

        :return: pre item
        :rtype: object
        """
        if self.parent.weakref_parent is None:
            return None
        else:
            pre_key = self.parent.weakref_parent().get_pre_key(self.parent.child_key)
            if pre_key is None:
                return None
            return pre_key, self.parent.weakref_parent()[pre_key]

    def get_post_item(self):
        """
        Delivers post item relative to this item

        :return: post item
        :rtype: object
        """
        if self.parent.weakref_parent is None:
            return None
        else:
            post_key = self.parent.weakref_parent().get_post_key(self.parent.child_key)
            if post_key is None:
                return None
            return post_key, self.parent.weakref_parent()[post_key]

    def get_ref_link(self):
        """
        reads the main reference info (key_path,file_path) and delivers this as a tuple
        :return: tuple with key_path and file_path
        """
        if self.ref is None:
            return None, None
        return self.ref.key_path, self.ref.file_path

    @staticmethod
    def get_version():
        """
        Version of llDict
        :return: version string
        """
        return llDict.VERSION

    # export/import functions

    def gen_exchange_dict(self, sub_dict=None):
        """
        gen exchange dict for data exchange related to llDicts
        :param sub_dict: Give an explicit llDict (or subdict of this lldict) that should been stored into the file
                         None (default) - self is used
        :type sub_dict: llDict/None
        :return:
        """
        if sub_dict is None:
            return llDict.ExchangeDataList(self)
        else:
            return llDict.ExchangeDataList(sub_dict)

    def dumps(self, sub_dict=None, protocol=None, struct_str=False):
        """
        dumps the llDict into a string

        :param sub_dict: Give an explicit llDict (or subdict of this lldict) that should been stored into the file
                         None (default) - self is used
        :type sub_dict: llDict/None
        :param protocol: pickle protocol version that should been used (needed for transfer in older python version)
        :type protocol: integer
        :param struct_str: Flag for generating the structural info string
        :type struct_str: boolean
        :return:
        """
        if sub_dict is None:
            exchange_data_list = llDict.ExchangeDataList(self)
        else:
            exchange_data_list = llDict.ExchangeDataList(sub_dict)
        if protocol is None:
            back = pickle.dumps(exchange_data_list)
        else:
            back = pickle.dumps(exchange_data_list, protocol=protocol)
        if struct_str:
            return back + bytes('\n' + llDict.STRUCT_TAG + '\n%s' % exchange_data_list.get_file_repr(), encoding='UTF8')
        return back

    def dump(self, file_path, overwrite=False, sub_dict=None, protocol=None, struct_str=True):
        """
        dumps the llDict into a file
        :param file_path: file_path where the llDict should been stored in
        :type file_path: string
        :param overwrite: Flag for overwriting an existing file (if not set an exception will be raised in case of the
        file exists already)
        :type overwrite: boolean
        :param sub_dict: Give an explicit llDict (or subdict of this lldict) that should been stored into the file
                         None (default) - self is used
        :type sub_dict: llDict/None
        :param protocol: pickle protocol version that should been used (needed for transfer in older python version)
        :type protocol: integer
        :param struct_str: Flag for generating the structural info string
        :type struct_str: boolean
        :return:
        """
        if os.path.exists(file_path):
            if not overwrite:
                raise FileExistsError('Error: File %s already exists!' % file_path)
        back = self.dumps(sub_dict=sub_dict, protocol=protocol, struct_str=struct_str)
        with open(file_path, 'wb') as fh:
            fh.write(back)
        return file_path

    @staticmethod
    def create_from_string(pickle_str, load_refs=True):
        """
        constructions the llDict object based on the pickled serialized string given as a parameter
        :param pickle_str: pickle string containing the serialization of the object
        :type pickle_str: string
        :param load_refs: We can stop loading references during load if parameter is set to False
                          True (default) - references are loaded
                          False - references not loaded
        :type load_refs: boolean
        :return: llDict object that is constructed from the pickle string
        """
        i = pickle_str.find(bytes('\n%s\n' % llDict.STRUCT_TAG, 'UTF8'))
        if i != -1:
            pickle_str = pickle_str[:i]
        else:
            i = pickle_str.find(bytes('\n%s\n' % llDict.STRUCT_TAG, 'ASCII'))
            if i != -1:
                pickle_str = pickle_str[:i]
        back = pickle_str
        new_lldict = pickle.loads(back).create_lldict(load_refs=False)
        if load_refs:
            new_lldict.update_reference(True)
        return new_lldict

    @staticmethod
    def create_from_file(file_path, load_refs=True, load_function=None):
        """
        loads an llDict object from a file
        :param file_path: file_path to the file that should been loaded
        :type file_path: string
        :param load_refs: We can stop loading references during load if parameter is set to False
                          True (default) - references are loaded
                          False - references not loaded
        :load_function: set function to use for loading instead of internal one
        :type load_function:
        :return:
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError('Error: File %s not found!' % file_path)
        abs_file_path = os.path.abspath(file_path)
        if load_function is not None:
            new_lldict = load_function(abs_file_path, target_version=llDict.VERSION)
            return new_lldict
        with open(file_path, 'rb') as fh:
            back = fh.read()
        try:
            new_lldict = llDict.create_from_string(back, load_refs=False)
            new_lldict._set_source_file_path(abs_file_path)
            if load_refs:
                new_lldict.update_reference(True)
        except:
            print('Error: Cannot unpickle file: %s' % repr(file_path))
            raise
        return new_lldict


if __name__ == '__main__':
    # build a dict:
    group_dict = llDict()
    print(dir(group_dict.__class__))
    group_dict.append(
        group_dict.gen_key('substep'), llDict(data='f1'))
    group_dict.append(
        group_dict.gen_key('substep'), llDict(data='f2'))
    group_dict.append(
        group_dict.gen_key('substep'), llDict(data='f3'))
    group_dict.append(
        group_dict.gen_key('substep'), llDict(data='f4'))
    group_dict.append(
        group_dict.gen_key('substep'), llDict(data='f5'))

    base_dict = llDict()
    base_dict.append(base_dict.gen_key('step'), llDict(data='b1'))
    base_dict.append(base_dict.gen_key('step'), llDict(data='b2'))
    base_dict.append(base_dict.gen_key('group'), group_dict)
    base_dict.append(base_dict.gen_key('step'), llDict(data='b3'))
    base_dict.append(base_dict.gen_key('step'), llDict(data='b4'))
    base_dict.append(base_dict.gen_key('step'), llDict(data='b5'))

    base_dict.get_deep(["group3", "xzc", "qwe"])
    exit(0)
    print('ITERATE')
    for i in base_dict.items():
        print(i)
        print(i[1].data)
    print('ITERATE DEEP:')
    for i in base_dict.items(deep=True):
        print(i)
        print(i[1].has_children())

    print('ITERATE DEEP KEYS:')
    for key in base_dict.keys(deep=True):
        print(key)

    print(base_dict.gen_exchange_dict())

    base_dict.dump('d:/test.cfg', True)
    print(base_dict.create_from_file('d:/test.cfg'))
