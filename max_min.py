def max_min(array, min=0, max=0, pos=0):
    if pos == len(array):
        return min,max
    if min > array[pos]:
        min = array[pos]
    if max < array[pos]:
        max = array[pos]

    return max_min(array,min,max,pos+1)

array=[2,5,8,5,10]
print(max_min(array,array[0],array[0]))

        
            

        
    
