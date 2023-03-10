#  taken from: https://tutorialedge.net/compsci/sorting/quicksort-in-python/
import math


def quicksort(array):
    # We define our 3 arrays
    less = []
    equal = []
    greater = []

    # if the length of our array is greater than 1
    # we perform a sort
    if len(array) > 1:
        # Select our pivot. This doesn't have to be
        # the first element of our array
        pivot = array[int(len(array)/2)]
        # print("pivot is " + str(pivot))
        # recursively go through every element
        # of the array passed in and sort appropriately
        for x in array:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)

        # recursively call quicksort on gradually smaller and smaller
        # arrays until we have a sorted list.
        return quicksort(less) + equal + quicksort(greater)

    else:
        return array


def main():
    print(quicksort([6, 4, 7, 1, 2, 9, 12, 3]))


if __name__ == "__main__":
    main()
