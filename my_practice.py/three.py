#import numpy as np
#arr2 = np.array([[10, 20, 30, 40, 50], [60, 70, 80, 90, 100]])
#print(arr2) # [[ 10 20 30 40 50 ] [ 60 70 80 90 100]]
#print(arr2 [0, 2]) # 30
#print(arr2[0:2, 2:4]) # [[3040] [8090]]
#print(arr2.sum()) # 550
#print(arr2.sum(axis=0)) #[ 70 90 110 130 150]
#print(arr2.sum(axis=1)) # [150 400]
#print(np.sum(arr2, axis=0)) # [ 70 90 110 130 150]
#print(np.mean(arr2, axis=1)) # [ 30. 80.]


from collections import deque
stack=deque()
stack.append("g")
stack.append("i")
stack.append("r")
stack.append("l")
stack.append("s")
print(stack)

print(stack.pop())
print(stack.popleft())
print(stack)

from queue import LifoQueue
stack=LifoQueue(maxsize=5)
stack.put("h")
stack.put("e")
stack.put("v")
stack.put("e")
stack.put("n")
print(stack.queue)
print(stack.get())
print(stack.get())
print(stack.get())
print(stack.get())
print(stack.queue)

def student_regis():
    regis=input("enter your name:")
    print(regis)
    student_info=deque()
    student_info.append(regis)
    print(student_info)
    
student_regis()
againregis=input("do you want to register another name(yes/no):")
while againregis == "yes":
     addname=input("enter the name:")
     print(addname)
  
addname=deque()
addname.append(addname)
print(addname)




from queue import LifoQueue
from collections import deque