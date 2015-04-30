import string

def open_file():
   return [line.strip() for line in open('rclist.txt')]

rc_array = open_file()

def update_title(old_title):

    temp_title = old_title
    new_title = temp_title
    capital_words = ["javascript", "rails", "ruby", "postgresql", "redcarpet", "jasmine", "faye", "capybara", "ajax", "stripe", "twitter", "bootstrap", "kaminari", "warden", "cucumber"]
    
    for item in capital_words:
        
        if temp_title.find(item) != -1:
        
            update_letter = temp_title[temp_title.find(item)].upper()
            new_title = new_title[:new_title.find(item)] + update_letter + new_title[new_title.find(item) + 1:]

    print new_title
            
    letter_i = " i "
    if temp_title.find(letter_i) != -1:
        new_title = new_title.replace(letter_i, " I ")

    return new_title
            
def clean_the_title(messy_title):
    clean_title = string.replace(messy_title, '-', ' ')  
    clean_title = clean_title[0].upper() + clean_title[1:]
    clean_title = update_title(clean_title)

    return clean_title


def parse_rc(array):
    
    for item in array:
    
        parse_rc_num = item.find("-")
        rc_num = item[:parse_rc_num]
        
        title = clean_the_title(item[parse_rc_num + 1:])
        #if need to print to file
        #title_file = open('titles.txt', 'a')
        #print >>title_file, title

        
parse_rc(rc_array)        