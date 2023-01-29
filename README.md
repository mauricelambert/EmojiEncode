![EmojiEncode logo](https://mauricelambert.github.io/info/python/security/EmojiEncode_small.png "EmojiEncode logo")

# EmojiEncode

## Description

This module encodes and decodes data into partially random Unicode Emoji, it's like a steganography in message or social network.

## Requirements

This package require:
 - python3
 - python3 Standard Library

## Installation

```bash
pip install EmojiEncode
```

## Usages

### Command line

```bash
python3 -m EmojiEncode 'my data'
python3 EmojiEncode.pyz --html 'first data' 'second data'
EmojiEncode --decode '<unicode emoji charaters>'
EmojiEncode --html --decode '&#x0001f674&#x0001f365&#x0001f373&#x0001f674'
```

### Python script

```python
from EmojiEncode import encode, decode, html_decode, html_encode

emojis: str = encode(b'my data')
data: bytes = decode(emojis)

html_emojis: str = encode(b'my data')
data: bytes = decode(html_emojis)
```

## Links

 - [Github Page](https://github.com/mauricelambert/EmojiEncode/)
 - [Documentation](https://mauricelambert.github.io/info/python/security/EmojiEncode.html)
 - [Pypi package](https://pypi.org/project/EmojiEncode/)
 - [Executable](https://mauricelambert.github.io/info/python/security/EmojiEncode.pyz)

## Licence

Licensed under the [GPL, version 3](https://www.gnu.org/licenses/).
