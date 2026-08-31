class SecondLargest:

    def second_largest(self, arr):

        largest = float("-inf")
        second_largest = float("-inf")

        for num in arr:

            if num > largest:
                second_largest = largest
                largest = num

            elif num > second_largest and num != largest:
                second_largest = num

        print(second_largest)


se = SecondLargest()

arr = [5, 2, 8, 1, 3]

se.second_largest(arr)
