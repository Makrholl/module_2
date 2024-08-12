my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
start_position = 0
end_position = len(my_list)

while start_position < end_position:
    if my_list[start_position] == 0:
        start_position = start_position + 1
    elif my_list[start_position] > 0:
        print(my_list[start_position])
        start_position = start_position + 1
    elif my_list[start_position] < 0:
        break
