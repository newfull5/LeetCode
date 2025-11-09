impl Solution {
    pub fn is_palindrome(x: i32) -> bool {
        let arr1: Vec<char> = x.to_string().chars().collect();
        let arr2: Vec<char> = x.to_string().chars().rev().collect();

        return arr1 == arr2;
    }
}
