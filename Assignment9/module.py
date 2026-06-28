def Kaprekar(n1):
    num = list(str(n1))
    asc = int(''.join(sorted(num)))
    des = int(''.join(sorted(num, reverse=True)))
    result = des - asc

    print(f"{des} - {asc} = {result}")

    if result == 6174:
        return f"{result} is a Kaprekar Constant after subtracting with {n1}"
    return Kaprekar(result)