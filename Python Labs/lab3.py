import argparse

# Cubes lab
# Enter a number n, and it will sum up all the cubes 
# from 1 to that n that have an even first digit
def main(n):
  total = 0
  for i in range(1, n+1):
    cube = i**3
    first_digit = cube
    # Trick to isolate the first digit
    while (first_digit >= 10):  
      first_digit = first_digit // 10
    
    if (first_digit % 2 == 0):  # If even
      total += cube

  return total

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, help="Provide an integer", required=True)
    args = parser.parse_args()

    total = main(args.n)

    print(f'cube({args.n}) = {total}')

