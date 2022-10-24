#Problem 1. Sort With Quicksort.
# Please build a function called "quicksort" that uses recursion to define the quicksort algorithm for a list of any length. 
# Build a main script that reads in the list provided, "numbers.txt", and runs it through your quicksort algorithm. 
# The main script should return the finished sorted list as "sorted.txt"
# All 3 files "In_class_assignment_5.py", "numbers.txt", and "sorted.txt" should all be added to your github repository and submitted as a github link.


'''Info on Quicksort Algorithm: 
The Quicksort algorithm is an efficient sorting algorithm developed by British computer scientist Tony Hoare in 1959.

Quicksort is a divide-and-conquer algorithm. Suppose you have a list of objects to sort. You start by choosing an item in the list, called the *pivot item*. 
This can be any item in the list. You then partition the list into two sublists based on the pivot item and recursively sort the sublists.

The steps of the algorithm are as follows:

1. Choose the pivot item.
2. Partition the list into two sublists:
        Those items that are less than the pivot item
        Those items that are greater than the pivot item
3. Quicksort the sublists recursively.
4. Each partitioning produces smaller sublists, so the algorithm is reductive. 

The base cases occur when the sublists are either empty or have one element, as these are inherently sorted. 
 '''
import numbers
import statistics
from asyncore import read

def partition(list, start, end):        #created partition for the quicksort function
    place = start                          

    for i in range(start, end):
        if list[i] < list[end]:
            list[i],list[place] = list[place],list[i]
            place += 1

    list[place],list[end] = list[end],list[place] 

    return place

def quicksort(list, start, end):

#WRITE YOUR CODE HERE FOR THE RECURSIVE SORTING FUNCTION 
   if start < end:                      
        place = partition(list, start, end)
        quicksort(list, start, place - 1)
        quicksort(list, place + 1, end)
        
def main():

# WRITE YOUR MAIN FUNCTION HERE TO READ IN YOUR numbers.txt FILE, RUN THE LIST THROUGH YOUR SORTING ALGORITHM, 
# AND WRITE OUT YOUR FILE

    f = open('numbers.txt','r')
    print()
    g = f.read()
    h = g.replace("[","")
    i = h.replace("]","")
    j = list(i.split(", "))
    numList = [int(z) for z in j]
    print("Original List:")
    print(numList)
    quicksort(numList, 0, len(numList) - 1)
    print("Sorted List:")
    print(numList)
    x = open("sorted.txt", "w")
    output = str(numList)
    print(output)
    
    return x.write(output)


if __name__ == "__main__":
    main()
