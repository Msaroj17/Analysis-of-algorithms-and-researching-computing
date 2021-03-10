def issubsetSum(set,n,sum):
    if(sum==0):
        return True
    if(n==0 and sum!=0):
        return False
    if(set[n-1]>sum):
        return issubsetSum(set,n-1,sum);
    return issubsetSum(set,n-1,sum)or issubsetSum(set,n-1,sum-set[n-1])
set=[3,34,4,12,5,2]
sum=100
n=len(set)
if(issubsetSum(set,n,sum)==True):
    print("found a subset with given sum")
else:
    print("no subset with given sum")
            
