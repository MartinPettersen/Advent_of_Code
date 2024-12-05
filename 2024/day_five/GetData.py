def get_file_data(file_name):
    lists = []
    with open(file_name, 'r') as file:
        for line in file:
            temp_line = line.strip()
            lists.append(temp_line)
    return lists