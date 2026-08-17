def main():
    s1 = "Hello"
    arr = ['W', 'o', 'r', 'l', 'd']
    s2 = "".join(arr)  # Join char array/list to string

    print(s1 + " " + s2)       # Concatenate: Hello World
    print(s1[1])               # Char at index 1: 'e'
    print(len(s1))             # Length: 5
    print(s1[0:2])             # Slicing (substring): "He"
    print(s1 == "Hello")       # Check content equality: True

if __name__ == "__main__":
    main()
