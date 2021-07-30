from collections import Counter
import copy


class Solution:
    def __init__(self):
        self.dict = {}

    def deleteAndEarn(self, nums: list) -> int:

        diction, answer = self.get_default_score(Counter(nums))
        self.dict = {k: k*v for k, v in diction.items()}
        arrays = self.split(self.dict)

        answer = 0

        for arr in arrays:
            answer += self.get_max(arr)

        return answer


    def split(self, diction: dict):
        return_arr = []

        keys = list(diction.keys())

        left = 0

        for right in range(len(keys)-1):
            if keys[right+1] - keys[right] == 1:
                continue

            return_arr.append(keys[left:right])
            left = right

        return_arr.append(keys[left:])
        return return_arr

    def get_default_score(self, diction: dict) -> (dict, int):
        answer = 0
        length = len(diction.keys())
        keys = list(diction.keys())

        diction_copy = copy.copy(diction)

        for k in diction.keys():

            if diction[k] + 1 in keys or diction[k] - 1 in keys:
                continue

            del diction_copy[k]
            answer += (k * diction[k])

        return diction_copy, answer

    def get_max(self, nums: list):

        def dfs(nums: list, nxt: bool, num_sum: int):
            nonlocal answer

            if not nums:
                answer = max(answer, num_sum)
                return

            if nxt:
                dfs(nums[:-1], False, num_sum + self.dict[nums[-1]])

            else:
                dfs(nums[:-1], True, num_sum)
                dfs(nums[:-1], False, num_sum)

        answer = 0

        dfs(list(self.dict.keys()), True, 0)
        dfs(list(self.dict.keys()), False, 0)

        return answer

if __name__ == '__main__':

    nums = [3,4,2]
    sol = Solution()
    print(sol.deleteAndEarn(nums))