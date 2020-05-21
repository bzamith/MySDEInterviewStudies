class Solution:
    # @param A : integer
    # @return a strings
    def intToRoman(self, A):
        ones = ["","I","II","III","IV","V","VI","VII","VIII","IX"]
        tens = ["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
        hundreds = ["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]
        thousands = ["","M","MM","MMM"]
        
        return thousands[(A//1000)]+hundreds[(A%1000)//100]+tens[(A%100)//10]+ones[A%10]

class Solution2:
    # @param A : integer
    # @return a strings
    def intToRoman(self, num):
        num_map = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
           (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
        roman = ''
        while num > 0:
            for i, r in num_map:
                while num >= i:
                    roman += r
                    num -= i
        return roman
