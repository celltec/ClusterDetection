use rand::thread_rng;
use rand::seq::SliceRandom;
use std::time::Instant;

const SIZE: usize = 10;

fn main() {
    let start = Instant::now();
    println!("{:?}", make_matrix());
    let duration = start.elapsed();
    println!("TIME: {:?}", duration);
}

fn make_matrix() -> [char; SIZE*SIZE] {
    let mut rng = thread_rng();
    [' '; SIZE*SIZE].map(|_| *['X', 'O'].choose(&mut rng).unwrap())
}
