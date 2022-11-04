import argparse

parser = argparse.ArgumentParser()
parser.add_argument("param1")
args = parser.parse_args()

print("args:", args)
print(args.param1)
