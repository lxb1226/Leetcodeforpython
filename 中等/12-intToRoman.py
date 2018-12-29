class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        lookup = {
            'M':1000,
            'CM':900,
            'D':500,
            'CD':400,
            'C':100,
            'XC':90,
            'L':50,
            'XL':40,
            'X':10,
            'IX':9,
            'V':5,
            'IV':4,
            'I':1
        }
        roman = ''
        for symbol,val in sorted(lookup.items(),key=lambda t: t[1])[::-1]:
            while num >= val:
                roman += symbol
                num -= val 
        return roman

if __name__ == "__main__":
    solution = Solution()
    num = 1994
    result = solution.intToRoman(num)
    print(result)

