p1 = list(map(int, input("输入第一个坐标两个数,空格分隔: ").split()))
p2 = list(map(int, input("输入第二个坐标两个数,空格分隔: ").split()))
dist = abs(p1[0]-p2[0]) + abs(p1[1] - p2[1])
print("曼哈顿距离: ",dist)