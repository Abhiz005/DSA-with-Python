class Graph:
    def __init__(self,vno):
        self.vertex_count=vno
        self.adj_matrix=[[0]*vno for e in range(vno)]
        
    def add_edge(self,u,v,weight=1):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            self.adj_matrix[u][v]=weight
            self.adj_matrix[v][u]=weight
            
    def remove_edge(self,u,v,weight=1):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            self.adj_matrix[u][v]=0
            self.adj_matrix[v][u]=0
        else:
            print("Invalid vertex")      
            
    def has_graph(self,u,v):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            return self.adj_matrix[u][v]!=0
        else:
            print("Invalid vertex")    
            
    def print_adj_matrix(self):
        for row in self.adj_matrix:
            print(" ".join(map(str,row)))
          
g=Graph(5)
g.add_edge(1,2)
g.add_edge(2,4)
g.add_edge(4,3)
g.print_adj_matrix()
print(g.has_graph(4,2))    
                        
            
            