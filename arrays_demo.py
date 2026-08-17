def main():
    # Python uses lists to store multiple values (equivalent to arrays)
    scores = [90, 80, 70]
    print(f"scores length: {len(scores)}")  # 3
    print(f"scores[0]: {scores[0]}")        # 90

    # Iterating with for loop (similar to for-each)
    print("Iterating with for loop:")
    for score in scores:
        print(score)

    # 2D Array / Nested List
    matrix = [[1, 2], [3, 4]]
    print(f"matrix[0][1]: {matrix[0][1]}")  # 2

if __name__ == "__main__":
    main()
