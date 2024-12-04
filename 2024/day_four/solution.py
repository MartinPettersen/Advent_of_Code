import re
from GetData import get_file_data

def detect_X_mas(data,index, i):
    isPossible = True
    
    text_down_right = ""
    text_up_right = ""
    
    try:
        if index > 0 and i > 0:
            text_down_right += data[i - 1][index - 1] + "A"
        else:
            isPossible = False
    except:
        print("someting wrong top-left")
    try:
        if (len(data) > (i+1)) and i > 0:
            text_up_right += data[i + 1][index - 1] + "A"
        else:
            isPossible = False
    except:
        print("someting wrong bottom-left")
    try:
        if index > 0 and (len(data[i]) > (index + 1)):
            text_up_right += data[i - 1][index + 1]
        else:
            isPossible = False
    except:        
        print("someting wrong top-right")
    try:
        if (len(data) > (i+1))  and (len(data[i]) > (index+1)):
            text_down_right += data[i + 1][index + 1]
        else:
            isPossible = False
    except:
        print("someting wrong bottom-right")
    if isPossible:
        if (text_down_right == "MAS" or text_down_right == "SAM") and (text_up_right == "MAS" or text_up_right == "SAM"):
            return 1
    return 0

def detect_a(line):
    a_matches = re.finditer('A',line)
    a_indexes = []
    for match in a_matches:
        a_indexes.append(match.span()[0])
    return a_indexes

def main(file_name):
    data = get_file_data(file_name)
    total_match_count = 0
    for i in range(len(data)):
        a_indexes = detect_a(data[i])
        for index in a_indexes:
            total_match_count += detect_X_mas(data, index, i)
    print("total mathces: ", total_match_count)
    
main("input.txt")