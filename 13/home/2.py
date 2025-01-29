from ipaddress import ip_network


node = '241.185.253.57'
mn = float('inf')
for i in range(0, 33):
    net = ip_network(f'{node}/{i}', False)
    if str(net[0]) == '241.185.252.0':
        print(32 - i)
