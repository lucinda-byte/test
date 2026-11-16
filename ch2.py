a =set (map(int, input("输入第一个集合，用逗号分隔: ").split(',')))
b =set (map(int, input("输入第二个集合，用逗号分隔: ").split(',')))
inter = a & b
union = a | b
diff = a - b
print("交集 :",inter)
print("并集 :",union)
print("差集(a -b): ",diff)