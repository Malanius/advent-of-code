import argparse
import datetime
import pathlib

from aocd import get_data

SCRIPT_DIR = pathlib.Path(__file__).parent
SOLUTION_DIR = SCRIPT_DIR.parent
TEMPLATE_DIR = pathlib.Path("_templates")
SOLVER_TEMPLATE = "solver.py"
ARGS_TEMPLATE = "arguments.py"
TEST_TEMPLATE = "test_solver.py"
EXAMPLE_FILE = "example.txt"
DATA_FILE = "data.txt"
SOLVER_PLACEHOLDER = "{{SOLVER}}"
DAY_PLACEHOLDER = "{{DAY}}"
YEAR_PLACEHOLDER = "{{YEAR}}"


RUST_TEMPLATE_FILES = [
    "Cargo.toml",
    "src/main.rs",
    "src/lib.rs",
    "tests/tests.rs",
]


def create_year_folder(year: str) -> pathlib.Path:
    """Creates a folder for the year if not already created"""
    year_dir = SOLUTION_DIR.joinpath(f"y{year}")
    year_dir.mkdir(exist_ok=True)
    return year_dir


def create_day_folder(year_dir: pathlib.Path, day: str) -> pathlib.Path:
    """Creates a folder for the day's code"""
    day_dir = SOLUTION_DIR.joinpath(year_dir, f"day_{day}")
    day_dir.mkdir(exist_ok=True)
    return day_dir


def copy_templates_python(year: str, day: str, day_dir: pathlib.Path) -> None:
    """Copies the template files into the day's folder"""
    solver_template = TEMPLATE_DIR.joinpath("python", SOLVER_TEMPLATE)
    test_template = TEMPLATE_DIR.joinpath("python", TEST_TEMPLATE)
    args_template = TEMPLATE_DIR.joinpath("python", ARGS_TEMPLATE)
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


def copy_templates_rust(year: str, day: str, day_dir: pathlib.Path) -> None:
    """Copies the Rust template files into the day's folder"""
    template_lang_dir = pathlib.Path(TEMPLATE_DIR).joinpath("rust")
    for template_file in RUST_TEMPLATE_FILES:
        template_path = template_lang_dir.joinpath(template_file)
        dest_path = day_dir.joinpath(template_file)
        if dest_path.exists():
            raise FileExistsError(
                f"File {dest_path} already exists. Refusing to overwrite!"
            )
        dest_path.parent.mkdir(parents=True, exist_ok=True)
        content = template_path.read_text()
        content = content.replace(DAY_PLACEHOLDER, day).replace(YEAR_PLACEHOLDER, year)
        dest_path.write_text(content)

    with open(pathlib.Path("Cargo.toml"), "r+") as cargo_file:
        # FIXME: probably dumb way of doing this, but works for now
        cargo_content = cargo_file.read()
        cargo_content = cargo_content.replace(
            '    # "advent_of_code/y{YEAR}/day_{DAY}",',
            f'    "advent_of_code/y{year}/day_{day}",\n    # "advent_of_code/y{{YEAR}}/day_{{DAY}}",',
        )
        cargo_file.truncate(0)
        cargo_file.seek(0)
        cargo_file.write(cargo_content)


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
        "-l",
        "--lang",
        help="The programming language",
        required=True,
        choices=["python", "rust"],
    )
    parser.add_argument(
        "-y", "--year", help="The year of the puzzle", required=False, default=year
    )
    parser.add_argument(
        "-d", "--day", help="The day of the puzzle", required=False, default=day
    )
    return parser.parse_args()


def main():
    args = init_args()
    lang = args.lang.lower()
    year = args.year
    day = args.day.zfill(2)
    print(f"Setting up Advent of Code {year} Day {day} in {lang}...")
    year_dir = create_year_folder(year)
    day_dir = create_day_folder(year_dir, day)
    if lang == "rust":
        copy_templates_rust(year, day, day_dir)
    if lang == "python":
        copy_templates_python(year, day, day_dir)
    create_example_file(day_dir)
    get_day_data(year, day, day_dir)


if __name__ == "__main__":
    main()
