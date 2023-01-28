import secrets, string


numbers = string.digits
letters = string.ascii_letters
punctuations = string.punctuation 


all_characters = numbers + letters + punctuations


my_dict = {
    'abc' : 0,
    'def' : 1,
    'ghi' : 2,
    'jkl' : 3,
    'mno' : 4,
    'pqr' : 5,
    'stu' : 6,
    'vwx' : 7,
    'yz' : 8,
    '.' : 9
}



def generate_pass_card() :
    '''
    returns a list conaining lists of rows which contain
    lists with values(future password parts)
    '''
    pass_card = []

    for row in range(10) :
        my_row = []
        for col in range(10) : 
            my_value = []
            cell_value = secrets.choice(all_characters) + secrets.choice(all_characters) + secrets.choice(all_characters)
            my_value.append(cell_value)
            my_row.append(my_value)

        pass_card.append(my_row)
    
    return pass_card



def write_to_file(card_list, file_name = 'pass_card.txt'):
    '''
    (first creates if file does not exist)
    overwrites to a txt file a string of all possible conbinations
    '''
    with open(file_name, 'w') as file:
        for rows in card_list:
            for data in rows :
                for values in data :
                    file.write(values + ' ')
            file.write('\n')





def create_new_pass_card():
    '''
    OUTPUT  creates a new pass card and write it to a file
    (if file not specified writes to pass_card.txt)
    '''   
    write_to_file(generate_pass_card())




def read_pass_card(file_name = 'pass_card.txt') :
    '''
    INPUT name of the file containing password card
    OUTPUT list containing password card
    '''
    password_card = []
    row = []
    value = []

    with open(file_name, 'r') as file :
        for line in file :
            line = line.replace(' ', '')

            for i in range(10) :
                cell_value = line[:3]
                line = line[3:]

                value.append(cell_value)
                row.append(value.copy())

                value.clear()


            
            password_card.append(row.copy())
            row.clear()
            

    return password_card





def find_column(letter) :
    '''
    INPUT a letter
    OUTPUT index of the letter's column
    '''
    for key in my_dict.keys() :
        if letter.lower() in key :
            return my_dict[key]





def user_input():
    '''
    INPUT a word
    check if it is a word with letters or .
    OUTPUT lowered word

    '''
    word = input('word :')

    if word.isalpha() or word == '.' :
        return word.lower()
    else :
        user_input()




def get_password(word,list) :
    '''
    INPUT word, list of password pieces
    OUTPUT password
    '''
    word = word.lower()
    password = ''
    line = 0

    for letter in word :
        column = find_column(letter)
        password += list[line][column][0]

        if line >= 9 :
            line = 0
        else :
            line += 1
    
    return password






