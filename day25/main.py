# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)


# import csv
# with open("weather_data.csv") as  data_file
#     data  = csv.reader(data_file)
#     for row in data:
#         print(row)

# import pandas 
# data = pandas.read_csv("weather_data.csv")
# print(data)

import pandas
data = pandas.read_csv("2018.csv")
grey_squirrel = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrel = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel = len(data[data["Primary Fur Color"] == "Black"])
print(grey_squirrel)
print(red_squirrel)
print(black_squirrel)

data_dict = {
    "Fur Color":["Gray","Cinnamon","Black"],
    "Count": [ grey_squirrel,red_squirrel,black_squirrel]
}

df =pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
