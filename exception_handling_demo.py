def main():
    try:
        my_numbers = [1, 2, 3]
        print(my_numbers[10])  # IndexError
    except IndexError as e:
        print(f"Something went wrong: {e}")
    finally:
        print("The 'try except' block is finished.")

if __name__ == "__main__":
    main()
