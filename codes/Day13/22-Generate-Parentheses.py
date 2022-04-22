class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        brckt_list = []
        
        OPEN = '('
        CLOSE = ')'
        
        def generate_brckt(open_num, close_num, brckt_str=''):
            if open_num == 0:
                brckt_str = brckt_str + CLOSE*close_num
                brckt_list.append(brckt_str)
                return
            
            if open_num < close_num:
                generate_brckt(open_num, close_num-1, brckt_str+CLOSE)
                
            generate_brckt(open_num-1, close_num, brckt_str+OPEN)
            
        generate_brckt(n, n)
        
        return brckt_list