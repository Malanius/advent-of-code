use simplelog::debug;

const INITIAL_STARTING_POSITION: isize = 50;
const DIAL_SIZE: isize = 100;

#[must_use]
pub fn parse_input(puzzle_input: &str) -> Vec<isize> {
    puzzle_input
        .lines()
        .map(|line| {
            line.replace('L', "-")
                .replace('R', "")
                .trim()
                .parse::<isize>()
                .unwrap()
        })
        .collect()
}

#[must_use]
pub fn wrap_position(pos: isize) -> isize {
    pos.rem_euclid(DIAL_SIZE)
}

#[must_use]
pub fn part1(data: &Vec<isize>) -> usize {
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

#[must_use]
pub fn passes_zero(start: isize, step: isize) -> isize {
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

#[must_use]
pub fn part2(data: &Vec<isize>) -> isize {
    let mut starting_position = INITIAL_STARTING_POSITION;
    let mut zeroes_visited: isize = 0;

    for step in data {
        let position_after = wrap_position(starting_position + step);
        let raw = starting_position + step;

        debug!(
            "Start: {starting_position:>4}, Step: {step:>4}, After: {position_after:>4}, Raw: {raw:>4}"
        );
        zeroes_visited += passes_zero(starting_position, *step);

        starting_position = position_after;
    }

    debug!("Zeroes visited: {zeroes_visited}");
    zeroes_visited
}
