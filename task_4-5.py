command1 = "switchport trunk allowed vlan 1,2,3,5,8"
command2 = "switchport trunk allowed vlan 1,3,8,9"

com1 = command1.split()
com2 = command2.split()

com1 = com1[4].split(',')
com2 = com2[4].split(',')

newvlan = []

for i in com1:
    if i in com2:
        newvlan.append(i)
        
print(newvlan)
