class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        l, r = 0, m-1
        while l <= r:
            mid = l + ((r-l) // 2)
            if matrix[mid][-1] < target:
                l = mid + 1
            elif matrix[mid][0] > target:
                r = mid - 1
            else:
                mid_m = mid
                print(mid_m)
                l_n, r_n = 0, n-1
                while l_n <= r_n:
                    mid_n = l_n + ((r_n-l_n) // 2)
                    print(l_n, r_n, mid_n)
                    if matrix[mid_m][mid_n] < target:
                        l_n = mid_n + 1
                    elif matrix[mid_m][mid_n] > target:
                        r_n = mid_n - 1
                        print(r_n)
                    else:
                        return True
                return False
        return False
