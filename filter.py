import re
import networkx as nx
import matplotlib.pyplot as plt
from operator import itemgetter, attrgetter

def main():
    
    cont = open('vemprarua_tweets.csv','r');
    lines = cont.readlines();
    
    # Graph related 
    Graph = nx.MultiGraph();
    #Graph.add_node('#vemprarua');
    
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
            
            #Graph.add_edge('#vemprarua',new_hashtag);
            for sub_hash in sub_list:
                Graph.add_edge(sub_hash,new_hashtag);
        
        print(lowered_reg);
    
    #Graph.add_node('#vemprarua');
    print(Graph.nodes());
    print(Graph.edges());
    #for i in Graph.adjacency_iter():
    #    print (i[0] + ' links to: ');
    #    for j in i[1]:
    #        print('(%s)' % j);
    edgewidth=[];
    composed_object = [];
    for (u,v,d) in Graph.edges(data=True):
        edgewidth.append(len(Graph.get_edge_data(u,v)));
        composed_object.append((u,v,len(Graph.get_edge_data(u,v))));
        #print _tmp_object;
    #print set(composed_object);    
    _sorted = sorted(list(set(composed_object)),reverse=True,key=itemgetter(2));
    twitter_cont = open('relation.txt','w');
    for wid in _sorted:
      print wid;
      twitter_cont.write(str(wid) + "\n");
      
      
    #print Graph.edges();
    #print _tmp_object;
    #  print(Graph[i] + " " + wid); 
    #nodewidth = [s*70 for s in edgewidth];
    #edgewidth = [s+5 for s in edgewidth];
    #nx.draw_networkx_edges(Graph,pos=nx.spring_layout(Graph),alpha=0.3,width=edgewidth, edge_color='m',ax=None);
    #nx.draw_networkx_nodes(Graph,pos=nx.spring_layout(Graph),node_size=nodewidth);
    #nx.draw_networkx_labels(Graph,pos=nx.spring_layout(Graph),fontsize=10);
    #nx.draw(Graph);
    #nx.draw_networkx_nodes(Graph,pos=nx.spring_layout(Graph));
    #nx.draw_networkx_edges(Graph,pos=nx.spring_layout(Graph));
    
    plt.show();
if __name__ == '__main__':
    main();
    