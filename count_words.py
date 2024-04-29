file_name = input("Enter the name of the text file: ")
n = int(input("Enter the number of most frequent words to display: "))

def word_frequency(file_name, n):
    # Dictionary to store word frequencies
    word_freq = {}

    # Open the file
    try:
        with open(file_name, 'r') as file:
            # Read each line
            for line in file:
                # Split the line into words
                words = line.split()
                # Count the frequency of each word
                for word in words:
                    word = word.lower()  # Convert word to lowercase
                    # Update the frequency count
                    word_freq[word] = word_freq.get(word, 0) + 1
    except FileNotFoundError:
        print("File not found.")
        return

    # Sort words by frequency
    sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)

    # Display the top N most frequent words
    print("Top",n, "Most Frequent Words:")
    for i in range(min(n, len(sorted_words))):
        print(f"{sorted_words[i][0]}: {sorted_words[i][1]}")


word_frequency(file_name, n)

