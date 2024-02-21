import re

def integers_in_brackets(s):
    # Use regular expression to find integers enclosed in brackets
    pattern = r'\[\s*([-+]?\d+)\s*\]'
    matches = re.findall(pattern, s)
    
    # Convert matches to integers
    integers = [int(match) for match in matches]
    
    return integers

def main():
    s = " afd [asd] [12 ] [a34] [ -43 ]tt [+12]xxx"
    
    # Call the integers_in_brackets function and print the result
    print(integers_in_brackets(s))

if __name__ == "__main__":
    main()
