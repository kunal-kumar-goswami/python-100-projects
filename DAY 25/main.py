import pandas
data = pandas.read_csv("C:/coding-programming/100 Days of Code/DAY 25/weather_data.csv")
print(type(data))
print(type(data["temp"]))

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(len(temp_list))

average = sum(temp_list) / len(temp_list)
print(average)

print(data["temp"].max())
print(data["temp"].mean())

#Get the data of row 
print(data[data.day == "Monday"])

