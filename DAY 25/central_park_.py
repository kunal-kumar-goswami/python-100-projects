import pandas as pd

data = pd.read_csv("C:/coding-programming/100 Days of Code/DAY 25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250618.csv")
grey_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels = len(data[data["Primary Fur Color"] == "Black"])
print(grey_squirrels)
print(red_squirrels)
print(black_squirrels)

data_dict = {
    "Fir Color": ["Grey", "Cinnamon","Black"],
    "Count":[grey_squirrels,red_squirrels,black_squirrels]
}

df  = pd.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")