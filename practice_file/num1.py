num = int(input())
count = 0
sum = 0
for number in range(1, num + 1) :
    if number % 2 == 0 :
        count += 1
        sum += number

print(f"짝수의 합: {sum}")
print(f"짝수의 합의 평균 : {sum / count}")