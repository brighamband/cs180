import argparse

def is_palindrome(num):
  fwd_str = str(num)
  rev_str = str(num)[::-1]

  if fwd_str == rev_str:
    return True
  return False

# Palindrome Lab
# See if a number is the same forwards and backwards
def main(input):
  if is_palindrome(input):
    print("true")
  else:
    print("false")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-x", type=int, help="Palindrome test number", required=True)
    args = parser.parse_args()

    main(args.x)