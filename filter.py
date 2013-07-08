import re
import networkx as nx
import matplotlib.pyplot as plt


def main():
    
    cont = open('content_vemprarua.txt','r');
    lines = cont.readlines();
    
    # Graph related 
    Graph = nx.Graph();
    Graph.add_node('#vemprarua');
    
    for line in lines:
        #line = cont.readline();
        reg = re.findall('#[a-zA-Z]+',line);
        
        # Creates a list with lowered results and stripping the main hashtag
        lowered_reg = [l.lower() for l in reg if l.lower() != '#vemprarua'];
        
        # Add nodes to the Graph
        Graph.add_nodes_from(lowered_reg);
        
        for j,new_hashtag in enumerate(lowered_reg):
            #print(str(j)+' '+new_hashtag);
            #print(lowered_reg[j+1:]);
            sub_list = lowered_reg[j+1:];
            
            Graph.add_edge('#vemprarua',new_hashtag);
            for sub_hash in sub_list:
                Graph.add_edge(sub_hash,new_hashtag);
        
        print(lowered_reg);
    
    Graph.add_node('#vemprarua');
    print(Graph.nodes());
    print(Graph.edges());
    nx.draw(Graph);
    plt.show();
if __name__ == '__main__':
    main();
    