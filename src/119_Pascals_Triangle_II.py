class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        element = 1

        for j in range(1, rowIndex // 2 + 1):
            element = element * (rowIndex - j + 1) // j
            row.append(element)

        match rowIndex % 2:
            case 0:
                row.extend(row[-2::-1])
            case 1:
                row.extend(row[::-1])

        return row
