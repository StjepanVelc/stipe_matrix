from core.matrix import Matrix
import time


def section(title):
    print("\n" + "=" * 50)
    print(title)
    print("=" * 50)


def main():
    section("MATRIX ENGINE — DEMO")

    time.sleep(0.3)

    A = Matrix([[1, 2], [3, 4]])
    B = Matrix([[5, 6], [7, 8]])

    section("Matrix A")
    print(A)

    time.sleep(0.3)

    section("Matrix B")
    print(B)

    time.sleep(0.3)

    section("Matrix Multiplication: A × B")
    C = A * B
    print(C)

    time.sleep(0.3)

    section("Matrix Properties")
    print(f"det(A)  = {A.det()}")
    print(f"rank(A) = {A.rank()}")

    print("\nDemo finished successfully.")


if __name__ == "__main__":
    main()
    input("\nPritisni Enter za izlaz...")
