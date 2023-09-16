def display_first_n_lines(file_name, n):
 try:
  with open(file_name, 'r') as file:
   for i in range(n):
    line = file.readline()
    if not line:
     break
    print(line.strip())
 except FileNotFoundError:
  print("File not found.")

def find_word_frequency(file_name, target_word):
 try:
  with open(file_name, 'r') as file:
   content = file.read()
   words = content.split()
   word_count = words.count(target_word)
   print(f"The word '{target_word}' occurs {word_count} times in the file.")
 except FileNotFoundError:
  print("File not found.")

file_name = input("Enter the file name: ")
try:
  n = int(input("Enter the number of lines to display: "))
  target_word = input("Enter the word to find frequency: ")
  display_first_n_lines(file_name, n)
  find_word_frequency(file_name, target_word)
except ValueError:
  print("Invalid input. Please enter a valid number.")

