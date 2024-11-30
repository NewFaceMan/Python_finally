n = int(input("숫자를 입력하세요 : "))

if n == 1:
    print(f"{n}은 소수가 아닙니다.")
else :
    for i in range(2, n) :
        if n % i == 0:
            print(f"{n}은 소수가 아닙니다.")
            break
    else :
        print(f"{n}은 소수입니다.")