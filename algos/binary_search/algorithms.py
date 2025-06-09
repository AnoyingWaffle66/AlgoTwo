class Algorithm():
    # Description
    # INPUT a sorted array
    # OUTPUT the index of the element being searched for
    
    # This algorithm will guess the middle element of its given range
    # it will know if the correct element is higher than the guess or lower than the guess.
    # The incorrect portion will be eliminated from the range.
    # It will continue to guess the middle element until it is correct.
    
    # Psuedo code
    # Guess the middle element of min (0 initially) and max (array length -1 initially)
    # if it is correct, return the idx
    # if it is incorrect determine if the element is above or below the guess
    # if the element is greater than the search item than set max to the guessed index
    # if the element is less than the search item then set miin to the guess index
    # call the function again giving it the new range that the element is in until the index is found
    
    # Big-O
    # The time complexity of this algorithm is O(log(n)) because of how the algorithm works, it eliminates half of the remaining elements to search on every iteration
    # for example, if there were 16 elements, the algorithm in the worst case would eliminate 8 then 4 then 2 then 1. It found the correct element in 4 steps rather than 16
    # The space complexity for this algorithm is also O(log(n)). It would be O(1) if it weren't for the recursive nature of the algorithm. However, because it is recursive
    # every iteration is stored in memory, it iterates log(n) times so the space used is also log(n).
    
    @staticmethod
    def binary_search(search_val, array, min=0, max=0):
        if max == 0:
            max = len(array) - 1
        current_idx = (max + min) // 2
        match Algorithm.guess(search_val, array[current_idx]):
            case 1: # guess was too high
                max = current_idx
            case -1: # guess was too low
                min = current_idx + 1
            case 0:
                return current_idx
        return Algorithm.binary_search(search_val, array, min, max)
    
    @staticmethod
    def guess(target, search_guess):
        return 1 if search_guess > target else -1 if search_guess < target else 0