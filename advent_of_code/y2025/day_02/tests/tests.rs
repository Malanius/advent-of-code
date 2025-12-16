use aoc_2025_day_02::{is_repeated_pattern, is_repeated_twice, parse_input, part1, part2};

static EXAMPLE_INPUT: &str = include_str!("../example.txt");
static DATA_INPUT: &str = include_str!("../data.txt");

#[test]
fn test_parse_example() {
    assert_eq!(
        parse_input(EXAMPLE_INPUT),
        vec![
            11..=22,
            95..=115,
            998..=1012,
            1188511880..=1188511890,
            222220..=222224,
            1698522..=1698528,
            446443..=446449,
            38593856..=38593862,
            565653..=565659,
            824824821..=824824827,
            2121212118..=2121212124
        ]
    );
}

#[test]
fn test_is_repeated_twice() {
    // examples that should return true
    assert_eq!(is_repeated_twice(55), true);
    assert_eq!(is_repeated_twice(6464), true);
    assert_eq!(is_repeated_twice(123123), true);
    // should be false
    assert_eq!(is_repeated_twice(7), false);
    assert_eq!(is_repeated_twice(111), false);
    assert_eq!(is_repeated_twice(1234), false);
}

#[test]
fn test_is_repeated_pattern() {
    // examples that should return true
    assert_eq!(
        is_repeated_pattern(12341234),
        true,
        "{} should be repeated pattern",
        12341234
    );
    assert_eq!(
        is_repeated_pattern(123123123),
        true,
        "{} should be repeated pattern",
        123123123
    );
    assert_eq!(
        is_repeated_pattern(1212121212),
        true,
        "{} should be repeated pattern",
        1212121212
    );
    assert_eq!(
        is_repeated_pattern(1111111),
        true,
        "{} should be repeated pattern",
        1111111
    );
    // example data from the puzzle
    assert_eq!(
        is_repeated_pattern(11),
        true,
        "{} should be repeated pattern",
        11
    );
    assert_eq!(
        is_repeated_pattern(22),
        true,
        "{} should be repeated pattern",
        22
    );
    assert_eq!(
        is_repeated_pattern(99),
        true,
        "{} should be repeated pattern",
        99
    );
    assert_eq!(
        is_repeated_pattern(111),
        true,
        "{} should be repeated pattern",
        111
    );
    assert_eq!(
        is_repeated_pattern(999),
        true,
        "{} should be repeated pattern",
        999
    );
    assert_eq!(
        is_repeated_pattern(1010),
        true,
        "{} should be repeated pattern",
        1010
    );
    assert_eq!(
        is_repeated_pattern(1188511885),
        true,
        "{} should be repeated pattern",
        1188511885
    );
    assert_eq!(
        is_repeated_pattern(222222),
        true,
        "{} should be repeated pattern",
        222222
    );
    assert_eq!(
        is_repeated_pattern(446446),
        true,
        "{} should be repeated pattern",
        446446
    );
    assert_eq!(
        is_repeated_pattern(38593859),
        true,
        "{} should be repeated pattern",
        38593859
    );
    assert_eq!(
        is_repeated_pattern(565656),
        true,
        "{} should be repeated pattern",
        565656
    );
    assert_eq!(
        is_repeated_pattern(824824824),
        true,
        "{} should be repeated pattern",
        824824824
    );
    assert_eq!(
        is_repeated_pattern(2121212121),
        true,
        "{} should be repeated pattern",
        2121212121
    );

    // have varying number of digis
    assert_eq!(
        is_repeated_pattern(12312312),
        false,
        "{} should not be repeated pattern",
        12312312
    );
    assert_eq!(
        is_repeated_pattern(1234123),
        false,
        "{} should not be repeated pattern",
        1234123
    );
    assert_eq!(
        is_repeated_pattern(121212121),
        false,
        "{} should not be repeated pattern",
        121212121
    );

    // have each digit exactly once
    assert_eq!(
        is_repeated_pattern(123456),
        false,
        "{} should not be repeated pattern",
        123456
    );
    assert_eq!(
        is_repeated_pattern(1698523),
        false,
        "{} should not be repeated pattern",
        1698523
    );
    // have same amout of digits but do not repeat the same pattern
    assert_eq!(
        is_repeated_pattern(123321),
        false,
        "{} should not be repeated pattern",
        123321
    );
    assert_eq!(
        is_repeated_pattern(12343412),
        false,
        "{} should not be repeated pattern",
        12343412
    );
    assert_eq!(
        is_repeated_pattern(67696976),
        false,
        "{} should not be repeated pattern",
        67696976
    );
    // single digit can't repeat
    assert_eq!(
        is_repeated_pattern(7),
        false,
        "{} should not be repeated pattern",
        7
    );
}

#[test]
fn test_part1_example() {
    let puzzle_input = parse_input(EXAMPLE_INPUT);
    assert_eq!(part1(&puzzle_input), 1227775554);
}

#[test]
fn test_part1_data() {
    let puzzle_input = parse_input(DATA_INPUT);
    assert_eq!(part1(&puzzle_input), 40214376723);
}

#[test]
fn test_part2_example() {
    let puzzle_input = parse_input(EXAMPLE_INPUT);
    assert_eq!(part2(&puzzle_input), 4174379265);
}

#[test]
fn test_part2_data() {
    let puzzle_input = parse_input(DATA_INPUT);
    assert_eq!(part2(&puzzle_input), 50793864718);
}
