from src.Edge import Edge
from src.GraphInterface import GraphInterface
from src.Node import Node


class DiGraph(GraphInterface):

   # def __init__(self, nodes:dict,edges:dict):
   #     self.nodes=nodes
   #     self.edges=edges
   #     self.mc=0
    def __init__(self,nodes={},edges={}):
        self.nodes=nodes
        self.edges=edges
        self.mc=0
    def __deepcopy__(self, memodict={})->dict:
       g1=DiGraph()
       for node in self.nodes.values():
           g1.nodes[node.getId()]=node
           g1.edges[node.getId()] = {}
           for edge in self.edges[node.getId()].keys():
               g1.edges.get(node.getId())[edge]=self.edges.get(node.getId()).get(edge)
       d={}
       d[0]=g1
       return d

    def v_size(self) -> int:
        return len(self.nodes)

    def e_size(self) -> int:
        return len(self.edges)

    def get_all_v(self) -> dict:
        return self.nodes


    def all_in_edges_of_node(self, id1: int) -> dict:
        allin={}
        for i in self.edges[id1].keys():
            if isinstance(self.edges.get(id1).get(i),Edge):
                if self.edges.get(id1).get(i) is not None:
                     allin[i]= self.edges.get(id1).get(i).getWeight()
        return allin


    def all_out_edges_of_node(self, id1: int) -> dict:
        allout={}
        for i in self.edges.keys():
            if isinstance(self.edges.get(i).get(id1), Edge):
                 if self.edges.get(i).get(id1) is not None:
                     allout[i]=self.edges.get(i).get(id1).getWeight()
        return allout

    def get_mc(self) -> int:
        return self.mc

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if self.edges.get(id1).get(id2) is None and id1 in self.nodes and id2 in self.nodes:
             edge=Edge(id1,weight,id2)
             self.edges.get(id1)[id2]=edge
             return True
        return False

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if self.nodes.get(node_id) is None:
            node = Node(node_id, pos)
            self.nodes[node_id]=node
            self.edges[node_id]={}
            return True
        return False

    def remove_node(self, node_id: int) -> bool:
        if self.nodes[node_id] is None:
            return False
        del self.nodes[node_id]
        del self.edges[node_id]
        return True

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if self.edges.get(node_id1)[node_id2] is None:
            return False
        del self.edges.get(node_id1)[node_id2]
        return True


