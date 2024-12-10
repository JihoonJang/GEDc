import subprocess
import argparse


def run_gedc(query_file_path, data_file_path):
    """
    Runs the GEDc command with the specified query and data files.
    """
    try:
        # Construct the command
        command = ["./bin/GEDc", "-q", query_file_path, "-d", data_file_path]

        # Use Popen to capture real-time output
        process = subprocess.Popen(
            command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )

        # Stream output line by line
        for line in iter(process.stdout.readline, ""):
            print(line.strip())  # Print each line as it is received

        # Wait for the process to complete
        process.stdout.close()
        process.wait()

        # Handle errors
        if process.returncode != 0:
            print("Error occurred while executing the command.")
            for line in iter(process.stderr.readline, ""):
                print(line.strip())
            process.stderr.close()

    except FileNotFoundError:
        print(
            "The command './bin/GEDc' was not found. Ensure the binary exists and is executable."
        )
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # Argument parsing
    parser = argparse.ArgumentParser(
        description="Run GEDc with specified query and data files."
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

    # Execute the GEDc command
    run_gedc(args.query_file_path, args.data_file_path)
