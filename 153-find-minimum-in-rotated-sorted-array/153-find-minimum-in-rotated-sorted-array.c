

int findMin(int* nums, int numsSize){

    int low = 0;
    int high = numsSize - 1;
    
    if(high == 0)
        return nums[0];

    if(nums[0] < nums[high])
        return nums[0];
    
    while(low <= high)
    {
        int mid = (low + high) / 2;
        if(nums[mid] > nums[mid + 1])
            return nums[mid + 1];
        if(nums[mid - 1] > nums[mid])
            return nums[mid];
        
        if(nums[mid] > nums[high])
            low = mid + 1;
        else
            high = mid - 1;
    }
    
    return -1;
}