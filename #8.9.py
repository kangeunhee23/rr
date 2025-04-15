import random

x = random.randint(1, 20)
n = 0

while True:
    n += 1
    guess = int(input("1~20까지의 숫자를 입력하세요: "))
    if guess < x:
        print(f"{guess} 보다 큽니다!")
    elif guess > x:
        print(f"{guess} 보다 작습니다!")
    else:
        print("정답입니다!")
        if n <= 3:
            print(f"{n}번만에 맞춘 당신은 천재!")
        elif 4 <= n <= 6:
            print(f"{n}번만에 맞추셨네요. 잘했어요^^")
        else:
            print(f"{n}번만에 맞추다니 쩝쩝...")
        break

with open("number1to10.txt", "w") as f:
    for i in range(1, 11):
        f.write(f"{i}\n")

with open("coord.txt", "r") as f:
    n = int(f.readline())
    coords = []

    for _ in range(n):
        x, y = map(int, f.readline().split())
        coords.append((x, y))

# 정렬
coords.sort()

# 출력
for x, y in coords:
    print(x, y)
