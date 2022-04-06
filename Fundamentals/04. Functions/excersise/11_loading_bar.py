def loading_bar(num):
    new_num = num // 10
    percent = new_num * "%"
    dots = (10 - new_num) * "."
    if num == 100:
        print(f"100% Complete!")
        print(f"[{percent}]")
    else:
        print(f"{num}% [{percent}{dots}]")
        print(f"Still loading...")


number = int(input())
loading_bar(number)
