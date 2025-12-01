
# class Solution:
#     def plusOne(self, digits: List[int]) -> List[int]:
#         length = len(digits)
        
#         digits = map(str, digits)
#         digits = list(str(int(''.join(digits)) + 1))
        
#         while len(digits) != length:
#             if len(digits) >= length:
#                 break
#             digits = [0] + digits
            
#         return digits


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return [int(t) for t in str(int(''.join([str(digit) for digit in digits])) + 1)]
