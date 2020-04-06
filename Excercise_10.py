tabby_cat = "\tI'm tabbed in." # \ is an escape character. The t after the backward slash is a tab.
persian_cat = "I'm split\non a line." # split's the text onto two lines with the text succeeding \n on a new line.
backslash_cat = "I'm \\ a \\ cat." # The \\ is actually an escape character for a backward slash. So \ is printed out.
# Note: (\\) is actually not needed, and can in this program be used as just (\). However this violates PEP 8 guidelines

# \t* Makes a tabbed space then an asterisk is used (*) to format the text as a bullet point.
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

# Prints out the the output to the terminal.
print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)


# This is a list of the escape characters used as an example within the book. This is so I can have a reference later.
# \\ = Backslash
print("Base 10 \\ Denary sucks! Base 2 \\ Binary is life!")

# \' = Single Quote
print("I haven\'t tested but, I\'m sure this works.")

# \a = ASCII Bell (BEL)
print("Ping\a!")

# \b = ASCII Backspace (BS)
print("oh oh, Hello World! is now hello\b World!")

# \f = ASCII formfeed (FF) or a page break much like shift +  enter in MS Word. Will often cause a Carriage Return.
print("This is the first page the printer prints.\fBut this sentence will be on the second page!")

# \r = Carriage return (CR) same as Execute or pressing Enter on your keyboard. Interrupts and sends operation to CPU.
print("Carriage \r Return")

# \n = ASCII linefeed (LF) or more commonly referred to as a newline
print("line 1\nline 2")

# \N{name} = Character named name in the Unicode database (Unicode only!)
print("\N{LATIN CAPITAL LETTER P}")

# \t = Horizontal tab (TAB)
print("column 1\tcolumn 2")

# \v = ASCII vertical (VT)
print("line 1 \v line 2")

# \000 = Character with octal (base 8) value 000
print("\110\145\154\154\157\40\127\157\162\154\144\41")

# \xhh = Character with hex value hh
print("\x48\x65\x6c\x6c\x6f\x20\x57\x6f\x72\x6c\x64\x21")

# \\ Explanation of Unicode Escape Encoding (Latin-1 encoding)
# \uxxxx = Character with 16-bit hex value
# \Uxxxxxxxx = Character with 32-bit hex value

# \\ Explanation of Unicode Escape Encoding
# For the above two examples. Each x in xxxx is Base 2(Binary) e.g. x(2)x(4)x(8)x(16) or x|x|x|x 2|4|8|16)
# Bytes apply here so 16 + 16 = 32-bit or [xxxx] + [xxxx] ) Matching unicode character is printed.
# So Hello\u0020World ! = Hello World! because a space ( ) is the 20th character in the Unicode database.
print('Hello\u0020World !')

# Combining formatting and escape sequences in order to make a complex string.
formatting = '{} {} {} {} {} {} {} {} {} {} {} {}'  # type: str
print(formatting.format(
    "Combining",
    "formatting",
    "and",
    "escape",
    "sequences\n",
    "ins\b",
    "order",
    "to",
    "make",
    "\u039B",
    "complex",
    "string\'s.\a"
))
