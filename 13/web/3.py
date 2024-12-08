from ipaddress import ip_network

node = '111.81.208.27'
mn = float('inf')
for mask in range(0,33):
    net = ip_network(f'{node}/{mask}', 0)
    if str(net[0]) == '111.81.192.0':
        print(net.netmask)

