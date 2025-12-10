impl Solution {
    pub fn reculsive(n: i32) -> bool {
        let quotient = n / 3;
        let remainder = n % 3;

        if remainder != 0 {
            return false;
        }

        if quotient == 1 {
            return true;
        }

        Self::reculsive(quotient)
    }

    pub fn is_power_of_three(n: i32) -> bool {
        if n <= 0 {
            return false;
        }
        if n == 1 {
            return true;
        }
        Self::reculsive(n)
    }
}
