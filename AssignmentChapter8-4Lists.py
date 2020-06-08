#8.4 Open the file romeo.txt and read it line
#by line. For each line, split the line into a
#list of words using the split() method.
#The program should build a list of words.
#For each word on each line check to see if
#the word is already in the list and if not append
#it to the list. When the program completes, sort
#and print the resulting words in alphabetical order.
fname = input ("Enter file name: ")
count = 0
finallist = list ()
word = ''
try:
    fhandle = open(fname)
except:
    print ('Incorrect file name, thanks')
    quit()
for line in fhandle:
    line = line.rstrip()
    words = line.split()
    for word in words:
        if word in finallist:continue
        finallist.append(word)
finallist.sort()
print (finallist)

