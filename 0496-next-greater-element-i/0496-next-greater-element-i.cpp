class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
         // vector<int> res(nums1.size(),-1);
        // int c =0;
        // for(int i=0;i<nums1.size();i++){
        //     for(int j=0;j<nums2.size();j++){
        //         if(nums1[i] == nums2[j]){
        //             for(int k = j+1; k < nums2.size();k++){
        //                 if(nums2[k] > nums2[j]){
        //                     res[c] = nums2[k];
        //                     break;
        //                 }
        //             }
        //         }
        //     }
        //     c++;
        // }
        // return res;
         vector<int> res(nums1.size(),-1);
        map<int,int> mapping;
        for(int i=0;i<nums1.size();i++)
            mapping[nums1[i]] = i;
        for(int i=0;i<nums2.size();i++){
            if(mapping.find(nums2[i])==mapping.end())
                continue;
            else{
                for(int j=i+1;j<nums2.size();j++){
                    if(nums2[j]>nums2[i]){
                        int idx = mapping[nums2[i]];
                        res[idx] = nums2[j];
                        break;
                    }
                }
            }
        }
        return res;
           
    }
};