import re
pattern = r"colour"
text1 = "my favrt colour is blue"

text2 = re.sub(pattern,"color",text1,count = 2)
print(text2)