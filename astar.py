graph = {
   'A': [('B',2),('E',3)],
   'B': [('C',1),('G',9),('A',2)],
   'C': [('B',1)],
   'D': [('E',6),('G',1)],
   'E': [('A',3),('D',6)],
   'F': [],
   'G': [('B',9),('D',1)]
}

 
def h(n):
    H = {
        'A': 11,
        'B': 6,
        'C': 99,
        'D': 1,
        'E': 7,
        'F': 1,
        'G': 0
    }
    return H[n]
 
def a_star_algorithm(start, stop):
    open_lst = set([start])
    closed_lst = set()
    
    adj = {}
    adj[start] = start
    
    cost = {}
    cost[start] = 0
    
    while len(open_lst) != 0:
        n = None
        for v in open_lst:
            if n == None or cost[v]+h(v) < cost[n]+h(n):
                n = v
        if n == None:
            print("NO PATH")
            return
        
        if n == stop:
            path = []
            while adj[n] != n:
                path.append(n)
                n = adj[n]
            path.append(start)
            print(path[::-1])
            return
        
        for (m,weight) in graph[n]:
            if m not in open_lst and m not in closed_lst:
                open_lst.add(m)
                adj[m] = n
                cost[m] = cost[n] + weight
                
            else:
                if cost[m] > cost[n] + weight:
                    cost[m] = cost[n] + weight
                    adj[m] = n
                    if m in closed_lst:
                        closed_lst.remove(m)
                        open_lst.add(m)
        
        open_lst.remove(n)
        closed_lst.add(n)

a_star_algorithm('A', 'G')