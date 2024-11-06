#!/usr/bin/env python3
import sys
import argparse
import math


def closest_squares(n):
	sqrt_n = int(math.sqrt(n))

	# Check if n itself is a perfect square
	if sqrt_n * sqrt_n == n:
		lower_square = (sqrt_n - 1)**2
		upper_square = (sqrt_n + 1)**2
	else:
		lower_square = sqrt_n**2
		upper_square = (sqrt_n + 1)**2

	return lower_square, upper_square


def main():
	parser = argparse.ArgumentParser(
	 description="Find the closest square numbers to a given input number.")
	parser.add_argument('number',
	                    type=int,
	                    nargs='?',
	                    help="The input number to find closest squares for.")
	parser.add_argument(
	 '--below',
	 action='store_true',
	 help="Output only the closest square below the input number.")
	parser.add_argument(
	 '--above',
	 action='store_true',
	 help="Output only the closest square above the input number.")
	parser.add_argument('--both',
	                    action='store_true',
	                    help="Output both closest squares (default).")

	args = parser.parse_args()

	# Check if a number was provided either as an argument or via stdin
	if args.number is not None:
		n = args.number
	else:
		try:
			n = int(input("Enter a number: "))
		except ValueError:
			print("Please provide a valid integer.")
			sys.exit(1)

	# Get the closest squares
	lower_square, upper_square = closest_squares(n)

	# Determine output based on flags
	if args.below:
		print(lower_square)
	elif args.above:
		print(upper_square)
	else:  # Default or --both
		print(f"{lower_square}, {upper_square}")


if __name__ == "__main__":
	main()
