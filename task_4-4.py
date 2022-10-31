vlans = [10, 20, 30, 1, 2, 100, 10, 30, 3, 4, 10]
vlans.sort()

vlan_new = []

for vlan in vlans:
    if vlan not in vlan_new:
        vlan_new.append(vlan)
        
print(vlan_new)

