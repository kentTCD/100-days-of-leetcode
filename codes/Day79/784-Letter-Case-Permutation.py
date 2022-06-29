class Solution(object):
    def letterCasePermutation(self, s):
        res = []
        
        def helper(res, path, options):
            if len(options) == 0:
                res.append(path)
            else:
				#Take one element from string and update remaining options
                num = options[0]
                options = options[1:]
				
				#If the element is number, simply append it and continue
				#otherwise append both the upper and lower case of the letter
                if num.isdigit():
                    helper(res, path+num, options)
                else:
                    helper(res, path+num.lower(), options)
                    helper(res, path+num.upper(), options)
                    
        helper(res, "", s)
        return res