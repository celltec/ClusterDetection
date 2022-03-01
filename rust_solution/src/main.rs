use clap::{App, Arg};
mod lib;

struct Matrix {
    size: u32,
    data: String,
}

// struct Square {
//     x: u32,
//     y: u32,
//     size: u32,
// }

// impl Square {
//     // Optional
//     fn new(x: u32, y: u32, size: u32) -> Self {
//         Self { x, y, size }
//     }
// }

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
        bench!(get_clusters, &make_matrix(size));
        std::process::exit(0);
    }

    run(size);
}

fn run(size: u32) {
    println!("Find clusters in a {0}x{0} matrix:", size);
    let matrix = make_matrix(size);
    get_clusters(&matrix);
    print_matrix(&matrix);
}

fn make_matrix(size: u32) -> Matrix {
    Matrix { size, data: random_string::generate((size*size) as usize, "XXO") }
}

fn get_clusters(matrix: &Matrix) {//-> Vec<Square> {
    let mut assumed_size = matrix.size as usize;

    // for (i, c) in matrix.data.chars().enumerate() {
    //     if i as u32 % matrix.size == 0 {
    //         println!();
    //     }
    //     print!("{} ", c);
    // }

    while assumed_size > 1 {

        let pos = matrix.data.find("X".repeat(assumed_size).as_str()).unwrap();
        matrix.data.


        assumed_size -= 1;
    }

    //Vec::new()
}

fn print_matrix(matrix: &Matrix) {
    for (i, c) in matrix.data.chars().enumerate() {
        if i as u32 % matrix.size == 0 {
            println!();
        }
        print!("{} ", c);
    }
    println!();
}
