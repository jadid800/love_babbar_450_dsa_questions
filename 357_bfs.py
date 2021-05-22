from collections import deque
class Solution:
    def bfsOfGraph(self, V, adj):
      q=deque()
      q.append(0)
      result=[]
      visited= [0]* (len(adj)+1)
      visited[0]=1
      while(q):
        vert=q.popleft()
        result.append(vert)
        for i in (adj[vert]):
          if( not visited[i]):
            q.append(i)
            visited[i]=1
      return result


