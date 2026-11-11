import argparse

from tabulate import tabulate

parser = argparse.ArgumentParser()
parser.add_argument("--name", default="World")
args = parser.parse_args()

rows = [
    ["Name", args.name],
    ["Course", "Open Source Software"],
    ["Library", "tabulate"],
    ["Version", "0.10.0"],
    ["My goal", "I want to be independent women"],
]
print(tabulate(rows, tablefmt="grid"))