#created by raymond octavious
#created in november,2017
#created for isc3u
#this program finds the smallest value in the array and returns it to a function

def value(array = []):
    min = array[0]
    for a_number in array:
        if min > a_number:
            min = a_number
         
        
    return min

array = [4,8,3,8]
lowest_value = value(array)
print(array)
print(lowest_value)
