#!/usr/bin/python

read_file = open('Data/Test Input.txt', 'rb')
write_file = open('Data/Test Output.txt', 'w+')

for num, line in enumerate(read_file):
    write_file.write( str( int(num) * int(line) ) + '\n' )

read_file.close()
write_file.close()