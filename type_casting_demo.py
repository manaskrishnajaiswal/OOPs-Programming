def main():
    my_int = 9
    my_float = float(my_int)  # Explicit conversion: 9.0
    print(f"my_int: {my_int}")
    print(f"my_float (float conversion): {my_float}")

    # Explicit narrowing equivalent in Python (cast float to int)
    heavy_int = int(9.78)     # Truncates decimal: 9
    print(f"heavy_int (int conversion of 9.78): {heavy_int}")

if __name__ == "__main__":
    main()
