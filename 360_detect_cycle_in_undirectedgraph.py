from collections import deque
class Solution:
    def isCycle(self, V, adj):
        visited= [0]* (V)
        for i in range(V):
            if (visited[i]==0):
                if(self.bfs( i, adj, visited) ==1):
                    return 1
        return 0
            
    def bfs(self, V, adj, visited):
            
        q=deque()
        q.append(V)
        q.append(-1)
        visited[V]=1
        while(q):
            vert=q.popleft()
            parent= q.popleft()
            
            for i in (adj[vert]):
              if( not visited[i]):
                q.append(i)
                q.append(vert)
                visited[i]=1
              elif(i!= parent):
                # print(vert ," to ", i)  
                return 1
        return 0        
        
