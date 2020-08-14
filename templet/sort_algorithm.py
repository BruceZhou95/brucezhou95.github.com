"""
1.冒泡排序	O(n2)
2.选择排序	O(n2)
3.插入排序	O(n2)
4.希尔排序	O(n1.5)
5.归并排序	O(N*logN)
6.快速排序	O(N*logN)
7.计数排序 	O(n+k)
8.桶排序		O(n+k)
9.堆排序		O(N*logN)
10.基数排序	O(d(n+r))
"""

# 1.冒泡排序

a=[3,2,6,4,9,1,0,11,-2]
print("冒泡排序", a)

def bulu_sort(a):
	for i in range(len(a)-1):
		for j in range(len(a)-i-1):
			if(a[j]>a[j+1]):
				a[j], a[j+1]=a[j+1], a[j]
bulu_sort(a)
print("冒泡排序后:", a)

# 2.选择排序
"""
工作原理是每一次从待排序的数据元素中选出最小（或最大）的一个元素，
存放在序列的起始位置，然后，再从剩余未排序元素中继续寻找最小（大）
元素，然后放到已排序序列的末尾。
"""
a=[2,3,6,4,9,1,0,11,-2]
print("选择排序", a)

def Select_sort(a):
	for i in range(len(a)-1):
		index=i
		for j in range(i+1, len(a)):
			if (a[index]>a[j]):
				index=j
		a[i], a[index]=a[index], a[i]
Select_sort(a)
print("选择排序后", a)



# 3.插入排序
"""
	它把一个无序数列看成两个数列，假如第一个元素构成了第一个数列，
	那么余下的元素构成了第二个数列，很显然，第一个数列是有序的
	（因为只有一个元素嘛，肯定有序哦），那么我们把第二个数列的第一个元素
	拿出来插入到第一个数列，使它依然构成一个有序数列，直到第二个数列中的
	所有元素全部插入到第一个数列，这时候就排好序了
"""
a=[3,2,6,6,4,9,1,0,11,-2]
print("插入排序", a)

def insert_sort(list1):
    for i in range(1, len(list1)):
        # print("第{}轮：".format(i))
        key=list1[i]
        j=i-1
        while j>=0 and list1[j]>key:
            list1[j+1]=list1[j]
            j-=1
        list1[j+1]=key
insert_sort(a)
print("插入排序后", a)



# 4.希尔排序
"""
	先取一个小于n的整数d1作为第一个增量，把文件的全部记录分组。
	所有距离为d1的倍数的记录放在同一个组中。先在各组内进行直接插入排序；
	然后，取第二个增量d2<d1重复上述的分组和排序，
	直至所取的增量  =1(  <  …<d2<d1)，即所有记录放在同一组中进行直接插入
	序为止。
"""
a=[3,2,6,4,9,1,0,11,-2]
print("希尔排序", a)

def shell_sort(a):

	step=len(a)//2
	while step:
		for i in range(step, len(a)):
			while(i>=step and a[i]<a[i-step]):
				a[i], a[i-step]=a[i-step], a[i]
				i-=step 
		step//=2

shell_sort(a)
print("希尔排序后:", a)

# 5.归并排序
"""
归并排序的思想就是先递归分解数组，再合并数组。
"""

a1=[3,2,6,4,9,1,0,11,-2]
print("归并排序", a1)

def merge(a,b):
	i,j=0,0
	result=[]
	while j<len(b) and i<len(a):
		if a[i]<b[j]:
			result.append(a[i])
			i+=1
		else:
			result.append(b[j])
			j+=1
	if i==len(a):
		result+=b[j:]
	else:
		result+=a[i:]
	return result

def merge_sort(a):
	if len(a)<=1:
		return a 
	mid=len(a)>>1 
	a1=merge_sort(a[:mid])
	b1=merge_sort(a[mid:])
	return merge(a1, b1)

a=merge_sort(a1)

print("归并排序后:", a)

# 6.快速排序
"""
快排的思想：首先任意选取一个数据（通常选用数组的第一个数）作为关键数据，
然后将所有比它小的数都放到它前面，所有比它大的数都放到它后面，这个过程称为一趟快速排序。
"""

a1=[3,2,6,4,9,1,0,11,-2]
print("快速排序", a1)


def quick_sort(a, start, end):
	if(start < end):
		i, j=start, end
		key=a[i]
		while i<j:
			while (i<j) and (key<=a[j]):
				j-=1 
			a[i], a[j]=a[j], a[i]
			while (i<j) and (key>=a[i]):
				i+=1 
			a[i], a[j]=a[j], a[i]

		quick_sort(a, start, i)
		quick_sort(a, i+1, end)
quick_sort(a1, 0, len(a1)-1)
print("快速排序后", a1)




# 7.计数排序
"""
计数排序的基本思想为一组数在排序之前先统计这组数中其他数小于这个数的个数，
则可以确定这个数的位置。例如要排序的数为 7 4 2 1 5 3 1 5；则比7小的有7个数，
所有7应该在排序好的数列的第八位，同理3在第四位，对于重复的数字，1在1位和2位
（暂且认为第一个1比第二个1小），5和1一样位于6位和7位。
"""
a1=[3,2,6,4,9,1,0,11,-2]
print("计数排序", a1)

def Count_sort(a):
	min_num=min(a)
	max_num=max(a)

	count_num=[0]*(max_num-min_num+1)
	for i in a:
		count_num[i-min_num]+=1
	a.clear()
	for ind, i in enumerate(count_num):
		while i:
			a.append(ind+min_num)
			i-=1

Count_sort(a1)
print("计数排序后：", a1)

# 8.桶排序
"""
区间跨度 = （最大值-最小值）/ （桶的数量 ）
每一个桶（bucket）代表一个区间范围，里面可以承载一个或多个元素。桶排序的第一步，
就是创建这些桶，确定每一个桶的区间范围：
"""

a1=[3,2,6,4,9,1,0,11,-2]
print("桶排序", a1)

def buck_sort(a):
	min_num=min(a)
	max_num=max(a)
	buckets_range=(max_num-min_num)/len(a) #桶的范围
	buckets_num=[[] for i in range(len(a)+1)] # 桶的数量len(a)+1
	for i in a:
		buckets_num[int((i-min_num)/buckets_range)].append(i)
	a.clear()
	for bucket in buckets_num:
		for i in sorted(bucket):			
			a.append(i)
	return a 
a1=buck_sort(a1)
print("桶排序后", a1)


# 9.堆排序
"""
堆排序（英语：Heapsort）是指利用堆这种数据结构所设计的一种排序算法。
堆是一个近似完全二叉树的结构，并同时满足堆积的性质：即子结点的键值或索引总
是小于（或者大于）它的父节点。
"""
a=[3,2,6,4,9,1,0,11]
print("堆排序",a)

def heapify(arr, n, i): 
	largest = i  
	le = 2 * i + 1     # left = 2*i + 1 
	ri = 2 * i + 2     # right = 2*i + 2 

	if le < n and arr[i] < arr[le]: 
		largest = le 

	if ri < n and arr[largest] < arr[ri]: 
		largest = ri 

	if largest != i: 
		arr[i], arr[largest] = arr[largest], arr[i]  # 交换
		heapify(arr, n, largest) 

def heapSort(arr): 
	n = len(arr) 

	# Build a maxheap. 
	for i in range(n, -1, -1): 
		heapify(arr, n, i) 

	# 一个个交换元素
	for i in range(n-1, 0, -1): 
		arr[i], arr[0] = arr[0], arr[i]   # 交换
		heapify(arr, i, 0)
	return arr
print("堆排序后", heapSort(a),)


# 10.基数排序
"""
首先根据个位数的数值，在走访数值时将它们分配至编号0到9的桶子中：
接下来将这些桶子中的数值重新串接起来，成为以下的数列：

"""

import math

a=[3,200,6,4,9,1,0,11] # 负数不能排序
print("基数排序",a)

def radixSort(n):
	mod=10
	div=1
	mostbit=len(str(max(n))) #最大位的个数
	buckets=[[] for row in range(mod)] # 构造mod个空桶
	while mostbit:
		for n_i in n: ## 将数据放入对应的桶中
			buckets[n_i//div%mod].append(n_i)
			# print(buckets)
		n.clear() # n的索引
		for bucket in buckets: #收集数据
			# print(bucket,"*"*len(bucket))
			while  bucket:
				n.append(bucket.pop(0))
		div *=10
		mostbit -= 1
	return n
print("基数排序后", radixSort(a))

