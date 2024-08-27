import subprocess
import argparse


def watch(input_file="global.css", output_file="output.css"):
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


def minify(input_file="global.css", output_file="output.min.css"):
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
    parser.add_argument(
        "command",
        choices=["watch", "minify"],
        help="The command to run: 'watch' or 'minify'.",
    )
    parser.add_argument(
        "-i",
        "--input",
        default="./app/static/css/global.css",
        help="The input CSS file path.",
    )
    parser.add_argument(
        "-o",
        "--output",
        default="./app/static/css/output.min.css",
        help="The output CSS file path.",
    )

    args = parser.parse_args()

    if args.command == "watch":
        watch(args.input, args.output)
    elif args.command == "minify":
        minify(args.input, args.output)


if __name__ == "__main__":
    main()
