# ==========================================================
# REGULAR EXPRESSIONS (re MODULE) IN PYTHON
# ==========================================================

import re


# ==========================================================
# CHARACTER SETS []
# ==========================================================

text = "abc123"

print(re.findall(r"[abc]", text))     # match a, b, or c
print(re.findall(r"[a-c]", text))     # range a-c
print(re.findall(r"[0-9]", text))     # digits
print(re.findall(r"[^5]", text))      # not 5


# ==========================================================
# SPECIAL METACHARACTERS
# ==========================================================

text = "Hello 123 \n"

print(re.findall(r"\d", text))   # digits
print(re.findall(r"\D", text))   # non-digits
print(re.findall(r"\s", text))   # whitespace
print(re.findall(r"\S", text))   # non-whitespace
print(re.findall(r"\w", text))   # alphanumeric
print(re.findall(r"\W", text))   # non-alphanumeric
print(re.findall(r".", text))    # any char except newline


# ==========================================================
# QUANTIFIERS (?, +, *, {n,m})
# ==========================================================

text = "aaaab"

print(re.findall(r"a?", text))       # 0 or 1
print(re.findall(r"a+", text))       # 1 or more
print(re.findall(r"a*", text))       # 0 or more
print(re.findall(r"a{2,4}", text))   # between 2 and 4


# ==========================================================
# ALTERNATION (|)
# ==========================================================

text = "cat dog bat"
print(re.findall(r"cat|dog", text))


# ==========================================================
# ESCAPE CHARACTER (\)
# ==========================================================

text = "price is 10.50"
print(re.findall(r"\.", text))   # match dot literally


# ==========================================================
# BOUNDARIES
# ==========================================================

text = "python is fun"
print(re.findall(r"\bpython\b", text))   # word boundary


# ==========================================================
# MATCH vs SEARCH
# ==========================================================

text = "hello python"

# match → only start
print(re.match(r"python", text))   # None

# search → anywhere
print(re.search(r"python", text))  # match object


# ==========================================================
# GROUPS
# ==========================================================

text = "Name: Alice Age: 25"

m = re.search(r"Name: (\w+) Age: (\d+)", text)

print(m.group(0))   # full match
print(m.group(1))   # first group
print(m.group(2))   # second group
print(m.groups())   # tuple of groups


# ==========================================================
# FINDALL
# ==========================================================

text = "a1 b2 c3"
print(re.findall(r"\w\d", text))   # ['a1', 'b2', 'c3']


# ==========================================================
# SUB (REPLACE)
# ==========================================================

text = "abc123"
print(re.sub(r"\d", "#", text))   # replace digits


# ==========================================================
# COMPILE
# ==========================================================

pattern = re.compile(r"\d+")

print(pattern.findall("a1 b22 c333"))


# ==========================================================
# FINDITER
# ==========================================================

text = "a1 b22 c333"

for match in re.finditer(r"\d+", text):
    print(match.group(), match.start(), match.end())


# ==========================================================
# FLAGS
# ==========================================================

text = "Python python"

print(re.findall(r"python", text))              # case-sensitive
print(re.findall(r"python", text, re.I))        # ignore case


# MULTILINE
text = "hello\npython"
print(re.findall(r"^python", text, re.M))


# DOTALL
text = "a\nb"
print(re.findall(r"a.b", text, re.S))   # dot matches newline


# ==========================================================
# ANCHORS (^, $)
# ==========================================================

text = "python"

print(re.findall(r"^python", text))   # start
print(re.findall(r"python$", text))   # end


# ==========================================================
# GREEDY vs NON-GREEDY
# ==========================================================

text = "<python>perl</python>"

print(re.findall(r"<.*>", text))    # greedy
print(re.findall(r"<.*?>", text))   # non-greedy


# ==========================================================
# BACKREFERENCES
# ==========================================================

text = "hello hello"

print(re.findall(r"(\w+)\s\1", text))   # repeated word


# ==========================================================
# LOOKAHEAD
# ==========================================================

text = "python!"

print(re.findall(r"python(?=! )", text))  # may not match due to space

print(re.findall(r"python(?=!)", text))   # match if followed by !


# ==========================================================
# SUMMARY (IN COMMENTS)
# ==========================================================

# [] → character set
# \d \w \s → special classes
# ?, +, *, {n,m} → repetition
# | → OR
# \ → escape special chars
# \b → word boundary

# re functions:
#   match() → start only
#   search() → anywhere
#   findall() → list of matches
#   sub() → replace
#   compile() → reusable pattern
#   finditer() → iterator

# flags:
#   re.I → ignore case
#   re.M → multiline
#   re.S → dot matches newline