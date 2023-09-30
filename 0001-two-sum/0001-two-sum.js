/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    let d = {}
    for (let i = 0; i < nums.length; i++){
        let comp = target - nums[i]
        if (comp in d){
            return [d[comp], i]
        }
        d[nums[i]] = i
    }
};