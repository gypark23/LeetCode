/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2){

    struct ListNode temp;
    struct ListNode* ret = &temp;
    
    while(list1 && list2)
    {
        if(list1->val > list2->val)
        {
            ret->next = list2;
            list2 = list2->next;
        }
        else
        {
            ret->next = list1;
            list1 = list1->next;
        }
        ret = ret->next;
    }
    
    ret->next = list1 ? list1 : list2;
    return temp.next;
    
}