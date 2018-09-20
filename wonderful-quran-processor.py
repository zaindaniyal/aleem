import re
with open('wonderful_quran.txt') as file :
    filedata = file.read()

wonderful_quran = open('wonderful_quran.txt')
quran_str = str(wonderful_quran)

# Replace the target string
filedata = filedata.replace('\n', '')

# Write the file out again
with open('wonderful_quran.txt', 'w') as file:
    file.write(filedata)

filtered = filter(lambda x: not re.match(r'^\s*$', x), quran_str)