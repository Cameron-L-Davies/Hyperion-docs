#set up initial minefield
minefield = [
["-","-","-","#","#"],
["-","#","-","-","-"],
["-","-","#","-","-"],
["-","#","#","-","-"],
["-","-","-","-","-"],]

#create the output minefield grid
new_minefield = [[0]*5 for _ in range (5)]


#create counter variables
curr_row = 0
curr_col = 0


#run through the rows and columns of the grid
#if an item in the grid is a '#', increase all the numbers around the '#' by 1
# if the item adjacent to the '#' is not a number, skip it 
for row in minefield:  
    curr_col = 0
    for col in row:
        
        if minefield[curr_row][curr_col] == '#':
            new_minefield[curr_row][curr_col] = '#'
            for i in range(-1,2):
                for x in range(-1,2):
                    if (curr_row + i) >= 0 and (curr_col + x) >= 0:
                        try: 
                            if type(new_minefield[curr_row + i][curr_col + x]) == int:
                                
                                new_minefield[curr_row + i][curr_col + x] += 1
                                #print(new_minefield)
                                
                            else:
                                continue
                        except(IndexError):         # learnt at https://www.excell-en.com/blog/2020/2/14/python-handling-errors-like-iferror
                            continue                
        curr_col +=1
    curr_row +=1

    
#convert new minefield to strings
curr_row = 0
curr_col = 0
for row in new_minefield:
    for col in new_minefield:
        new_minefield[curr_row][curr_col] = str(new_minefield[curr_row][curr_col])
        curr_col += 1
    curr_row += 1
    curr_col = 0


print('-------Initial Input-------')
for row in minefield:
    print(row)

print('\n-------Final Output-------')
for row in new_minefield:
    print(row)    