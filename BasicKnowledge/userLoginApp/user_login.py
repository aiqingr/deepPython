# 1. 确定在文件里储存账号信息的结构

# 2. 把帐号数据读到内存， 为了方便调用， 可以改成list
accounts = {
    # "Alex": ["Alex", "abc!123", "1"]
}

# 3. loop 要求用户输入账户信息 然后判断
f = open("account.db", "r")
for line in f:
    line = line.strip().split(",")
    accounts[line[0]] = line
print(accounts)

count = 0
while True:
    username = input("Please enter your username: ").strip()
    if username not in accounts:
        print("该用户未注册")
        continue
    elif accounts[username][2] == "1":
        print("此账号已被锁定")
        continue

    count = 0
    while count < 3:
        password = input("Password: ").strip()
        if password == accounts[username][1]:
            print(f"Welcome {username} ...登陆成功 ...")
            exit("Welcome Back!")
        else:
            print("Wrong password")

        count += 1

    if count == 3:
        print(f"输错了{count}次密码, 账号{username}被锁定")

        # 1. 现在内存中的dict账号信息的用户状态
        # 2. 把dict里的数据转成account.db的数据格式 并且存储回文件
        accounts[username][2] = "1"
        f2 = open("account.db", "w")
        for username, val in accounts.items():
            line = ",".join(val) + "\n"  # 把列表在转换成字符
            f2.write(line)
        f2.close()

        exit("Bye")
