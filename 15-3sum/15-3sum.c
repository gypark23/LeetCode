int cmp(int *a, int *b)
{
    return *a - *b;
}

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** threeSum(int* nums, int numsSize, int* returnSize, int** returnColumnSizes){

    int** ret = malloc(sizeof(int*) * numsSize * (numsSize - 1));
    int size = 0;
    qsort(nums, numsSize, sizeof(int), cmp);
    
    for(int i = 0; i < numsSize; i++)
    {
        if(i > 0 && nums[i - 1] == nums[i])
            continue;
        
        int low = i + 1;
        int high = numsSize - 1;
        
        while(low < high)
        {
            if(nums[low] + nums[high] == -nums[i])
            {
                int *temp = (int*)malloc(sizeof(int) * 3);
                temp[0] = nums[i];
                temp[1] = nums[low];
                temp[2] = nums[high];
                ret[size++] = temp;
                low++;
                while(low < high && nums[low - 1] == nums[low])
                    low++;
            }
            else if(nums[low] + nums[high] < -nums[i])
            {
                low++;
            }
            else
            {
                high--;
            }
        }
    }
    *returnSize = size;
    *returnColumnSizes = malloc(size * sizeof(int));    
    for (int i = 0; i < size; ++i)
        (*returnColumnSizes)[i] = 3;
    return ret;
    
}