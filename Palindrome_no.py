from typing import List

def isPalindrome(x: int) -> bool:
    original = x
    reverse = 0
    while x > 0:
        reverse = reverse * 10 + x % 10
        x //= 10

    return original == reverse




x = 33
save = isPalindrome(x)
print(save)
