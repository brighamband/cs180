import argparse

def calc_mean(array):
  total = 0
  for num in array:
    total += num
  return total / len(array)

def calc_variance(array, mean):
  square_diff = 0
  for i in range(len(array)):
    square_diff += (array[i] - mean) * (array[i] - mean)
  return square_diff / len(array);

# Mean and variance lab
# Given an array as input, output its mean and variance
def main(array):
  mean = calc_mean(array)
  variance = calc_variance(array, mean)
  print(f'mean = {mean}')
  print(f'variance = {variance}')

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--array", nargs="+", type=int, help="An array of which you want to know the mean and variance")
    args = parser.parse_args()

    if (args.array is None):
      print("Make sure to pass in an array")
      quit()

    main(args.array)

