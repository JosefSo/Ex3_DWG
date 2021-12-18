class Edge:
    def __init__(self, src:int, dest:int, tag: int, weight: float, info: str):
        self.src = src
        self.dest = dest
        self.tag = tag
        self.weight = weight
        self.info = info

    def __init__(self, src:int, weight: float, dest:int):
        self.src = src
        self.weight = weight
        self.dest = dest
        self.tag = 0
        self.info = ""

    def getSrc(self) -> int:
        return self.src

    def getDest(self) -> int:
        return self.dest

    def getWeight(self) -> float:
        return self.weight


    def getInfo(self) -> str:
        return self.info

    def setInfo(self, info: str):
        self.info - info

    def getTag(self) -> int:
        return self.tag

    def setTag(self, tag: int):
        self.tag = tag