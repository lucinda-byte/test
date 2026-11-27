s = input("请输入字符串: ")
d = {}
for ch in s:
    if ch in d:
        d[ch] += 1
    else:
        d[ch] =1
max_char = max(d, key=d.get)
max_count = d[max_char]
print(f"出现最多的字符: {max_char}, 次数: {max_count}")
input("按回车关闭窗口")
