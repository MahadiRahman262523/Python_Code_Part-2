import re

pattern = r"colour"

#if re.match(pattern,"colour is a colour, I love blue colour"):
#if re.search(pattern,"colour is a colour, I love blue colour"):
print(re.findall(pattern,"colour is a colour, I love blue colour"))
