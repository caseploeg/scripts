PAD = int(input())
print(bytes.fromhex('00'*PAD) + bytes.fromhex(input()[::-1]))
