# Python program to get average of a list
def Average(lst):
    return sum(lst) / len(lst)
 
# Driver Code
lst = [1,2,2,15, 9, 55, 41, 35, 20, 62, 49]
average = Average(lst)
sum=sum(lst)
# Printing sum of the list
print("sum is ",sum)
print(average)
# Printing average of the list
print("Average of the list =", round(average,0))
