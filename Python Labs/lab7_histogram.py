import argparse

def print_inputs(array, num_bins):
  print('a =', array)
  print('b =', num_bins)
  print()


def calc_bin_width(highest_num, lowest_num, num_bins):
  width = (highest_num - lowest_num + 1) / num_bins
  width = round(width, 1) # Round to nearest tenths
  return width


def make_bins(array, num_bins, bin_width, lower_bound, upper_bound):
  bins = [0] * (num_bins) # Initialize bins (as many as num_bins)

  for i in range(len(bins)):
      # Populate bins
      for num in array:
        if num >= lower_bound and num < upper_bound: 
          bins[i] += 1

      lower_bound, upper_bound = update_bounds(lower_bound, upper_bound, bin_width)
  
  return bins


''' 
Updates lower and upper bounds for the next bin.
lower_b - Lower bound (inclusive '[').
upper_b - Upper bound (exclusive ')').
'''
def update_bounds(lower_b, upper_b, bin_width):
  lower_b = upper_b
  upper_b = round(upper_b + bin_width, 1) # Round to nearest tenths
  return lower_b, upper_b


def print_bins(bins, bin_width, lower_bound, upper_bound):
  for bin in bins:
    print('# [' + str(lower_bound) + ',' + str(upper_bound) + '):', bin)  
    lower_bound, upper_bound = update_bounds(lower_bound, upper_bound, bin_width)


def main(array, num_bins):
  # print_inputs(array, num_bins)

  # Initialize values
  highest_num = max(array)
  lowest_num = min(array)
  bin_width = calc_bin_width(highest_num, lowest_num, num_bins)
  init_lower_b = lowest_num # Initial lower bound 
  init_upper_b = lowest_num + bin_width # Initial upper bound

  bins = make_bins(array, num_bins, bin_width, init_lower_b, init_upper_b)
 
  # Print entire bins array
  print(bins)
  print()

  # Prints bins individually
  print_bins(bins, bin_width, init_lower_b, init_upper_b)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--array", nargs="+", type=int, help="An array of numbers", required=True)
    parser.add_argument("-b", "--bins", type=int, help="Number of bins", required=True)
    args = parser.parse_args()

    main(args.array, args.bins)

