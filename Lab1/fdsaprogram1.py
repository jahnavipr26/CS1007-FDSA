arr=['10','89','9','56','4','80','8']
mini=10
maxi=10
for num in arr:
    num=int(num)
    if num < mini:
      mini=num
    if num > maxi:
      maxi=num

print("smallest element",mini)
print("largest element",maxi)
    
