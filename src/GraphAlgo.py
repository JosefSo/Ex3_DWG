import random
import sys
from _ast import List
import heapq as heap
from collections import defaultdict

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
        with open(file_name+".json","w") as f:
            json.dump(toSave,fp=f,indent=4,default=lambda o:o.__dict__)

    def dijkstra(self, startingNode):
        visited = set()
        parentsMap = {}
        pq = []
        nodeCosts = defaultdict(lambda: float('inf'))
        nodeCosts[startingNode] = 0
        heap.heappush(pq, (0, startingNode))

        while pq:
            # go greedily by always extending the shorter cost nodes first
            _, node = heap.heappop(pq)
            visited.add(node)

            for adjNode, weight in self.graph.all_in_edges_of_node(node).items():
                if adjNode in visited:
                    continue

                newCost = nodeCosts[node] + weight
                if nodeCosts[adjNode] > newCost:
                    parentsMap[adjNode] = node
                    nodeCosts[adjNode] = newCost
                    heap.heappush(pq, (newCost, adjNode))

        return parentsMap, nodeCosts


    def shortest_path(self, id1: int, id2: int) -> (float, list):
        stack=[]
        curr=id2
        stack.append(self.graph.get_all_v()[curr])
        if id1 == id2:
            return (0,stack)
        parentsMap, nodeCosts =self.dijkstra(id1)
        print(len(parentsMap),"bbb",len(nodeCosts),"ccc",len(self.graph.get_all_v()))
        dist = -1
        if str(nodeCosts[id2]) != "inf":
            dist = nodeCosts[id2]
        if dist == -1:
            return (-1, [])
        while curr != id1:
            curr = parentsMap[curr]
            stack.append(self.graph.get_all_v()[curr])
        NodeList=[]
        while(stack):
            NodeList.append(stack.pop())
        return (dist,NodeList)

    def TSP(self, node_lst: list[int]) -> (list[int], float):
        pass

    def centerPoint(self) -> (int, float):
        #if self.graph is None or len(self.graph.get_all_v())==0:
        #    return None
        #for k in self.graph.get_all_v().keys():
        #    parentsMap, nodeCosts = self.dijkstra(k)
        #    break
        #V = len(self.graph.get_all_v())
        #if len(nodeCosts) == V:
        #    center = 0
        #    dist =[]
        #    for i in range (V):
        #       dist[i]=[]
        #       for j in range (V):
        #          dist[i][j].appand(float('inf')*-1)
        #           print(dist[i][j])
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