use pyo3::prelude::*;
mod stopwords;
use stopwords::STOPWORDS;

/// Formats the sum of two numbers as string.
#[pyfunction]
fn sum_as_string(a: usize, b: usize) -> PyResult<String> {
    Ok((a + b).to_string())
}

#[pyfunction]
fn find(hypo: String, kw: String) -> PyResult<bool> {
    Ok(hypo.contains(&kw))
}

#[pyfunction]
fn filter_stopwords(words: Vec<String>) -> PyResult<Vec<String>> {
    let filterd_words = words.into_iter()
        .filter(|w|
            !STOPWORDS.contains(&w.as_str()))
        .collect();
    Ok(filterd_words)
}

/// A Python module implemented in Rust.
#[pymodule]
fn _rougek(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(sum_as_string, m)?)?;
    m.add_function(wrap_pyfunction!(find, m)?)?;
    m.add_function(wrap_pyfunction!(filter_stopwords, m)?)?;
    Ok(())
}
