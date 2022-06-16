

int search(int* nums, int numsSize, int target){

    int low = 0;
    int high = numsSize - 1;
    
    while(low <= high)
    {
        int mid = (low + high) / 2;
        printf("%d %d %d\n", low, mid, high);
        if(nums[mid] == target)
            return mid;
        
        //[low...mid] sorted
        if(nums[mid] >= nums[low])
        {
            //within the first subarray
            if(target >= nums[low] && target <= nums[mid])
                high = mid - 1;
            else
                low = mid + 1;
        }
        else
        {
            if(target <= nums[high] && target >= nums[mid])
                low = mid + 1;
            else
                high = mid - 1;
        }
    }
    
    return -1;
    
}