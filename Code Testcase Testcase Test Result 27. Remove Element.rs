impl Solution {
    pub fn remove_element(nums: &mut Vec<i32>, val: i32) -> i32 {
        for i in 0..nums.len() {
            if nums[i] == val {
                nums[i] = -1;
            }
        }
        
        let mut k = 0;
        for i in 0..nums.len() {
            if nums[i] != -1 {
                nums[k] = nums[i];
                k += 1;
            }
        }
        
        k as i32 
    }
}
