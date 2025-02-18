def count_words(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read() # read all text into a string
            words = text.split() # split on whitespace and newline into a list
            return len(words)
    except FileNotFoundError: # catch error of file not being found
        print(f"Error: The file '{filename}' was not found.")
        return None