class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ''

        for char in s:
            if 97 <= ord(char) <= 122 or 65 <= ord(char) <=  90 or 48 <= ord(char) <= 57:
                string += char.lower()

        return string == string[::-1]
