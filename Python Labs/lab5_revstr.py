import argparse

# Word Reverser Lab
# Must reverse all words, but maintain spacing
def main(input):
  print(f'Was:\t\t"{input}"')
  print(f'Reversed:\t"{input[::-1]}"')  # Reverses string

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--string", type=str, help="String you want to reverse", required=True)
    args = parser.parse_args()

    main(args.string)