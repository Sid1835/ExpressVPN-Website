age = 29
first_name = 'Sid'
last_name = 'Katkar'
myval = 1
age = age + 3

atom_name = 'helium'

# This will Count the alphabets
html_text: str = "express"
if __name__ == __name__:
    print(len(html_text))


# Prints Addition
print(5 + 3)

# Print Fname and Age
print(first_name, 'is', age, 'years old')
print(last_name)

# Print Value
print(myval)

# Print Age and + years
print('Age in three years:', age)

# Print First Char
print(atom_name[0])

# Print Several Chars
print(atom_name[0:3])

# Print Length
print(len('helium'))

b, c, d = 5, 6.5, "Sid"
#print("Value is " b)
print("{}{}".format("value is", b))

print(type(b))
print(type(c))
print(type(d))

values = [1, 2, "Sid", 4]


values.insert(3, "Katkar") # Insert Values
print(values)


values.append("End") # Append Values
print(values)

values[2] = "Siddhesh" #update Value
print(values)

del values [0] #deletes Value
print(values)


#tuple Data Type This is an immutable data type-diff is brackets are round instead of square
val1 = (1, 2, "Sid", 4, 5)
print(val1[0])

#Dictonary this is always with braces
val2 = {"a": 2, 4:"bcd", "c" : "hello world"} #text should be in quotes
print(val2)
print(val2[4])
print(val2["c"])

dict ={} #blank dictionary and passed 2 values and print
dict["firstname"] = "Sid"
dict["lastname"] = "Katkar"
print(dict)
print(dict["lastname"])