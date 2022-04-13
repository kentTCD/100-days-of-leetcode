class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        mx_wealth = 0
        for account in accounts:
            wealth = sum(account)
            if wealth > mx_wealth:
                mx_wealth = wealth

        return mx_wealth