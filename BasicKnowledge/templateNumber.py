import string
import random

count = 0
while count < 3:
    template_nums = []
    for i in range(20):
        n1 = random.choice(string.ascii_uppercase) # first letter generated
        n2 = "".join(random.sample(string.ascii_uppercase + string.digits, 5))
        template_num = f"{n1}-{n2}"
        template_nums.append(template_num)
        print(template_num)

    choice = input("Select the number you like: ").strip()
    if choice in template_nums:
        print(f"Congratulation. Your Number is {choice}!")
        exit("Good luck")
    else:
        print("Invalid choice")

    count +=1
