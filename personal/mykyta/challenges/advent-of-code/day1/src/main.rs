fn main() {
    let nums: Vec<i32> = include_str!("../input.txt")
        .lines()
        .map(|n| n.parse().unwrap())
        .collect();

    for i in &nums {
        for j in &nums {
            if i + j == 2020 {
                println!("{}", i * j);
            }
        }
    }
}
