class Solution:
    def searchMatrix(self, matrix, target):
        # an empty matrix obviously does not contain `target` (make this check
        # because we want to cache `width` for efficiency's sake)
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        # cache these, as they won't change.
        height = len(matrix)
        width = len(matrix[0])

        # start our "pointer" in the bottom-left
        row = height - 1
        col = 0

        while col < width and row >= 0:
            if matrix[row][col] > target:
                row -= 1
            elif matrix[row][col] < target:
                col += 1
            else:  # found it
                return True

        return False


if __name__ == '__main__':
    so = Solution()
    # matrix = [
    #           [1,   4,  7, 11, 15],
    #           [2,   5,  8, 12, 19],
    #           [3,   6,  9, 16, 22],
    #           [10, 13, 14, 17, 24],
    #           [18, 21, 23, 26, 30]
    #         ]
    matrix = [[1,2,3,4,5],
              [6,7,8,9,10],
              [11,12,13,14,15],
              [16,17,18,19,20],
              [21,22,23,24,25]]
    target = 20
    print(so.searchMatrix(matrix,target))