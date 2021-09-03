import argparse
import json
import string

def main(input_str):
  # Make entire string lowercase
  input_str = input_str.lower()

  # Remove punctuation (besides spaces) from string
  translator = str.maketrans("","",string.punctuation)
  input_str = input_str.translate(translator)

  # Make list of strings separated by space
  words = input_str.split(" ")

  # Create & populate dictionary with words and counts
  output_dict = {}

  for word in words:
    output_dict[word] = words.count(word)

  with open("word-counts.json", "w") as f:
    f.write(json.dumps(output_dict))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("string", type=str, help="Provide an input string")
    args = parser.parse_args()

    main(args.string)

