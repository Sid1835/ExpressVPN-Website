greeting = "Good Morning"
a = 4

if greeting == "Good Morning":
    print("Mrng")
else:
    print("Alag")

print("Outside If Else")


if a > 2:
    print("Positive")
else:
    print("Negative")



# For Loop
obj = [2, 4, 6, 8, 10]
for i in obj:
    print(i)
    print(i*2)

#Sum of 1st 5 Natural no
Add = 0
# (int i = 0 i = 10 i++)
for j in range (1,6): # range from 1 to 5 (j to j-1) This will increment with 1
    print(j)
    Add = Add + j
print(Add)


print("*+*+*+*+*+*+*+*+")
for k in range (1,10,2): # i++ = 2 in this case
    print(k)
print("new sep * + * +* + * ")

#first value not passed so started from 0 & 10 is defined as max value
for m in range(10):
    print(m)
