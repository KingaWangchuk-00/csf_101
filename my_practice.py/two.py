course=[]
course.append("kinga")
course.insert(1,"namgay")
course1=["cat", "dog" ,"rat","pig"]
course.extend(course1)


print(course)

course.remove("dog")
course.pop()
print(course)
popped= course.pop()
print(popped)

for index,course in enumerate(course):
    print( index,course)

for x in course:
    print(x)

for index,course in enumerate(course, start=1):
    print(index,course)




from collections import deque
stack=deque()
stack.append(12)
stack.pop()


from queue import LifoQueue
queue=[]
print(queue.pop())