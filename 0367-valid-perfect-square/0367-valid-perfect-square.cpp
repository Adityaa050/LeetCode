class Solution {
public:
    bool isPerfectSquare(int num) {
        int sqr = sqrt(num);
        return sqr*sqr == num;
    }
};