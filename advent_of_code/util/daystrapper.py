import argparse
import datetime
import pathlib

from aocd import get_data

SCRIPT_DIR = pathlib.Path(__file__).parent
SOLUTION_DIR = SCRIPT_DIR.parent
TEMPATE_DIR = SOLUTION_DIR.joinpath("templates")
SOLVER_TEMPLATE = "solver.py"
ARGS_TEMPLATE = "arguments.py"
TEST_TEMPLATE = "test_solver.py"
EXAMPLE_FILE = "example.txt"
DATA_FILE = "data.txt"
SOLVER_PLACEHOLDER = "{{SOLVER}}"
DAY_PLACEHOLDER = "{{DAY}}"
YEAR_PLACEHOLDER = "{{YEAR}}"


def create_year_folder(year: str) -> pathlib.Path:
    """Creates a folder for the year if not already created"""
    year_dir = SOLUTION_DIR.joinpath(f"y{year}")
    year_dir.mkdir(exist_ok=True)
    return year_dir


def create_day_folder(year_dir: pathlib.Path, day: str) -> pathlib.Path:
    """Creates a folder for the day's code"""
    day_dir = SOLUTION_DIR.joinpath(year_dir, f"day_{day}")
    try:
        day_dir.mkdir(exist_ok=False)
    except FileExistsError:
        print(f"Day {day} folder already exist, refusing to overwrite!")
        exit(1)
    return day_dir


def copy_templates(year: str, day: str, day_dir: pathlib.Path) -> None:
    """Copies the template files into the day's folder"""
    solver_template = TEMPATE_DIR.joinpath(SOLVER_TEMPLATE)
    test_template = TEMPATE_DIR.joinpath(TEST_TEMPLATE)
    args_template = TEMPATE_DIR.joinpath(ARGS_TEMPLATE)
    day_name = f"aoc_{year}_{day}"
    day_short = f"day_{day}"
    solver_file = day_dir.joinpath(f"{day_name}.py")
    test_file = day_dir.joinpath(f"test_{day_name}.py")
    args_file = day_dir.joinpath("arguments.py")
    init_file = day_dir.joinpath("__init__.py")
    init_file.touch()
    args_file.write_text(args_template.read_text())
    solver_file.write_text(
        solver_template.read_text()
        .replace(DAY_PLACEHOLDER, day_short)
        .replace(YEAR_PLACEHOLDER, year)
    )
    test_file.write_text(
        test_template.read_text()
        .replace(DAY_PLACEHOLDER, day_short)
        .replace(YEAR_PLACEHOLDER, year)
        .replace(SOLVER_PLACEHOLDER, day_name)
    )


def create_example_file(day_dir: pathlib.Path) -> None:
    """Creates an example file for the day"""
    example_file = day_dir.joinpath(EXAMPLE_FILE)
    example_file.touch()


def get_day_data(year: str, day: str, day_dir: pathlib.Path) -> None:
    """Gets the puzzle data for the day"""
    data = get_data(year=int(year), day=int(day))
    data_file = day_dir.joinpath(DATA_FILE)
    data_file.write_text(data)


def init_args() -> argparse.Namespace:
    """Initializes the command line arguments"""
    today = datetime.date.today()
    year = today.strftime("%Y")
    day = today.strftime("%d")
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-y", "--year", help="The year of the puzzle", required=False, default=year
    )
    parser.add_argument(
        "-d", "--day", help="The day of the puzzle", required=False, default=day
    )
    return parser.parse_args()


def main():
    args = init_args()
    year_dir = create_year_folder(args.year)
    day_dir = create_day_folder(year_dir, args.day)
    copy_templates(args.year, args.day, day_dir)
    create_example_file(day_dir)
    get_day_data(args.year, args.day, day_dir)


if __name__ == "__main__":
    main()
