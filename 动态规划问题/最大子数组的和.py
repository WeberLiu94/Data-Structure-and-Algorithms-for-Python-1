#使用动态规划
#F（i）：以array[i]为末尾元素的子数组的和的最大值，子数组的元素的相对位置不变
#F（i）=max（F（i-1）+array[i] ， array[i]）
#res：所有子数组的和的最大值
#res=max（res，F（i））




def FindGreatestSumOfSubArray(array):
    # write code here
    if array == None:
        return 0
    max_num = array[0]
    res = array[0]
    for i in range(1,len(array)):
        max_num = max(array[i],max_num+array[i]) #array[i]结尾的子数组的最大和
        res = max(res,max_num)
    return res
