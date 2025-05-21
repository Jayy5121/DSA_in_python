class Solution(object):
    def romanToInt(self, s):
        op=0
        roman_values = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        i=0
        while i<len(s):
                if i+1<len(s) and roman_values[s[i]]<roman_values[s[i+1]]:
                    op+=roman_values[s[i+1]]-roman_values[s[i]]
                    i+=2
                else:
                    op+=roman_values[s[i]]
                    i+=1
        return op
s1=Solution()
result=s1.romanToInt("IX")
print(result)