class Solution:
    #use sub dicst?
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        myRows = []
        myCols = []
        for i in range(len(board)):
            row = [set() for _ in range(3)]
            col = [set() for _ in range(3)]
            myRows.append(row)
            myCols.append(col)

        for i, row in enumerate(board):
            for j, num in enumerate(row):
                if num == ".":
                    continue

                if num in myRows[i][0] or num in myRows[i][1] or num in myRows[i][2]:
                    print(num)
                    print(myRows)
                    return False

                if num in myCols[j][0] or num in myCols[j][1] or num in myCols[j][2]:
                    print(num)
                    print(myRows)
                    return False

                iRow = i//3 * 3

                if num in myRows[iRow][j//3] or num in myRows[iRow + 1][j//3] or num in myRows[iRow + 2][j//3]:
                    print(num)
                    print(myRows)
                    return False


                myRows[i][j//3].add(num)
                myCols[j][i//3].add(num)

        return True