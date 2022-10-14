from sinus import *
import pyautogui as p
from pygame import*
#import numpy
from math import*
from block import*
#from chunks import*
from numba import njit

class Chunk:
    def __init__(self,x,y):
        self.coords=[x,y]
        self.vid={}
        self.nevid={}


texture=image.load("texture.png")
#wall_line=texture.subsurface()

#sens=1.5
Schunk=11.3137#22.6274
Scube=0.866#0.707
dal=40
dal16=dal+16
dal16kv=dal16*dal16
dalkv=dal*dal
mas_size=dalkv*30+5

nx=0 #180 norm
ny=0
mx=1918
my=1080
class Window:
    def __init__(self):

        self.chunks=[]
        y=8
        for s1 in range(0,16):
            self.chunks.append([])
            x=8
            for s2 in range(0,16):
                self.chunks[s1].append(Chunk(x,y))
                x+=16
            y+=16


        # for i in range(16, 32):
        #    for j in range(16,32):
        #        self.chunks[1][1].vid[(i,64,j)]=1


        temp=2
        for i in range(0,16):
            for j in range(0,16):
                for k in range(-8,8):
                    if (temp==1):
                        temp=2
                    else:
                        temp=1
                    for z in range(-8,8,temp):
                        self.chunks[i][j].vid[(self.chunks[i][j].coords[0]+k,63 ,self.chunks[i][j].coords[1]+z)]=\
                            Block((self.chunks[i][j].coords[0]+k,63 ,self.chunks[i][j].coords[1]+z),1)
        # for i in range(0,16):
        #     for j in range(0,16):
        #         for k in range(30,120):
        #             for z in range(-8,8,2):
        #                 self.chunks[i][j].vid[(self.chunks[i][j].coords[0],k ,self.chunks[i][j].coords[1]+z)]=\
        #                     Block((self.chunks[i][j].coords[0]+k,63 ,self.chunks[i][j].coords[1]+z),1)

        for i in range(0,16):
            for j in range(0,16):
                for el in self.chunks[i][j].vid:
                    self.chunks[i][j].vid[el].neigh=[]
                    if (el[0]-1,el[1],el[2]) in self.chunks[i][j].vid:
                        self.chunks[i][j].vid[el].neigh.append([el[0]-1,el[1],el[2]])
                    else:
                        self.chunks[i][j].vid[el].neigh.append(False)
                    if (el[0]+1,el[1],el[2]) in self.chunks[i][j].vid:
                        self.chunks[i][j].vid[el].neigh.append([el[0]+1,el[1],el[2]])
                    else:
                        self.chunks[i][j].vid[el].neigh.append(False)
                    if (el[0],el[1]-1,el[2]) in self.chunks[i][j].vid:
                        self.chunks[i][j].vid[el].neigh.append([el[0],el[1]-1,el[2]])
                    else:
                        self.chunks[i][j].vid[el].neigh.append(False)
                    if (el[0],el[1]+1,el[2]) in self.chunks[i][j].vid:
                        self.chunks[i][j].vid[el].neigh.append([el[0],el[1]+1,el[2]])
                    else:
                        self.chunks[i][j].vid[el].neigh.append(False)
                    if (el[0],el[1],el[2]-1) in self.chunks[i][j].vid:
                        self.chunks[i][j].vid[el].neigh.append([el[0],el[1],el[2]-1])
                    else:
                        self.chunks[i][j].vid[el].neigh.append(False)
                    if (el[0],el[1],el[2]+1) in self.chunks[i][j].vid:
                        self.chunks[i][j].vid[el].neigh.append([el[0],el[1],el[2]+1])
                    else:
                        self.chunks[i][j].vid[el].neigh.append(False)






        # for i in range(0,16):
        #     for j in range(0,16):
        #         self.chunks[i][j].vid[(self.chunks[i][j].coords[0]+0.5,60 ,self.chunks[i][j].coords[1]+0.5)]=1
        #         self.chunks[i][j].vid[(self.chunks[i][j].coords[0] + 0.5, 60, self.chunks[i][j].coords[1] + 2.5)] = 1

        self.n0=[0,0,1]
        self.n1=[[-0.68,0,0.73],[0.68,0,0.73]]
        self.n2=[[0,-0.858,0.515],[0,0.858,0.515]]
        self.run=True
        self.gradv=0
        self.gradg=0
        self.plcoords=[0,65,0]#[128,-64,128]
        p.moveTo(850, 550)


        self.fps = 200
        init()
        mouse.set_pos(850, 550)
        mixer.init()  # для звука
        self.sc = display.set_mode((0,0),FULLSCREEN|DOUBLEBUF)
        #self.sc=display.set_mode((600,600))
        display.set_caption("Minecraft")
        self.clock = time.Clock()
        mouse.set_visible(False)

        self.full=True
        self.i=0
        self.y=0


    def draw(self):
        fp=self.clock.tick(self.fps)
        if(fp!=0):
            sens=0.05*fp
            sens1=0.0085 *fp
        else:
            sens=1.5
            sens1=0.1
        self.sc.fill((220, 220, 250))

        x,y=mouse.get_pos()
        mouse.set_pos(850, 550)
        if (x!=850 or y!=550):
            if(self.gradv + int((y - 550) * sens) > 4490):
                self.gradv=890
            elif(self.gradv+int((y-550)*sens)<-900):
                self.gradv = 2710
            elif(self.gradv+int((y-550)*sens)>890 and (self.gradv+int((y-550)*sens)<2710)):
                if(self.gradv<900):
                    self.gradv = 890
                else:
                    self.gradv=2710
            else:
                self.gradv+=int((y-550))#*sens)
            self.gradg-=int((x-850))#*sens)
        if(self.gradg<0):
            self.gradg=3600+self.gradg
        if (self.gradv < 0):
            self.gradv=3600+self.gradv
        if(self.gradv>=3600):
            self.gradv%=3600
        if (self.gradg >= 3600):
            self.gradg %= 3600

        self.My = [[1, 0, 0],
                   [0, COS[self.gradv], -SIN[self.gradv]],
                   [0, SIN[self.gradv], COS[self.gradv]]]
        self.Mx = [[COS[self.gradg], 0, SIN[self.gradg]],
                   [0, 1, 0],
                   [-SIN[self.gradg], 0, COS[self.gradg]]]
        self.gradv2=(3600-self.gradv)%3600
        self.gradg2 = (3600 - self.gradg) % 3600
        self.Mx2 = [[COS[self.gradg2], 0, SIN[self.gradg2]],
                   [0, 1, 0],
                   [-SIN[self.gradg2], 0, COS[self.gradg2]]]
        self.Mrez = MuMnozh3(self.My, self.Mx)
        self.Mrez2=MuMnozh3(self.Mx2, self.My)
        self.n0=MuMnozh1(self.Mrez2, [0,0,1], [0,0,0])
        self.n1[0]=MuMnozh1(self.Mrez2, [-0.68,0,0.73], [0,0,0])
        self.n1[1] = MuMnozh1(self.Mrez2, [0.68, 0, 0.73], [0, 0, 0])
        self.n2[0]=MuMnozh1(self.Mrez2, [0,-0.858,0.515], [0,0,0])
        self.n2[1]=MuMnozh1(self.Mrez2, [0,0.858,0.515], [0,0,0])

        x1=(self.plcoords[0]-dal)//16
        x2 = (self.plcoords[0] + dal)//16+1
        z1 = (self.plcoords[2] - dal)//16
        z2 = (self.plcoords[2] + dal)//16+1
        if(x1<0):
            x1=0
        if (x2>15):
            x2 = 15
        if (z1 < 0):
            z1 = 0
        if (z2>15):
            z2 = 15

        mas_cubes = [False]*mas_size
        for q in range(int(z1), int(z2)):
            for j in range(int(x1), int(x2)):
                #self.draw_part_chunk(self.chunks[i][j])

                for i in self.chunks[q][j].vid:
                    a0 = i[0] - self.plcoords[0]
                    a1 = (i[1] - self.plcoords[1])
                    a2 = i[2] - self.plcoords[2]
                    d = a0 * a0 + a1 * a1 + a2 * a2
                    if d >= dalkv:
                        continue
                    c = a0 * self.n0[0] + a1 * self.n0[1] + a2 * self.n0[2]
                    if c <= -Scube + 1.6:
                        continue
                    a = a0 * self.n1[0][0] + a1 * self.n1[0][1] + a2 * self.n1[0][2]
                    if a < -Scube:
                        continue
                    b = a0 * self.n1[1][0] + a1 * self.n1[1][1] + a2 * self.n1[1][2]
                    if b < -Scube:
                        continue
                    aa = a0 * self.n2[0][0] + a1 * self.n2[0][1] + a2 * self.n2[0][2]
                    if aa < -Scube:
                        continue
                    bb = a0 * self.n2[1][0] + a1 * self.n2[1][1] + a2 * self.n2[1][2]
                    if bb < -Scube:
                        continue
                    if not mas_cubes[int(d*30)]:
                        mas_cubes[int(d*30)]=(a0, a1, a2, d, self.chunks[q][j].vid[i], self.chunks[q][j])
                    elif not mas_cubes[int(d * 30+1)]:
                        mas_cubes[int(d * 30+1)] = (a0, a1, a2, d, self.chunks[q][j].vid[i], self.chunks[q][j])
                    elif not mas_cubes[int(d * 30 + 2)]:
                        mas_cubes[int(d * 30 + 2)] = (a0, a1, a2, d, self.chunks[q][j].vid[i], self.chunks[q][j])
                    elif not mas_cubes[int(d * 30 -1)]:
                        mas_cubes[int(d * 30 -1)] = (a0, a1, a2, d, self.chunks[q][j].vid[i], self.chunks[q][j])
                    elif not mas_cubes[int(d * 30 -2)]:
                        mas_cubes[int(d * 30 -2)] = (a0, a1, a2, d, self.chunks[q][j].vid[i], self.chunks[q][j])

                    self.chunks[q][j].vid[i].prvert=[False]*8





        #mas_cubes=Sort(mas_cubes,temp)
        #for i in mas_cubes:
        for z in reversed(range(len(mas_cubes))):#temp):
            if mas_cubes[z]==False:
                continue
            i=mas_cubes[z]
            vect=[i[0],i[1],i[2]]

            r1=0
            g1=220
            b1=0
            r2=170
            g2=100
            b2=10
            if(vect[2]>0.5):
                if( not i[4].neigh[4]):
                    if not i[4].prvert[0]:
                        a = i[4].prvert[0] = self.ProjectVertex(
                            MuMnozh1(self.Mrez, [i[0] + 0.5, -i[1] - 0.5, i[2] - 0.5], self.plcoords))
                    else:
                        a = i[4].prvert[0]
                    if not i[4].prvert[1]:
                        b = i[4].prvert[1] = self.ProjectVertex(
                            MuMnozh1(self.Mrez, [i[0] - 0.5, -i[1] + 0.5, i[2] - 0.5], self.plcoords))
                    else:
                        b = i[4].prvert[1]
                    if not i[4].prvert[2]:
                        c = i[4].prvert[2] = self.ProjectVertex(
                            MuMnozh1(self.Mrez, [i[0] - 0.5, -i[1] - 0.5, i[2] - 0.5], self.plcoords))
                    else:
                        c = i[4].prvert[2]
                    if not i[4].prvert[3]:
                        d = i[4].prvert[3] = self.ProjectVertex(
                            MuMnozh1(self.Mrez, [i[0] + 0.5, -i[1] + 0.5, i[2] - 0.5], self.plcoords))
                    else:
                        d = i[4].prvert[3]
                    draw.polygon(self.sc, (r2,g2,b2), [a,c,b,d])
                    draw.polygon(self.sc, (0,0,0),[a, c, b, d],1)
            elif (vect[2] < -0.5):
                if( not i[4].neigh[5]):
                    if not i[4].prvert[4]:
                        a=i[4].prvert[4]=self.ProjectVertex(MuMnozh1(self.Mrez, [i[0] - 0.5, -i[1] - 0.5, i[2] + 0.5], self.plcoords))
                    else:
                        a = i[4].prvert[4]
                    if not i[4].prvert[5]:
                        b=i[4].prvert[5]=self.ProjectVertex(MuMnozh1(self.Mrez, [i[0] + 0.5, -i[1] + 0.5, i[2] + 0.5], self.plcoords))
                    else:
                        b = i[4].prvert[5]
                    if not i[4].prvert[6]:
                        c=i[4].prvert[6]=self.ProjectVertex(MuMnozh1(self.Mrez, [i[0] + 0.5, -i[1] - 0.5, i[2] + 0.5], self.plcoords))
                    else:
                        c = i[4].prvert[6]
                    if not i[4].prvert[7]:
                        d=i[4].prvert[7]=self.ProjectVertex(MuMnozh1(self.Mrez, [i[0] - 0.5, -i[1] + 0.5, i[2] + 0.5],self.plcoords))
                    else:
                        d = i[4].prvert[7]
                    draw.polygon(self.sc, (r2, g2, b2), [a, c, b, d])
                    draw.polygon(self.sc, (0, 0, 0), [a, c, b, d], 1)
            if(vect[1]<-0.5):
                if(not i[4].neigh[3]):
                    if not i[4].prvert[0]:
                        a=i[4].prvert[0]=self.ProjectVertex(MuMnozh1(self.Mrez, [i[0] + 0.5, -i[1] - 0.5, i[2] - 0.5], self.plcoords))
                    else:
                        a = i[4].prvert[0]
                    if not i[4].prvert[4]:
                        b=i[4].prvert[4]=self.ProjectVertex(MuMnozh1(self.Mrez, [i[0] - 0.5, -i[1] - 0.5, i[2] + 0.5], self.plcoords))
                    else:
                        b = i[4].prvert[4]
                    if not i[4].prvert[2]:
                        c=i[4].prvert[2]=self.ProjectVertex(MuMnozh1(self.Mrez, [i[0] - 0.5, -i[1] - 0.5, i[2] - 0.5],self.plcoords))
                    else:
                        c = i[4].prvert[2]
                    if not i[4].prvert[6]:
                        d=i[4].prvert[6]=self.ProjectVertex(MuMnozh1(self.Mrez, [i[0] + 0.5, -i[1] - 0.5, i[2] + 0.5],self.plcoords))
                    else:
                        d = i[4].prvert[6]
                    draw.polygon(self.sc, (r1, g1, b1), [a, c, b, d])
                    draw.polygon(self.sc, (0, 0, 0), [a, c, b, d], 1)

            elif (vect[1] >0.5):
                if(not i[4].neigh[2]):

                    if not i[4].prvert[1]:
                        a=i[4].prvert[1]=self.ProjectVertex(MuMnozh1(self.Mrez, [i[0] - 0.5, -i[1] + 0.5, i[2] - 0.5], self.plcoords))
                    else:
                        a = i[4].prvert[1]
                    if not i[4].prvert[5]:
                        b=i[4].prvert[5]=self.ProjectVertex(MuMnozh1(self.Mrez, [i[0] + 0.5, -i[1] + 0.5, i[2] + 0.5], self.plcoords))
                    else:
                        b = i[4].prvert[5]
                    if not i[4].prvert[7]:
                        c=i[4].prvert[7]=self.ProjectVertex(MuMnozh1(self.Mrez, [i[0] - 0.5, -i[1] + 0.5, i[2] + 0.5],self.plcoords))
                    else:
                        c = i[4].prvert[7]
                    if not i[4].prvert[3]:
                        d=i[4].prvert[3]=self.ProjectVertex(MuMnozh1(self.Mrez, [i[0] + 0.5, -i[1] + 0.5, i[2] - 0.5],self.plcoords))
                    else:
                        d = i[4].prvert[3]
                    draw.polygon(self.sc, (r2, g2, b2), [a, c, b, d])
                    draw.polygon(self.sc, (0, 0, 0), [a, c, b, d], 1)
            if(vect[0]>0.5):
                if (not i[4].neigh[0]):

                    if not i[4].prvert[4]:
                        a=i[4].prvert[4]=self.ProjectVertex(MuMnozh1(self.Mrez, [i[0] - 0.5, -i[1] - 0.5, i[2] + 0.5], self.plcoords))
                    else:
                        a = i[4].prvert[4]
                    if not i[4].prvert[1]:
                        b=i[4].prvert[1]=self.ProjectVertex(MuMnozh1(self.Mrez, [i[0] - 0.5, -i[1] + 0.5, i[2] - 0.5], self.plcoords))
                    else:
                        b = i[4].prvert[1]
                    if not i[4].prvert[2]:
                        c=i[4].prvert[2]=self.ProjectVertex(MuMnozh1(self.Mrez, [i[0] - 0.5, -i[1] - 0.5, i[2] - 0.5],self.plcoords))
                    else:
                        c = i[4].prvert[2]
                    if not i[4].prvert[7]:
                        d=i[4].prvert[7]=self.ProjectVertex(MuMnozh1(self.Mrez, [i[0] - 0.5, -i[1] + 0.5, i[2] + 0.5],self.plcoords))
                    else:
                        d = i[4].prvert[7]
                    draw.polygon(self.sc, (r2, g2, b2), [a, c, b, d])
                    draw.polygon(self.sc, (0, 0, 0), [a, c, b, d], 1)
            elif(vect[0]<-0.5):
                if (not i[4].neigh[1]):

                    if not i[4].prvert[0]:
                        a=i[4].prvert[0]=self.ProjectVertex(MuMnozh1(self.Mrez, [i[0] + 0.5, -i[1] - 0.5, i[2] - 0.5], self.plcoords))
                    else:
                        a = i[4].prvert[0]
                    if not i[4].prvert[5]:
                        b=i[4].prvert[5]=self.ProjectVertex(MuMnozh1(self.Mrez, [i[0] + 0.5, -i[1] + 0.5, i[2] + 0.5], self.plcoords))
                    else:
                        b = i[4].prvert[5]
                    if not i[4].prvert[6]:
                        c=i[4].prvert[6]=self.ProjectVertex(MuMnozh1(self.Mrez, [i[0] + 0.5, -i[1] - 0.5, i[2] + 0.5],self.plcoords))
                    else:
                        c = i[4].prvert[6]
                    if not i[4].prvert[3]:
                        d=i[4].prvert[3]=self.ProjectVertex(MuMnozh1(self.Mrez, [i[0] + 0.5, -i[1] + 0.5, i[2] - 0.5],self.plcoords))
                    else:
                        d = i[4].prvert[3]
                    draw.polygon(self.sc, (r2, g2, b2), [a, c, b, d])
                    draw.polygon(self.sc, (0, 0, 0), [a, c, b, d], 1)





        for even in event.get():
            if even.type == QUIT:
                self.run = False
        if key.get_pressed()[K_ESCAPE]:
            self.run = False
        if key.get_pressed()[K_w]:
            self.plcoords[2]+=COS[self.gradg]*sens1
            self.plcoords[0]-=SIN[self.gradg]*sens1
        if key.get_pressed()[K_s]:
            self.plcoords[2] -= COS[self.gradg] * sens1
            self.plcoords[0] += SIN[self.gradg] * sens1
        if key.get_pressed()[K_d]:
            self.plcoords[2] += SIN[self.gradg] * sens1
            self.plcoords[0] += COS[self.gradg] * sens1
        if key.get_pressed()[K_a]:
            self.plcoords[2] -= SIN[self.gradg] * sens1
            self.plcoords[0] -= COS[self.gradg] * sens1
        if key.get_pressed()[K_DOWN]:
            self.plcoords[1]-=0.4
        if key.get_pressed()[K_UP]:
            self.plcoords[1]+=0.4



        draw.aaline(self.sc, (255, 0, 0), [0, 6], [int(self.clock.get_fps() * 8), 6])
        draw.aaline(self.sc, (255, 0, 0), [480, 8], [480, 16])#60 fps
        draw.aaline(self.sc, (0, 0, 0), [240, 8], [240, 12])#30 fps
        draw.aaline(self.sc, (0, 0, 255), [800, 8], [800, 12])#100 fps
        draw.aaline(self.sc, (0, 0, 0), [960, 8], [960, 12])#120 fps
        draw.aaline(self.sc, (0, 200, 0), [1600, 8], [1600, 12])#200 fps

        draw.aaline(self.sc, (0, 0, 0), [951, 540], [967, 540])
        draw.aaline(self.sc, (0, 0, 0), [959, 532], [959, 548])  # 200 fps
        display.flip()
        #print("vid= ",self.chunks[1][1].vid)

        #display.set_caption(str(self.clock.get_fps()))

        return self.run



    def ProjectVertex(self,v):
        return [int(959+900*v[0]/v[2]),int(540+900*v[1]/v[2])]
