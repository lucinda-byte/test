s = input("请输入字符串: ")
freq = {}
for ch in s:
    if ch.isalnum():
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1
print("字母数字频次字典: ",freq)
input("按回车关闭窗口")
