import re

re_c = re.compile("^(.*hangzhou)")
lists = re_c.findall('/hellhangzhou')
print(lists)