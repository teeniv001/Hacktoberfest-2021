numlist = list()                # create an empty list
while (True):
    inp = input('Enter a number: ')
    if inp == 'done': break
    value = float(inp)
    numlist.append(value)       # append values in numlist

average = sum(numlist) / len(numlist)
print('Average:', average)
