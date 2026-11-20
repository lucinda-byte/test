lstA = list(map(int, input("请输入列表A的整数,空格分隔: ").split()))
lstB = list(map(int, input("请输入列表B的整数,空格分隔: ").split()))
n = min(len(lstA), len(lstB))
d = {lstA[i]:lstB[i] for i in range(n)}
print(d)
