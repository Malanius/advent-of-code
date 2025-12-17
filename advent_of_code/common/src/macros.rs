#[macro_export]
macro_rules! perf {
    ($expr:expr) => {{
        let __start = ::std::time::Instant::now();
        let __result = $expr;
        let __elapsed = __start.elapsed();

        let __ms = __elapsed.as_millis() as f64;
        let __took = if __ms > 60_000.0 {
            format!("{:.4} min", __ms / 60_000.0)
        } else if __ms > 1_000.0 {
            format!("{:.4} s", __ms / 1_000.0)
        } else {
            format!("{:.4} ms", __ms)
        };

        println!("{} took {}", stringify!($expr), __took);
        __result
    }};
}
