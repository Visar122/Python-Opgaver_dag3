#!/usr/bin/env python3

def file_extensions(filename):
    no_extension = []
    extension_dict = {}

    with open(filename, 'r') as file:
        for line in file:
            filename = line.strip()
            if '.' not in filename:
                no_extension.append(filename)
                continue

            parts = filename.split('.')
            extension = parts[-1]
            if extension not in extension_dict:
                extension_dict[extension] = []
            extension_dict[extension].append(filename)

    return no_extension, extension_dict

def main():
    no_extension, extension_dict = file_extensions("src/filenames.txt")

    print(f"{len(no_extension)} files with no extension")
    for ext in sorted(extension_dict):
        print(f"{ext} {len(extension_dict[ext])}")

if __name__ == "__main__":
    main()
