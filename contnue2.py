num = 60
print ("Prime factors for: ", num)
i=2
while num > 1:
   if num%i==0:
      print (i)
      num=num/i
      continue
   i=i+1