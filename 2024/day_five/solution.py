import re
from GetData import get_file_data

class Safety_manual_printer():
    def __init__(self, file_name):
        data = get_file_data(file_name)
        separation_index = data.index('')
        self.page_ordering_rules = data[:separation_index]
        self.pages_to_produce = data[separation_index:]

    def check_with_rules(self, page, tempPage):
        for rule in self.page_ordering_rules:
            split_rules =  rule.split('|')
            if (tempPage == split_rules[0] and  page == split_rules[1]):
                return False
        return True


    def check_if_valid(self, page, pages, i):
        isValid = True
        for j in range(len(pages)):
            tempPage = pages[j]
            res = self.check_with_rules(page,tempPage)      
            if res == False:
                print("page|tempPage ", page,tempPage)
                pages[i], pages[j] = pages[j], pages[i]
                isValid = False
        
        return isValid
        
    def check_order(self):
        
        sum = 0
        
        for print_order in self.pages_to_produce:
            pages = re.split(",", print_order)
            inOrder= True
            
            for i in range(len(pages)):
                res = self.check_if_valid(pages[i],pages[i:], i)
                if res == False:
                    inOrder = False
            if inOrder:
                midle_number = pages[int(len(pages)/2)]
                if midle_number != "":
                    sum += int(midle_number)
        print("sum: ",sum)
safety_manual_printer = Safety_manual_printer("input2.txt")
safety_manual_printer.check_order()