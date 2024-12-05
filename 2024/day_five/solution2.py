import re
from GetData import get_file_data
import sys
sys.setrecursionlimit(3000)

def prepare_data(file_name):
    data = get_file_data(file_name)
    separation_index = data.index('')
    page_ordering_rules = data[:separation_index]
    pages_to_produce = data[separation_index:]
    return page_ordering_rules, pages_to_produce

def check_with_rules(page_ordering_rules, page, tempPage):
    combined = tempPage + "|" + page 
    if combined in page_ordering_rules:
        return False 
    return True

def pass_checker(page_ordering_rules, pages, i):
    
    for page in pages[(1 + i):]:
        #print(page)
        passes = check_with_rules(page_ordering_rules, pages[i], page)
        #print("passes", passes)
        if passes:
            passed = pass_checker(page_ordering_rules, pages, (i +1))
            if passed == False:
                return False
        else:
            return False
    return True
    
def checking_pages(page_ordering_rules, pages, i):
    
    if (len(pages["pages"]) > (i+1)):
        passes = check_with_rules(page_ordering_rules, pages["pages"][i], pages["pages"][i+1])
        if passes:
            checking_pages(page_ordering_rules, pages, (i +1))
        else:
            pages["pages"][i], pages["pages"][i+1] = pages["pages"][i+1], pages["pages"][i]
            pages["passed"] = False
            i = 0
    
            checking_pages(page_ordering_rules, pages, (i))
    
    

def loop_print_orders(page_ordering_rules, pages_to_produce):
    sum = 0
    for print_order in pages_to_produce[1:]:
        pages = re.split(",", print_order.strip())
        
        lines = {
            "pages": pages,
            "passed": True,
        }
        
        checking_pages(page_ordering_rules,lines, 0)
        if (lines["passed"] == False):
            midle_number = pages[int(len(lines["pages"])/2)]
            
            if midle_number != "":
                sum += int(midle_number)
    
    return sum
        
def main(file_name):
    page_ordering_rules, pages_to_produce = prepare_data(file_name)
    sum = loop_print_orders(page_ordering_rules, pages_to_produce)
    print("sum ", sum)
main("input.txt")