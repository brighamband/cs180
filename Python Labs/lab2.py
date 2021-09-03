import argparse
import json
import string

def main(input_str):
  input_str = "Data Science is cool. data science is my favorite class"
  input_str = input_str.lower() # Make entire string lowercase

  # Remove punctuation (besides spaces) from string
  translator = str.maketrans('','',string.punctuation)
  input_str = input_str.translate(translator)
  print(input_str)

  words = input_str.split(' ') # Make list of strings separated by space
  print(words)

  # Create & populate dictionary with words and counts
  output_dict = {}

  for i in range(len(words)):
    cur_word = words[0]
    print('cw', cur_word)

    words.pop()

    count = 0

    for w in words:
      if w == cur_word:
        count += 1
    
    output_dict[cur_word] = count    

  # for word in words:
  #   output_dict[word] = input_str.count(word) # Grabs how many times word occurs in input string

  print('output_dict', output_dict)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("string", type=str, help="Provide an input string")
    args = parser.parse_args()

    main(args.string)

