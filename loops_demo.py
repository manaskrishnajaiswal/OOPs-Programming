def main():
    # For Loop
    print("--- For Loop ---")
    for i in range(5):
        print(i)

    # While Loop
    print("--- While Loop ---")
    i = 0
    while i < 5:
        print(i)
        i += 1

    # Do-While Loop (Simulated using while True and break)
    print("--- Do-While Loop Simulation ---")
    j = 0
    while True:
        print(j)
        j += 1
        if j >= 5:
            break

if __name__ == "__main__":
    main()
