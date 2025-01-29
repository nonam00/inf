from ipaddress import ip_network

net = ip_network('192.168.31.80/255.255.255.240', False)

mx = -float('inf')
for ip in net:
    mx = max(bin(int(ip))[2:].zfill(32).count('1'), mx)
print(mx)

