##           1
##        1     1  
##      1    2     1
##    1   3    *3*    1 
## 1    4    6     4    1
##
##int pascal(int row, int col);
##pascal(3,2) = 3


def nextRow(row):
    nextRow = [1]
    for i in range(len(row)-1):
        x = row[i] + row[i+1]
        nextRow.append(x)
    nextRow.append(1)
    return nextRow
    

def pascalIterative(numRows, col):
    row = [1]
    x = 0
    while x < numRows:
        print ' '*(numRows-x),  row
        row = nextRow(row)       
        x += 1
    print row
    return row[col]

def pascalRecursive( numRows, col, count, row ):
    print ' '*(numRows-count),  row
    if count==numRows: return row[col]
    return pascalRecursive( numRows, col, count+1, nextRow(row) )

print pascalIterative(3,2)
print pascalRecursive(3, 2, 0, [1])
