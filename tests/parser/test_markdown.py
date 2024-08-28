#──██████──────██████───█████████████──────██████████████───████████████████─────────
#──██──██──────██──██───██─────────██────██────────────██───██────────────██─────────
#──██──██──────██──██───██──█████████───██───████████████───██───███████──██─────────
#──██──██──────██──██───██──██──────────██──██──────────────██───██───██──██─────────
#──██──██──────██──██───██──█▉──────────██──██──────────────██───██───██──██─────────
#──██──██──────██──██───██──██──────────██──██──────────────██───██───██──██─────────
#──██──██──────██──█▉───██──██──────────██──██──────────────██───██───██──██─────────
#──██──██──────██──██───██──█████████───██──█▉───███████────██───███████──██─────────
#──██───██────██───██───██─────────██───██──██───██────██───██────────────██─────────
#───██───██──██───██────██──█████████───██──██───████──██───██───███████──██─────────
#────██───████───██─────██──██──────────██──██─────██──██───██───██───██──██─────────
#─────██───██───██──────██──██──────────██───██────██──██───██───██───██──██─────────
#──────██──────██───────██──██───────────██───██───██──██───██───██───██──██─────────
#───────██────██────────██──█████████─────██──███████──██───██───██───██──██─────────
#────────██──██─────────██─────────█▉──────██──────────██───██───██───██──██─────────
#─────────████──────────█████████████───────████████████────███████───██████─────────
import VeGagram
from VeGagram.parser.markdown import Markdown


# expected: the expected unparsed Markdown
# text: original text without entities
# entities: message entities coming from the server

def test_markdown_unparse_bold():
    expected = "**bold**"
    text = "bold"
    entities = VeGagram.types.List(
        [VeGagram.types.MessageEntity(type=VeGagram.enums.MessageEntityType.BOLD, offset=0, length=4)])

    assert Markdown.unparse(text=text, entities=entities) == expected


def test_markdown_unparse_italic():
    expected = "__italic__"
    text = "italic"
    entities = VeGagram.types.List(
        [VeGagram.types.MessageEntity(type=VeGagram.enums.MessageEntityType.ITALIC, offset=0, length=6)])

    assert Markdown.unparse(text=text, entities=entities) == expected


def test_markdown_unparse_strike():
    expected = "~~strike~~"
    text = "strike"
    entities = VeGagram.types.List(
        [VeGagram.types.MessageEntity(type=VeGagram.enums.MessageEntityType.STRIKETHROUGH, offset=0, length=6)])

    assert Markdown.unparse(text=text, entities=entities) == expected


def test_markdown_unparse_spoiler():
    expected = "||spoiler||"
    text = "spoiler"
    entities = VeGagram.types.List(
        [VeGagram.types.MessageEntity(type=VeGagram.enums.MessageEntityType.SPOILER, offset=0, length=7)])

    assert Markdown.unparse(text=text, entities=entities) == expected


def test_markdown_unparse_url():
    expected = '[URL](https://VeGagram.org/)'
    text = "URL"
    entities = VeGagram.types.List([VeGagram.types.MessageEntity(type=VeGagram.enums.MessageEntityType.TEXT_LINK,
                                                                 offset=0, length=3, url='https://VeGagram.org/')])

    assert Markdown.unparse(text=text, entities=entities) == expected


def test_markdown_unparse_emoji():
    expected = '![🥲](tg://emoji?id=5195264424893488796) im crying'
    text = "🥲 im crying"
    entities = VeGagram.types.List([VeGagram.types.MessageEntity(type=VeGagram.enums.MessageEntityType.CUSTOM_EMOJI,
                                                                 offset=0, length=2, custom_emoji_id=5195264424893488796)])

    assert Markdown.unparse(text=text, entities=entities) == expected


def test_markdown_unparse_code():
    expected = '`code`'
    text = "code"
    entities = VeGagram.types.List(
        [VeGagram.types.MessageEntity(type=VeGagram.enums.MessageEntityType.CODE, offset=0, length=4)])

    assert Markdown.unparse(text=text, entities=entities) == expected


def test_markdown_unparse_pre():
    expected = """```python
for i in range(10):
    print(i)
```"""

    text = """for i in range(10):
    print(i)"""

    entities = VeGagram.types.List([VeGagram.types.MessageEntity(type=VeGagram.enums.MessageEntityType.PRE, offset=0,
                                                                 length=32, language='python')])

    assert Markdown.unparse(text=text, entities=entities) == expected


def test_markdown_unparse_blockquote():
    expected = """> Hello
> from

> VeGagram!"""

    text = """Hello\nfrom\n\nVeGagram!"""

    entities = VeGagram.types.List(
        [VeGagram.types.MessageEntity(type=VeGagram.enums.MessageEntityType.BLOCKQUOTE, offset=0, length=10),
         VeGagram.types.MessageEntity(type=VeGagram.enums.MessageEntityType.BLOCKQUOTE, offset=12, length=9)])

    assert Markdown.unparse(text=text, entities=entities) == expected


def test_markdown_unparse_mixed():
    expected = "**aaaaaaa__aaabbb**__~~dddddddd||ddeee~~||||eeeeeeefff||ffff`fffggggggg`ggghhhhhhhhhh"
    text = "aaaaaaaaaabbbddddddddddeeeeeeeeeeffffffffffgggggggggghhhhhhhhhh"
    entities = VeGagram.types.List(
        [VeGagram.types.MessageEntity(type=VeGagram.enums.MessageEntityType.BOLD, offset=0, length=13),
         VeGagram.types.MessageEntity(type=VeGagram.enums.MessageEntityType.ITALIC, offset=7, length=6),
         VeGagram.types.MessageEntity(type=VeGagram.enums.MessageEntityType.STRIKETHROUGH, offset=13, length=13),
         VeGagram.types.MessageEntity(type=VeGagram.enums.MessageEntityType.SPOILER, offset=21, length=5),
         VeGagram.types.MessageEntity(type=VeGagram.enums.MessageEntityType.SPOILER, offset=26, length=10),
         VeGagram.types.MessageEntity(type=VeGagram.enums.MessageEntityType.CODE, offset=40, length=10)])

    assert Markdown.unparse(text=text, entities=entities) == expected


def test_markdown_unparse_no_entities():
    expected = "text"
    text = "text"
    entities = []

    assert Markdown.unparse(text=text, entities=entities) == expected
