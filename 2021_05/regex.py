# https://stackoverflow.com/questions/67485587/python-regex-matching-a-text-that-has-a-certain-string-more-than-once/67485660#67485660

import re

pattern = 'English'
string = 'English people speaks English'
result = re.findall(pattern, string)
print(result)