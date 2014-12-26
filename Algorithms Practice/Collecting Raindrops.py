##The following bar graph could be considered an elevation profile of land (grey squares) with hills and valleys.
##If it rained all over the graph, the valleys would fill with water and turn to lakes, eventually overflowing to the sides.  Write code to determine how much water (unit squares) would be held in the lakes.
##
##Example Input (for the graph above):
##any reasonable input format is acceptable):
##(0,5), (1,2), (2,3), (3,1), (4,6), (5,3), (6,8)
##or
##5,2,3,1,6,3,8
##Note: any reasonable input format is fine with me - the point of the question is the amount of water, not parsing input.
##
##This input should return the value 12 (the blue water squares are numbered to demonstrate this).


def raining(arr):
    counter=i=start=end=0
    length = len(arr)-1
    while (end !=length):
        while ((arr[end] <= arr[start]) and (end != length)):
            end += 1
        print start, end, counter
        low = min(arr[start], arr[end])
        if (low != arr[end]):
            for i in range(start+1, end):
                counter += low - arr[i]
        start = end
        print "counter: ",counter
    return counter
    
        
#hills = [5,2,3,1,6,3,8]
#hills = [2,5,1,2,3,4,7,7,6]
hills = [2,5,1,3,1,2,1,7,6]
print raining(hills)
