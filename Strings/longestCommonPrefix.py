def longest_common_prefix(words):
   k = 0
   n = len(words)
   if n == 0:
       return ""
   if n == 1:
       return words[0]
   
   while True:
       for i in range(1, n):
           if k == len(words[i]) or k == len(words[0]):
               return words[0][:k]
           if words[i][k] != words[0][k]:
               return words[0][:k]
       
       k += 1