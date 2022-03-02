#Functin in Python

#def is compulsory
#fun declare// Will work w/o name also
def GreetMe(name):
    print("Gd Mrng" + " " + name)
#Func Call
GreetMe("Sid")

def AddInt (a,b):
    print(a+b)
AddInt(2,3)

#same with return
def AddInt1 (c,d):
    return  c+d
print(AddInt1(2,3))

print("Seperator ++-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")


i = 4

while i > 1:
    print(i)
    i = i - 1

print("While loop done")

# While + if Will skip 3 now
j = 4
while j > 1:
    if j != 3:  # Not equal to 3
        break  # this will break the loop
        print(j)
    j = j - 1

print("While loop done")

k = 4
while k > 1:
    if k != 3:  # Not equal to 3
        break  # this will break the loop
    print(k)  # this is for while upper one is for if check spacing in print
    k = k - 1


print("Seperator *****************************")

l = 9


while l>1:
    if l == 9:
        l == l - 1
        continue
    if l == 3:
        break
    print(l)
    l = l-1