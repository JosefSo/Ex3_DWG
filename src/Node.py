
class Node:
    def __init__(self, weight:float,id:int,tag:int,pos:tuple,info:str):
       self.eout,self.ein=0,0
       self.weight = weight
       self.id = id
       x, y, z = pos
       if pos is not None:
           x, y, z = pos
           self.pos = float(x), float(y), float(z)
       else:
           self.pos = None
       self.info = info
       self.tag = tag

    def __init__(self, node_id: int, pos: tuple=None):
        self.eout, self.ein = 0, 0
        self.weight = 0
        self.id = node_id
        if pos is not None:
            x,y,z=pos
            self.pos = float(x),float(y),float(z)
        else:
            self.pos = None
        self.info = ""
        self.tag = 0



    def getWeight(self) ->float:
        return self.weight
    def setWeight(self,weight:float):
        self.weight=weight

    def getId(self) ->int:
        return self.id
    def setId(self,id:int):
        self.id=id

    def getLocation(self) ->tuple:
        return self.pos
    def setLocation(self,x:float,y:float,z:float):
        self.pos=(x,y,z)

    def getInfo(self) ->str:
        return self.info
    def setInfo(self,info:str):
        self.info=info

    def getTag(self) ->int:
        return self.tag
    def setTag(self,tag:int):
        self.tag=tag

    def __repr__(self):
        return f"{self.id}: |edges_out| {self.eout} |edges in| {self.ein}"