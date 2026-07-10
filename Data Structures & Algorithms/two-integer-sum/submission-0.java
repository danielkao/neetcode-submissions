public class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> map = new HashMap<>(); // value -> index

        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];

            if (map.containsKey(complement)) {
                int j = map.get(complement);
                // return smaller index first
                return (j < i) ? new int[]{j, i} : new int[]{i, j};
            }

            map.put(nums[i], i);
        }

        // given the assumption, this should never happen
        return new int[]{-1, -1};
    }
}