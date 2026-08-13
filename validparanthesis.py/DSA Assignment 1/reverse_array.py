class RA:

    def reverse_array(self, arr):

        left = 0
        right = len(arr) - 1

        # for num in range(len(arr) - 1, -1, -1):
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left = left + 1
            right = right - 1
        print(arr)


rev = RA()
arr = [3, 6, 90, 12, 15]
rev.reverse_array(arr)
