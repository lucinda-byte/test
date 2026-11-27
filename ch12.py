import random
def game_guess():
    """任务1:猜数游戏"""
    print("\n====任务1 猜数字游戏 ====")
    num = random.randint(1 ,100)
    count = 0
    max_times = 10
    print(f"范围1~100,共有{max_times}次机会！")
    while count < max_times:
        guess = int(input("请输入猜测数字: "))
        count += 1
        if guess == num:
            print(f"猜对啦！答案是{num},一共猜了{count}次")
            break
        elif guess > num:
            print("太大了")
        else:
            print("太小了")
    else:
        print(f"次数用完了！游戏结束了，正确答案是{num}")
def count_score():
    """任务2: 统计成绩等级"""
    print("\n==== 任务2 成绩统计 ====")
    you = 0
    liang = 0
    zhong = 0 
    jige = 0
    bujige = 0
    print("请输入成绩,输入-1结束输入")
    while True:
        score = int(input("成绩： "))
        if score == -1:
            break
        if score < 0 or score > 100:
            print("成绩无效,请重新输入!")
            continue
        if 90 <= score <= 100:
            you += 1
        elif 80 <= score <=89:
            liang += 1
        elif 70 <= score <=79:
            zhong += 1
        elif 60 <= score <=69:
            jige += 1
        else:
            bujige += 1
    print("------统计结果-------")
    print(f"优: {you}")
    print(f"良: {liang}")
    print(f"中: {zhong}")
    print(f"及格: {jige}")
    print(f"不及格: {bujige}")
def narcissus():
    """任务3: 10000以内水仙花数"""
    print("\n==== 任务3 10000以内水仙花数====")
    for n in range(1, 10001):
        s = str(n)
        length = len(s)
        total = 0
        for c in s:
            digit = int(c)
            total += digit ** length
        if total == n:
            print(n, end=" ")
    print()
# 主菜单
while True:
    print("\n========= 实验六菜单 =========")
    print("1. 猜数字游戏")
    print("2. 成绩等级统计")
    print("3. 输出10000以内水仙花数")
    print("0. 退出程序")
    choice = int(input("请选择功能(0-3) : "))
    if choice == 1:
        game_guess()
    elif choice == 2:
        count_score()
    elif choice == 3:
        narcissus()
    elif choice == 0:
        print("程序退出!")
        break
    else:
        print("输入错误,请输出0-3!")




            
            
