
impl Solution {
    pub fn longest_common_prefix(strs: Vec<String>) -> String {
        let mut answer: String = String::new();
        let min_length: usize = strs.iter().map(|s: &String| s.len()).min().unwrap_or(0);

        for i in 0..min_length{
            let first_char: Option<char> = strs[0].chars().nth(i);

            for s in &strs{
                if s.chars().nth(i) != first_char{
                    return answer;
                }
            }

            answer.push(first_char.unwrap());
        }
        
        return answer;
    }
}
