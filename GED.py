import subprocess
import argparse


def run_ged(query_file_path, data_file_path):
    """
    Runs the GED command with the specified query and data files.
    """
    try:
        # Construct the command
        command = ["./bin/GED", "-q", query_file_path, "-d", data_file_path]

        # Run the command
        result = subprocess.run(
            command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )

        # Output results
        if result.returncode == 0:
            print(result.stdout)
        else:
            print("Error occurred while executing the command.")
            print("Error output:")
            print(result.stderr)
    except FileNotFoundError:
        print(
            "The command './bin/GED' was not found. Ensure the binary exists and is executable."
        )
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # Argument parsing
    parser = argparse.ArgumentParser(
        description="Run GED with specified query and data files."
    )
    parser.add_argument("query_file_path", help="Path to the query file.")
    parser.add_argument("data_file_path", help="Path to the data file.")

    args = parser.parse_args()

    if not args.query_file_path:
        print("Query file path not provided.")
        exit(1)
    if not args.data_file_path:
        print("Data file path not provided.")
        exit(1)

    # Execute the GED command
    run_ged(args.query_file_path, args.data_file_path)
