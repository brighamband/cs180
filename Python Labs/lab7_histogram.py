import argparse

def find_slot(num, bins):
  pass

def main(array, num_bins):
  print('a =', array)
  print('b =', num_bins)
  print()

  highest = max(array)
  lowest = min(array)
  bin_width = (highest - lowest + 1) / num_bins
  bin_width = round(bin_width, 1) # Round to nearest tenths

  bins = [0] * (num_bins)

  print(bins)
  print()

  lower_bound = lowest # Inclusive '['
  upper_bound = lower_bound + bin_width # Exclusive ')'

  for bin in bins:
    print('# [' + str(lower_bound) + ',' + str(upper_bound) + '):', bin)
    lower_bound = upper_bound
    upper_bound = round(upper_bound + bin_width, 1) # Round to nearest tenths

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--array", nargs="+", type=int, help="An array of numbers", required=True)
    parser.add_argument("-b", "--bins", type=int, help="Number of bins", required=True)
    args = parser.parse_args()

    main(args.array, args.bins)

