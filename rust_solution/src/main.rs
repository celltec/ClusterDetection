use clap::{App, Arg};
mod lib;

fn main() {
    let args = App::new("ClusterDetection")
                    .about("Find the largest square cluster in a matrix")
                    .arg(Arg::new("bench").short('b').long("bench"))
                    .arg(Arg::new("size").default_value("10"))
                    .get_matches();

    let size: u32 = std::cmp::max(args.value_of("size").unwrap().parse::<i32>().unwrap_or(10), 0) as u32;

    if args.is_present("bench") {
        println!("Bench a {}x{} matrix", size, size);
        bench!(make_matrix, size);
        bench!(get_clusters, make_matrix(size));
        std::process::exit(0);
    }

    run(size);
}

#[derive(Debug)]
struct Square {
    x: u32,
    y: u32,
    size: u32,
}

impl Square {
    fn new(x: u32, y: u32, size: u32) -> Self {
        Square { x, y, size }
    }

    fn print_info(&self) {
        println!("{} {} {}", self.x, self.y, self.size);
    }
}

fn run(size: u32) {
    println!("Find clusters in a {0}x{0} matrix:", size);
    get_clusters(make_matrix(size));
}

fn make_matrix(size: u32) -> String {
    random_string::generate((size*size) as usize, "XO")
}

fn get_clusters(matrix: String) {
    let m1 = Square::new(1,2,4);
    m1.print_info();
    println!("{:?}", matrix);
}