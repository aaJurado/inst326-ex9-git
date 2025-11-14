import argparse
import pandas as pd
import sys

def most_educated(csv_path, state_code):
    df = pd.read_csv(csv_path)
    state_df = df[df["State"] == state_code]
    max_percent = state_df["Percent of adults with a bachelor's degree or higher"].max()
    top_row = state_df[state_df["Percent of adults with a bachelor's degree or higher"] == max_percent]
    county = top_row["Area name"].iloc[0]
    return county, max_percent

def parse_args(args_list):
    parser = argparse.ArgumentParser()
    parser.add_argument("csv_path")
    parser.add_argument("state_code")
    return parser.parse_args(args_list)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    county, percent = most_educated(args.csv_path, args.state_code)
    print(f"{percent}% of adults in {county} have at least a bachelor's degree")
