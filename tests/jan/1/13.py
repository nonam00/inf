from ipaddress import ip_network

mask = '255.255.252.0'
ip = '156.132.15.138'
net = ip_network(f'{ip}/{mask}', 0)

for i, item in enumerate(net.hosts()):
    if str(item) == ip:
        print(i + 1)