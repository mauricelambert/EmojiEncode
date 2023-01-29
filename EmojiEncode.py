#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###################
#    This module encodes and decodes data into partially random Unicode Emoji
#    Copyright (C) 2023  Maurice Lambert

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
###################

"""
This module encodes and decodes data into partially random Unicode Emoji,
it's like a steganography in message or social network.

~# python3 EmojiEncode.py mytest
<unicode emoji charaters>
~# python3 EmojiEncode.py --html my test
&#x0001f66d&#x0001f379
&#x0001f674&#x0001f365&#x0001f373&#x0001f674
~# python3 EmojiEncode.py --html --decode '&#x0001f674&#x0001f365&#x0001f373&#x0001f674'
test
~# python3 EmojiEncode.py --decode '<unicode emoji charaters>'
<data encoded>
~#

>>> data = bytes(list(range(256)))
>>> emojis1 = encode(data)
>>> emojis2 = encode(data)
>>> assert emojis1 != emojis2
>>> assert isinstance(emojis1, str)
>>> assert isinstance(emojis2, str)
>>> assert data == decode(emojis1)
>>> assert data == decode(emojis2)
>>> emojis1 = html_encode(data)
>>> emojis2 = html_encode(data)
>>> assert emojis1 != emojis2
>>> assert isinstance(emojis1, str)
>>> assert isinstance(emojis2, str)
>>> assert data == html_decode(emojis1)
>>> assert data == html_decode(emojis2)

~# python3 -m doctest -v EmojiEncode.py
15 tests in 5 items.
15 passed and 0 failed.
Test passed.
~#
"""

__version__ = "0.0.1"
__author__ = "Maurice Lambert"
__author_email__ = "mauricelambert434@gmail.com"
__maintainer__ = "Maurice Lambert"
__maintainer_email__ = "mauricelambert434@gmail.com"
__description__ = (
    "This module encodes and decodes data into partially random Unicode Emoji,"
    " it's like a steganography in message or social network."
)
license = "GPL-3.0 License"
__url__ = "https://github.com/mauricelambert/EmojiEncode"

copyright = """
EmojiEncode  Copyright (C) 2023  Maurice Lambert
This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it
under certain conditions.
"""
__license__ = license
__copyright__ = copyright

__all__ = ["encode", "decode", "html_encode", "html_decode"]

from io import StringIO
from random import choice
from typing import Dict, List
from codecs import raw_unicode_escape_encode, raw_unicode_escape_decode

mapping: Dict[int, List[str]] = {x: [raw_unicode_escape_decode(f"\\U0001f{y}{x:0>2x}")[0] for y in "543"] for x in range(211, 256)}
mapping_temp: Dict[int, List[str]] = {x: [raw_unicode_escape_decode(f"\\U0001f{y}{x:0>2x}")[0] for y in "643"] for x in range(211)}
mapping.update(mapping_temp)

html_mapping: Dict[int, List[str]] = {x: [raw_unicode_escape_decode(f"&#x0001f{y}{x:0>2x}")[0] for y in "543"] for x in range(211, 256)}
html_mapping_temp: Dict[int, List[str]] = {x: [raw_unicode_escape_decode(f"&#x0001f{y}{x:0>2x}")[0] for y in "643"] for x in range(211)}
html_mapping.update(html_mapping_temp)

def encode(data: bytes) -> str:

    """
    This function encodes data as emoji encoding.
    """
    
    string: str = ""
    
    for char in data:
        string += choice(mapping[char])
    
    return string

def decode(emojis: str) -> bytes:

    """
    This function decodes emoji encoding as bytes.
    """
    
    data: List[int] = []
    for char in emojis:
        data.append(int(raw_unicode_escape_encode(char)[0][-2:].decode(), 16))
    
    return bytes(data)

def html_encode(data: bytes) -> str:

    """
    This function encodes data as HTML emoji encoding.
    """
    
    string: str = ""
    
    for char in data:
        string += choice(html_mapping[char])
    
    return string

def html_decode(emojis: str) -> bytes:

    """
    This function decodes emoji encoding as bytes.
    """
    
    data: List[int] = []
    emojis = StringIO(emojis)
    emoji = emojis.read(11)

    while emoji:
        data.append(int(emoji[-2:], 16))
        emoji = emojis.read(11)
    
    return bytes(data)

if __name__ == "__main__":
    from sys import exit, argv
    html = False
    decode_ = False

    if "--html" in argv:
        html = True
        argv.remove("--html")

    if "-h" in argv:
        html = True
        argv.remove("-h")
        
    if "--decode" in argv:
        decode_ = True
        argv.remove("--decode")

    if "-d" in argv:
        decode_ = True
        argv.remove("-d")

    if html and decode_:
        callback = html_decode
    elif decode_:
        callback = decode
    else:
        callback = html_encode if html else encode

    for argument in argv[1:]:
        if decode_:
            print(callback(argument).decode())
        else:
            print(callback(argument.encode()))
    
    exit(0)