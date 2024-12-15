from ipaddress import ip_network

net = ip_network('192.168.240.0/255.255.255.0', 0)
count = 0
for item in net.hosts():
    s = bin(int(item))[2:].zfill(32)
    if s.count('1') == s.count('0'):
        count += 1
print(count)