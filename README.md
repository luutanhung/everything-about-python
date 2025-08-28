<div align="center">
    <h2>Everything About Python</h2>
    <img src="https://img.shields.io/badge/python-3.13-brightgreen.svg" alt="Python 3.13" />
</div>

## Table of Contents
* [Lists](#lists)
    * [Declarations](#state-you-want-to-hold-a-bunch-of-items)
    * [Loop](#pay-a-visit-to-each-elements)
* [License](#license)
* [Authors](#authors)

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
    print(f"Hi {neighborhood}. Have a good day!")
```
```bash
Hi Phương. Have a good day!
Hi Anh. Have a good day!
Hi Lâm. Have a good day!
Hi Khoa. Have a good day!
```

## License

This project is distributed under MIT License. See `License.txt` for more details.

## Authors
- Lưu Tấn Hưng | [GitHub](https://github.com/luutanhung) | [X](https://x.com/luu_tan_hung)
