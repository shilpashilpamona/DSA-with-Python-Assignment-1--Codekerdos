class SecondSmallest:

    def second_smallest(self, arr):

        smallest = float("inf")
        second_smallest = float("inf")

        for num in arr:

            if num < smallest:
                second_smallest = smallest
                smallest = num

            elif num < second_smallest and num != smallest:
                second_smallest = num

        print(second_smallest)


se = SecondSmallest()

arr = [5, 2, 8, 1, 3]

se.second_smallest(arr)
