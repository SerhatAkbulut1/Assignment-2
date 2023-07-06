import string
import sys

alphabet = list(string.ascii_uppercase)
categories = {}

temp = sys.stdout
sys.stdout = open('output.txt', 'w', encoding='utf-8')

def createSeats(row, column):
    """ Create a 2D list of seats. """
    seats = []
    for i in range(row):
        seats.append([])
        for j in range(column):
            seats[i].append('X')
    return seats


def createCategory(categoryName, row , column):
    """ Create a dictionary of categories. """
    global row_num
    row_num = row
    global column_num
    column_num = column

    if (categoryName in categories):
        print('Warning:Cannot create the category for the second time. The stadium has already ', categoryName)
    else:
        category = {'category-name': categoryName, 'student': 0, 'full': 0, 'season': 0 , 'row-num' : row_num , 'column-num' : column_num}
        category['seats'] = createSeats(row_num, column_num)
        categories.update({categoryName: category})
        print('The category ', categoryName, ' having ', row_num * column_num, ' seats has been created ')


def sellTicket(customer_name, ticketType , categoryName , location):

    sell_seats = location.split(' ')
    sold_seats = []
    alphabet = list(string.ascii_uppercase)
    local_seats = categories[categoryName]['seats']

    for i in sell_seats:
        if int(alphabet.index(i[0])) > categories[categoryName]['row-num'] and int(i[1])-1 <= categories[categoryName]['column-num']:
            print('Error: The category ', categoryName, ' has less row than the specified index ', location, '!')
        elif int(alphabet.index(i[0])) <= categories[categoryName]['row-num'] and int(i[1])-1 > categories[categoryName]['column-num']:
            print('Error: The category ', categoryName, ' has less column than the specified index ', location, '!')
        elif int(alphabet.index(i[0])) > categories[categoryName]['row-num'] and int(i[1])-1 > categories[categoryName]['column-num']:
            print('Error: The category ', categoryName, ' has less column and row than the specified index ', location,
                  '!')
        elif len(i) == 2:
            if local_seats[alphabet.index(i[0])][int(i[1]) -1 ] == "X":
                if ticketType == "student":
                    local_seats[alphabet.index(i[0])][int(i[1]) -1] = "S"
                    categories[categoryName]['seats'] = local_seats
                    categories[categoryName][ticketType] += 1

                elif ticketType == "full":
                    local_seats[alphabet.index(i[0])][int(i[1]) -1] = "F"
                    categories[categoryName]['seats'] = local_seats
                    categories[categoryName][ticketType] += 1

                elif ticketType == "season":
                    local_seats[alphabet.index(i[0])][int(i[1]) -1] = "T"
                    categories[categoryName]['seats'] = local_seats
                    categories[categoryName][ticketType] += 1
                sold_seats.append(i)

            else:
                print('Warning: The seats', location, 'cannot be sold to', customer_name,'due some of them have already been sold')

        else:
            temp_list = i.split("-")
            if (int(temp_list[0][1])) > categories[categoryName]['column-num'] or int(temp_list[1]) > categories[categoryName]['column-num']:
                print('Error: The category ', categoryName, ' has less column than the specified index ', i , '!')
            else:
                sold_seats.append(i)
                if local_seats[alphabet.index(i[0])][int(i[1]) - 1] == "X":
                    for j in range(int(temp_list[1]) - int(temp_list[0][1]) + 1):
                        if ticketType == "student":
                            local_seats[alphabet.index(temp_list[0][0])][(j + int(temp_list[0][1]))-1] = "S"
                            categories[categoryName]['seats'] = local_seats
                            categories[categoryName][ticketType] += 1

                        elif ticketType == "full":
                            local_seats[alphabet.index(temp_list[0][0])][j + int(temp_list[0][1])-1] = "F"
                            categories[categoryName]['seats'] = local_seats
                            categories[categoryName][ticketType] += 1

                        elif ticketType == "season":
                            local_seats[alphabet.index(temp_list[0][0])][j + int(temp_list[0][1])-1] = "T"
                            categories[categoryName]['seats'] = local_seats
                            categories[categoryName][ticketType] += 1
                else:
                    print('Warning: The seats', location, 'cannot be sold to', customer_name,'due some of them have already been sold')
                    sold_seats.remove(i)
    for j in range(len(sold_seats)):
        print('Success : ', customer_name, 'has bought', sold_seats[j], 'at', categoryName)

def cancelTicket(categoryName, location):
    alphabet = list(string.ascii_uppercase)
    cancel_seats = location.split(' ')
    seat_range_start = 0
    local_seats = categories[categoryName]['seats']

    for i in cancel_seats:
        if int(alphabet.index(i[0])) > categories[categoryName]['row-num'] and int(i[1]) <= categories[categoryName]['column-num']:
            print('Error: The category ', categoryName, ' has less row than the specified index ', location, '!')
        elif int(alphabet.index(i[0])) <= categories[categoryName]['row-num'] and int(i[1]) > categories[categoryName]['column-num']:
            print('Error: The category ', categoryName, ' has less column than the specified index ', location, '!')
        elif int(alphabet.index(i[0])) > categories[categoryName]['row-num'] and int(i[1]) > categories[categoryName]['column-num']:
            print('Error: The category ', categoryName, ' has less column and row than the specified index ', location,'!')
        else:
            if local_seats[alphabet.index(i[0])][int(i[1])] != "X":
                if local_seats[alphabet.index(i[0])][int(i[1])] == "S":
                    categories[categoryName]["student"] -= 1
                    print('Success: The seat', location, 'at', categoryName,'has been canceled and now ready to sell again')
                elif local_seats[alphabet.index(i[0])][int(i[1])] == "F":
                    categories[categoryName]["full"] -= 1
                    print('Success: The seat', location, 'at', categoryName,'has been canceled and now ready to sell again')
                elif local_seats[alphabet.index(i[0])][int(i[1])] == "T":
                    categories[categoryName]["season"] -= 1
                    print('Success: The seat', location, 'at', categoryName,'has been canceled and now ready to sell again')

                local_seats[alphabet.index(i[0])][int(i[1]) - 1] = "X"
            else:
                print("Error: The seat ", i ,categoryName,
                      " has already been free! Nothing to cancel")

def balance(categoryName):
    student_ticket_price, full_ticket_price, season_ticket_price = 10, 20, 250
    total_price = (int(categories[categoryName]['student']) * int(student_ticket_price)) + (
            int(categories[categoryName]['full']) * int(full_ticket_price)) + (
                          int(categories[categoryName]['season']) * int(season_ticket_price))
    print('category report of ', categoryName)
    print("-------------------------------")
    print('Sum of students = ', int(categories[categoryName]['student']), 'Sum of full pay = ',
          int(categories[categoryName]['full']), 'Sum of season ticket = ', int(categories[categoryName]['season']),
          'and Revenues = ', int(total_price), 'Dollars')

def showCategory(categoryName):
    for i in range(int(categories[categoryName]['row-num']) , 0 , -1 ):
        print(alphabet[i - 1],end=" ")
        for j in range(int(categories[categoryName]['column-num']) - 1):
            print(categories[categoryName]['seats'][i-1][j-1],end="  ")
        print(categories[categoryName]['seats'][i-1][int(categories[categoryName]['column-num']) - 1])
    print(' ',end= " ")
    for k in range(int((categories[categoryName]['row-num'])) - 1):
        if k<9:
            print(k , end="  ")
        else:
            print(k, end=" ")
    print(int((categories[categoryName]['row-num'])) - 1)

input = str(sys.argv[1])
file = open(input, "r")
lines = file.readlines()

for line in lines:
    line=line.replace("\n","")
    splited_line = line.split(" ")

    if splited_line[0] == "CREATECATEGORY":
        output = createCategory(splited_line[1], int(splited_line[2].split('x')[0]), int(splited_line[2].split('x')[1]))

    elif splited_line[0] == 'SELLTICKET':
        for i in range(len(splited_line) - 4):
            output = sellTicket(splited_line[1],splited_line[2],splited_line[3],splited_line[i+4])

    elif splited_line[0] == 'CANCELTICKET':
        for i in range(len(splited_line) - 2):
            output = cancelTicket(splited_line[1],splited_line[i+2])

    elif splited_line[0] == 'BALANCE':
        output = balance(splited_line[1])

    elif splited_line[0] == 'SHOWCATEGORY':
        output = showCategory(splited_line[1])


sys.stdout = temp
with open('output.txt', 'r') as file:
    print(*file.readlines())






