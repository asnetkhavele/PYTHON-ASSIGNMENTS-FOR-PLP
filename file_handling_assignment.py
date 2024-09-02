# file_handling_assignment.py

# File Creation
try:
    with open('my_file.txt', 'w') as file:
        file.write("Hello, this is the first line.\n")
        file.write("Here is the second line with some numbers: 12345\n")
        file.write("Finally, the third line is here.\n")

    print("File 'my_file.txt' created and text written successfully.")

    # File Reading and Display
    try:
        with open('my_file.txt', 'r') as file:
            content = file.read()
            print("Content of 'my_file.txt':")
            print(content)

        # File Appending
        try:
            with open('my_file.txt', 'a') as file:
                file.write("Appending this as the fourth line.\n")
                file.write("Here's the fifth line.\n")
                file.write("And the sixth line.\n")

            print("Additional lines appended to 'my_file.txt' successfully.")
        except Exception as e:
            print(f"An error occurred while appending to the file: {e}")

    except FileNotFoundError:
        print("Error: The file 'my_file.txt' was not found.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")

except Exception as e:
    print(f"An error occurred while creating or writing to the file: {e}")
