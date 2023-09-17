'''
Basic File I/O
'''

# open a file in read mode
inReadFile = open('/home/zaphod/vscode/h2g2.csv', 'r')
# create an write a file
# don't forget to close it
outWriteFile = open('/home/zaphod/vscode/pythonWrite.tmp', 'w')
for line in inReadFile:
    # prints the lines wihout a CRLF
    print(line, end='')
    outWriteFile.write(line)

# use a variable in a filename spamANDeggs.txt
# uses print format
tmpVariable1 = 'spam'
tmpVariable2 = 'eggs'
outWriteVariable = open('{}AND{}.txt'.format(tmpVariable1, tmpVariable2), 'w')
outWriteVariable.write('spammy')

# closing the open file
inReadFile.close()
outWriteFile.close()
outWriteVariable.close()
