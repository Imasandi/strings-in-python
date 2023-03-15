#string
# insert a new line in the same string
print("male \nman")

#quotation mark with back slash,escape
print("male\"man")

#string variable
"""variable name is phrase in here """
phrase="male man"
print(phrase+ " is cool")  #type the name of the variable inside the paranthesis
# or concatnation

print(phrase)

#function
""" little block of code that we can run, performs a specific operation"""
# when using a function in a string
# modify string
# get information about the string
print(phrase.upper())  # function
print(phrase.lower())
print(phrase.isupper())
print(phrase.upper().isupper())  # can run functions one after the other
print(len(phrase))  # length of the string
# individual characters of a string
print(phrase[0])  # 1st letter

"""index function"""
# tell us where a specific character located in our string
print(phrase.index("m"))  # reverse of the previous function
# passing a parameter
print(phrase.index("man"))

"""replace function """
print(phrase.replace("male","elephant"))