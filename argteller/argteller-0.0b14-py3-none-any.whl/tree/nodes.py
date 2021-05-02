from .base_node import BaseNode

import collections

class MessengerNode():

    def __init__(self, fail_not_messaged=None, used_conditional_params=None):

        self.fail_not_messaged = fail_not_messaged
        self.used_conditional_params = used_conditional_params

class ArgTree(BaseNode):
    
    def __init__(self, name=None, depth=None):
        super(ArgTree, self).__init__(name, depth, node_type='tree')

        self.total_num_missing_args = 0
        self.tested_topics = []
        self.used_conditional_params = []

    def traverse_tree_find_used_params(self):

        self.used_conditional_params = []

        self.messenger_node_pre = MessengerNode(used_conditional_params=self.used_conditional_params)

        ArgTree._traverse_tree_find_used_params(self, self.messenger_node_pre)

    @staticmethod
    def _traverse_tree_find_used_params(self, messenger_node):

        if self.has_topics():  # perhaps change it to checking the type of the node for stronger contract

            for topic in self.topics:
                
                ArgTree._traverse_tree_find_used_params(topic, messenger_node=messenger_node)
                    
        if self.has_params() and (self.node_type=='topic' or self.node_type=='avail' or 
            (self.node_type=='cond' and self.value==True)):

            missing_required_arguments = []
            for param in self.params:
                if param.value is None:
                    missing_required_arguments.append(param.name)

            if len(missing_required_arguments)>0 and self.node_type=='avail':

                for param in self.params:

                    messenger_node.used_conditional_params.append([param.name, param.preset_value])

            for param in self.params:

                if param.name in missing_required_arguments:
                
                    ArgTree._traverse_tree_find_used_params(param, messenger_node=messenger_node)

                else:
                    ArgTree._traverse_tree_find_used_params(param, messenger_node=messenger_node)
                
        if self.has_avails() and self.node_type=='param':
            
            for avail in self.avails:
                
                if self.value == avail.name:  # checks the avails!

                    ArgTree._traverse_tree_find_used_params(avail, messenger_node=messenger_node)

        if self.has_examples() and self.node_type=='param':
            
            for example in self.examples:

                ArgTree._traverse_tree_find_used_params(example, messenger_node=messenger_node)

        if self.has_options():
            
            for option in self.options:
                
                ArgTree._traverse_tree_find_used_params(option, messenger_node=messenger_node)

    def traverse_tree_tell(self):
        
        self.messenger_node = MessengerNode(used_conditional_params=self.used_conditional_params)

        ArgTree._traverse_tree_tell(self, False, self.messenger_node)
        ArgTree._traverse_tree_tell_options(self, self.messenger_node)

    @staticmethod
    def _traverse_tree_tell_options(self, messenger_node=None):

        if self.has_topics():

            for topic in self.topics:

                if topic not in self.tested_topics:
                    return

                ArgTree._traverse_tree_tell_options(topic, messenger_node)

        if self.has_params() and (self.node_type=='topic' or self.node_type=='avail'):

            missing_required_arguments = []
            for param in self.params:
                if param.value is None:
                    missing_required_arguments.append(param.name)

            for param in self.params:

                ArgTree._traverse_tree_tell_options(param, messenger_node)

        if self.has_avails() and self.node_type=='param':

            for avail in self.avails:
                
                ArgTree._traverse_tree_tell_options(avail, messenger_node)

        if self.has_examples() and self.node_type=='param':
            
            for example in self.examples:

                ArgTree._traverse_tree_tell_options(example, messenger_node)

        if self.has_options():

            missing_optional_arguments = []

            for option in self.options:

                used_param_names = [elem[0] for elem in messenger_node.used_conditional_params]

                if option.name in used_param_names:
                    continue

                if option.value is None:
                    missing_optional_arguments.append(option.name)

            if len(missing_optional_arguments) > 0:

                print('\nOptional argument(s) for {}:\n\n\u25BA {}'.format(self.name, '  '.join(missing_optional_arguments)))


            for option in self.options:

                ArgTree._traverse_tree_tell_options(option, messenger_node)

    @staticmethod
    def _traverse_tree_tell(self, missing=False, messenger_node=None):

        num_missing_args = 0
        
        
        if self.has_topics():  # perhaps change it to checking the type of the node for stronger contract
        
            for topic in self.topics:

                self.tested_topics.append(topic)

                print("\u2714 Checking {} requirements...     ".format(
                    topic.name), end="", flush=True)
                
                messenger_node.fail_not_messaged=True
                num_missing_args = ArgTree._traverse_tree_tell(topic, messenger_node=messenger_node)

                self.total_num_missing_args += num_missing_args

                if num_missing_args > 0:

                    return 

                else:
                    print('Passed!')
                    
                
        if self.has_params() and (self.node_type=='topic' or self.node_type=='avail' or 
            (self.node_type=='cond' and self.value==True)):

            num_missing_args = 0

            missing_required_arguments = []
            for param in self.params:
                if param.value is None:
                    missing_required_arguments.append(param.name)


            num_missing_args += len(missing_required_arguments)

            if len(missing_required_arguments)>0 and self.node_type=='topic':

                if messenger_node.fail_not_messaged:
                    print("Failed!")
                    messenger_node.fail_not_messaged = False

                print('\nRequired argument(s):\n\n\u25BA {}'.format('  '.join(missing_required_arguments)))

            elif len(missing_required_arguments)>0 and self.node_type=='cond':

                if messenger_node.fail_not_messaged:
                    print("Failed!")
                    messenger_node.fail_not_messaged = False

                print('\nRequired argument(s) for [ {} ] option:\n\n\u25BA {}'.format(self.name, '  '.join(missing_required_arguments)))

            elif len(missing_required_arguments)>0 and self.node_type=='avail':

                if messenger_node.fail_not_messaged:
                    print("Failed!")
                    messenger_node.fail_not_messaged = False

                print('\nRequired argument(s) for [ {} ] {}:\n\n\u25BA {}'.format(
                    self.name, self.param, '  '.join(missing_required_arguments)))

            for param in self.params:

                num_missing_args_from_below = 0

                if param.name in missing_required_arguments:
                
                    num_missing_args_from_below = ArgTree._traverse_tree_tell(param, True, messenger_node=messenger_node)

                else:
                    num_missing_args_from_below = ArgTree._traverse_tree_tell(param, False, messenger_node=messenger_node)


                if num_missing_args_from_below is None:

                    num_missing_args_from_below = 0

                num_missing_args += num_missing_args_from_below

        if self.has_avails() and self.node_type=='param':

            available_arguments = []

            num_missing_args = 0
            
            for avail in self.avails:

                available_arguments.append(avail.name)
                
                if self.value == avail.name:  # checks the avails!

                    num_missing_args_from_below = ArgTree._traverse_tree_tell(avail, messenger_node=messenger_node)

                    if num_missing_args_from_below is None:
                        num_missing_args_from_below = 0

                    num_missing_args += num_missing_args_from_below

            if missing:
                print('\nAvailable [ {} ] options:\n\n'
                      '\u25BA {}'.format(self.name, '  '.join(available_arguments)))

            return num_missing_args

        if self.has_examples() and self.node_type=='param':
            
            for example in self.examples:

                if missing:
                    print('\nExamples for [ {} ]: {}'.format(self.name, example.name))

                ArgTree._traverse_tree_tell(example, messenger_node=messenger_node)
                
        if self.has_options():
            
            for option in self.options:
                
                ArgTree._traverse_tree_tell(option, messenger_node=messenger_node)

        if num_missing_args is not None:
            return num_missing_args
        else:
            return 0
        
class TopicNode(BaseNode):
    
    def __init__(self, name, depth):
        super(TopicNode, self).__init__(name, depth, node_type='topic')
        
class ParamNode(BaseNode):
    
    def __init__(self, name, depth):
        super(ParamNode, self).__init__(name, depth, node_type='param')

        self._is_preset = False
        self.preset_value = None

    def set_value(self, value):

        self.value = value

    def has_value(self):

        return self.value is None

    def set_preset_value(self, preset_value):

        self.preset_value = preset_value

    def has_preset_value(self):

        return self.preset_value is None

    def make_preset(self):

        self._is_preset = True

    def is_preset(self):

        return self._is_preset

class CondNode(BaseNode):
    
    def __init__(self, name, depth):
        super(CondNode, self).__init__(name, depth, node_type='cond')

    def set_value(self, value):

        self.value = value

    def has_value(self):

        return self.value is None
        

class AvailNode(BaseNode):
    
    def __init__(self, name, depth):
        super(AvailNode, self).__init__(name, depth, node_type='avail')

        self.param = None

    def set_param(self, value):

        self.param = value

    def has_param(self):

        return self.param is not None
        
class ExampleNode(BaseNode):
    
    def __init__(self, name, depth):
        super(ExampleNode, self).__init__(name, depth, node_type='example')
