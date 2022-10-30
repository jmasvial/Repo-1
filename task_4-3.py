vlans = ["1", "3", "10", "20", "30", "100"]
vlan_jo = ','.join(vlans)
res = "switchport trunk allowed vlan " + vlan_jo
print(res)

