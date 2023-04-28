class Solution:
    def convertToTitle(self, column_number: int) -> str:
        column_title = ''
        while column_number > 0:
            column_number -= 1
            column_title = chr(column_number % 26 + 65) + column_title
            column_number //= 26
        return column_title
