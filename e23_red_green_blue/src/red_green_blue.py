import re

def red_green_blue(filename="src/rgb.txt"):

    cleaned_lines = []


    with open(filename, "r") as file:
        next(file)

        for line in file:
            match = re.match(r'\s*(\d+)\s+(\d+)\s+(\d+)\s+(.+)$', line.strip())
            if match:
                red = match.group(1)
                green = match.group(2)
                blue = match.group(3)
                colorname = match.group(4)

                cleaned_line = f"{red}\t{green}\t{blue}\t{colorname}"
                cleaned_lines.append(cleaned_line)

    return cleaned_lines

def main():
    result = red_green_blue("src/rgb.txt")
    print(result[0]) 

if __name__ == "__main__":
    main()
