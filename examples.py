from priv_matr import Matrix
import utils


print("====================================")
print("  BASIC MATRIX CREATION")
print("====================================")

A = Matrix([[1, 2], [3, 4]])
B = Matrix([[5, 6], [7, 8]])

print("\nMatrix A:")
print(A)
print("\nMatrix B:")
print(B)


print("\n====================================")
print("  ADDITION, SUBTRACTION, MULTIPLICATION")
print("====================================")

print("\nA + B:")
print(A + B)

print("\nA - B:")
print(A - B)

print("\nA * B:")
print(A * B)

print("\nA * 3 (scalar multiply):")
print(A * 3)


print("\n====================================")
print("  TRANSPOSE")
print("====================================")

print("\nA^T:")
print(A.transpose())


print("\n====================================")
print("  DETERMINANT & INVERSE")
print("====================================")

print("\nDet(A):", A.det())

print("\nInverse of A:")
print(A.inverse())


print("\n====================================")
print("  RANDOM MATRICES")
print("====================================")

R = utils.random_matrix(3, 3, 0, 9)
print("\nRandom integer matrix R:")
print(R)

Rf = utils.random_float_matrix(3, 3)
print("\nRandom float matrix (0-1):")
print(Rf)

v = utils.random_vector(4)
print("\nRandom vector:")
print(v)


print("\n====================================")
print("  SPECIAL MATRICES")
print("====================================")

D = utils.diagonal_matrix([2, 5, 7])
print("\nDiagonal matrix:")
print(D)

S = utils.scalar_matrix(3, 4)
print("\nScalar (4I) matrix:")
print(S)


print("\n====================================")
print("  CHECKS")
print("====================================")

print("\nIs A square?", utils.is_square(A))
print("Is zero matrix?", utils.is_zero_matrix(Matrix.zeros(2, 2)))
print("Is identity?", utils.is_identity(Matrix.identity(3)))


print("\n====================================")
print("  FILE SAVE/LOAD")
print("====================================")

utils.save_to_file(A, "A_matrix.txt")
print("\nMatrix A saved to A_matrix.txt")

A_loaded = utils.load_from_file("A_matrix.txt")
print("\nLoaded matrix A:")
print(A_loaded)


print("\n====================================")
print("  CONVERSIONS")
print("====================================")

lst = [[9, 8], [7, 6]]
print("\nList → Matrix:")
print(utils.list_to_matrix(lst))

print("\nVector → List:")
vec = Matrix([[1], [2], [3]])
print(utils.vector_to_list(vec))


print("\n====================================")
print("  CONCAT (HSTACK & VSTACK)")
print("====================================")

A2 = Matrix([[1, 1], [1, 1]])
print("\nHorizontal stack (A | A2):")
print(utils.hstack(A, A2))

print("\nVertical stack:")
print(utils.vstack(A, A2))


print("\n====================================")
print("  GAUSS-JORDAN & SOLVE AX = b")
print("====================================")

C = Matrix([[2, 1], [5, 3]])
b = Matrix([[1], [2]])

print("\nMatrix C:")
print(C)

print("\nb vector:")
print(b)

print("\nGauss-Jordan form of C:")
print(C.gauss_jordan())

print("\nSolution to Cx = b:")
print(C.solve(b))


print("\n====================================")
print("  RANK & TRACE")
print("====================================")

print("\nRank of A:", A.rank())
print("Trace of A:", A.trace())


print("\n====================================")
print("  SYMMETRY & ORTHOGONALITY")
print("====================================")

Sym = Matrix([[1, 2], [2, 1]])
print("\nSymmetric matrix:")
print(Sym)
print("Is symmetric?", Sym.is_symmetric())

Q = Matrix([[0, 1], [-1, 0]])
print("\nOrthogonal test matrix:")
print(Q)
print("Is orthogonal?", Q.is_orthogonal())