/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        priority_queue<int,vector<int>,greater<int>>q;
        for(int i=0;i<lists.size();i++){
            while(lists[i]!=NULL){
                q.push(lists[i]->val);
                lists[i]=lists[i]->next;
            }
        }
        ListNode*head;
        if(!q.empty()){
            head=new ListNode(q.top());
            q.pop();}
        else 
            head=NULL;
        ListNode*temp1=head;
        while(!q.empty()){
            ListNode* temp2=new ListNode(q.top()); q.pop();
            temp1->next=temp2;
            temp1=temp2;
        }
        return head;
    }
};