import numpy as np
# @arg arr The input list like object to be sorted
# @arg cmp A compare function which takes two element in the array, 
#          cmp(a,b)<0   if a should be placed before b,
#          cmp(a,b)==0  if arr is still sorted after a and b are exchanged,
#          cmp(a,b)>0   if a should be placed behind b.
def multi_sort(arr, cmp, method="None"):
    if(method=="quick"):
        quick_sort(arr,cmp)
    elif(method=="merge"):
        merge_sort(arr,cmp)
    elif(method=="None"): # do nothing
        return
    else:
        print("invalid argument!")




# must be in-place sort
def merge_sort(arr,cmp):
    pass

# must be in-place sort
def quick_sort(arr, cmp):
    if len(arr)<=1: 
        return arr
    pvt=arr[np.random.randint(len(arr))]   # Picks random element as pivot
    arrlarge,arrsmall,arrequal=[],[],[]
    for e in arr:
        if cmp(e, pvt) == 1:
            arrlarge.append(e)
        elif cmp(e,pvt) == -1:
            arrsmall.append(e)
        else:
            arrequal.append(e)

    # Call recursion on left and right
    arrsmall=quick_sort(arrsmall)
    arrlarge=quick_sort(arrlarge)
    arr=arrsmall+arrequal+arrlarge
    return arr


# def cmp(a,b):
#     if(a<b):
#         return -1
#     elif(a==b):
#         return 0
#     else:
#         return 1