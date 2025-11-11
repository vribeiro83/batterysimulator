import argparse

from model.analysis import run_analysis

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run solar battery analysis.")
    parser.add_argument("--csv", type=str, required=True, help="Path to the CSV file")
    args = parser.parse_args()

    run_analysis(args.csv)