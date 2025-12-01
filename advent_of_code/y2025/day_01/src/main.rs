use clap::Parser;
use std::fs;

static STARTING_POSITION: isize = 50;

#[derive(Parser, Debug)]
struct Args {
    #[clap(long, short, action)]
    data: bool,
}

fn parse_input(puzzle_input: &str) -> Vec<isize> {
    puzzle_input
        .lines()
        .map(|line| {
            line.replace("L", "-")
                .replace("R", "")
                .trim()
                .parse::<isize>()
                .unwrap()
        })
        .collect()
}

fn part1(data: &Vec<isize>) -> usize {
    let mut position = STARTING_POSITION;
    let mut zeroes_seen: usize = 0;

    for step in data {
        position = (100 + (position + step)) % 100;
        if position == 0 {
            zeroes_seen += 1;
        }
    }

    zeroes_seen
}

fn part2(data: &Vec<isize>) -> usize {
    0
}

fn solve(puzzle_input: &str) -> (usize, usize) {
    let data = parse_input(puzzle_input);
    let result1 = part1(&data);
    let result2 = part2(&data);

    (result1, result2)
}

fn main() {
    let args = Args::parse();
    let file = match args.data {
        true => "data.txt",
        false => "example.txt",
    };
    let path = format!("data/{}", file);
    let puzzle_input = fs::read_to_string(&path).expect(&format!("Could not read file: {}", path));
    let solutions = solve(&puzzle_input);
    println!("Part 1: {}", solutions.0);
    println!("Part 2: {}", solutions.1);
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_parse_example() {
        let puzzle_input = fs::read_to_string("data/example.txt").unwrap();
        let result = parse_input(&puzzle_input);
        assert_eq!(result.len(), 10);
        assert_eq!(result, vec![-68, -30, 48, -5, 60, -55, -1, -99, 14, -82]);
    }

    #[test]
    fn test_part1_example() {
        let puzzle_input = fs::read_to_string("data/example.txt").unwrap();
        let data = parse_input(&puzzle_input);
        let result = part1(&data);
        assert_eq!(result, 3);
    }
}
