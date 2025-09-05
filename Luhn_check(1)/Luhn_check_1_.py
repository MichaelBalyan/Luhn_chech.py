digits=[]

count=0
while count<16:
    num=int(input())
    digits.append(num)
    count+=1

print(*digits)
print()

arr1=[]

for i in range(0, len(digits)):

    n=digits[i]

    a=0
    b=0
    if i%2==0:
        n*=2
        if n>9:
            a=n//10
            b=n%10
            n=a+b
    arr1.append(n)

print(*arr1)

s=0
for num in arr1:
    s+=num

print(f"Sum: {s}")


text=""

if s%10==0:
    text="Valid"
else:
    text="Invalid"

print(text)



