import pandas 

data = pandas.read_csv("C:/coding-programming/100 Days of Code/DAY 25/weather_data.csv")

monday = data[data.day == "Monday"]
temp = monday.temp[0]
temp_F = temp * 9/5 + 32 
print(temp_F)

#Creat a dataframe from  scratch 
data_dict = {
    "students": ["king","queen", "raja"],
    "score": [89,85,91]
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")

