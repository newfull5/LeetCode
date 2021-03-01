"""
#Runtime: 100 ms, faster than 59.14% Memory Usage: 17.1 MB, less than 92.97%
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
"""
#Runtime: 220 ms, faster than 5.59% Memory Usage: 17.9 MB, less than 45.76%    
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict

        anagrams = defaultdict(list)

        for word in strs:

            anagrams[''.join(sorted(word))].append(word)

        return anagrams.values()
