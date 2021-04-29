from .nodes import ArgTree
from .nodes import TopicNode
from .nodes import ParamNode
from .nodes import AvailNode
from .nodes import ExampleNode
from .nodes import CondNode
# from .nodes import OptionNode

from collections import defaultdict
import re

class TreeParser():


    def __init__(self):

        self.topic_nodes_dict = dict()
        self.param_nodes_dict = defaultdict(list)
        self.option_nodes_dict = defaultdict(list)

        self.tree = None

    def parse_tree(self, string):
        
        current_topic = None
        current_param = None

        self.tree = ArgTree(name='tree', depth=-2)

        node_count = 0
        current_pos_dict = {}

        uses_tabs = False
        if sum([line.count('\t') for line in string.splitlines()]) > 0:
            uses_tabs = True

        for line in string.splitlines():

            if uses_tabs:
                depth = line.count('\t')
            else:
                num_white_spaces = len(line) - len(line.lstrip(' '))
                depth = int(num_white_spaces/4)

            line = line.strip()

            if line=='':
                continue
            if line[0] == '-':
                node_type = 'param'
            elif line[0] == '+':
                node_type = 'option'
            elif line[0:2] == '==':
                node_type = 'example'
            elif line[0] == '=':
                node_type = 'avail'
            elif line[0] == '?':
                node_type = 'cond'
            else:
                node_type = 'topic'


            name = re.sub('^[\s=+-?]+', '', line)

            if node_type=='topic':

                if name != current_topic:
                    current_topic = name
                    topic_node = TopicNode(name, depth=-1)
                    self.tree.add_topic(topic_node)

                    current_pos_dict[-1] = topic_node

                    self.topic_nodes_dict[name] = topic_node

            elif node_type=='param':


                if ':' in name:
                    

                    name, value = name.split(':')
                    value = eval(value)

                else:
                    value = None

                # print(name)

                if name in self.param_nodes_dict:

                    for node in self.param_nodes_dict[name]:

                        value = node.value




                current_param = name

                prev_node = current_pos_dict[depth-1]

                current_node = ParamNode(name, depth)
                prev_node.add_param(current_node)

                current_pos_dict[depth] = current_node

                if value is not None:

                    current_node.set_value(value)
                    value = None

                    # print(current_node.name, current_node.value)


                self.param_nodes_dict[name].append(current_node)

            elif node_type=='cond':


                if name in self.param_nodes_dict:

                    for node in self.param_nodes_dict[name]:

                        value = node.value
                        




                current_param = name

                prev_node = current_pos_dict[depth-1]

                current_node = CondNode(name, depth)
                prev_node.add_param(current_node)

                current_pos_dict[depth] = current_node

                if value is not None:

                    current_node.set_value(value)
                    value = None


                self.param_nodes_dict[name].append(current_node)


            elif node_type=='avail':

                prev_node = current_pos_dict[depth-1]

                current_node = AvailNode(name, depth)
                current_node.set_param(current_param)

                prev_node.add_avail(current_node)

                current_pos_dict[depth] = current_node

            elif node_type=='example':

                prev_node = current_pos_dict[depth-1]

                current_node = ExampleNode(name, depth)
                prev_node.add_example(current_node)

                current_pos_dict[depth] = current_node

            elif node_type=='option':

                prev_node = current_pos_dict[depth-1]

                current_node = ParamNode(name, depth)
                prev_node.add_option(current_node)

                current_pos_dict[depth] = current_node

                self.option_nodes_dict[name].append(current_node)
                
        return self.tree


