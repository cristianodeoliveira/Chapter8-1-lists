#it keeps the numbers in a list
numlist = list()
while True:
    inp = input ('Enter a number: ')
    if inp == 'done': break
    try:
        value = float (inp)
    except:
        continue
    numlist.append(value)
#outside the loop it calculates the sum ()
#then it shows the average by dividing the sum
#by the number of items in the list
average = sum(numlist) / len (numlist)
print (numlist)
print (average)