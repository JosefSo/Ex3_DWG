import random
import sys
from _ast import List

from matplotlib import pyplot as plt

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


    def findInit(self)-> []:
        queue =[]
        for n in self.graph.get_all_v().values():
            n.setWeight(sys.maxsize)
            print(n.getWeight())
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
        while q:
            ni=q.pop()
            gcopy.append(ni)
            if ni.getWeight() < minweight:
                minweight = ni.getWeight()
                key =ni.getId()
        while gcopy:
            q.append(gcopy.pop())
        return key

    def relax (self,src:int,dest:int):
        if self.graph.get_all_v()[src].getWeight()< sys.maxsize:
            if self.graph.get_all_v()[dest].getWeight()>self.graph.get_all_v()[src].getWeight()+self.graph.all_in_edges_of_node(src)[dest]:
                self.graph.get_all_v()[dest].setWeight(self.graph.get_all_v()[src].getWeight()+self.graph.all_in_edges_of_node(src)[dest])
                self.graph.get_all_v()[dest].setTag(src)

    def dijkstra (self,src:int):
        queue = self.findInit()
        self.graph.get_all_v()[src].setWeight(0)
        while queue:
            node=self.graph.get_all_v()[self.ExtractMin(queue)]
            queue.remove(node)
            for d in self.graph.all_in_edges_of_node(node.getId()).keys():
                self.relax(node.getId(),d)


    def shortest_path(self, id1: int, id2: int) -> (float, list):
        stack=[]
        stack.append(self.graph.get_all_v()[id2])
        if id1 == id2:
            return (0,stack)
        self.dijkstra(id1)
        dist=-1
        if self.graph.get_all_v()[id2].getWeight()<sys.maxsize:
            dist=self.graph.get_all_v()[id2].getWeight
        return (dist,stack)

    def TSP(self, node_lst: list[int]) -> (list[int], float):
        pass

    def centerPoint(self) -> (int, float):
        pass

    def plot_graph(self) -> None:
        plt.title("Directed Weighted Graph")
        plt.xlabel("x")
        plt.ylabel("y")
        locations = {}
        for node in self.graph.get_all_v().values():
            if node.getId() in locations.keys():
                x, y, z = locations[node.getId()]
            elif node.getLocation() is None:
                x, y, z = random.uniform(0, 100), random.uniform(0, 100),random.uniform(0, 100)
                locations[node.getId()]=(x,y,z)
            else:
                x, y, z = node.getLocation()
                locations[node.getId()] = (x, y, z)
            plt.plot(x, y, markersize=10, marker='.', color='blue')
            plt.text(x, y, str(node.getId()), color="red", fontsize=10)

            for dest in self.graph.all_in_edges_of_node(node.getId()).items():
                d, w = dest
                if d in locations.keys():
                    his_x, his_y, his_z = locations[d]
                elif self.graph.get_all_v()[d].getLocation() is None:
                    his_x, his_y, his_z = random.uniform(0, 100), random.uniform(0, 100), random.uniform(0, 100)
                    locations[d] = (his_x, his_y, his_z)
                else:
                    his_x, his_y, his_z = self.graph.get_all_v()[d].getLocation()
                    locations[d] = (his_x, his_y, his_z)

                plt.annotate("", xy=(x, y), xytext=(his_x, his_y), arrowprops=dict(arrowstyle="<-"))
                plt.text((x+his_x)/2, (y+his_y)/2, w, color="red", fontsize=5)
        plt.show()