impl Solution {
    pub fn remove_duplicates(nums: &mut Vec<i32>) -> i32 {
        let n = nums.len();
        if n == 0 {
            return 0;
        }

        let mut write = 1usize;
        for read in 1..n {
            if nums[read] != nums[write - 1] {
                nums[write] = nums[read];
                write += 1;
            }
        }
        return write as i32;
    }
}
