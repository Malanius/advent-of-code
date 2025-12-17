use aoc_2025_day_02::{parse_input, part1, part2};
use clap::Parser;
use simplelog::{ColorChoice, Config, LevelFilter, TermLogger, TerminalMode};

static EXAMPLE_INPUT: &str = include_str!("../example.txt");
static DATA_INPUT: &str = include_str!("../data.txt");

#[derive(Parser, Debug)]
struct Args {
    #[clap(long, short, action)]
    data: bool,

    #[clap(long, short, action)]
    verbose: bool,
}

fn solve(puzzle_input: &str) -> (isize, isize) {
    let data = parse_input(puzzle_input);
    let result1 = part1(&data);
    let result2 = part2(&data);

    (result1, result2)
}

fn main() {
    let args = Args::parse();
    TermLogger::init(
        if args.verbose {
            LevelFilter::Debug
        } else {
            LevelFilter::Info
        },
        Config::default(),
        TerminalMode::Mixed,
        ColorChoice::Auto,
    )
    .unwrap();

    let puzzle_input = if args.data { DATA_INPUT } else { EXAMPLE_INPUT };
    let solutions = solve(puzzle_input);
    println!("Part 1: {}", solutions.0);
    println!("Part 2: {}", solutions.1);
}
