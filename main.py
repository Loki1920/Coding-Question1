#coding question
s = []  #initialized an array to store output 
def fun(Arr,sum):
  for i in range(len(Arr)):
    for j in range(len(Arr)):
      if Arr[i]+Arr[j]==sum and (Arr[i]+Arr[i]!=sum or Arr[j]+Arr[j]!=sum):
        s.append(Arr[i])
        s.append(Arr[j])
  return list(set(s))

Arr = [3, 5, -4, 8, 11, 1, -1, 6]
sum = 10
print('solutionn Array is :',fun(Arr,sum))
        
  
  