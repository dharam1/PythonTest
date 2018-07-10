def BinarySearch(sorted_list,left,right,element):
    if(right >= left):
        mid = (left + right )//2
        if(sorted_list[mid] == element):
            return sorted_list[mid]
        elif(sorted_list[mid] > element):
            return (BinarySearch(sorted_list,left,mid-1,element))
        elif(sorted_list[mid] < element):
            return (BinarySearch(sorted_list,mid+1,right,element))
    else:
        return "No Element"
        
ip_list = list(map(int,input().split()))
element = int(input())
sorted_list = sorted(ip_list)
unsorted_list = ip_list
answer = BinarySearch(sorted_list,0,len(sorted_list)-1,element)
try:
    if(answer != "No Element"):
        print(unsorted_list.index(answer))
except:
    print("Element Not Found")