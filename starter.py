import argparse

def main(n):
  print('hello')

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, help="Print hello world n times")
    args = parser.parse_args()

    main(args.n)

