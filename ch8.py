from functools import reduce
list_sets = [{1,2,3},{3,4,5},{5,6,7}]
res = reduce(lambda a,b:a | b, list_sets)
print("并集: ",res)
input("按回车关闭窗口")
