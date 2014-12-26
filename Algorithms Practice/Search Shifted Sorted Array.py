def binarySearch(arr,key, start, end):
    #print "here"
    while (end >= start):
        mid = (end+start)/2
        if (arr[mid] == key): return mid
        elif (key > arr[mid]): start = mid+1
        else: end = mid-1
    return -1

def shiftedSearch(arr, key):
    start, end = 0, len(arr)-1
    while (end >= start):
        mid = (end+start)/2
        #print "mid:", arr[mid]
        if (arr[mid] == key): return mid
        elif (arr[start]<=key<=arr[mid]):
            return binarySearch(arr,key,start,mid-1)
        elif (arr[mid]<=key<=arr[end]):
            return binarySearch(arr,key,mid+1,end)
        elif arr[mid]<=arr[end]: end = mid-1
        elif arr[start]<=arr[mid]: start = mid+1
        #print "start:", arr[start], "end:", arr[end]
    return -1

print shiftedSearch([6,7,8,9,10,11,12,1,2,3,4,5],3)
print shiftedSearch([6,7,8,9,10,11,12,1,2,3,4,5],8)
print shiftedSearch([6,7,8,9,10,11,12,1,2,3,4,5],0)
print shiftedSearch([6,7,8,9,10,11,12,1,2,3,4,5],13)
print shiftedSearch([6,7,8,9,10,11,12,1,2,3,4,5],6)
print shiftedSearch([6,7,8,9,10,11,12,1,2,3,4,5],5)

