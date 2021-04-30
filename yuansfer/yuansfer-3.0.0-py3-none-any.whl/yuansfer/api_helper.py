from yuansfer.exception import InvalidParamsError
import collections

class APIHelper(object):

    @staticmethod
    def merge_dicts(dict1, dict2):
        """Merges two dictionaries into one as a shallow copy.
        Args:
            dict1 (dict): The first dictionary.
            dict2 (dict): The second dictionary.
        Returns:
            dict: A dictionary containing key value pairs
            from both the argument dictionaries. In the case
            of a key conflict, values from dict2 are used
            and those from dict1 are lost.
        """
        temp = dict1.copy()
        temp.update(dict2)
        return temp

    @staticmethod
    def to_dictionary(dictionary):
        """Create a key value pair dictionary
        Args:
            obj: The dictionary.
        Returns:
            dictionary: A ordered dictionary form of the model with properties in
            their API formats.
        """

        # Return the result
        return collections.OrderedDict(sorted(dictionary.items()))

    @staticmethod
    def append_parameters(parameters):
        """Conconcate parameters
        Args:
            parameters (OrderedDict): The parameters to append.
        Returns:
            str: string with appended parameters.
        """
        # Parameter validation
        if parameters is None:
            raise InvalidParamsError('Parameters are missing')

        queryString = ""

        # Loop through all parameters and concatenate the parameter names and values using '=' and '&' character
        for key, value in parameters.items():
            seperator = '&'
            if value is not None:
                queryString += "{0}{1}={2}".format(seperator, key, str(value))
        queryString = queryString[1:]
        return queryString


