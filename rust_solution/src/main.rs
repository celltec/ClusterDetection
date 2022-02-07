use rand::thread_rng;
use rand::seq::SliceRandom;
use clap::{App, Arg};

mod lib;

const SIZE: usize = 10;

fn main() {
    let args = App::new("ClusterDetection")
                    .about("Find the largest square cluster in a matrix")
                    .arg(Arg::new("bench"))
                    .get_matches();

    if args.is_present("bench") {
        bench!(make_matrix);
        std::process::exit(0);
    }

    run();
}

fn run() {
    let matrix = make_matrix();
    get_clusters(matrix);

}

fn make_matrix() -> [char; SIZE*SIZE] {
    let mut rng = thread_rng();
    [' '; SIZE*SIZE].map(|_| *['X', 'O'].choose(&mut rng).unwrap())
}

fn get_clusters(matrix: [char; SIZE*SIZE]) {
    println!("{:?}", matrix);
}