class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_list = list(str(x))
        cent_list = len(x_list) // 2
        front_list = x_list[:cent_list]
        if len(x_list) % 2 == 0:
            rear_list = x_list[cent_list:]
        else:
            rear_list = x_list[cent_list + 1:]
        rear_list.reverse()

        return front_list == rear_list