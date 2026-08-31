class Smallest_Element:

    def largest_element(self, arr):
        largest = arr[0]
        for i in range(1, len(arr)):
            if arr[i] > largest:
                largest = arr[i]
        print(largest)


se = Smallest_Element()
arr = [2, 3, 6, 2, 12, 15, 0, 2, 2, 2, 2, 22, 22.3, 2]
se.largest_element(arr)
