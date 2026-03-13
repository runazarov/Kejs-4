n = int(input("Введите общее количество голов драконьей стаи: "))

# dp[i] — максимальная сила для i голов
dp = [0] * (n + 1)
dp[0] = 1

for i in range(1, n + 1):
    max_power = 0
    for heads in range(1, 8):  # у одного дракона максимум 7 голов
        if i - heads >= 0:
            power = dp[i - heads] * heads
            if power > max_power:
                max_power = power
    dp[i] = max_power

print("Максимальная сила стаи:", dp[n])
