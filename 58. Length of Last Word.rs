impl Solution {
    pub fn length_of_last_word(s: String) -> i32 {
        let last_word_length = s.trim().split_whitespace().last().unwrap().len();
        return last_word_length as i32;
    }
}
