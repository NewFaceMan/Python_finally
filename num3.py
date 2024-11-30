import random

secret_number = random.randint(1, 10)
attempts = 3

while attempts > 0 :
    num = int(input("숫자를 맞춰보세요 (1~10) :"))
    if secret_number == num :
        print("정답입니다!")
        break
    elif num == -1 :
        print(f"치트키 사용! 비밀 숫자 : {secret_number}")
    else :
        attempts -= 1
        print(f"틀렸습니다. 남은 시도 횟수: {attempts}")

else :
    print("아쉽지만 모든 기회를 다 썼습니다. 게임이 종료됩니다.")
    
        