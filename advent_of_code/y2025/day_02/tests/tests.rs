use aoc_2025_day_02::{parse_input, part1, part2};

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

// #[test]
// fn test_part1_example() {
//     panic!("not implemented");
// }

// #[test]
// fn test_part1_data() {
//     panic!("not implemented");
// }

// #[test]
// fn test_part2_example() {
//     panic!("not implemented");
// }

// #[test]
// fn test_part2_data() {
//     panic!("not implemented");
// }
