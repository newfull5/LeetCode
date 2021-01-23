class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        idx = 2000
        answer = []
        for i in range(len(list1)):
            if list1[i] in list2:
                if idx > i + list2.index(list1[i]):
                    idx = i + list2.index(list1[i])
                    answer = [list1[i]]
                if idx == i + list2.index(list1[i]):
                    if list1[i] not in answer:
                        answer.append(list1[i])
                    
        return answer
