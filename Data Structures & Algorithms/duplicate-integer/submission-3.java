class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashMap<Integer, Integer> hashMap = new HashMap<>();

        // count frequency of each number
        for (int i : nums) {
            if (hashMap.containsKey(i)) {
                hashMap.put(i, hashMap.get(i) + 1);
            } else {
                hashMap.put(i, 1);
            }
        }

        // check if any value > 1
        for (int count : hashMap.values()) {
            if (count > 1) {
                return true;
            }
        }

        return false;
    }
}