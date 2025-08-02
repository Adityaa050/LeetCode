class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        int minn_sum = 0;             
        int minDiff = INT_MAX;     

        for (int i = 0; i < nums.size() - 2; i++) {
            for (int j = i + 1; j < nums.size() - 1; j++) {
                for (int k = j + 1; k < nums.size(); k++) {

                    int x = nums[i] + nums[j] + nums[k];
                    int y = abs(x - target);

                    if (y == 0) {
                        return x; 
                    }

                    if (y < minDiff) {
                        minDiff = y;
                        minn_sum = x;
                    }
                }
            }
        }

        return minn_sum;
    }
};