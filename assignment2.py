# 소수 판별
num = int(input("숫자를 입력하세요 : ")) #검사할 최대 숫자를 입력
count = 0 # 소수의 개수를 저장하는 변수
arr = [] #소수를 저장할 빈 리스트
for i in range(2, num + 1) : #2부터 입력한 숫자까지 반복하며 소수를 찾음
    for j in range(2, int(i**0.5) + 1) : #2부터 i의 제곱근까지 숫자로 나누어 소수 여부 확인 (숫자는 계속 증가)
        if (i % j == 0) : #만약 i를 j로 나누었을 때 나머지가 0이면 소수가 아니다.
            break #멈추고 i 반복문으로 감 (break가 걸리지 않으면 else로 넘어감)
    else : # break가 실행되지 않은 경우, i는 소수이다.
        count += 1 #숫자를 올린다
        arr.append(i) #리스트에 i(소수)를 집어넣는다
        
print(f"소수는 {count}개 입니다.")
print(f"{arr}")
