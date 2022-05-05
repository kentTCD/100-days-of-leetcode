class Solution:
    def freqAlphabets(self, s: str) -> str:
        decrypt_dict = {
            '1':'a', '2':'b', '3':'c', '4':'d',
            '5':'e', '6':'f', '7':'g', '8':'h',
            '9':'i', '10':'j', '11':'k', '12':'l',
            '13':'m', '14':'n', '15':'o', '16':'p',
            '17':'q', '18':'r', '19':'s', '20':'t',
            '21':'u', '22':'v', '23':'w', '24':'x',
            '25':'y', '26':'z'
        }
        rtn_str = ""
        for i in range(len(s)):
            if i <= len(s)-3:
                if s[i+2] == '#':
                    rtn_str += decrypt_dict[s[i]+s[i+1]]
                elif s[i+1] == '#' or s[i] == '#':
                    continue
                else:
                    rtn_str += decrypt_dict[s[i]]
            elif i == len(s)-2:
                if s[i+1] == '#' or s[i] == '#':
                    continue
                else:
                    rtn_str += decrypt_dict[s[i]]
            else:
                if s[i] == '#':
                    continue
                else:
                    rtn_str += decrypt_dict[s[i]]
        return rtn_str