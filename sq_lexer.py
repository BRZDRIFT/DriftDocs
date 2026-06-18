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
    tokens = copy.deepcopy(CppLexer.tokens)

    tokens['root'] = [
        # 1) make #... a single-line comment
        (r'#.*?$', Comment.Single),

        # 2) treat // as an operator (must come BEFORE anything else that could match)
        (r'//', Operator),

        # 3) then include the rest of CppLexer rules EXCEPT the original // comment rule
        # we reuse everything else from original root except problematic entries
        *[
            rule for rule in CppLexer.tokens['root']
            if not (isinstance(rule[1], type(Comment.Single)) and rule[0].startswith(r'//'))
        ],
    ]

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
            'UnaryOp', 'Random', 'DynValType', 'AABR_int', 'AABR_float'
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
