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

# closing the open file
inReadFile.close()
outWriteFile.close()