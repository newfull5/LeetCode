class Solution:
    def trap(self, height: List[int]) -> int:
        
        # 해당 알고리즘은 2회 수행되는 까닭에 함수로 만들어서 재사용했어요!
        def solution(height, answer):

            left = None

            # 0 이 아닌 최초의 값을 찾아서 left에 할당합니다.
            for i in range(len(height)):
                if left == None and height[i] != 0:
                    left = i

            
            while True:
                try:
                    # 현재값 height[i]를 기준으로 선형탐색 합니다.
                    # len(height)+10에서 +10은 그냥 넉넉히 넣은거에요. +1해도 괜찮아요 
                    for i in range(left+1, len(height)+10):
                        
                        # 현재값 보다 크거나 같은 값이 나온다면
                        if height[i] >= height[left]:
                            
                            # 각각의 요소에서 현재값을 뺀 값을 모두 합하여 answer 변수에 더합니다.
                            answer += (height[left] * (i-left)) - sum(height[left:i])
                            
                            # 오른쪽 포인터를 왼쪽으로 넘겨 받아서 위의 과정을 계속 진행합니다.
                            left = i
                            break
                
                # 선형 탐색을 끝까지 마쳤다면 (인덱스가 배열의 크기를 넘어갔다면) while문을 탈출합니다.
                except IndexError:
                    break

            return answer
        
        # 혹시 길이가 2 이하의 배열이 인풋으로 들어온다면 0을 반환합니다. (예외처리)
        if len(height) <=2 :
            return 0

        # 가장 큰 값을 찾아봅니다.
        idx = height.index(max(height))
        
        # 정답 값으로 리턴할 answer 배열을 선언
        answer = 0

        # 가장 큰 값을 기준으로 2등분하여 위의 알고리즘을 2회 수행합니다.
        answer = solution(height[:idx+1], answer)
        answer = solution(height[idx:][::-1], answer)
        
        return answer
