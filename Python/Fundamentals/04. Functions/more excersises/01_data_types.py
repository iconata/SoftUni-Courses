def data_types(cmd, num):
    if cmd == "int":
        result = int(num) * 2
        return result
    elif cmd == "real":
        result = float(num) * 1.50
        return f"{result:.2f}"
    else:
        return f"${num}$"


print(data_types(cmd=input(), num=input()))
