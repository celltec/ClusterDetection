#[macro_export]
macro_rules! bench {
    ($func: expr, $param: expr) => {
        let mut times: Vec<std::time::Duration> = vec!();
        for _ in 0..1000 {
            let start = std::time::Instant::now();
            $func($param);
            times.push(start.elapsed());
        }
        println!("{}: {:?}", stringify!($func), times.iter().sum::<std::time::Duration>() / times.len() as u32);
    }
}
