#! /usr/bin/python3
# Copyright (C) 2021 Fares Ahmed
#
# This file is part of matrix-py.
#
# matrix-py is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# matrix-py is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with matrix-py.  If not, see <http://www.gnu.org/licenses/>.

"""Hackable Matrix module written in pure Python + CLI

https://github.com/faresahemdb/matrix-py

Please refer to the link above for more information
on how to use the module.

You can call matrix-py CLI help with:
$ matrixpy --help
OR $ python -m matrixpy --help
"""

# pylint: disable=C0103 # Variable name "m" is "iNvAlId-nAmE"

import argparse as _argparse
import json as _json
import random as _random


__all__     = ['Matrix', 'MatrixError']
__version__ = '0.6.1'
__author__  = "Fares Ahmed <faresahmed@zohomail.com>"


class MatrixError(Exception):
    """Error for the Matrix Object invalid operations"""


class Matrix:
    """Matrix Object that support Addition, Substraction, [...]
    And Capable of manipulation, Hackable
    """

    # Object Creation: START
    def __init__(self, matrix):
        """Initialize Matrix Object | 3 Ways.

        [Nested List]    Matrix([[1, 2, 3], [4, 5, 6]])
        [One Number (I)] Matrix(3) -> (3x3) Identity Matrix
        [String]         Matrix("1 2 3; 4 5 6")
        """
        # Matrix([[1, 2, 3], [4, 5, 6]]) -> Row1 = (1 2 3), Row2 = (4 5 6)
        self.matrix = matrix

        # Matrix(3) -> (3x3) Identity Matrix
        if isinstance(matrix, int):
            self.matrix = Matrix.identity(matrix).tolist()

        # Matrix("1 2 3; 4 5 6") -> Row1 = (1 2 3), Row2 = (4 5 6)
        if isinstance(matrix, str):
            # input: Matrix("1 2 3; 4 5 6") | output: Matrix([[1, 2, 3], [4, 5, 6]])
            matrix = matrix.split(';')             # ["1 2 3", " 4 5 6"]
            matrix = list(map(str.lstrip, matrix)) # ["1 2 3", "4 5 6"]
            for i, nums in enumerate(matrix):      # [['1', '2', '3'], ['4', '5', '6']]
                matrix[i] = nums.split(' ')

            # list From str -> int
            self.matrix = [list(map(int, matrix[i]))
            for i in range(len(matrix))]

        self.rowsnum = len(self.matrix)
        self.colsnum = len(self.matrix[0])

    def __repr__(self):
        """Returnt a representation of the Matrix Object
        Appears when using an interactive Python shell

        >>> Matrix(3)
        Output: '1 0 0; 0 1 0; 0 0 1'
        """
        result = list()

        ma_str = [list(map(str, self.matrix[i]))
        for i in range(self.rowsnum)]

        for i in ma_str:
            result.append(" ".join(i))

        return "; ".join(result)

    def __str__(self):
        """Return the matrix in `str` representation
        Appears when using print(Matrix)

        >>> print(Matrix.random((3,3), 1, 1000))
        Output: 133 23  388
                4   335 6
                72  8   933
                   (3x3)
        """
        matrix_str = list()
        rows = str()

        for row in self.matrix:  # [[1, 2, 3]] -> [["1", "2", "3"]]
            matrix_str.append(list(map(str, row)))

        # Get the maximum number in the matrix
        maxlen = int()
        for row in matrix_str:
            if len(max(row, key=len)) > maxlen:
                maxlen = len(max(row, key=len))

        for i in range(len(matrix_str)):
            for x in range(len(matrix_str[0])):
                rows += matrix_str[i][x] + " "
                rows += " " * (maxlen-len(matrix_str[i][x]))
            rows = rows.rstrip()
            rows += "\n"

        # Calculate the spaces before (ROWSNUMxCOLSNUM)
        rwcl_spaces = " " * (len(rows.split("\n")[-2]) // 2 -
                            len(f"({self.rowsnum}x{self.colsnum})") // 2)

        return rows + rwcl_spaces + f"({self.rowsnum}x{self.colsnum})"

    def __getitem__(self, rowcol):
        """Return row, col, or item of Matrix Object
        MatrixObject = Matrix("1 2 3; 4 5 6")

        [Row] MatrixObject[1]  -> '4 5 6'
        [Col] MatrixObject[:1] -> '2; 5'
        [Item] MatrixObject[1, 2] -> 6

        Note: in [Item] the first arg is the row
        num and the second is the col num.
        """
        # Return row if one argument (int) was given (M[1])
        if isinstance(rowcol, int):
            return Matrix(self.matrix).row(rowcol)

        # Return col if slice was given (M[:1])
        if isinstance(rowcol, slice):
            return Matrix(self.matrix).col(rowcol.stop)

        # Return Matrix item if 2 arguments (list) was given
        return self.matrix[rowcol[0]][rowcol[1]]

    def __contains__(self, item):
        """If item `in` MatrixObject | True if in the Matrix else False"""
        for row in self.matrix:
            if item in row:
                return True
        return False
    # Object Creation: END

    # Object Expressions: START
    def __pos__(self):
        """Positive operator: +MatA | Return MatA * 1 (copy)"""
        result = list()

        for i in range(self.rowsnum):
            result.append([])
            for m in range(self.colsnum):
                result[i].append(+self.matrix[i][m])

        return Matrix(result)

    def __neg__(self):
        """Negative operator: -MatA. | Returns MatA * -1"""
        result = [[-x for x in y] for y in self.matrix]

        return Matrix(result)
    # Object Expressions: END

    # Object Math operations: START
    def __add__(self, other):
        """Matrix Addition: MatA + MatB or MatA + INT."""
        if isinstance(other, Matrix):
            # MatA + MatB
            result = list()

            if (self.rowsnum != other.rowsnum or
                self.colsnum != other.colsnum):
                raise MatrixError('To add matrices, the matrices must have'
                ' the same dimensions') from None

            for m in range(self.rowsnum):
                result.append([])
                for j in range(self.colsnum):
                    result[m].append(self.matrix[m][j] + other.matrix[m][j])

        else:
            # MatA + INT
            result = list()

            for m in range(self.rowsnum):
                result.append([])
                for i in range(self.colsnum):
                    result[m].append(self.matrix[m][i] + other)

        return Matrix(result)

    def __sub__(self, other):
        """Matrix Subtraction: MatA - MatB or MatA - INT."""
        if isinstance(other, Matrix):
            # MatA + MatB
            result = list()

            if (self.rowsnum != other.rowsnum or
                self.colsnum != other.colsnum):
                raise MatrixError('To sub matrices, the matrices must have'
                ' the same dimensions') from None

            for m in range(self.rowsnum):
                result.append([])
                for j in range(self.colsnum):
                    result[m].append(self.matrix[m][j] - other.matrix[m][j])
        else:
            # MatA + INT
            result = list()

            for m in range(self.rowsnum):
                result.append([])
                for i in range(self.colsnum):
                    result[m].append(self.matrix[m][i] - other)

        return Matrix(result)

    def __mul__(self, other):
        """Matrix Multiplication: MatA * MatB or MatA * INT."""
        if isinstance(other, Matrix):
            # MatA * MatB
            if self.colsnum != other.rowsnum:
                raise MatrixError('The number of Columns in MatA must be'
                ' equal to the number of Rows in MatB') from None

            # References:
            # https://www.geeksforgeeks.org/python-program-multiply-two-matrices
            result = [[sum(a * b for a, b in zip(A_row, B_col))
                            for B_col in zip(*other.matrix)]
                                    for A_row in self.matrix]
        else:
            # MatA * INT
            result = list()

            for m in range(self.rowsnum):
                result.append([])
                for i in range(self.colsnum):
                    result[m].append(self.matrix[m][i] * other)

        return Matrix(result)
    # Object Math opertaions: END

    # Object Manpulation: START
    def row(self, num: int, start=0):
        """Return the row of the position `num`
        Alternative to `MatrixObject[INT]` (it's
        actullay what `MatrixObject[INT]` is using)

        start=1 if you want to use the Matrix like
        in real life.
        """
        if num > start-1:
            num -= start

        try:
            return Matrix([self.matrix[num]])
        except IndexError:
            raise MatrixError('Matrix Index out of range') from None


    def col(self, num: int, start=0):
        """Return the col in the position `num`
        Alternative to `MatrixObject[:INT]` (it's
        actullay what `MatrixObject[:INT]` is using)

        start=1 if you want to use the Matrix Object
        like in real life
        """
        if num > start-1:
            num -= start

        try:
            return Matrix([[row[num]] for row in self.matrix])
        except IndexError:
            raise MatrixError('Matrix Index out of range') from None


    def addrow(self, row, index=-1):
        """Add a new row to your Matrix Object
        MatrixObject -> '1 2 3'

        MatrixObject.addrow('4 5 6')
        Output: '1 2 3; 4 5 6'

        DON'T USE IT. IT'S BUGGY AND UNDER
        DEVOLPMENT RIGHT NOW.
        """
        result = self.matrix

        if index == -1:
            result.insert(self.rowsnum, (Matrix(row).tolist()[0]))
        else:
            result.insert(index, (Matrix(row).tolist()[0]))

        return Matrix(result)


    def addcol(self, col, index=-1):
        """Add a new col to your Matrix Object
        MatrixObject -> '1 2 3; 5 6 7'

        MatrixObject.addcol('4 8')
        Output: '1 2 3 4; 5 6 7 8'

        DON'T USE IT. IT'S BUGGY AND UNDER
        DEVOLPMENT RIGHT NOW.
        """
        result = self.matrix

        if index == -1:
            for i in range(self.rowsnum):
                result[i].insert(self.colsnum, Matrix(col)[0, i])
        else:
            for i in range(self.rowsnum):
                result[i].insert(index, Matrix(col)[0, i])

        return Matrix(result)


    def rmrow(self, index):
        """Remove an Existing row from your Matrix Object.
        MatrixObject -> '1 2 3; 4 5 6'

        MatrixObject.rmrow(1)
        Output: '1 2 3'

        DON'T USE IT. IT'S BUGGY AND UNDER
        DEVOLPMENT RIGHT NOW.
        """
        result = self.matrix

        try:
            result.pop(index)
        except IndexError:
            raise MatrixError("Matrix index out of range") from None

        return Matrix(result)


    def rmcol(self, index):
        """Remove an Existing col from your Matrix Object.
        MatrixObject -> '1 2 3 4; 5 6 7 8'

        MatrixObject.rmcol(1)
        Output: '1 3 4; 5 7 8'

        DON'T USE IT. IT'S BUGGY AND UNDER
        DEVOLPMENT RIGHT NOW.
        """
        result = self.matrix

        try:
            for i in range(self.rowsnum):
                result[i].pop(index)
        except IndexError:
            raise MatrixError("Matrix index out of range") from None

        return Matrix(result)


    def transpose(self: list):
        """Return the Matrix transposed
        rows -> cols, cols -> rows
        """
        return Matrix([list(i) for i in zip(*self.matrix)])


    def tolist(self):
        """Convert Matrix Object to a Nested List"""
        return self.matrix
    # Object Manpulation: END

    # Booleon Expressions: START
    def is_square(self):
        """True if the matrix is square else False"""
        return bool(self.rowsnum == self.colsnum)


    def is_symmetric(self):
        """True if the matrix is symmetric else False"""
        if self.matrix == (Matrix(self.matrix).transpose()).tolist():
            return True
        return False
    # Booleon Expressions: END

    # Pre Made Objects: START
    @staticmethod
    def identity(size: int):
        """Return a New Identity Matrix (I)
        Alternative to `Matrix(INT)`

        I Matrix is always square that's why
        there's one arg
        """
        result = list()

        for i in range(size):
            result.append([0] * size)
            result[i][i] = 1

        return Matrix(result)


    @staticmethod
    def zero(size: int):
        """Return a New Zero Matrix (All it's items = 0)"""
        return Matrix([[0] * size] * size)


    @staticmethod
    def diagonal(*numbers: int):
        """"Return a New diagonal Matrix OR get the
        diagonal of YOUR MatrixObject.
        MatrixObject = '1 2; 3 4'

        [New] Matrix.diagonal(1, 2, 3) -> '1 0 0; 0 2 0; 0 0 3'
        [Get] Matrix.diagonal(MatrixObject) -> '1 4'
        """
        result = list()

        if isinstance(numbers[0], Matrix):
            result = numbers[0]
            return Matrix([[result[i, i] for i in range(result.rowsnum)]])

        for i, number in enumerate(numbers):
            result.append([0] * len(numbers))
            result[i][i] = number

        return Matrix(result)


    @staticmethod
    def randint(size: tuple, a: int, b: int):
        """Return random matrix in range [a, b]
        Using randint from random module to generate
        a MatrixObject (size) with random numbers
        in range [a, b]

        print(Matrix.randint((3,3), 1, 100))
        Output: 1  25 58
                59 18 48
                15 6  70
                  (3x3)
        """
        result  = list()
        rowsnum = size[0]
        colsnum = size[1]

        for row in range(rowsnum):
            result.append([])
            for _ in range(colsnum):
                result[row].append(_random.randint(a, b))

        return Matrix(result)
    # Pre Made Objects: END


def _cli():
    """The Command-Line Interface (CLI) for the module"""

    parser=_argparse.ArgumentParser(
        prog="matrix-py",
        description = 'matrix-py module to add, substract, multiply'
        'matrices.',
        epilog = 'Usage: .. -ma "[[1, 2, 3], [4, 5, 6]]" -op "+" -mb'
        ' "[[7, 8, 9], [10, 11, 12]]"')

    parser.add_argument('-v', '--version',
        action="version",
        version=__version__,
    )

    parser.add_argument('-s', '--size',
        type=_json.loads,
        metavar='',
        help='Size of MatA'
    )

    parser.add_argument('-t', '--transpose',
        type=_json.loads,
        metavar='',
        help='Transpose of MatA (-t "[[1, 2, 3], [4, 5, 6]]")'
    )

    parser.add_argument('-ma', '--matrixa',
        type=_json.loads,
        metavar='',
        help='MatA (.. -ma "[[1, 2, 3], [4, 5, 6]]")'
    )

    parser.add_argument('-op', '--operator',
        type=str,
        metavar='',
        help='Operator (.. -op "+", "-", "*")'
    )

    parser.add_argument('-mb', '--matrixb',
        type=_json.loads,
        metavar='',
        help='MatB (.. -mb "[[1, 2, 3], [4, 5, 6]]")'
    )

    parser.add_argument('-I', '--identity',
        type=int,
        metavar='',
        help='Identity (.. -I 3)'
    )

    parser.add_argument('-i', '--int',
        type=int,
        metavar='',
        help='Integer (.. -i 5)'
    )

    parser.add_argument('-diag', '--diagonal',
        type=_json.loads,
        metavar='',
        help='Diagonal (.. -diag [1, 2, 3, 4])'
    )

    args = parser.parse_args()

    if args.size:
        print(Matrix(args.size))

    elif args.transpose:
        print(Matrix(args.transpose).transpose())

    elif args.matrixa:
        if args.matrixb:
            b = Matrix(args.matrixb)
        elif args.int:
            b = args.int
        elif args.identity:
            b = Matrix.identity(args.identity)
        elif args.diagonal:
            b = Matrix.diagonal(args.diagonal)

        if args.operator == '+':
            print(Matrix(args.matrixa) + b)
        elif args.operator == '-':
            print(Matrix(args.matrixa) - b)
        elif args.operator == '*':
            print(Matrix(args.matrixa) * b)
        else:
            raise SyntaxError('The avillable operations are +, -, *')
    else:
        print(parser.print_help())


if __name__ == '__main__':
    _cli()
