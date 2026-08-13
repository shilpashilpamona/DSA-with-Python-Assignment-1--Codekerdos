class Smallest_Element:

    def smallest_element(self, arr):
        small = arr[0]
        for i in range(1, len(arr)):
            if arr[i] < small:
                small = arr[i]
        print(small)


se = Smallest_Element()
arr = [2, 3, 6, 2, 12, 15, 0, 2, 2, 2, 2, 22, 22.3, 2, -1]
se.smallest_element(arr)
