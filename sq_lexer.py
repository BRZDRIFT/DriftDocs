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
import copy

__all__ = ['SquirrelLexer']

class MyCppLexer(CppLexer):
    """
    C++-like lexer where `//` is a math operator and `#` is always a
    single-line comment.
    """
    name = 'C++ (math // , comment #)'
    aliases = ['cpp-math']
    filenames = []  # don't hijack *.cpp by default; opt in explicitly
    mimetypes = []
 
    # Re-use identifier regex already defined on the base class.
    _ident = CppLexer._ident
 
    tokens = {
        'whitespace': [
            # `#` -> always a single-line comment, anywhere it appears.
            # (Original lexer only special-cased '^#' for preprocessor
            # directives / #if 0 blocks -- that's all gone now.)
            (r'#.*', Comment.Single),
 
            # Keep the original "label:" detection (e.g. `done:` before a
            # goto target). Remove this block if you don't need it.
            (r'(^[ \t]*)'
             r'(?!(?:public|private|protected|default)\b)'
             r'(' + _ident + r')(\s*)(:)(?!:)',
             bygroups(Whitespace, Name.Label, Whitespace, Punctuation)),
 
            (r'\n', Whitespace),
            (r'[^\S\n]+', Whitespace),
            (r'\\\n', Whitespace),  # line continuation
 
            # NOTE: the original `//...\n` single-line-comment rule is
            # intentionally NOT included here. `//` is now handled as an
            # Operator token in the 'statements' state below.
 
            # /* ... */ multi-line comments still work as normal.
            (r'/(?:\\\n)?[*](?:[^*]|[*](?!(?:\\\n)?/))*[*](?:\\\n)?/',
             Comment.Multiline),
            # Unterminated /* comment running to EOF.
            (r'/(\\\n)?[*][\w\W]*', Comment.Multiline),
        ],
        'statements': [
            # Must come before the inherited single-char operator rule
            # (which would otherwise just match one `/` at a time).
            (r'//', Operator),
            inherit,
        ],
    
        }

class SquirrelLexer(MyCppLexer):
    name = 'SquirrelLexer'
    aliases = ['squirrel', 'sq']
    filenames = ['*.nut', '*.sq']

    EXTRA_TYPES = ('table', 'string', 'Vec2', 'Vec3', 'Vec4',
            'AABR', 'BoundsCheck', 'function', 'void', 'local',
            'foreach', 'in', 'constructor', 'EventType', 'Event',
            'mixed', 'ComplexColor', 'ColorType', 'Float2', 'Float3',
            'Float4', 'Int2', 'Int3', 'Int4', 'is', 'is_not', 'not_in',
            'AttackType', 'DeathCause', 'ExplosionEventType', 'EffectType',
            'CommandType', 'Unicode', 'GunShipState', 'Race', 'LocationProp',
            'DecalProp', 'UnitProp', 'PlayerProp', 'ForceProp', 'SimProp',
            'SecondaryTerrainTypeNormal', 'TerrainType', 'ArmorType',
            'DynVarType', 'ShapeType', 'VictoryStatus', 'SpecialForce',
            'SpecialPlayer', 'AutoAttackTable', 'AttackTable',
            'DamageExtraTable', 'Expr', 'DynValType ', 'BinaryOp',
            'UnaryOp', 'Random', 'DynValType', 'AABR_int', 'AABR_float',
            'array', 'delete', 'print'
    )

    def get_tokens_unprocessed(self, text, stack=('root',)):
        for index, token, value in \
                MyCppLexer.get_tokens_unprocessed(self, text, stack):
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
