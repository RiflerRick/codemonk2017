"""
Xenny's is competing in a race and his car has X litres of fuel. There are N milestones in the competition. It takes no fuel at all to travel between gas stations, but at the ith gas station, Pi amount of petrol is drained.

Find the number milestones Xenny crosses before his car gets out of fuel.
"""
n, x=input().split()
litres=int(x)
gasStations=input().split()
c=0
for i in gasStations:
    if litres<=0:
        break
    litres-=int(i)
    c+=1

print(c)