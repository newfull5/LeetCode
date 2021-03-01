class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        diction = dict()

        for string in strs:
            temp = ''.join(sorted(list(string)))
            if temp not in diction.keys():
                diction[temp] = [string]
            else:
                diction[temp].append(string)

        return list(diction.values())
