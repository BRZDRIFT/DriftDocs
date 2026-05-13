from pygments.lexer import RegexLexer, bygroups
from pygments.token import Text, Keyword, Name, String, Number, Operator, Punctuation, Comment
from pygments.lexers._mapping import LEXERS
from markdown.extensions import Extension
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers.scripting import LuaLexer
import pprint
from pygments.token import *
from pygments.lexer import RegexLexer, inherit
from pygments.lexers.c_cpp import CppLexer
from pygments.token import Comment, Name, Keyword
from pygments.lexer import RegexLexer, include, bygroups, using, \
    this, inherit, default, words

__all__ = ['SquirrelLexer']

class SquirrelLexer(CppLexer):
    name = 'SquirrelLexer'
    aliases = ['squirrel', 'sq']
    filenames = ['*.nut', '*.sq']

    EXTRA_TYPES = ('table', 'string', 'Vec2', 'Vec3', 'Vec4',
            'AABR', 'BoundsCheck', 'function', 'void', 'local',
            'foreach', 'in', 'constructor', 'EventType', 'Event',
            'mixed', 'ComplexColor', 'ColorType'
    )

    def get_tokens_unprocessed(self, text, stack=('root',)):
        for index, token, value in \
                CppLexer.get_tokens_unprocessed(self, text, stack):
            if token is Name:
                if value in self.EXTRA_TYPES:
                    token = Keyword.Type
            yield index, token, value

class SquirrelExtension(Extension):
    def extendMarkdown(self, md):
        LEXERS["SquirrelLexer"] = (
            "sq_lexer",                         # module path to lexer
            "SquirrelLexer",                    # class name
            ("squirrel", "sq"),                 # aliases
            ("*.nut",),                         # file patterns
            ("text/x-squirrel",)                # MIME types
       )

def makeExtension(**kwargs):
    return SquirrelExtension(**kwargs)
