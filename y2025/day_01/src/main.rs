#![warn(clippy::all, clippy::pedantic)]

use aoc_2025_day_01::*;
use clap::Parser;

static EXAMPLE_INPUT: &str = include_str!("example.txt");
static DATA_INPUT: &str = include_str!("data.txt");

#[derive(Parser, Debug)]
struct Args {
    #[clap(long, short, action)]
    data: bool,
}

fn solve(puzzle_input: &str) -> (usize, isize) {
    let data = parse_input(puzzle_input);
    let result1 = part1(&data);
    let result2 = part2(&data);

    (result1, result2)
}

fn main() {
    let args = Args::parse();
    let puzzle_input = match args.data {
        true => DATA_INPUT,
        false => EXAMPLE_INPUT,
    };
    let solutions = solve(&puzzle_input);
    println!("Part 1: {}", solutions.0);
    println!("Part 2: {}", solutions.1);
}
