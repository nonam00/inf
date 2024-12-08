al = '0123456789ABCDEFGHI'
print(max([x for x in al if (int(f'98897{x}21', 19) + int(f'2{x}923', 19)) % 18 == 0]))
