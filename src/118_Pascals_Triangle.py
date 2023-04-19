class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        for i in range(numRows):
            row = [1]
            element = 1
            for j in range(1, i // 2 + 1):
                element = element * (i - j + 1) // j
                row.append(element)
            match i % 2:
                case 0:
                    row.extend(row[-2::-1])
                case 1:
                    row.extend(row[::-1])
            triangle.append(row)

        return triangle
