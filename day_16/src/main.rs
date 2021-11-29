use std::fs;

fn main() {

    let input: String = read_input("input.txt");
    // println!("{}", input);
    
    let mut a: Vec<i32> = Vec::new();
    for c in input.trim().chars() {
        a.push(c as i32 - 0x30);
    }

    let solution = solve(a.clone());
    println!("Part 1: {}", solution);

    let solution2 = solve2(a);
    println!("Part 2: {}", solution2);

}

fn read_input(filename: &str) -> String {
    let result = fs::read_to_string(filename)
        .expect("Something went wrong reading the file");
    result
}

fn solve(mut digits: Vec<i32>) -> String {
    // Find the hundredth phase
    let pattern: [i32; 4] = [0,1,0,-1];
    for _ in 0..100 {
        // println!("{:?}", &digits);
        digits = next_phase(&digits, pattern);
    }

    // Convert answer to a string    
    let mut solution: String = String::new();
    for i in 0..8 { solution.push(char::from_digit(digits[i] as u32, 10).unwrap()) }
    solution
}

fn solve2(mut digits: Vec<i32>) -> String {
    // Find the hundredth phase
    let pattern: [i32; 4] = [0,1,0,-1];
    let mut offset: i32 = 0;
    for i in 0..7 { offset = offset * 10 + digits[i]; }
    let base: Vec<i32> = digits.clone();
    for _ in 0..(10_000 - 1) { digits.extend(base.clone()); }
    for i in 0..100 {
        // println!("{:?}", &digits);
        println!("{}", i);
        digits = next_phase(&digits, pattern);
    }

    // Convert answer to a string    
    let mut solution: String = String::new();
    for i in offset..(offset+8) { solution.push(char::from_digit(digits[i as usize] as u32, 10).unwrap()) }
    solution
}

fn next_phase(digits: &Vec<i32>, pattern: [i32; 4]) -> Vec<i32> {
    let mut i: usize = 0; // For position in digits
    let mut new: Vec<i32> = Vec::new();

    while i < digits.len() {

        let mut j: usize = 1; // For number of repetitions of a pattern
        let mut k: usize = 0; // For position in pattern
        let mut n: i32 = 0;
        for d in digits.iter() {
            if j >= i + 1 { j = 0; k = (k+1)%4; }
            match pattern[k] {
                -1 => n -= *d,
                1  => n += *d,
                _ => (),
            }
            // print!("{}*{} + ", *d, pattern[k % 4]);
            j += 1;
        }
        
        new.push((n % 10).abs());
        // print!("= {}\n", n);
        i += 1;
    }
    
    new
}
