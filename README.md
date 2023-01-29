![EmojiEncoding logo](https://mauricelambert.github.io/info/python/security/EmojiEncoding_small.png "EmojiEncoding logo")

# EmojiEncoding

## Description

This module encodes and decodes data into partially random Unicode Emoji, it's like a steganography in message or social network.

## Requirements

This package require:
 - python3
 - python3 Standard Library

## Installation

```bash
pip install EmojiEncoding
```

## Usages

### Command line

```bash
python3 -m EmojiEncoding 'my data'
python3 EmojiEncoding.pyz --html 'first data' 'second data'
EmojiEncoding --decode '<unicode emoji charaters>'
EmojiEncoding --html --decode '&#x0001f674&#x0001f365&#x0001f373&#x0001f674'
```

### Python script

```python
from EmojiEncoding import encode, decode, html_decode, html_encode

emojis: str = encode(b'my data')
data: bytes = decode(emojis)

html_emojis: str = encode(b'my data')
data: bytes = decode(html_emojis)
```

## Links

 - [Github Page](https://github.com/mauricelambert/EmojiEncoding/)
 - [Documentation](https://mauricelambert.github.io/info/python/security/EmojiEncoding.html)
 - [Pypi package](https://pypi.org/project/EmojiEncoding/)
 - [Executable](https://mauricelambert.github.io/info/python/security/EmojiEncoding.pyz)

## Licence

Licensed under the [GPL, version 3](https://www.gnu.org/licenses/).
