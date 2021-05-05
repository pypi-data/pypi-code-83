from .chart import Chart
import networkx as nx
import plotly.graph_objects as go

class Graph(Chart):
    def __init__(self, dataframe):
        """
        Constructs all the necessary attributes for the Tree object

        Parameters:
            dataframe (pandas.Dataframe): The dataframe
        """
        Chart.__init__(self, dataframe)

    def _check_requirements(self):
        """
        Check the requirements for generating tree visualization

        Returns:
            (list) filter_column: list of filter label name
        """
        filter_column = None
        if self._is_uri_column_exist(2):
            filter_column = self._object_column
            if len(self._object_column) < 2:
                filter_column = self._uri_column
        
        return filter_column

    def plot(self):
        """
        Generate graph visualization
        """
        #filter_column
        filter_column = self._check_requirements()

        if filter_column is not None:
            node_list = self.create_node_list(filter_column)
            graph, positions = self.create_graph_nx(filter_column, node_list)
            edge_trace = self.create_edge_trace(graph)
            node_trace = self.create_node_trace(graph)

            annotations = self.add_annotations(graph, positions)

            figure = self.create_figure_go(edge_trace, node_trace, annotations)
            figure.show()
            print(f"{nx.info(graph)}\nDensity graph: {nx.density(graph)}")


    def create_node_list(self, filter_column):
        """
        Create the node list

        Paramaters:
            (list) filter_column: list of source and target name column

        Returns:
            (list) node_list: list of node
        """
        source = list(self.dataframe[filter_column[0]].unique())
        target = list(self.dataframe[filter_column[1]].unique())
        node_list = set (source + target)

        return node_list

    def create_graph_nx(self, filter_column, node_list):
        """
        Create graph networkx

        Paramaters:
            (list) node_list: list of node
            (list) filter_column: list of source and target name column

        Returns:
            (networkx.DiGraph) Graph: Digraph graph
        """
        Graph = nx.DiGraph()

        #add node to graph
        for node in node_list:
            Graph.add_node(node)
        
        #add edges to graph
        for key, node in self.dataframe.iterrows():
            Graph.add_edges_from([(node[filter_column[0]],node[filter_column[1]])])

        #Getting positions for each node.
        positions = nx.spring_layout(Graph, k=2)

        #Adding positions of the nodes to the graph
        for node, position in positions.items():
            Graph.nodes[node]['position'] = position

        return Graph, positions

    def create_edge_trace(self, Graph):
        """
        Create edge_trace object

        Paramaters:
            (networkx.DiGraph) Graph: Digraph graph        

        Returns:
            (plotly.Scatter) edge_trace: edge_trace object
        """
        edge_trace = go.Scatter(
            x=[],
            y=[],
            line=dict(width=0.5,color='#888'),
            hoverinfo='text',
            mode='lines')

        #Add edges as disconnected lines in a single trace 
        for edge in Graph.edges():
            x0, y0 = Graph.nodes[edge[0]]['position']
            x1, y1 = Graph.nodes[edge[1]]['position']
            edge_trace['x'] += tuple([x0, x1, None])
            edge_trace['y'] += tuple([y0, y1, None])

        return edge_trace

    def create_node_trace(self, Graph):
        """
        Create node_trace object

        Paramaters:
            (networkx.DiGraph) Graph: Digraph graph     

        Returns:
            (plotly.Scatter) node_trace: node_trace object
        """
        node_trace = go.Scatter(
            x=[],
            y=[],
            text=[],
            mode='markers',
            hoverinfo='text',
            marker=dict(
                showscale=True,
                colorscale='Viridis',
                reversescale=True,
                color=[],
                size=12,
                colorbar=dict(
                    thickness=15,
                    title='Node Connections',
                    xanchor='left',
                    titleside='right'
                ),
                line=dict(width=2)))
        
        #Add nodes as a scatter trace
        for node in Graph.nodes():
            x, y = Graph.nodes[node]['position']
            node_trace['x'] += tuple([x])
            node_trace['y'] += tuple([y])

        #Add hover text
        node_trace = self.add_hover_text(Graph, node_trace) 

        return node_trace

    def add_hover_text(self, Graph, node_trace):
        """
        Creating the hover text, that will display the info of node on the figure

        Paramaters:
            (networkx.DiGraph) Graph: Digraph graph 
            (plotly.Scatter) node_trace: node_trace object    

        Returns:
             (plotly.Scatter) node_trace: node_trace object with hover text

        """
        #Create degree dictionary (degree, in_degree, out_degree)
        degree_dict = {}
        for key, value in (Graph.degree()):
            degree_dict.setdefault(key, []).append(value)
        for key, value in (Graph.in_degree()):
            degree_dict.setdefault(key, []).append(value)
        for key, value in (Graph.out_degree()):
            degree_dict.setdefault(key, []).append(value)

        for key, value in enumerate(degree_dict):
            node_trace['marker']['color']+=tuple([(degree_dict[value][0])])
            node_info = str(value) + ', Degree:'+ str(degree_dict[value][0]) + " In:" + str(degree_dict[value][1]) + " Out:" + str(degree_dict[value][2])
            node_trace['text']+=tuple([node_info])
        
        return node_trace

    def add_annotations(self, Graph, positions):
        """
        Creating the annotations, that will display the node name on the figure

        Paramaters:
            (networkx.DiGraph) Graph: Digraph graph
            (dict) positions: dictionary of positions for each node in graph    

        Returns:
            (list) annotations: list of annotations        
        """
        # Creating the annotations, that will display the node name on the figure
        annotations = []
        for node, adjacencies in enumerate(Graph.adjacency()):
            annotations.append(
                dict(x=positions[adjacencies[0]][0],
                    y=positions[adjacencies[0]][1],
                    text=adjacencies[0], # node name that will be displayed
                    xanchor='left',
                    xshift=10,
                    font=dict(color='black', size=11),
                    showarrow=False, arrowhead=1, ax=-10, ay=-10)
                )
        
        return annotations


    def create_figure_go(self, edge_trace, node_trace, annotations):
        """
        Create figure of graph

        Paramaters:
            (plotly.Scatter) node_trace: node_trace object
            (plotly.Scatter) edge_trace: edge_trace object                  

        Returns:
            (list) annotations: list of annotations  
        """
        #Coloring based on the number of connections of each node.
        figure = go.Figure(data=[edge_trace, node_trace],
                    layout=go.Layout(
                        titlefont=dict(size=16),
                        showlegend=False,
                        hovermode='closest', 
                        margin=dict(b=20,l=5,r=5,t=40),
                        annotations=annotations, 
                        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False)))
        return figure

    def _add_info_graph(self, Graph):
        """
        Add infomation of graph

        Paramaters:
            (networkx.DiGraph) Graph: Digraph graph    

        Returns:
            (string) number_of_nodes: number of nodes in graph
            (string) number_of_edges: number of edges in graph
            (string) info_density: information of density graph
        """
        number_of_nodes = Graph.number_of_nodes()
        number_of_edges = Graph.number_of_edges()
        info_density = nx.density(Graph)

        return number_of_nodes, number_of_edges, info_density  

