from xml.etree import cElementTree as ET
from xml.etree.ElementTree import Element
import os
import time


class XMLReader:

    def __init__(self, file_path, arguments={}):
        self.__file_path = file_path
        self.__arguments = arguments

        if 'tag_path' not in arguments:
            raise Exception('"tag_path" argument is required to parse XML.')

        self.__tag_path = arguments['tag_path']

    def iterate(self, normalize=False):
        """ Iterates over objects specified with "tag_path" argument and yields them one by one. """

        root = ET.parse(self.__file_path).getroot()

        generator = root.iterfind(self.__tag_path)
        for entry in generator:
            if normalize:
                entry = XMLReader.normalize_element(entry, {})
            yield entry

    @staticmethod
    def normalize_element(element: Element, normalized):
        for sub in element:
            is_object = len(sub) > 0
            if is_object:
                if XMLReader.check_if_element_array(sub):
                    normalized = XMLReader.normalize_array_element(sub, normalized)
                else:
                    normalized_temp = XMLReader.normalize_element(sub, {})
                    attrs = sub.attrib
                    if attrs == {}:
                        attrs = None
                    normalized_temp['@attributes'] = attrs
                    normalized[sub.tag] = normalized_temp
            else:
                attrs = sub.attrib
                if attrs == {}:
                    attrs = None
                normalized[sub.tag] = {'@attributes': attrs, 'value': sub.text}

        attrs = element.attrib
        if attrs == {}:
            attrs = None
        normalized['@attributes'] = attrs

        return normalized

    @staticmethod
    def normalize_array_element(element: Element, normalized={}):
        array_tag = element.tag
        array_res = []
        for item in element:
            is_object = len(item) > 0
            if is_object:
                normalized_item = XMLReader.normalize_element(item, {})
            else:
                attrs = item.attrib
                if attrs == {}:
                    attrs = None
                normalized_item = {'@attributes': attrs, 'value': item.text}
            array_res.append(normalized_item)

        attrs = element.attrib
        if attrs == {}:
            attrs = None
        normalized[array_tag] = {'@attributes': attrs, 'value': array_res}

        return normalized

    @staticmethod
    def check_if_element_array(element: Element):
        is_array = True
        first_elem_name = None
        for i, item in enumerate(element):
            if i == 0:
                first_elem_name = item.tag
            else:
                if item.tag != first_elem_name:
                    is_array = False

        return is_array
