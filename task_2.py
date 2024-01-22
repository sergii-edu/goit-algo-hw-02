from collections import deque


def is_palindrome(str):
    str = "".join(char.lower() for char in str if char.isalnum())
    char_deque = deque(str)

    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False
    return True


# Повинно бути True
print(is_palindrome("янукович вивчив окуня."))

# Повинно бути True
print(
    is_palindrome("Чи в окуня? Ні, тупі дяді — путін, янукович")
)  

# Повинно бути False
print(is_palindrome("Окунь вивчив януковича."))  
