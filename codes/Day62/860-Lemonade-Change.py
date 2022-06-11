class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five_bill = 0
        ten_bill = 0
        for bill in bills:
            change = bill - 5
            while change > 0:
                if change >= 10 and ten_bill > 0:
                    ten_bill -= 1
                    change -= 10
                elif change >= 5 and five_bill > 0:
                    five_bill -= 1
                    change -= 5
                else:
                    return False
            if bill == 5:
                five_bill += 1
            elif bill == 10:
                ten_bill += 1
        return True