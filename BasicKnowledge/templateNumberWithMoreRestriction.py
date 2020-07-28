import random
import string

count = 0

while count < 3:
    template_nums = []
    for i in range(20):
        n1 = random.choice(string.ascii_uppercase)
        n2 = "".join(random.sample((string.ascii_uppercase + string.digits), 5))
        template_num = f"{n1}-{n2}"
        template_nums.append(template_num)
        print(template_num)

    choice = input("Please select your template number: ").strip()
    if choice in template_nums:
        print(f"Your template number is {choice}!")
        exit("Congratulations!")
    else:
        print("Invalid Number")

    count +=1