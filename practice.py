def validPos(table,enemy):
    for ene in enemy:
        if ene in table:
            return False
    return True


def csp(enemies,noOfPeople,noOfTables):
    table = [[] for i  in range(noOfTables)]
    visited = [False for i in range(noOfPeople)]
    for i in range(noOfPeople):
        
        for j in table:
            
            if validPos(j,enemies[i]):
                visited[i] = True
                j.append(i)
                break
        if visited[i] == False:
            print("NOT POSSIBLE")
            return
    print(table)
    return 


noOfPeople = int(input("ENTER THE NO OF PEOPLE:"))
noOfTables = int(input("ENTER THE NO OF TABLES:"))
noOfConstriants = int(input("ENTER THE NO OF CONSTRIANTS:"))

enemies = {}
for i in range(noOfPeople):
    enemies[i] = set()
    
for i in range(noOfConstriants):
    a , b = map(int,input("ENTER THE PAIR:").split())
    enemies[a].add(b)
    enemies[b].add(a)
    
    
csp(enemies,noOfPeople,noOfTables)