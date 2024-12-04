import re
from GetData import get_file_data

def check_down(data, index, i, left, right):
    match_count = 0
    
    down_text = ""
    for j in range(4):
        down_text += (data[i + j][index])
    if (down_text == "XMAS"):
        match_count += 1
    
    if left:
        left_text = ""
        for j in range(4):
            left_text += (data[i + j][index-j])
        if (left_text == "XMAS"):
            match_count += 1
    
    if right:
        right_text = ""
        for j in range(4):
            right_text += (data[i + j][index+j])
        print(right_text)
        if (right_text == "XMAS"):
            match_count += 1
    
    return match_count


def check_up(data, index, i, left, right):
    match_count = 0
    
    up_text = ""
    for j in range(4):
        up_text += (data[i - j][index])
    if (up_text == "XMAS"):
        match_count += 1
    
    if left:
        left_text = ""
        for j in range(4):
            left_text += (data[i - j][index-j])
        print(left_text)
        if (left_text == "XMAS"):
            match_count += 1
    
    if right:
        right_text = ""
        for j in range(4):
            right_text += (data[i - j][index+j])
        if (right_text == "XMAS"):
            match_count += 1
    
    return match_count

def check_horizontal(data, index, i, left, right):
    
    match_count = 0
    
    if right:
        text = data[i][index:(4 + index)]
        if (text == "XMAS"):
            match_count += 1

    if left:    
        text = data[i][(-4 + (index+1)):(index+1)]
        if (text == "SAMX"):
            match_count += 1

    return match_count

def candidate_check(data,index, i):
    left_posibility = False
    right_posibility = False
    up_posibility = False
    down_posibility = False

    total_match_count = 0
    
    print("len", len(data[i]), "i",i )

    if (len(data[i]) - index) > 3:
        right_posibility = True 
    
    if (index) >= 3:
        left_posibility = True 

    if i > 2:
        up_posibility = True    
        
    if (len( data) - (len("XMAS")+ i)) >= 0:
        down_posibility = True
    
    print("left_posibility",left_posibility)
    print("right_posibility",right_posibility)
    print("up_posibility",up_posibility)
    print("down_posibility",down_posibility)
    if (left_posibility or right_posibility):
        total_match_count += check_horizontal(data, index, i, left_posibility, right_posibility)
    
    if up_posibility:
        total_match_count += check_up(data, index, i, left_posibility, right_posibility)
    
    if down_posibility:
        total_match_count += check_down(data, index, i, left_posibility, right_posibility)
    
        
    return total_match_count
    
def detect_x(line):
    x_matches = re.finditer('X',line)
    x_indexes = []
    for match in x_matches:
        x_indexes.append(match.span()[0])
    return x_indexes

def main():
    data = get_file_data("input.txt")
    total_match_count = 0
    for i in range(len(data)):
        x_indexes = detect_x(data[i])
        print(x_indexes)
        for index in x_indexes:
            total_match_count += candidate_check(data, index, i)
    print("total mathces: ", total_match_count)
    
main()