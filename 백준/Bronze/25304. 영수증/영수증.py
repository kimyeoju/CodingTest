total = int(input())
n = int(input())

sub_total = 0
for i in range(n):
    price, obj = map(int,input().split())
    sub_total += (price*obj)

if sub_total == total:
    print("Yes")
else:
    print("No")