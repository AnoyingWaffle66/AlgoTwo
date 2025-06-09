#INPUT - array of numbers
#OUTPUT - sorted array of numbers

#EFFICIENCY GAINS
# sorted index?
# track whether any swaps are made on an iteration?

# for every number in array
#   from the beginning until the last comparison from previous iteration
#       compare each element to the next
#           if the first element is greater than the 2nd
#               swap the elements


# n iterations
# n comparisons per iteration
# n * n = n^2
#unoptimized comparisons -> n = 5, c = 16
#unoptimized comparisons -> n = 6, c = 25
# total comparisons = (n-1)^2
# UNOPTOMIZED BUBBLE SORT COMPLEXITY O(n^2)

# n = length of the array
# number of iterations = n - 1
# number of comparisons per iteration
# total comparisons = sum 1 -> n - 1
# n * 1/2 n <=> n * n/2 <=> n^2/2
# O(n^2)


def bubble_sort(numbers: list):
    for i in range(len(numbers) - 1):
        for j in range(len(numbers) - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers = swap(numbers, j, j + 1)
    return numbers

def swap(array, index, index2):
    array[index], array[index2] = array[index2], array[index]
    return array

