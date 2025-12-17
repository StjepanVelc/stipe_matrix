from core.matrix import Matrix


def main():
    print("=== Matrix Engine ===")

    A = Matrix([[1, 2], [3, 4]])
    B = Matrix([[5, 6], [7, 8]])

    print("\nA:")
    print(A)

    print("\nB:")
    print(B)

    print("\nA * B:")
    print(A * B)

    print("\ndet(A):", A.det())
    print("rank(A):", A.rank())


if __name__ == "__main__":
    main()
    input("\nPritisni Enter za izlaz...")
