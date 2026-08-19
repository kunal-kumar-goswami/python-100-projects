coding_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again."
    }

print(coding_dictionary["Function"])

#To add a key: value in dictionary
coding_dictionary["Loop"]= "The action of doing something over and over again."
print(coding_dictionary)

#To create empty dictionary.
empty_dictionary = {}

#Wipeout an existing dictionary.
# coding_dictionary = {}
# print(coding_dictionary)

#Edit an item in a dictionary.
coding_dictionary["Bug"] = " A ERROR in your system."
print(coding_dictionary)

#Loop through a dictionary 
for key in coding_dictionary:
    print(key)
    print(coding_dictionary[key])
    