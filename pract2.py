def heapify(arr,n,i):  #to heapify subtree rooted at index i,n is size of heap
    largest=i          #initialize largest as root
    L=2*i+1            #left=2*i+1
    R=2*i+2            #right=2*i+2
    if L<n and arr[i]< arr[L]:  #see if left child of root exists and is greater than root
        largest=L

    if R<n and arr[largest]< arr[R]:  #see if right child of root exists and is greater than root
        largest=R
                                      #change root ,if needed
    if largest !=i:
        arr[i],arr[largest]=arr[largest],arr[i]  #swap
        heapify(arr,n,largest)                   #heapify the root

def heapSort(arr):                      #the main function to sort an array of given size
    n=len(arr)
                                        #build a maxheap
    for i in range(n,-1,-1):            
        heapify(arr,n,i)
                                        #one by one extract elements
    for i in range(n-1,0,-1):
        arr[i],arr[0]=arr[0],arr[i]     #swap
        heapify(arr,i,0)
        
#driver code to test the above
arr=[12,11,13,5,6,7]
heapSort(arr)
n=len(arr)
print("sorted array is:")
for i in range(n):
    print("%d"%arr[i])
    
        
