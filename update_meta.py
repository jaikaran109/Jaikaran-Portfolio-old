import os

# Update package.json
path = 'C:/Users/Lenovo/OneDrive/Desktop/vinayakkulkarni.dev/package.json'
with open(path, 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace('"description": "Vinayak\'s personal website"', '"description": "Jai Karan Gupta\'s personal website"')
c = c.replace('"name": "Vinayak Kulkarni"', '"name": "Jai Karan Gupta"')

with open(path, 'w', encoding='utf-8') as f:
    f.write(c)
print('package.json updated')

# Update README.md
path = 'C:/Users/Lenovo/OneDrive/Desktop/vinayakkulkarni.dev/README.md'
with open(path, 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace('MIT © [Vinayak Kulkarni](https://vinayakkulkarni.dev)', 'MIT © [Jai Karan Gupta](https://vinayakkulkarni.dev)')

with open(path, 'w', encoding='utf-8') as f:
    f.write(c)
print('README.md updated')
