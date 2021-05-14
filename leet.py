

j = 0
n = len(nums)
for i in range(0, n - 1):
   if nums[i] != nums[i+1]:
    nums[j] = nums[i]
    j += 1
    nums[j] = nums[n - 1]

print(len(nums[0:j+1]))