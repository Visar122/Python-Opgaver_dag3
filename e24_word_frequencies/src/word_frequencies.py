def word_frequencies(filename):
    word_freq = {}
    with open(filename, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                word = word.strip('!"#$%&\'()*,-./:;?@[]_')  # Remove punctuation from the ends of words
                if word in word_freq:
                    word_freq[word] += 1
                else:
                    word_freq[word] = 1
    return word_freq

def main():
    filename = "src/alice.txt"
    frequencies = word_frequencies(filename)
    for word, count in frequencies.items():
        print(f"{word}\t{count}")

if __name__ == "__main__":
    main()
