#!/home/hmsjwzb/python/bin/python3.5

from In import In
import sys
from Digraph import Digraph

class DirectedCycle:
    def __init__(self, G):
        self.marked = [False] * G.Vertex()
        self.onStack = [False] * G.Vertex()
        self.edgeTo = [0] * G.Vertex()
        self.cycle = []
        for v in range(0, G.Vertex()):
            if not self.marked[v] and self.cycle == []:
                self.dfs(G, v)

    def dfs(self, G, v):
        self.onStack[v] = True
        self.marked[v] = True
        for w in G.adj[v]:
            if self.cycle != []:
                return
            elif not self.marked[w]:
                self.edgeTo[w] = v
                self.dfs(G, w);
            elif self.onStack[w]:
                self.cycle = []
                x = v
                while x != w:
                    self.cycle.append(x)
                    x = self.edgeTo[x]
                self.cycle.append(w)
                self.cycle.append(v)
        self.onStack[v] = False

    def hasCycle(self):
        return self.cycle != []

    def cycle_l(self):
        return self.cycle

if __name__ == '__main__':
    myin = In(sys.argv[1])
    G = Digraph(myin)

    finder = DirectedCycle(G)
    s = ""
    if finder.hasCycle():
        print("Directed cycle: ")
        for v in finder.cycle_l():
            s += "%d " % v
        print(s)
    else:
        print("No directed cycle")
    print("\n")
