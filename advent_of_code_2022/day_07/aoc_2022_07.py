import pathlib
from collections import deque
from dataclasses import dataclass, field

from advent_of_code_2022.util.perf import perf

PUZZLE_DIR = pathlib.Path(__file__).parent


@dataclass
class File:
    name: str
    size: int


@dataclass
class Directory:
    name: str
    parent: "Directory | None" = None
    subdirs: dict[str, "Directory"] = field(default_factory=dict)
    files: list[File] = field(default_factory=list)

    @property
    def size(self):
        file_sizes = sum(file.size for file in self.files)
        subdir_sizes = sum(subdir.size for subdir in self.subdirs.values())
        return file_sizes + subdir_sizes


@dataclass
class FileSystem:
    root: Directory

    def __post_init__(self):
        self.pwd = self.root

    def cd(self, name: str) -> None:
        if name == ".." and self.pwd.parent is not None:
            self.pwd = self.pwd.parent
        elif name == "/":
            self.pwd = self.root
        else:
            self.pwd = self.pwd.subdirs[name]

    def mkdir(self, name: str) -> None:
        if name not in self.pwd.subdirs:
            self.pwd.subdirs[name] = Directory(name, self.pwd)

    def addfile(self, name: str, size: int) -> None:
        self.pwd.files.append(File(name, size))


@dataclass
class Device:
    terminal_history: deque[str]
    filesystem: FileSystem = field(default_factory=lambda: FileSystem(Directory("/")))

    def process_history(self) -> None:
        while self.terminal_history:
            line = self.terminal_history.popleft()
            if line.startswith("$"):
                self._proccess_command(line[2:])

    def _proccess_command(self, command: str) -> None:
        command, *args = command.split()
        match command:
            case "cd":
                self.filesystem.cd(args[0])
            case "ls":
                self._proccess_ls()

    def _proccess_ls(self) -> None:
        while self.terminal_history and not self.terminal_history[0].startswith("$"):
            line = self.terminal_history.popleft()
            if line.startswith("dir"):
                _, dir = line.split()
                self.filesystem.mkdir(dir)
            else:
                size, file_name = line.split()
                self.filesystem.addfile(file_name, int(size))


def parse(puzzle_input: str) -> FileSystem:
    """Parse input"""
    terminal_history = deque(puzzle_input.splitlines())
    device = Device(terminal_history)
    device.process_history()
    return device.filesystem


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
