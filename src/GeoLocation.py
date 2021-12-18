class GeoLocation:
    def __init__(self,x:float,y:float,z:float):
        self.x= float(x)
        self.y = float(y)
        self.z = float(z)
    #def __init__(self,L:GeoLocation):
    #    self.x= float(L.getX())
    #    self.y = float(L.getY())
     #   self.z = float(L.getZ())

    def getX(self)->float:
        return self.x
    def getY(self)->float:
        return self.y
    def getZ(self)->float:
        return self.z
  # def distance(self,g:GeoLocation)->float:
   #     dx=g.getX()=self.x
   #     dy = g.getY() = self.y
   #     dz = g.getZ() = self.z
    def __repr__(self) -> str:
        return f"{self.x},{self.y},{self.z}"

    def __str__(self) -> str:
        return f"{self.x},{self.y},{self.z}"

