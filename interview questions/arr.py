#n : size of the array
#val1 : an integer
#array : an array of integers

def count_ints(n, val1, array):
    smaller_int = sum(1 for _ in array if _ < val1)
    equal_int = sum(1 for _ in array if _ ==val1)
    greater_int = sum( 1 for _ in array if _ > val1)
    return [smaller_int, equal_int, greater_int]
    
n =5
val1 = 6
array = [2,4,6,8,10]
result = count_ints(n,val1,array)
print('.'.join(map(str,result)))
#O/P: 2 1 2