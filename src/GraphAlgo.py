import sys
from _ast import List

from src.DiGraph import DiGraph
from src.GraphAlgoInterface import GraphAlgoInterface
from src.GraphInterface import GraphInterface
import json

from src.Node import Node


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, graph:GraphInterface= DiGraph()):
        self.graph=graph

   # def __init__(self,graph:GraphInterface):
   #     self.graph=graph

    def get_graph(self) -> GraphInterface:
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        with open(file_name, 'r') as f:
            dict = json.load(f)
        nodes = dict.get("Nodes")
        for n in nodes:
            if "pos" in n.keys():
                s = n["pos"].split(",")
                self.graph.add_node((int)(n["id"]), (s[0], s[1], s[2]))
            else:
                self.graph.add_node((int)(n["id"]))
        edges = dict.get("Edges")
        for n in edges:
            self.graph.add_edge((int)(n["src"]), (int)(n["dest"]), (float)(n["w"]))
    def save_to_json(self, file_name: str) -> bool:
        class JsonGraph():
            def __init__(self,g:DiGraph):
                self.Edges = []
                for n in g.get_all_v().values():
                    for d,w in g.all_in_edges_of_node(n.getId()).items():
                        edge = {}
                        edge["src"] = n.getId()
                        edge["w"] = w
                        edge["dest"] = d
                        self.Edges.append(edge)
                self.Nodes = []
                for n in g.get_all_v().values():
                    node = {}
                    if (n.getLocation() is not None):
                        x, y, z = n.getLocation()
                        node["pos"] = f"{x},{y},{z}"
                    node["id"] = n.getId()
                    self.Nodes.append(node)

        toSave = JsonGraph(self.graph)
        with open(file_name,"w") as f:
            json.dump(toSave,fp=f,indent=4,default=lambda o:o.__dict__)


    def findInit(self,g1:GraphInterface)-> []:
        queue =[]
        for n in g1.get_all_v().values():
            n.setWeight(float(sys.maxsize))
            n.setTag(-sys.maxsize)
            n.setInfo("")
            queue.append(n)
        return queue;
    def ExtractMin(self, q:[])->int:
        gcopy=[]
        ni=q.pop()
        gcopy.append(ni)
        minweight=ni.getWeight()
        key= ni.getId()
        while len(q)>0:
            ni=q.pop()
            gcopy.append(ni)
            if ni.getWeight()<minweight:
                minweight = ni.getWeight()
                key =ni.getId()
        while len(gcopy)>0:
            q.append(gcopy.pop())
        return key

    def relax (self,g1:GraphInterface,src:int,dest:int):
        if g1.get_all_v()[src].getWeight()<float(sys.maxsize) and g1.get_all_v()[dest].getWeight()<g1.get_all_v()[src].getWeight()+g1.all_in_edges_of_node(src)[dest]:
            g1.get_all_v()[dest].setWeight(g1.get_all_v()[src].getWeight()+g1.all_in_edges_of_node(src)[dest])
            g1.get_all_v()[dest].setTag(src)

    def dijkstra (self, g1:GraphInterface,src:int):
        queue = self.findInit(g1)
        g1.get_all_v()[src].setWeight(0)
        while len(queue)>0:
            node=g1.get_all_v()[self.ExtractMin(queue)]
            queue.remove(node)
            for d in g1.all_in_edges_of_node(node.getId()).keys():
                self.relax(g1,node.getId(),d)


    def shortest_path(self, id1: int, id2: int) -> (float, list):
        stack=[]
        stack.append(self.graph.get_all_v()[id2])
        if id1 == id2:
            return (0,stack)
        self.dijkstra(self.graph,id1)
        dist=-1
        if self.graph.get_all_v()[id2].getWeight==float(sys.maxsize):
            dist=self.graph.get_all_v()[id2].getWeight
        return (dist,stack)

    def TSP(self, node_lst: list[int]) -> (list[int], float):
        pass

    def centerPoint(self) -> (int, float):
        pass

    def plot_graph(self) -> None:
        pass