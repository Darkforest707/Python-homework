1. Age Calculator
from datetime import datetime
def calculate_age():
    name = input("Enter your name: ").strip()
    birth_year = int(input("Enter your year of birth: ").strip())
    current_year = datetime.now().year
    age = current_year - birth_year
    print(f"{name}, your age is {age}.")
calculate_age()
2. Extract Car Names (txt = 'LMaasleitbtui')
def extract_hidden_word(text: str) -> str:
    # Often encoded by taking characters at even indices
    return text[::2]
txt = "LMaasleitbtui"
print(extract_hidden_word(txt))
3. Extract Car Names (txt = 'MsaatmiazD')
txt = "MsaatmiazD"
print(extract_hidden_word(txt))
4. Extract Residence Area
def extract_residence(text: str) -> str:
    if "from" not in text:
        raise ValueError("Could not find residence information.")
    return text.split("from", 1)[1].strip()
txt = "I'am John. I am from London"
print(extract_residence(txt))
5. Reverse String
def reverse_string():
    user_input = input("Enter a string: ").strip()
    print(user_input[::-1])
reverse_string()
6. Count Vowels
def count_vowels(text: str) -> int:
    vowels = set("aeiouAEIOU")
    return sum(1 for char in text if char in vowels)
user_input = input("Enter a string: ").strip()
print("Number of vowels:", count_vowels(user_input))
7. Find Maximum Value
def find_max_value():
    raw = input("Enter numbers separated by space: ").strip()
    numbers = [float(item) for item in raw.split()]
    print("Maximum value:", max(numbers))
find_max_value()
8. Check Palindrome
def is_palindrome(word: str) -> bool:
    cleaned = word.strip().lower()
    return cleaned == cleaned[::-1]
word = input("Enter a word: ")
print("Palindrome" if is_palindrome(word) else "Not a palindrome")
9. Extract Email Domain
def extract_domain(email: str) -> str:
    if "@" not in email:
        raise ValueError("Invalid email format.")
    return email.split("@")[1]
email = input("Enter your email: ").strip()
print("Domain:", extract_domain(email))
10. Generate Random Password
import secrets
import string
def generate_password(length: int = 12) -> str:
    alphabet = string.ascii_letters + string.digits + string.punctuation
    return "".join(secrets.choice(alphabet) for _ in range(length))

print("Generated password:", generate_password())
