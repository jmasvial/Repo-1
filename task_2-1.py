nat = "ip nat inside source list ACL interface FastEthernet0/1 overload"
nat_r = nat.replace("FastEthernet0/1", "GigabitEthernet0/1")
print(nat_r)

