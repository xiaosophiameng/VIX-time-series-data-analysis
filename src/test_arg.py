import argparse

# step 2
parser = argparse.ArgumentParser()

# step 3
parser.add_argument('input_file')
parser.add_argument('statistic')
parser.add_argument('variable')

# step 4
args = parser.parse_args()

# step 5
print(args.input_file)
