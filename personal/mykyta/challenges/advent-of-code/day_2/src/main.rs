fn main() {
    let passwords: Vec<_> = include_str!("../input.txt")
        .lines()
        .map(|i| {
            let tokens: Vec<_> = i.split(" ").collect();
            let minmax: Vec<_> = tokens[0].split("-").collect();

            let min: usize = minmax[0].parse().unwrap();
            let max: usize = minmax[1].parse().unwrap();
            let character: char = tokens[1].parse().unwrap();
            let passwords = tokens[2];

        })
        .collect();
    println!("Hello, world!");
}

struct PasswordPolicy {
    min: usize,
    max: usize,
    character: char,
}

impl PasswordPolicy {
    fn check_password(&self, password: &str) -> bool {
        let count = password.chars().filter(|c| c == &self.character).count();
        count >= self.min && count <= self.max
    }
}
