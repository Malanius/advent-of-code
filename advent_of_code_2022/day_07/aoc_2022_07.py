from dataclasses import dataclass
import pathlib

from advent_of_code_2022.util.perf import perf

PUZZLE_DIR = pathlib.Path(__file__).parent


@dataclass
class File:
    name: str
    size: int

    def __str__(self) -> str:
        return f"- {self.name} (file, size={self.size})"


@dataclass
class Directory:
    name: str
    parent: "Directory" | None = None
    subdirs: dict[str, "Directory"] = dict()
    files: list[File] = list()

    def __str__(self) -> str:
        repr = f"- {self.name} (dir)"
        for subdir in self.subdirs:
            repr += f"\t{subdir}"
        for file in self.files:
            repr += f"\t{file}"
        return repr


@dataclass
class FileSystem:
    root: Directory

    def __post_init__(self):
        self.pwd = self.root

    def __str__(self) -> str:
        return str(self.root)

    def cd(self, name: str) -> None:
        if name == ".." and self.pwd.parent is not None:
            self.pwd = self.pwd.parent
        else:
            self.pwd = self.pwd.subdirs[name]

    def mkdir(self, name: str) -> None:
        if name not in self.pwd.subdirs:
            self.pwd.subdirs[name] = Directory(name, self.pwd)

    def addfile(self, name: str, size: int) -> None:
        self.pwd.files.append(File(name, size))


def parse(puzzle_input):
    """Parse input"""


@perf
def part1(data):
    """Solve part 1"""


@perf
def part2(data):
    """Solve part 2"""


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2


if __name__ == "__main__":
    puzzle_input = (PUZZLE_DIR / "data.txt").read_text().strip()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
