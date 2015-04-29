from . agents import *

class AgentOrange(Agent):
    def __init__(self):
        Agent.__init__(self)
        self.img="agent_v3.png"
        self.x=0
        self.y=0
        self.prev="GoEast"
        self.walls=list()
        self.visited=dict()
        self.reachDest=list()
        self.toEnd=50
        def program((status, bump)):
            if self.prev!="NoOp":
                if status=="Dirty":
                    self.toEnd=50
                    return "Suck"
                elif bump=="Bump":
                    self.toEnd-=1
                    self.walls.append((self.x,self.y))
                    if self.prev=="GoEast":
                        self.y+=1
                    elif self.prev=="GoWest":
                        self.y-=1
                    elif self.prev=="GoSouth":
                        self.x-=1
                    elif self.prev=="GoNorth":
                        self.x+=1
                    return self.findNextMove()
                else:
                    self.toEnd-=1
                    if self.reachDest==[]:
                        if (self.x,self.y) not in self.visited.keys():
                            count=0   
                            if (self.x-1,self.y) in self.visited.keys() or (self.x-1,self.y) in self.walls:
                                count+=1
                            if (self.x+1,self.y) in self.visited.keys() or (self.x+1,self.y) in self.walls:
                                count+=1
                            if (self.x,self.y-1) in self.visited.keys() or (self.x,self.y-1) in self.walls:
                                count+=1
                            if (self.x,self.y+1) in self.visited.keys() or (self.x,self.y+1) in self.walls:
                                count+=1
                            self.visited[(self.x,self.y)]=count
                        return self.findNextMove()
                    else:
                        move=self.reachDest[0]
                        self.prev=move
                        if move=="GoEast":
                            self.y-=1
                        elif move=="GoWest":
                            self.y+=1
                        elif move=="GoSouth":
                            self.x+=1
                        else:
                            self.x-=1
                        self.reachDest=self.reachDest[1:]
                        return move
            else:
                return "NoOp"
        self.program = program
        
        def findNextMove():
            if self.visited[(self.x,self.y)]<4 and self.toEnd>0:
                self.visited[(self.x,self.y)]+=1
                if (self.x,self.y-1) not in self.visited.keys() and (self.x,self.y-1) not in self.walls:
                    self.y-=1
                    if (self.x-1,self.y) in self.visited.keys():
                        self.visited[(self.x-1,self.y)]+=1
                    if (self.x+1,self.y) in self.visited.keys():
                        self.visited[(self.x+1,self.y)]+=1
                    if (self.x,self.y-1) in self.visited.keys():
                        self.visited[(self.x,self.y-1)]+=1
                    self.prev="GoEast"
                    return "GoEast"
                elif (self.x,self.y+1) not in self.visited.keys() and (self.x,self.y+1) not in self.walls:
                    self.y+=1
                    if (self.x-1,self.y) in self.visited.keys():
                        self.visited[(self.x-1,self.y)]+=1
                    if (self.x+1,self.y) in self.visited.keys():
                        self.visited[(self.x+1,self.y)]+=1
                    if (self.x,self.y+1) in self.visited.keys():
                        self.visited[(self.x,self.y+1)]+=1
                    self.prev="GoWest"
                    return "GoWest"
                elif (self.x+1,self.y) not in self.visited.keys() and (self.x+1,self.y) not in self.walls:
                    self.x+=1
                    if (self.x+1,self.y) in self.visited.keys():
                        self.visited[(self.x+1,self.y)]+=1
                    if (self.x,self.y+1) in self.visited.keys():
                        self.visited[(self.x,self.y+1)]+=1
                    if (self.x,self.y-1) in self.visited.keys():
                        self.visited[(self.x,self.y-1)]+=1
                    self.prev="GoSouth"
                    return "GoSouth"
                else:
                    self.x-=1
                    if (self.x-1,self.y) in self.visited.keys():
                        self.visited[(self.x-1,self.y)]+=1
                    if (self.x,self.y+1) in self.visited.keys():
                        self.visited[(self.x,self.y+1)]+=1
                    if (self.x,self.y-1) in self.visited.keys():
                        self.visited[(self.x,self.y-1)]+=1
                    self.prev="GoNorth"
                    return "GoNorth"
            else:
                if self.toEnd>0 and self.goOn():
                    return self.pathTo()
                else:
                    self.prev="NoOp"
                    return "NoOp"
        self.findNextMove = findNextMove
        
        def goOn():
            for i in self.visited.keys():
                if self.visited[i]<4:
                    return True
            return False
        self.goOn = goOn

        def pathTo():
            fringe=(["NoOp"],(self.x,self.y))
            queue=list()
            while self.visited[fringe[1]]>=4:
                if fringe[0][0]!="GoEast" and (fringe[1][0],fringe[1][1]+1) not in self.walls:
                    queue=queue+[(["GoWest"]+fringe[0],(fringe[1][0],fringe[1][1]+1))]
                if fringe[0][0]!="GoWest" and (fringe[1][0],fringe[1][1]-1) not in self.walls:
                    queue=queue+[(["GoEast"]+fringe[0],(fringe[1][0],fringe[1][1]-1))]
                if fringe[0][0]!="GoNorth" and (fringe[1][0]+1,fringe[1][1]) not in self.walls:
                    queue=queue+[(["GoSouth"]+fringe[0],(fringe[1][0]+1,fringe[1][1]))]
                if fringe[0][0]!="GoSouth" and (fringe[1][0]-1,fringe[1][1]) not in self.walls:
                    queue=queue+[(["GoNorth"]+fringe[0],(fringe[1][0]-1,fringe[1][1]))]
                fringe=queue[0]
                queue=queue[1:]
            move=fringe[0][::-1][1]
            self.reachDest=fringe[0][::-1][2:]
            self.prev=move
            if move=="GoEast":
                self.y-=1
            elif move=="GoWest":
                self.y+=1
            elif move=="GoSouth":
                self.x+=1
            else:
                self.x-=1
            return move
        self.pathTo = pathTo
