var_a=75
def func():
    var_b=38
    def B_inner_func():
        var_c=24

x,y= [(x) for x in input("Please enter two values for variables ").split()]
# a,b=[(a) for x in input().split()]

result_and=x and y
print("result is :",result_and)

result_or=x or y
print("result is:",result_or)

result_not=not x 
print(result_not)




grade=int(input("enter a grade:"))

if grade >= 90:
    print("a")
elif grade >=70:
    print("b")
elif grade >=50:
    print("c")
else:
    print("fail")
    


hungry= False
amount_money=80
mood= False 

if hungry == True and amount_money >= 80:
    print("lets eat")

spam={2,"cat", "monkey","dog"}
spam1={2,True }
spamdifferrence=spam.difference(spam1)
spam={2,"cat", "monkey","dog"}
print(spam)
spam1={2,True }
spamdifference=spam.difference(spam1)
print(spamdifference)

dict={ "name":"kinga","age":20}
print(dict)
dict.keys()
print(dict["age"])
print(dict["name"])

dictget=dict.get("name")
print(dictget)

dictde=dict.setdefault("height",176)
print(dictde)
print(dict)
x=dict.items()
print(x)

y="kinga wangchuk"
print(len(y))
y=y.upper()
print(y)
y=y.lower()
print(y)

p="hello".isupper()
print(p)

p="hello"
print(p.count('o'))
print(p.count("l"))
print(p.find("o"))
print(p.find("l"))

u="hello,welcome to bhutan"
print(u)
o= u.split()
print(o)

print("hello\n bhutan \n i\nam\nkinga ")
print("i\\am\tkinga\in")

name="kinga"
print(f"hello\n{name}")
print("hello bro{}".format(name))
print("hey bro {}".format(name))

print("hello" + 2)

book_list=[]
book_set=set()
book_dict={}


book_list.append("sjdhsd")
book_set.add("oki")
book_dict["kinga"]="jam"

print(book_dict)
print(book_list)
print(book_set)



fruits=["banana", "apple", "mango" ]
for items in fruits:
    print(items)

num=1

for number in range(1,45,5):
    print("attend",number +1,(number +1)*".")


x=False
for number in range(5):
    print("done")
    if x :
        print("oki")
        break
    else:
        print("get out")



for x in range(5):
    for y in range(6):
        for z in range(20):
            print(f"({x},{y},{z})")


for i in range (5):
    print(i)
    j=0
    while j<2:
        print(j +1)
        j=+1
        break

x=0
while x<5:
    print("kinga")
    x= x+1

def name(x):
    print(f"welcome to bhutan\n{x}")
name("pema")

x=2
def fun():
    x=12
    y=67

    print(f"x is equal to {x}")
    print(f"y is equal to {y}")
fun()
print(f"gobal x is equal to {x}")



def factorial(n):
    if n==1:
        return 1
    else:
        return(n*factorial(n-1))
print(factorial(67))

factorial(num)


nums=[5,3,8,6,7,2]
def sort(nums):
    for i in range(len(nums)-1,0,-1):
        for j in range (i):
            if nums[j]> nums[j+1]:
                temp=nums[j]
                nums[j]=nums[j+1]
                nums[j+1]=temp

sort(nums)
print(nums)