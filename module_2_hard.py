def generate_password(n):
    result = ""

    pairs = []
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            pairs.append((i, j))


    for a, b in pairs:
        pair_sum = a + b
        if n % pair_sum == 0:
            result += f"{a}{b}"

    return result

while 1>0:
    n = int(input('Введите число от 3х до 20: '))
    if n>2 and n<21:
        password = generate_password(n)
        print(f"Пароль для числа {n}: {password}")
        break
    else:
        print('Число не в диопазоне от 3х до 20!')

print("Поздравляю! Ты выжил и выбрался из ловушки! ")


