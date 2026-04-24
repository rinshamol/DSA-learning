from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        self.findSum(0,target,[],ans,candidates)
        return ans
    def findSum(self,index, target, sub, ans, candidates) :
        if(index == len(candidates)) :
            if(target == 0) :
                ans.append(sub.copy())
            return
        if(candidates[index] <= target):
            sub.append(candidates[index])
            self.findSum(index, target - candidates[index], sub, ans, candidates)
            sub.remove(candidates[index])
        self.findSum(index + 1, target, sub, ans, candidates)

print(Solution().combinationSum([2,3,6,7], 7))