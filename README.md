<div align="center">
    <img src="assets/python_logo.png" alt="Python logo" width="70" height="70">
    <h2>Everything About Python</h2>
    <img src="https://img.shields.io/badge/python-3.13-brightgreen.svg" alt="Python 3.13" />
</div>

## Table of Contents
* [Recipes](#recipes)
* [Lists](#lists)
    * [Declarations](#state-you-want-to-hold-a-bunch-of-items)
    * [Loop](#pay-a-visit-to-each-elements)
    * [Sort](#order-in-a-chaotic-world)
* [Regex](#regex)
* [License](#license)
* [Authors](#authors)

## Recipes
This section provides practical code snippets for various common programming tasks, serving as a quick reference guide.
- [Check File Existence](/security/check_file_existence.py)
- [Check File Permissions](/security/check_file_permissions.py)

## Lists

### State you want to hold a bunch of items
1. Adopt square bracket []
```python
# Empty list
ops_empty = []
print(ops_empty) # []

# List of whole numbers
nums = [20, 8, 2002]
print(nums) # [20, 8, 2002]

# List of well-known car manufacturers
manufacturers = ["Honda", "Cadillac", "Volkswagen Beetle", "TOYOTA"]
print(manufacturers) # ["Honda", "Cadillac", "Volkswagen Beetle", "TOYOTA"]
```

2. Use list() constructor
```python
# Empty list
ops_empty = []
print(ops_empty) # []

# Transform the name of Elon Musk to a list of characters
chrs = list("Elon Musk")
print(chrs) # ['E', 'l', 'o', 'n', ' ', 'M', 'u', 's', 'k']
```

### Pay a visit to each elements
```python
# Go through each neighborhoods' house and give a greet
intimate_neighborhoods = ["Phương", "Anh", "Lâm", "Khoa"]
for neighborhood in intimate_neighborhoods:
    print(f"🙋 Hi {neighborhood}. Have a good day!")
```
```bash
🙋 Hi Phương. Have a good day !
🙋 Hi Anh. Have a good day!
🙋 Hi Lâm. Have a good day!
🙋 Hi Khoa. Have a good day!
```

### Order in a Chaotic World
```python
# Declare a list of well-known scientists
scientists: list[str] = ["Issac Newton", "Albert Einstein", "Niels Bohr", "Michael Faraday", "Max Born", "Johannes Kepler"]

# Arrange elements in ascending order
print(sorted(scientists))

# Rearrange items in descending order
print(sorted(scientists, reverse=True))
```
```bash
['Albert Einstein', 'Issac Newton', 'Johannes Kepler', 'Max Born', 'Michael Faraday', 'Niels Bohr']
['Niels Bohr', 'Michael Faraday', 'Max Born', 'Johannes Kepler', 'Issac Newton', 'Albert Einstein']
```

## Regex
This section contains examples of regular expressions question to practice and solutions.

- [Extract numbers](/regex/extract_numbers.py)
- [Extract three-digit numbers that are not immediately followed by a letter](/regex//three_digit_numbers_not_followed_by_a_letter.py)

## License

This project is distributed under MIT License. See [License.txt](/LICENSE.txt) for more details.

## Authors
- Lưu Tấn Hưng | [GitHub](https://github.com/luutanhung) | [X](https://x.com/luu_tan_hung)
