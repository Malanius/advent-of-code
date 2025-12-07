use aoc_2025_day_01::{parse_input, part1, part2};

static EXAMPLE_INPUT: &str = include_str!("../example.txt");
static DATA_INPUT: &str = include_str!("../data.txt");

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
