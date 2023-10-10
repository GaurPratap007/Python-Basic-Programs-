import pandas

data = pandas.read_csv("weather_data.csv")
print(data)

# Printing temperatures as seperate list
temp_list = data["temp"].to_list()
print(temp_list)
avg_temp = sum(temp_list)/len(temp_list)
print(avg_temp)

# Accessing columns
#print(data["conditions"])
#print(data.conditions)

# Accessing Rows
print(data[data.day == "Monday"])

#Get the details of max temp day
print(data[data.temp == data.temp.max()])

# Creating a data frame from scratch
data_dict = {"students": ["Andy", "Murray"], "marks": [90, 85]}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")