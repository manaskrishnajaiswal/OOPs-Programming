def main():
    print("Enter age (int) and name (string) on separate lines:")
    try:
        age = int(input())
        name = input()
        print(f"{name} is {age}")
    except ValueError:
        print("Invalid input format.")

if __name__ == "__main__":
    main()
