import random
from core.matrix import Matrix


# ---------------------------------------------------------
#  RANDOM GENERATION
# ---------------------------------------------------------

def random_matrix(rows, cols, min_val=0, max_val=10):
    """Generira matricu sa slučajnim brojevima."""
    data = [
        [random.randint(min_val, max_val) for _ in range(cols)]
        for _ in range(rows)
    ]
    return Matrix(data)


def random_float_matrix(rows, cols, min_val=0.0, max_val=1.0):
    """Generira matricu sa slučajnim realnim brojevima."""
    data = [
        [random.uniform(min_val, max_val) for _ in range(cols)]
        for _ in range(rows)
    ]
    return Matrix(data)


def random_vector(n, min_val=0, max_val=10):
    """Generira kolonu-vektor (n x 1) sa slučajnim cijelim brojevima."""
    return Matrix([[random.randint(min_val, max_val)] for _ in range(n)])


# ---------------------------------------------------------
#  SPECIAL MATRICES
# ---------------------------------------------------------

def diagonal_matrix(values):
    """Generira dijagonalnu matricu iz liste vrijednosti."""
    n = len(values)
    data = [[0]*n for _ in range(n)]
    for i in range(n):
        data[i][i] = values[i]
    return Matrix(data)


def scalar_matrix(n, value):
    """Generira skalarnu matricu (value na dijagonali)."""
    return Matrix([[value if i == j else 0 for j in range(n)] for i in range(n)])


# ---------------------------------------------------------
#  VALIDATION HELPERS
# ---------------------------------------------------------

def is_square(A):
    """Provjerava je li matrica kvadratna."""
    return A.rows == A.cols


def is_zero_matrix(A):
    """Provjerava je li matrica potpuno nula."""
    return all(all(val == 0 for val in row) for row in A.data)


def is_identity(A, eps=1e-9):
    """Provjera je li matrica identična."""
    if not is_square(A):
        return False
    I = Matrix.identity(A.rows)
    return A.approx_equal(I, eps)


# ---------------------------------------------------------
#  FILE I/O
# ---------------------------------------------------------

def save_to_file(A, filename="matrix.txt"):
    """Spremi matricu u tekstualni fajl."""
    with open(filename, "w") as f:
        for row in A.data:
            f.write(" ".join(map(str, row)) + "\n")


def load_from_file(filename="matrix.txt"):
    """Učita matricu iz tekstualnog fajla."""
    data = []
    with open(filename, "r") as f:
        for line in f:
            parts = line.strip().split()
            row = [float(x) if "." in x else int(x) for x in parts]
            data.append(row)
    return Matrix(data)


# ---------------------------------------------------------
#  FORMAT CONVERSIONS
# ---------------------------------------------------------

def list_to_matrix(lst):
    """Pretvara listu listi u Matrix objekt."""
    return Matrix(lst)


def vector_to_list(vec):
    """Pretvara kolonu-vektor u običnu Python listu."""
    if vec.cols != 1:
        raise ValueError("vector_to_list radi samo za vektore (n × 1).")
    return [vec.data[i][0] for i in range(vec.rows)]


# ---------------------------------------------------------
#  CONCATENATION
# ---------------------------------------------------------

def hstack(A, B):
    """Spaja dvije matrice horizontalno."""
    if A.rows != B.rows:
        raise ValueError("Za horizontalno spajanje matrice moraju imati isti broj redova.")
    data = [A.data[i] + B.data[i] for i in range(A.rows)]
    return Matrix(data)


def vstack(A, B):
    """Spaja dvije matrice vertikalno."""
    if A.cols != B.cols:
        raise ValueError("Za vertikalno spajanje matrice moraju imati isti broj kolona.")
    return Matrix(A.data + B.data)
