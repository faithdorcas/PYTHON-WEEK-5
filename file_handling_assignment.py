# file_handling_assignment.py

# File Creation
def create_and_write_file(filename):
    with open(filename, 'w') as file:
        file.write("Hello, world!\n")
        file.write("This is the second line.\n")
        file.write("The number is 123.\n")

# File Reading and Display
def read_and_display_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
        print("File Content:")
        print(content)

# File Appending
def append_to_file(filename):
    with open(filename, 'a') as file:
        file.write("This is an appended line.\n")
        file.write("Here is another appended line.\n")
        file.write("Appending one more line.\n")

# Main function to execute the file handling tasks
def main():
    filename = 'my_file.txt'
    
    # Create and write to the file
    create_and_write_file(filename)
    
    # Read and display the file content
    read_and_display_file(filename)
    
    # Append additional lines to the file
    append_to_file(filename)
    
    # Read and display the updated file content
    print("\nUpdated File Content After Appending:")
    read_and_display_file(filename)

if __name__ == "__main__":
    main()