#![warn(clippy::all, clippy::pedantic)]

use clap::Parser;

static EXAMPLE_INPUT: &str = include_str!("example.txt");
static DATA_INPUT: &str = include_str!("data.txt");

const INITIAL_STARTING_POSITION: isize = 50;
const DIAL_SIZE: isize = 100;

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

fn wrap_position(pos: isize) -> isize {
    pos.rem_euclid(DIAL_SIZE)
}

fn part1(data: &Vec<isize>) -> usize {
    let mut position = INITIAL_STARTING_POSITION;
    let mut zeroes_encoded: usize = 0;

    for step in data {
        position = wrap_position(position + step);
        if position == 0 {
            zeroes_encoded += 1;
        }
    }

    zeroes_encoded
}

fn passes_zero(start: isize, step: isize) -> isize {
    const N: isize = DIAL_SIZE;

    if step == 0 {
        return 0;
    }

    if step > 0 {
        // Moving right: positions visited are start+1, ..., start+step (mod N)
        // We want k in [1, step] s.t. s + k ≡ 0 (mod N)
        let mut k0 = (-start).rem_euclid(N); // first k >= 0 with s + k ≡ 0 (mod N)

        // If k0 == 0, that would mean we're already at 0 (starting state),
        // so the next time we hit 0 is after a full revolution.
        if k0 == 0 {
            k0 = N;
        }

        if step < k0 {
            0
        } else {
            // first hit at k0, then every N steps
            1 + (step - k0) / N
        }
    } else {
        // step < 0: moving left
        let total = -step; // make it positive

        // Moving left: positions visited are start-1, ..., start+step (mod N)
        // We want t in [1, total] s.t. s - t ≡ 0 (mod N)
        // This is t ≡ s (mod N), first t >= 0 is t0 = s.
        let mut t0 = start.rem_euclid(N);

        // If t0 == 0, that's the starting state; next hit is after a full revolution.
        if t0 == 0 {
            t0 = N;
        }

        if total < t0 {
            0
        } else {
            // first hit at t0, then every N steps
            1 + (total - t0) / N
        }
    }
}

fn part2(data: &Vec<isize>) -> isize {
    let mut starting_position = INITIAL_STARTING_POSITION;
    let mut zeroes_visited: isize = 0;

    for step in data {
        let position_after = wrap_position(starting_position + step);
        let raw = starting_position + step;

        println!(
            "Start: {:>4}, Step: {:>4}, After: {:>4}, Raw: {:>4}",
            starting_position, step, position_after, raw
        );
        zeroes_visited += passes_zero(starting_position, *step);

        starting_position = position_after;
    }

    println!("Zeroes visited: {}", zeroes_visited);
    zeroes_visited
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

#[cfg(test)]
mod tests {

    use super::*;

    #[test]
    fn test_parse_example() {
        let result = parse_input(EXAMPLE_INPUT);
        assert_eq!(result.len(), 10);
        assert_eq!(result, vec![-68, -30, 48, -5, 60, -55, -1, -99, 14, -82]);
    }

    #[test]
    fn test_part1_example() {
        let data = parse_input(EXAMPLE_INPUT);
        let result = part1(&data);
        assert_eq!(result, 3);
    }

    #[test]
    fn test_part1_data() {
        let data = parse_input(DATA_INPUT);
        let result = part1(&data);
        assert_eq!(result, 1141);
    }

    #[test]
    fn test_part2_example() {
        let data = parse_input(EXAMPLE_INPUT);
        let result = part2(&data);
        assert_eq!(result, 6);
    }

    #[test]
    fn test_big_rotation_left() {
        let puzzle_input = "L1000";
        let data = parse_input(&puzzle_input);
        let result = part2(&data);
        assert_eq!(result, 10);
    }

    #[test]
    fn test_big_rotation_right() {
        let puzzle_input = "R1000";
        let data = parse_input(&puzzle_input);
        let result = part2(&data);
        assert_eq!(result, 10);
    }

    #[test]
    fn test_zeroes_counting_one() {
        let inputs = vec![
            ("L50\nR50", 1),
            ("L50\nL50", 1),
            ("R50\nL50", 1),
            ("R50\nR50", 1),
        ];
        for (input, expected) in inputs {
            let data = parse_input(input);
            let result = part2(&data);
            assert_eq!(result, expected);
        }
    }

    #[test]
    fn test_zeroes_counting_two() {
        let inputs = vec![
            ("L150\nL50", 2),
            ("L150\nR50", 2),
            ("R150\nL50", 2),
            ("R150\nR50", 2),
        ];
        for (input, expected) in inputs {
            let data = parse_input(input);
            let result = part2(&data);
            assert_eq!(result, expected);
        }
    }

    #[test]
    fn test_part2_data() {
        let data = parse_input(DATA_INPUT);
        let result = part2(&data);
        assert_eq!(result, 6634);
    }
}
