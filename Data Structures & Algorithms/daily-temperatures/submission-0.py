class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = []
        n = len(temperatures)
        for i in range(n):
            for j in range(i+1, n):
                if temperatures[j] > temperatures[i]:
                    output.append(j-i)
                    break
            else:
                output.append(0)
        return output
        