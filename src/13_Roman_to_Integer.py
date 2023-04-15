class Solution:
    def romanToInt(self, roman_number: str) -> int:
        roman_to_arabic_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        arabic_number = 0

        for i in range(len(roman_number)):
            current_value = roman_to_arabic_dict[roman_number[i]]
            if i < len(roman_number) - 1 and current_value < roman_to_arabic_dict[roman_number[i + 1]]:
                arabic_number -= current_value
            else:
                arabic_number += current_value

        return arabic_number
