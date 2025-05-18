# All inputs must be strings

# Section 1
filename = input("Please enter the input filename: ")
if not filename.endswith('.txt'):
    print("Invalid file format. Please provide a .txt file.")

read_word_from_file = []
file = open(filename, 'r')
for line in file:
    read_word_from_file.append(line.strip())
file.close()

print(f"Words read from {filename}: {read_word_from_file}")

# Section 2
min_length = int(input("Please enter the minimum word length: "))
filter_words_by_length = []

for word in read_word_from_file:
    if len(word) >= min_length:
        filter_words_by_length.append(word)

print(f"Words with length >= {min_length}: {filter_words_by_length}")

# Section 3
output_filename = input("Please enter the new filename: ")
save_words_to_file = open(output_filename, 'w')

for word in filter_words_by_length:
    save_words_to_file.write(word + '\n')

save_words_to_file.close()
