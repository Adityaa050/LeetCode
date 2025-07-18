class Solution {
public:
    string removeDuplicates(string s) {
        string str="";
        int n=0;
        while(n<s.length()){
        if ( str.empty() || str.back()!=s[n]) {
            str.push_back(s[n]);
        }
        else{
            str.pop_back();
        }
        n++;
    }
    return str;
    }
};