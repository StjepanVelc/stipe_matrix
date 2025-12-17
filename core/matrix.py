class Matrix:
    def __init__(self, data):
        if not data or not isinstance(data, list):
            raise ValueError("Matrix data must be a non-empty list.")

        self.data = data
        self.rows = len(data)
        self.cols = len(data[0])

        for row in data:
            if len(row) != self.cols:
                raise ValueError("All rows in the matrix must have the same length.")

    # ---------- Helpers ----------

    def shape(self):
        return (self.rows, self.cols)

    def copy(self):
        return Matrix([row[:] for row in self.data])

    def __repr__(self):
        col_widths = [max(len(str(self.data[i][j])) for i in range(self.rows)) for j in range(self.cols)]
        lines = []
        for row in self.data:
            line = " ".join(str(val).rjust(col_widths[j]) for j, val in enumerate(row))
            lines.append(line)
        return "\n".join(lines)

    # ---------- Basic operations ----------

    def __add__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError("Can only add Matrix to Matrix.")
        if self.shape() != other.shape():
            raise ValueError("Matrices must have the same dimensions to add.")

        result = [
            [self.data[i][j] + other.data[i][j] for j in range(self.cols)]
            for i in range(self.rows)
        ]
        return Matrix(result)

    def __sub__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError("Can only subtract Matrix from Matrix.")
        if self.shape() != other.shape():
            raise ValueError("Matrices must have the same dimensions to subtract.")

        result = [
            [self.data[i][j] - other.data[i][j] for j in range(self.cols)]
            for i in range(self.rows)
        ]
        return Matrix(result)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Matrix([[val * other for val in row] for row in self.data])

        if isinstance(other, Matrix):
            if self.cols != other.rows:
                raise ValueError("Matrix multiplication requires A.cols == B.rows.")

            result = [
                [
                    sum(self.data[i][k] * other.data[k][j] for k in range(self.cols))
                    for j in range(other.cols)
                ]
                for i in range(self.rows)
            ]
            return Matrix(result)

        raise TypeError("Unsupported operand type for multiplication.")

    __rmul__ = __mul__

    # ---------- Transpose ----------

    def transpose(self):
        result = [
            [self.data[j][i] for j in range(self.rows)]
            for i in range(self.cols)
        ]
        return Matrix(result)

    # ---------- Determinant ----------

    def det(self):
        if self.rows != self.cols:
            raise ValueError("Determinant is defined only for square matrices.")

        if self.rows == 2:
            a, b = self.data[0][0], self.data[0][1]
            c, d = self.data[1][0], self.data[1][1]
            return a * d - b * c

        if self.rows == 3:
            a, b, c = self.data[0]
            d, e, f = self.data[1]
            g, h, i = self.data[2]
            return (
                a*(e*i - f*h)
                - b*(d*i - f*g)
                + c*(d*h - e*g)
            )

        total = 0
        for col in range(self.cols):
            minor = self._minor(0, col)
            sign = (-1) ** col
            total += sign * self.data[0][col] * minor.det()
        return total

    def _minor(self, row_to_remove, col_to_remove):
        data = [
            [
                self.data[r][c]
                for c in range(self.cols)
                if c != col_to_remove
            ]
            for r in range(self.rows)
            if r != row_to_remove
        ]
        return Matrix(data)

    # ---------- Inverse ----------

    def inverse(self):
        if self.rows != self.cols:
            raise ValueError("Inverse is defined only for square matrices.")

        detA = self.det()
        if detA == 0:
            raise ValueError("Matrix is singular (det = 0), no inverse exists.")

        if self.rows == 2:
            a, b = self.data[0][0], self.data[0][1]
            c, d = self.data[1][0], self.data[1][1]
            inv_data = [
                [ d, -b],
                [-c,  a]
            ]
            return (1 / detA) * Matrix(inv_data)

        cofactors = []
        for r in range(self.rows):
            cofactor_row = []
            for c in range(self.cols):
                minor = self._minor(r, c)
                sign = (-1) ** (r + c)
                cofactor_row.append(sign * minor.det())
            cofactors.append(cofactor_row)

        adj = Matrix(cofactors).transpose()
        return (1 / detA) * adj

    # ---------- Gauss-Jordan elimination ----------

    def gauss_jordan(self):
        mat = self.copy().data
        rows, cols = self.rows, self.cols

        r = 0
        for c in range(cols):
            pivot = None
            for i in range(r, rows):
                if mat[i][c] != 0:
                    pivot = i
                    break
            if pivot is None:
                continue

            mat[r], mat[pivot] = mat[pivot], mat[r]

            pivot_val = mat[r][c]
            mat[r] = [val / pivot_val for val in mat[r]]

            for i in range(rows):
                if i != r:
                    factor = mat[i][c]
                    mat[i] = [mat[i][j] - factor * mat[r][j] for j in range(cols)]

            r += 1

        return Matrix(mat)

    # ---------- Solve Ax = b ----------

    def solve(self, b):
        if self.rows != self.cols:
            raise ValueError("Solve requires square matrix A.")

        if not isinstance(b, Matrix) or b.cols != 1:
            raise ValueError("b must be a column vector (n×1 Matrix).")

        augmented = Matrix([self.data[i] + b.data[i] for i in range(self.rows)])
        reduced = augmented.gauss_jordan()

        solution = [reduced.data[i][-1] for i in range(self.rows)]
        return Matrix([[x] for x in solution])

    # ---------- Rank ----------

    def rank(self):
        rref = self.gauss_jordan().data
        rank = 0
        for row in rref:
            if any(abs(val) > 1e-12 for val in row):
                rank += 1
        return rank

    # ---------- Trace ----------

    def trace(self):
        if self.rows != self.cols:
            raise ValueError("Trace undefined for non-square matrices.")
        return sum(self.data[i][i] for i in range(self.rows))

    # ---------- Symmetry ----------

    def is_symmetric(self):
        return self == self.transpose()

    # ---------- Orthogonality ----------

    def is_orthogonal(self):
        if self.rows != self.cols:
            return False
        I = Matrix.identity(self.rows)
        return (self * self.transpose()).approx_equal(I)

    # ---------- Approx equal ----------

    def approx_equal(self, other, eps=1e-9):
        if self.shape() != other.shape():
            return False
        for i in range(self.rows):
            for j in range(self.cols):
                if abs(self.data[i][j] - other.data[i][j]) > eps:
                    return False
        return True

    # ---------- Static matrices ----------

    @staticmethod
    def identity(n):
        return Matrix([[1 if i == j else 0 for j in range(n)] for i in range(n)])

    @staticmethod
    def zeros(n, m):
        return Matrix([[0 for _ in range(m)] for _ in range(n)])