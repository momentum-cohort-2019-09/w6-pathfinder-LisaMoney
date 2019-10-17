with open("elevation_small.txt") as text_file:
    text_contents = text_file.read()

elevations = [[int(each) for each in line.split()] for line in text_contents.split("\n")]
# print(elevations[0])
# min = 5000000
# max = 1

min = elevations[0][0]
max = elevations[0][0]

for each in elevations:
    for integer in each:
        if integer < min:
            min = integer
        if integer > max:
            max = integer
# print(min)
# print(max)

colors_big_list = []
little_rows_of_colors = []

for rows in elevations:
    for number in rows:
        color_int = round(((number - min) / (max - min)) * 255)
        little_rows_of_colors.append(color_int)
    colors_big_list.append(little_rows_of_colors)
    little_rows_of_colors = []

print(colors_big_list[0][0])
print(len(colors_big_list[0]))

