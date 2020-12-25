info = list()

info.append(input("Please input your First name\n"))
info.append(input("Please input your Last name\n"))
info.append(int(input("Please input your Age\n")))
info.append(int(input("Please input your Year of Birth\n")))

for i in range(len(info)):
    print(info[i])

if info[2] >= 18:
    print("You can go out on the street")
else:
    print("You cannot go out on the street")
