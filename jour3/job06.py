string = "abcdefghijklmnopqrstuvwxyz" * 10
n = len(string)
rows = int((2 * n - 1) ** 0.7)  # Nombre de rangées dans la pyramide
index = 0

for i in range(rows):
    for j in range(rows - i - 1):
        print(" ", end="")
    for j in range(2 * i + 1):
        if index >= n:
            break
        print(string[index], end="")
        index += 1
    print()
