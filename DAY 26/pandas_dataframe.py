student_dict = {
    "student":["King","Jonshon","Angel"],
    "score":[65,72,88]
}

#looping through dictionaries:
# for(key,value) in student_dict.items():
    # print(value)

import pandas 

x = pandas.DataFrame(student_dict)
print(x)

#Looping though rows of Data Frame
for (index, row) in x.iterrows():
    if row.student == "Angel":
        print(row.score)
