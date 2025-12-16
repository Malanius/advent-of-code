use std::ops::RangeInclusive;

type PuzzleInput = Vec<RangeInclusive<isize>>;

pub fn parse_input(puzzle_input: &str) -> PuzzleInput {
    let ranges = puzzle_input.split(",");

    let mut result: PuzzleInput = Vec::new();
    for range_input in ranges {
        let (start, end) = range_input.split_once("-").unwrap();
        let start: isize = start.parse().unwrap();
        let end: isize = end.parse().unwrap();
        let range = start..=end;
        result.push(range);
    }
    result
}

pub fn part1(data: &PuzzleInput) -> usize {
    0
}

pub fn part2(data: &PuzzleInput) -> isize {
    0
}
