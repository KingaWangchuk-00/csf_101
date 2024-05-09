class dog:
    def __init__(self,name,color,age): #_init_ is to initiallised
        self.name= name
        self.color=color
        self.age=age
puku=dog("puku","brown",20)
hancy=dog("hancy","black",23)

print("my dog name is",puku.name,"his color is",puku.color,"he is", puku.age)
print(puku.color)
print(puku.age)
print(hancy.name)
print(hancy.color)
print(hancy.age)