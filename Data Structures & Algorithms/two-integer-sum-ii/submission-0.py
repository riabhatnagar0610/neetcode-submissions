class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        for i in range(n):
            for j in range(i+1, n):
                sum = numbers[i] + numbers[j]
                if sum == target:
                    return [i+1, j+1]
        return [-1, -1]