import os
from pathlib import Path
import subprocess
import argparse


def watch(input_file="global.css", output_file="styles.css"):
    """
    Start a Tailwind CSS watcher that watches for changes in the input file
    and compiles to the output file.

    :param input_file: The input CSS file path
    :param output_file: The output CSS file path
    """
    try:
        subprocess.run(
            ["./tailwindcss", "-i", input_file, "-o", output_file, "--watch"],
            check=True,
        )
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while starting the watcher: {e}")
    except FileNotFoundError:
        print(
            "tailwindcss executable not found. Please ensure it is installed and accessible in the current directory."
        )


def minify(input_file="global.css", output_file="styles.min.css"):
    """
    Compile and minify the CSS file for production.

    :param input_file: The input CSS file path
    :param output_file: The output CSS file path
    """
    try:
        subprocess.run(
            ["./tailwindcss", "-i", input_file, "-o", output_file, "--minify"],
            check=True,
        )
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while minifying the CSS: {e}")
    except FileNotFoundError:
        print(
            "tailwindcss executable not found. Please ensure it is installed and accessible in the current directory."
        )


def main() -> None:
    parser = argparse.ArgumentParser(description="Run Tailwind CSS commands.")

    css_dir = Path(os.getcwd(), "app", "static", "css")
    input_file = Path(css_dir, "global.css")
    output_file = Path(css_dir, "styles.css")
    output_file_min = Path(css_dir, "styles.min.css")

    parser.add_argument(
        "command",
        choices=["watch", "minify"],
        help="The command to run: 'watch' or 'minify'.",
    )

    parser.add_argument(
        "-i",
        "--input",
        default=None,
        help="The input CSS file path.",
    )
    parser.add_argument(
        "-o",
        "--output",
        default=None,
        help="The output CSS file path.",
    )

    args = parser.parse_args()

    if args.command == "watch":
        watch(
            input_file if args.input is None else args.input,
            output_file if args.output is None else args.output,
        )
    elif args.command == "minify":
        minify(
            input_file if args.input is None else args.input,
            output_file_min if args.output is None else args.output,
        )


if __name__ == "__main__":
    main()
