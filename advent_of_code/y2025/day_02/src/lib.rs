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

pub fn is_repeated_twice(num: isize) -> bool {
    let s = num.to_string();
    let len = s.len();
    (len % 2 == 0) && (s[..len / 2] == s[len / 2..])
}

pub fn is_repeated_pattern(num: isize) -> bool {
    let s = num.to_string();

    if is_repeated_twice(num) {
        return true;
    }

    let counts = s
        .chars()
        .fold(std::collections::HashMap::new(), |mut acc, c| {
            *acc.entry(c).or_insert(0) += 1;
            acc
        });

    if counts.len() == 1 {
        // all digits are the same
        return true;
    }

    if counts.len() == s.len() {
        // all digits are unique
        return false;
    }

    let first_counted = counts.values().next().unwrap();
    if !counts.values().all(|&count| count == *first_counted) {
        return false;
    }

    let pattern_length = counts.len();
    let pattern = &s[..pattern_length];
    for i in 0..(s.len() / pattern_length) {
        let start = i * pattern_length;
        let end = start + pattern_length;
        let current = &s[start..end];
        if current != pattern {
            return false;
        }
    }

    true
}

pub fn part1(data: &PuzzleInput) -> isize {
    let mut result = 0;

    for range in data {
        for num in range.clone() {
            if is_repeated_twice(num) {
                result += num;
            }
        }
    }
    result
}

pub fn part2(data: &PuzzleInput) -> isize {
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
