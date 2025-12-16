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

pub fn is_repeated_pattern(num: isize) -> bool {
    let s = num.to_string();
    let len = s.len();
    (len % 2 == 0) && (s[..len / 2] == s[len / 2..])
}

pub fn part1(data: &PuzzleInput) -> isize {
    let mut result = 0;

    for range in data {
        for num in range.clone() {
            if is_repeated_pattern(num) {
                result += num;
            }
        }
    }
    result
}

pub fn part2(data: &PuzzleInput) -> isize {
    0
}
