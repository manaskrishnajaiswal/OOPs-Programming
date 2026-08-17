def main():
    # If-Elif-Else
    marks = 85
    print(f"Grade for {marks}: ", end="")
    if marks > 90:
        print("A")
    elif marks > 80:
        print("B")
    else:
        print("C")

    # Match-Case (Python 3.10+, equivalent to Switch)
    day = 2
    print(f"Day {day}: ", end="")
    match day:
        case 1:
            print("Monday")
        case 2:
            print("Tuesday")
        case _:
            print("Invalid")

if __name__ == "__main__":
    main()
