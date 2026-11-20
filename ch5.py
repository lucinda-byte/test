lst = list(map(int, input("请输入若干整数,空格分隔: ").split()))
new_lst= sorted(lst, reverse = True)
print("降序列表: ",new_lst)