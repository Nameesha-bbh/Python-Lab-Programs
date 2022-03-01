def checkEnemy(table,e):
    if len(table)==0:
        return True
    for i in e:
        if i in table:
            return False
    return True

def csp(n,tables,enemy):
    visited=[False for i in range(n)]
    for i in range(n):
        for j in contentTable:
            print(contentTable)
            if checkEnemy(j,enemy[i])==True:
                j.append(i)
                visited[i]=True
                break;
        if visited[i]==False:
            print("not possible")
            return False
    print(contentTable)
    return True

n=int(input("enter number of people:"))
tables=int(input("enter number of tables:"))
enemy={}
for i in range(n):
    enemy[i]=set()

e=int(input("enter the number of social mishap\n"))
for i in range(e):
    a,b=[int(i) for i in input("enter pair").split()]
    enemy[a].add(b)
    enemy[b].add(a)
print(enemy)
contentTable=[[] for i in range(tables)]
csp(n,tables,enemy)