



def isPalindrome(s: str) -> bool:
 cor_str =  " ".join([ch for ch in s if ch.isalnum()]).lower()
 print(cor_str)
 i = 0
 j = len(cor_str)-1
 # print(j)
 while i < j:
  if cor_str[i] != cor_str[j]:
   return False
  i += 1
  j -= 1
 return True


print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome("race a car"))
print(isPalindrome(" "))