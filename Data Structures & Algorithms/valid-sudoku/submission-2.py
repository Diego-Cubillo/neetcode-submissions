class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        mySquares = []

        myRows = [set() for _ in range(9)]
        myCols = [set() for _ in range(9)]
        mySquares = [[set(), set(), set()] for _ in range(3)]
        print(mySquares)

        for i, row in enumerate(board):
            for j, num in enumerate(row):
                if num == ".":
                    continue

                if num in myRows[i]:
                    return False

                if num in myCols[j]:
                    return False

                squareRow = i//3 
                squareCol = j//3 
                if num in mySquares[squareRow][squareCol]:
                    return False

                myRows[i].add(num)
                myCols[j].add(num)
                mySquares[squareRow][squareCol].add(num)

        return True