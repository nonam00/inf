from ipaddress import ip_network

for mask in range(33):
    net = ip_network(f'76.155.48.2/{mask}', 0)
    if str(net[0]) == '76.155.48.0':
        print(net.netmask)
