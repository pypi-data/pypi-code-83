import pandas as pd
import networkx as nx

def get_bigraph(nodetype1, nodetype2, edgetype, neo4j_session):
    """
    Queries a bipartite subgraph of EpigraphDB and returns a Networkx instance of it.
    
    :param nodetype1: (str) The first node type to extract from epigraph.
    :param nodetype2: (str) As above, second node type.
    :param edgetype: (str) A viable edge type between nodetype1 & 2 in EpigraphDB.
    :param neo4j_session: (neo4j.GraphDatabase.driver.session) A Neo4j session.
    
    :return g: (networkx.graph) The target subgraph in Networkx form.
    """

    # Get data from epigraph
    query = f"match({nodetype1.lower()}:{nodetype1})-[:{edgetype}]-({nodetype2.lower()}:{nodetype2}) return {nodetype1.lower()}, {nodetype2.lower()}"
    return_data = neo4j_session.run(query).data()
    output_df = pd.io.json.json_normalize(return_data)

    # Convert returned df to a networkx graph
    attr_dict = {
        nodetype1.lower() : ([col for col in output_df.columns if nodetype1.lower() in col], 0), # Tuple[1] is the id for the distinct parts of the bipartite network
        nodetype2.lower() : ([col for col in output_df.columns if nodetype2.lower() in col], 1)
    }
    g = nx.Graph()
    for _, row in output_df.iterrows():
        node_labels = []
        for node_type in attr_dict.keys():
            node_label = row[node_type + '.label']
            node_labels.append(node_label)
            if node_label not in g.nodes:
                g.add_node(node_label)
                g.nodes[node_label]['bipartite'] = attr_dict[node_type][1] 
                for attribute in attr_dict[node_type][0]:
                    if '.label' not in attribute:
                        g.nodes[node_label][attribute.split('.')[1]] = row[attribute]
        g.add_edge(node_labels[0], node_labels[1])
        
    return g

