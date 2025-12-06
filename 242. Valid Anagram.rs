impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
        let mut s = s.chars().collect::<Vec<char>>();
        let mut t = t.chars().collect::<Vec<char>>();
        s.sort();
        t.sort();
        return s == t;
    }
}
