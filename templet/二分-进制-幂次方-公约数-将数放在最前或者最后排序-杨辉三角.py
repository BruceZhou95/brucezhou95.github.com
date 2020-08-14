
#11.折半查找

a=[3,200,6,4,9,1,0,11] # 负数不能排序
print(a)

def BinSearch(array,key):
	low=0
	high=len(array)-1
	while low<=high:
		mid=(low+high)//2
		if key==array[mid]:
			return key
		elif key<array[mid]:
			high=mid-1
		elif key>array[mid]:
			low=mid+1

	return "没找到"

	
a1=BinSearch(a,6)
print(a1)



#最大公约数
# 方法1 
def gcd1(a, b):

	while b:
		tmp=a%b
		a=b 
		b=tmp 
	return a 

f=gcd1(12, 8)
print("最大公约数1", f)


def gcd2(a, b):
	if b>a:
		a, b=b, a 
	index=0
	for i in range(b+1,1,-1):
		if (a%i==0 and b%i==0):
			return i


def gcd3(a, b):
	if a<b:
		a, b=b, a 
	if b==0:
		return a 

	if (a%2==0 and b%2==0):
		return 2*gcd3(a>>1, b>>1)
	if(a%2==0):
		return gcd3(a>>1, b)
	if(b%2==0):
		return gcd3(a, b>>1)
	return gcd3((a+b)>>1, (a-b)>>1)


f=gcd3(42,56)
print("最大公约数3（（（", f)

print("**************************")

def numberOfSteps (num) :
    count=0
    # print(num>>1)
    while num:
        if num%2==0:
            num=num>>1
            count+=1
        else:
            num=num-1
            count+=1
    return count

print(numberOfSteps(14))




a=[]
# b=""
# 求二进制
def t(n):
	a=""
	while n>0:
		a+=str((n%7))
		n//=7

	# return a[::-1] # 一定要反转
	# b+="1"
	# a.append("2")


print(t(7))


# 求某个数是否是3的幂次方
def diV(n):
	while n%3==0:
		n//=3

	return n==1

print(diV(15))

# 把一个数放在最前面排序
def sorthigh(array):
    n=len(array)
    ls=sorted(array)
    count = 0
 
    j = n-1
    for i in range(n-1,-1,-1):
        if ls[j] == array[i]:
            count+=1
            j-=1
    print(count, "*")
    return n-count


print(sorthigh([3,6,1,4,2,5]), "!")

# 把一个数放在最后面排序
def sorthand(arr):
	a=arr
	b=sorted(a)
	j=0 
	count=0 
	for i in range(len(a)):  
		if a[i] == b[j]:
			j+=1    
			count+=1  
	print(count, "#")
	print(len(b)-count, "@")

print(sorthand([3,6,1,4,2,5]))

def yanghui(num):
	# pass
# list 用来保存杨辉三角
	list1=[]
	for n in range(num):
		row =[1] #保存行
		list1.append(row)
		if n ==0:
			print([1])
			continue
		for m in range(1, n):
			row.append(list1[n - 1][m - 1] + list1[n - 1][m])
		row.append(1)
		# print(', '.join(str(i) for i in row)) 
		print(row) 






