class Block:
    def __init__(self,coords,type):
        self.vertex=[]
        self.coords=coords
        self.prvert=[False]*8
        if type==1:
            self.vertex.append([coords[0] - 0.5, -coords[1] + 0.5, coords[2] - 0.5])
            self.vertex.append([coords[0] + 0.5, -coords[1] + 0.5, coords[2] - 0.5])
            self.vertex.append([coords[0] + 0.5, -coords[1] - 0.5, coords[2] - 0.5])
            self.vertex.append([coords[0] - 0.5, -coords[1] - 0.5, coords[2] - 0.5])
            self.vertex.append([coords[0] - 0.5, -coords[1] + 0.5, coords[2] + 0.5])
            self.vertex.append([coords[0] + 0.5, -coords[1] + 0.5, coords[2] + 0.5])
            self.vertex.append([coords[0] + 0.5, -coords[1] - 0.5, coords[2] + 0.5])
            self.vertex.append([coords[0] - 0.5, -coords[1] - 0.5, coords[2] + 0.5])

            # self.vertex.append([coords[0] - 0.5, coords[1] + 0.5, coords[2] - 0.5])
            # self.vertex.append([coords[0] + 0.5, coords[1] + 0.5, coords[2] - 0.5])
            # self.vertex.append([coords[0] + 0.5, coords[1] - 0.5, coords[2] - 0.5])
            # self.vertex.append([coords[0] - 0.5, coords[1] - 0.5, coords[2] - 0.5])
            # self.vertex.append([coords[0] - 0.5, coords[1] + 0.5, coords[2] + 0.5])
            # self.vertex.append([coords[0] + 0.5, coords[1] + 0.5, coords[2] + 0.5])
            # self.vertex.append([coords[0] + 0.5, coords[1] - 0.5, coords[2] + 0.5])
            # self.vertex.append([coords[0] - 0.5, coords[1] - 0.5, coords[2] + 0.5])