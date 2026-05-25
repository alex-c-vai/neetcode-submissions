class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        
        for i, temperature in enumerate(temperatures): # 5, 40
            if stack:
                while stack and temperature > stack[-1][0]: # [(38, 1)]; 40
                    temp, idx = stack.pop() # 36, 3
                    res[idx] = i - idx # res = [1,0,1,2,1,0,0]
            stack.append((temperature, i)) # [(38,1), (36, 3)]
            print(stack)

        return res