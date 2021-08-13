x = int(input("enter number of list items :"))
n = int(input("enter the Divisor :"))
l = []

for i in range(0, x):
    print("item",i+1,"of the list =")
    item = int(input())
    l.append(item)

def check_dev(l,n):
    print("the numbers in", l, "that are divisible by", n, "are:")
    for i in range(0,len(l)):
      if l[i] % n == 0:
        print(l[i])

check_dev(l,n)
