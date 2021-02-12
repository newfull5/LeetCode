class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        
        if m*k > len(bloomDay):
            return -1

        def linearsearch(bloomDay, k, m):

            answer = []

            cnt = 0
            for i in range(len(bloomDay)-1):
                if bloomDay[i] <= 0:
                    cnt += 1
                if bloomDay[i+1] > 0:
                    answer.append(cnt)
                    cnt = 0
            else:
                if bloomDay[-1] <= 0:
                    answer.append(cnt+1)
                else:
                    answer.append(cnt)

            ans = 0

            for num in answer:
                ans += (num // k)

            return ans >= m


        sorted_bloom = sorted(list(set(bloomDay)))

        left, right = 0, len(sorted_bloom)-1

        while left <= right:
            mid = (left+right) // 2
            bloom = list(map(lambda x: x-sorted_bloom[mid], bloomDay))

            if linearsearch(bloom, k, m):
                right = mid - 1

            else:
                left = mid + 1

        return sorted_bloom[left]
