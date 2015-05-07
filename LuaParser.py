# Generated from java-escape by ANTLR 4.5
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO
package = globals().get("__package__", None)
ischild = len(package)>0 if package is not None else False
if ischild:
    from .LuaListener import LuaListener
else:
    from LuaListener import LuaListener
def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3")
        buf.write(u"?\u018b\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t")
        buf.write(u"\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write(u"\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4")
        buf.write(u"\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30")
        buf.write(u"\t\30\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t")
        buf.write(u"\35\4\36\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\3\2")
        buf.write(u"\3\2\3\2\3\3\7\3K\n\3\f\3\16\3N\13\3\3\3\5\3Q\n\3\3\4")
        buf.write(u"\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write(u"\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write(u"\3\4\3\4\3\4\3\4\3\4\3\4\3\4\7\4u\n\4\f\4\16\4x\13\4")
        buf.write(u"\3\4\3\4\5\4|\n\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write(u"\3\4\5\4\u0088\n\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write(u"\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write(u"\4\3\4\3\4\5\4\u00a2\n\4\5\4\u00a4\n\4\3\5\3\5\5\5\u00a8")
        buf.write(u"\n\5\3\5\5\5\u00ab\n\5\3\6\3\6\3\6\3\6\3\7\3\7\3\7\7")
        buf.write(u"\7\u00b4\n\7\f\7\16\7\u00b7\13\7\3\7\3\7\5\7\u00bb\n")
        buf.write(u"\7\3\b\3\b\3\b\7\b\u00c0\n\b\f\b\16\b\u00c3\13\b\3\t")
        buf.write(u"\3\t\3\t\7\t\u00c8\n\t\f\t\16\t\u00cb\13\t\3\n\3\n\3")
        buf.write(u"\n\7\n\u00d0\n\n\f\n\16\n\u00d3\13\n\3\13\3\13\3\13\3")
        buf.write(u"\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\5\13")
        buf.write(u"\u00e2\n\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3")
        buf.write(u"\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write(u"\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\7\13\u0100")
        buf.write(u"\n\13\f\13\16\13\u0103\13\13\3\f\3\f\3\f\3\f\3\f\3\f")
        buf.write(u"\5\f\u010b\n\f\3\f\7\f\u010e\n\f\f\f\16\f\u0111\13\f")
        buf.write(u"\3\r\3\r\7\r\u0115\n\r\f\r\16\r\u0118\13\r\3\16\3\16")
        buf.write(u"\6\16\u011c\n\16\r\16\16\16\u011d\3\17\3\17\3\17\3\17")
        buf.write(u"\3\17\5\17\u0125\n\17\3\20\3\20\5\20\u0129\n\20\3\20")
        buf.write(u"\3\20\3\21\7\21\u012e\n\21\f\21\16\21\u0131\13\21\3\21")
        buf.write(u"\3\21\3\21\3\21\3\21\3\21\5\21\u0139\n\21\3\22\3\22\5")
        buf.write(u"\22\u013d\n\22\3\22\3\22\3\22\5\22\u0142\n\22\3\23\3")
        buf.write(u"\23\3\23\3\24\3\24\5\24\u0149\n\24\3\24\3\24\3\24\3\24")
        buf.write(u"\3\25\3\25\3\25\5\25\u0152\n\25\3\25\5\25\u0155\n\25")
        buf.write(u"\3\26\3\26\5\26\u0159\n\26\3\26\3\26\3\27\3\27\3\27\3")
        buf.write(u"\27\7\27\u0161\n\27\f\27\16\27\u0164\13\27\3\27\5\27")
        buf.write(u"\u0167\n\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3")
        buf.write(u"\30\3\30\5\30\u0173\n\30\3\31\3\31\3\32\3\32\3\33\3\33")
        buf.write(u"\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3 \3 \3!\3!")
        buf.write(u"\3\"\3\"\3#\3#\3#\2\3\24$\2\4\6\b\n\f\16\20\22\24\26")
        buf.write(u"\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BD\2\t\4\2\3\3")
        buf.write(u"\21\21\3\2%*\3\2,-\3\2.\60\4\2--\61\62\3\28;\3\2\65\67")
        buf.write(u"\u01a6\2F\3\2\2\2\4L\3\2\2\2\6\u00a3\3\2\2\2\b\u00a5")
        buf.write(u"\3\2\2\2\n\u00ac\3\2\2\2\f\u00b0\3\2\2\2\16\u00bc\3\2")
        buf.write(u"\2\2\20\u00c4\3\2\2\2\22\u00cc\3\2\2\2\24\u00e1\3\2\2")
        buf.write(u"\2\26\u010a\3\2\2\2\30\u0112\3\2\2\2\32\u0119\3\2\2\2")
        buf.write(u"\34\u0124\3\2\2\2\36\u0128\3\2\2\2 \u012f\3\2\2\2\"\u0141")
        buf.write(u"\3\2\2\2$\u0143\3\2\2\2&\u0146\3\2\2\2(\u0154\3\2\2\2")
        buf.write(u"*\u0156\3\2\2\2,\u015c\3\2\2\2.\u0172\3\2\2\2\60\u0174")
        buf.write(u"\3\2\2\2\62\u0176\3\2\2\2\64\u0178\3\2\2\2\66\u017a\3")
        buf.write(u"\2\2\28\u017c\3\2\2\2:\u017e\3\2\2\2<\u0180\3\2\2\2>")
        buf.write(u"\u0182\3\2\2\2@\u0184\3\2\2\2B\u0186\3\2\2\2D\u0188\3")
        buf.write(u"\2\2\2FG\5\4\3\2GH\7\2\2\3H\3\3\2\2\2IK\5\6\4\2JI\3\2")
        buf.write(u"\2\2KN\3\2\2\2LJ\3\2\2\2LM\3\2\2\2MP\3\2\2\2NL\3\2\2")
        buf.write(u"\2OQ\5\b\5\2PO\3\2\2\2PQ\3\2\2\2Q\5\3\2\2\2R\u00a4\7")
        buf.write(u"\3\2\2ST\5\16\b\2TU\7\4\2\2UV\5\22\n\2V\u00a4\3\2\2\2")
        buf.write(u"W\u00a4\5\32\16\2X\u00a4\5\n\6\2Y\u00a4\7\5\2\2Z[\7\6")
        buf.write(u"\2\2[\u00a4\7\64\2\2\\]\7\7\2\2]^\5\4\3\2^_\7\b\2\2_")
        buf.write(u"\u00a4\3\2\2\2`a\7\t\2\2ab\5\24\13\2bc\7\7\2\2cd\5\4")
        buf.write(u"\3\2de\7\b\2\2e\u00a4\3\2\2\2fg\7\n\2\2gh\5\4\3\2hi\7")
        buf.write(u"\13\2\2ij\5\24\13\2j\u00a4\3\2\2\2kl\7\f\2\2lm\5\24\13")
        buf.write(u"\2mn\7\r\2\2nv\5\4\3\2op\7\16\2\2pq\5\24\13\2qr\7\r\2")
        buf.write(u"\2rs\5\4\3\2su\3\2\2\2to\3\2\2\2ux\3\2\2\2vt\3\2\2\2")
        buf.write(u"vw\3\2\2\2w{\3\2\2\2xv\3\2\2\2yz\7\17\2\2z|\5\4\3\2{")
        buf.write(u"y\3\2\2\2{|\3\2\2\2|}\3\2\2\2}~\7\b\2\2~\u00a4\3\2\2")
        buf.write(u"\2\177\u0080\7\20\2\2\u0080\u0081\7\64\2\2\u0081\u0082")
        buf.write(u"\7\4\2\2\u0082\u0083\5\24\13\2\u0083\u0084\7\21\2\2\u0084")
        buf.write(u"\u0087\5\24\13\2\u0085\u0086\7\21\2\2\u0086\u0088\5\24")
        buf.write(u"\13\2\u0087\u0085\3\2\2\2\u0087\u0088\3\2\2\2\u0088\u0089")
        buf.write(u"\3\2\2\2\u0089\u008a\7\7\2\2\u008a\u008b\5\4\3\2\u008b")
        buf.write(u"\u008c\7\b\2\2\u008c\u00a4\3\2\2\2\u008d\u008e\7\20\2")
        buf.write(u"\2\u008e\u008f\5\20\t\2\u008f\u0090\7\22\2\2\u0090\u0091")
        buf.write(u"\5\22\n\2\u0091\u0092\7\7\2\2\u0092\u0093\5\4\3\2\u0093")
        buf.write(u"\u0094\7\b\2\2\u0094\u00a4\3\2\2\2\u0095\u0096\7\23\2")
        buf.write(u"\2\u0096\u0097\5\f\7\2\u0097\u0098\5&\24\2\u0098\u00a4")
        buf.write(u"\3\2\2\2\u0099\u009a\7\24\2\2\u009a\u009b\7\23\2\2\u009b")
        buf.write(u"\u009c\7\64\2\2\u009c\u00a4\5&\24\2\u009d\u009e\7\24")
        buf.write(u"\2\2\u009e\u00a1\5\20\t\2\u009f\u00a0\7\4\2\2\u00a0\u00a2")
        buf.write(u"\5\22\n\2\u00a1\u009f\3\2\2\2\u00a1\u00a2\3\2\2\2\u00a2")
        buf.write(u"\u00a4\3\2\2\2\u00a3R\3\2\2\2\u00a3S\3\2\2\2\u00a3W\3")
        buf.write(u"\2\2\2\u00a3X\3\2\2\2\u00a3Y\3\2\2\2\u00a3Z\3\2\2\2\u00a3")
        buf.write(u"\\\3\2\2\2\u00a3`\3\2\2\2\u00a3f\3\2\2\2\u00a3k\3\2\2")
        buf.write(u"\2\u00a3\177\3\2\2\2\u00a3\u008d\3\2\2\2\u00a3\u0095")
        buf.write(u"\3\2\2\2\u00a3\u0099\3\2\2\2\u00a3\u009d\3\2\2\2\u00a4")
        buf.write(u"\7\3\2\2\2\u00a5\u00a7\7\25\2\2\u00a6\u00a8\5\22\n\2")
        buf.write(u"\u00a7\u00a6\3\2\2\2\u00a7\u00a8\3\2\2\2\u00a8\u00aa")
        buf.write(u"\3\2\2\2\u00a9\u00ab\7\3\2\2\u00aa\u00a9\3\2\2\2\u00aa")
        buf.write(u"\u00ab\3\2\2\2\u00ab\t\3\2\2\2\u00ac\u00ad\7\26\2\2\u00ad")
        buf.write(u"\u00ae\7\64\2\2\u00ae\u00af\7\26\2\2\u00af\13\3\2\2\2")
        buf.write(u"\u00b0\u00b5\7\64\2\2\u00b1\u00b2\7\27\2\2\u00b2\u00b4")
        buf.write(u"\7\64\2\2\u00b3\u00b1\3\2\2\2\u00b4\u00b7\3\2\2\2\u00b5")
        buf.write(u"\u00b3\3\2\2\2\u00b5\u00b6\3\2\2\2\u00b6\u00ba\3\2\2")
        buf.write(u"\2\u00b7\u00b5\3\2\2\2\u00b8\u00b9\7\30\2\2\u00b9\u00bb")
        buf.write(u"\7\64\2\2\u00ba\u00b8\3\2\2\2\u00ba\u00bb\3\2\2\2\u00bb")
        buf.write(u"\r\3\2\2\2\u00bc\u00c1\5\26\f\2\u00bd\u00be\7\21\2\2")
        buf.write(u"\u00be\u00c0\5\26\f\2\u00bf\u00bd\3\2\2\2\u00c0\u00c3")
        buf.write(u"\3\2\2\2\u00c1\u00bf\3\2\2\2\u00c1\u00c2\3\2\2\2\u00c2")
        buf.write(u"\17\3\2\2\2\u00c3\u00c1\3\2\2\2\u00c4\u00c9\7\64\2\2")
        buf.write(u"\u00c5\u00c6\7\21\2\2\u00c6\u00c8\7\64\2\2\u00c7\u00c5")
        buf.write(u"\3\2\2\2\u00c8\u00cb\3\2\2\2\u00c9\u00c7\3\2\2\2\u00c9")
        buf.write(u"\u00ca\3\2\2\2\u00ca\21\3\2\2\2\u00cb\u00c9\3\2\2\2\u00cc")
        buf.write(u"\u00d1\5\24\13\2\u00cd\u00ce\7\21\2\2\u00ce\u00d0\5\24")
        buf.write(u"\13\2\u00cf\u00cd\3\2\2\2\u00d0\u00d3\3\2\2\2\u00d1\u00cf")
        buf.write(u"\3\2\2\2\u00d1\u00d2\3\2\2\2\u00d2\23\3\2\2\2\u00d3\u00d1")
        buf.write(u"\3\2\2\2\u00d4\u00d5\b\13\1\2\u00d5\u00d6\5> \2\u00d6")
        buf.write(u"\u00d7\5\24\13\t\u00d7\u00e2\3\2\2\2\u00d8\u00e2\7\31")
        buf.write(u"\2\2\u00d9\u00e2\7\32\2\2\u00da\u00e2\7\33\2\2\u00db")
        buf.write(u"\u00e2\5B\"\2\u00dc\u00e2\5D#\2\u00dd\u00e2\7\34\2\2")
        buf.write(u"\u00de\u00e2\5$\23\2\u00df\u00e2\5\30\r\2\u00e0\u00e2")
        buf.write(u"\5*\26\2\u00e1\u00d4\3\2\2\2\u00e1\u00d8\3\2\2\2\u00e1")
        buf.write(u"\u00d9\3\2\2\2\u00e1\u00da\3\2\2\2\u00e1\u00db\3\2\2")
        buf.write(u"\2\u00e1\u00dc\3\2\2\2\u00e1\u00dd\3\2\2\2\u00e1\u00de")
        buf.write(u"\3\2\2\2\u00e1\u00df\3\2\2\2\u00e1\u00e0\3\2\2\2\u00e2")
        buf.write(u"\u0101\3\2\2\2\u00e3\u00e4\f\n\2\2\u00e4\u00e5\5@!\2")
        buf.write(u"\u00e5\u00e6\5\24\13\n\u00e6\u0100\3\2\2\2\u00e7\u00e8")
        buf.write(u"\f\b\2\2\u00e8\u00e9\5<\37\2\u00e9\u00ea\5\24\13\t\u00ea")
        buf.write(u"\u0100\3\2\2\2\u00eb\u00ec\f\7\2\2\u00ec\u00ed\5:\36")
        buf.write(u"\2\u00ed\u00ee\5\24\13\b\u00ee\u0100\3\2\2\2\u00ef\u00f0")
        buf.write(u"\f\6\2\2\u00f0\u00f1\58\35\2\u00f1\u00f2\5\24\13\6\u00f2")
        buf.write(u"\u0100\3\2\2\2\u00f3\u00f4\f\5\2\2\u00f4\u00f5\5\66\34")
        buf.write(u"\2\u00f5\u00f6\5\24\13\6\u00f6\u0100\3\2\2\2\u00f7\u00f8")
        buf.write(u"\f\4\2\2\u00f8\u00f9\5\64\33\2\u00f9\u00fa\5\24\13\5")
        buf.write(u"\u00fa\u0100\3\2\2\2\u00fb\u00fc\f\3\2\2\u00fc\u00fd")
        buf.write(u"\5\62\32\2\u00fd\u00fe\5\24\13\4\u00fe\u0100\3\2\2\2")
        buf.write(u"\u00ff\u00e3\3\2\2\2\u00ff\u00e7\3\2\2\2\u00ff\u00eb")
        buf.write(u"\3\2\2\2\u00ff\u00ef\3\2\2\2\u00ff\u00f3\3\2\2\2\u00ff")
        buf.write(u"\u00f7\3\2\2\2\u00ff\u00fb\3\2\2\2\u0100\u0103\3\2\2")
        buf.write(u"\2\u0101\u00ff\3\2\2\2\u0101\u0102\3\2\2\2\u0102\25\3")
        buf.write(u"\2\2\2\u0103\u0101\3\2\2\2\u0104\u010b\7\64\2\2\u0105")
        buf.write(u"\u0106\7\35\2\2\u0106\u0107\5\24\13\2\u0107\u0108\7\36")
        buf.write(u"\2\2\u0108\u0109\5 \21\2\u0109\u010b\3\2\2\2\u010a\u0104")
        buf.write(u"\3\2\2\2\u010a\u0105\3\2\2\2\u010b\u010f\3\2\2\2\u010c")
        buf.write(u"\u010e\5 \21\2\u010d\u010c\3\2\2\2\u010e\u0111\3\2\2")
        buf.write(u"\2\u010f\u010d\3\2\2\2\u010f\u0110\3\2\2\2\u0110\27\3")
        buf.write(u"\2\2\2\u0111\u010f\3\2\2\2\u0112\u0116\5\34\17\2\u0113")
        buf.write(u"\u0115\5\36\20\2\u0114\u0113\3\2\2\2\u0115\u0118\3\2")
        buf.write(u"\2\2\u0116\u0114\3\2\2\2\u0116\u0117\3\2\2\2\u0117\31")
        buf.write(u"\3\2\2\2\u0118\u0116\3\2\2\2\u0119\u011b\5\34\17\2\u011a")
        buf.write(u"\u011c\5\36\20\2\u011b\u011a\3\2\2\2\u011c\u011d\3\2")
        buf.write(u"\2\2\u011d\u011b\3\2\2\2\u011d\u011e\3\2\2\2\u011e\33")
        buf.write(u"\3\2\2\2\u011f\u0125\5\26\f\2\u0120\u0121\7\35\2\2\u0121")
        buf.write(u"\u0122\5\24\13\2\u0122\u0123\7\36\2\2\u0123\u0125\3\2")
        buf.write(u"\2\2\u0124\u011f\3\2\2\2\u0124\u0120\3\2\2\2\u0125\35")
        buf.write(u"\3\2\2\2\u0126\u0127\7\30\2\2\u0127\u0129\7\64\2\2\u0128")
        buf.write(u"\u0126\3\2\2\2\u0128\u0129\3\2\2\2\u0129\u012a\3\2\2")
        buf.write(u"\2\u012a\u012b\5\"\22\2\u012b\37\3\2\2\2\u012c\u012e")
        buf.write(u"\5\36\20\2\u012d\u012c\3\2\2\2\u012e\u0131\3\2\2\2\u012f")
        buf.write(u"\u012d\3\2\2\2\u012f\u0130\3\2\2\2\u0130\u0138\3\2\2")
        buf.write(u"\2\u0131\u012f\3\2\2\2\u0132\u0133\7\37\2\2\u0133\u0134")
        buf.write(u"\5\24\13\2\u0134\u0135\7 \2\2\u0135\u0139\3\2\2\2\u0136")
        buf.write(u"\u0137\7\27\2\2\u0137\u0139\7\64\2\2\u0138\u0132\3\2")
        buf.write(u"\2\2\u0138\u0136\3\2\2\2\u0139!\3\2\2\2\u013a\u013c\7")
        buf.write(u"\35\2\2\u013b\u013d\5\22\n\2\u013c\u013b\3\2\2\2\u013c")
        buf.write(u"\u013d\3\2\2\2\u013d\u013e\3\2\2\2\u013e\u0142\7\36\2")
        buf.write(u"\2\u013f\u0142\5*\26\2\u0140\u0142\5D#\2\u0141\u013a")
        buf.write(u"\3\2\2\2\u0141\u013f\3\2\2\2\u0141\u0140\3\2\2\2\u0142")
        buf.write(u"#\3\2\2\2\u0143\u0144\7\23\2\2\u0144\u0145\5&\24\2\u0145")
        buf.write(u"%\3\2\2\2\u0146\u0148\7\35\2\2\u0147\u0149\5(\25\2\u0148")
        buf.write(u"\u0147\3\2\2\2\u0148\u0149\3\2\2\2\u0149\u014a\3\2\2")
        buf.write(u"\2\u014a\u014b\7\36\2\2\u014b\u014c\5\4\3\2\u014c\u014d")
        buf.write(u"\7\b\2\2\u014d\'\3\2\2\2\u014e\u0151\5\20\t\2\u014f\u0150")
        buf.write(u"\7\21\2\2\u0150\u0152\7\34\2\2\u0151\u014f\3\2\2\2\u0151")
        buf.write(u"\u0152\3\2\2\2\u0152\u0155\3\2\2\2\u0153\u0155\7\34\2")
        buf.write(u"\2\u0154\u014e\3\2\2\2\u0154\u0153\3\2\2\2\u0155)\3\2")
        buf.write(u"\2\2\u0156\u0158\7!\2\2\u0157\u0159\5,\27\2\u0158\u0157")
        buf.write(u"\3\2\2\2\u0158\u0159\3\2\2\2\u0159\u015a\3\2\2\2\u015a")
        buf.write(u"\u015b\7\"\2\2\u015b+\3\2\2\2\u015c\u0162\5.\30\2\u015d")
        buf.write(u"\u015e\5\60\31\2\u015e\u015f\5.\30\2\u015f\u0161\3\2")
        buf.write(u"\2\2\u0160\u015d\3\2\2\2\u0161\u0164\3\2\2\2\u0162\u0160")
        buf.write(u"\3\2\2\2\u0162\u0163\3\2\2\2\u0163\u0166\3\2\2\2\u0164")
        buf.write(u"\u0162\3\2\2\2\u0165\u0167\5\60\31\2\u0166\u0165\3\2")
        buf.write(u"\2\2\u0166\u0167\3\2\2\2\u0167-\3\2\2\2\u0168\u0169\7")
        buf.write(u"\37\2\2\u0169\u016a\5\24\13\2\u016a\u016b\7 \2\2\u016b")
        buf.write(u"\u016c\7\4\2\2\u016c\u016d\5\24\13\2\u016d\u0173\3\2")
        buf.write(u"\2\2\u016e\u016f\7\64\2\2\u016f\u0170\7\4\2\2\u0170\u0173")
        buf.write(u"\5\24\13\2\u0171\u0173\5\24\13\2\u0172\u0168\3\2\2\2")
        buf.write(u"\u0172\u016e\3\2\2\2\u0172\u0171\3\2\2\2\u0173/\3\2\2")
        buf.write(u"\2\u0174\u0175\t\2\2\2\u0175\61\3\2\2\2\u0176\u0177\7")
        buf.write(u"#\2\2\u0177\63\3\2\2\2\u0178\u0179\7$\2\2\u0179\65\3")
        buf.write(u"\2\2\2\u017a\u017b\t\3\2\2\u017b\67\3\2\2\2\u017c\u017d")
        buf.write(u"\7+\2\2\u017d9\3\2\2\2\u017e\u017f\t\4\2\2\u017f;\3\2")
        buf.write(u"\2\2\u0180\u0181\t\5\2\2\u0181=\3\2\2\2\u0182\u0183\t")
        buf.write(u"\6\2\2\u0183?\3\2\2\2\u0184\u0185\7\63\2\2\u0185A\3\2")
        buf.write(u"\2\2\u0186\u0187\t\7\2\2\u0187C\3\2\2\2\u0188\u0189\t")
        buf.write(u"\b\2\2\u0189E\3\2\2\2$LPv{\u0087\u00a1\u00a3\u00a7\u00aa")
        buf.write(u"\u00b5\u00ba\u00c1\u00c9\u00d1\u00e1\u00ff\u0101\u010a")
        buf.write(u"\u010f\u0116\u011d\u0124\u0128\u012f\u0138\u013c\u0141")
        buf.write(u"\u0148\u0151\u0154\u0158\u0162\u0166\u0172")
        return buf.getvalue()


class LuaParser ( Parser ):

    grammarFileName = "java-escape"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"';'", u"'='", u"'break'", u"'goto'", 
                     u"'do'", u"'end'", u"'while'", u"'repeat'", u"'until'", 
                     u"'if'", u"'then'", u"'elseif'", u"'else'", u"'for'", 
                     u"','", u"'in'", u"'function'", u"'local'", u"'return'", 
                     u"'::'", u"'.'", u"':'", u"'nil'", u"'false'", u"'true'", 
                     u"'...'", u"'('", u"')'", u"'['", u"']'", u"'{'", u"'}'", 
                     u"'or'", u"'and'", u"'<'", u"'>'", u"'<='", u"'>='", 
                     u"'~='", u"'=='", u"'..'", u"'+'", u"'-'", u"'*'", 
                     u"'/'", u"'%'", u"'not'", u"'#'", u"'^'" ]

    symbolicNames = [ u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"NAME", u"NORMALSTRING", 
                      u"CHARSTRING", u"LONGSTRING", u"INT", u"HEX", u"FLOAT", 
                      u"HEX_FLOAT", u"COMMENT", u"LINE_COMMENT", u"WS", 
                      u"SHEBANG" ]

    RULE_chunk = 0
    RULE_block = 1
    RULE_stat = 2
    RULE_retstat = 3
    RULE_label = 4
    RULE_funcname = 5
    RULE_varlist = 6
    RULE_namelist = 7
    RULE_explist = 8
    RULE_exp = 9
    RULE_var = 10
    RULE_prefixexp = 11
    RULE_functioncall = 12
    RULE_varOrExp = 13
    RULE_nameAndArgs = 14
    RULE_varSuffix = 15
    RULE_args = 16
    RULE_functiondef = 17
    RULE_funcbody = 18
    RULE_parlist = 19
    RULE_tableconstructor = 20
    RULE_fieldlist = 21
    RULE_field = 22
    RULE_fieldsep = 23
    RULE_operatorOr = 24
    RULE_operatorAnd = 25
    RULE_operatorComparison = 26
    RULE_operatorStrcat = 27
    RULE_operatorAddSub = 28
    RULE_operatorMulDivMod = 29
    RULE_operatorUnary = 30
    RULE_operatorPower = 31
    RULE_number = 32
    RULE_string = 33

    ruleNames =  [ u"chunk", u"block", u"stat", u"retstat", u"label", u"funcname", 
                   u"varlist", u"namelist", u"explist", u"exp", u"var", 
                   u"prefixexp", u"functioncall", u"varOrExp", u"nameAndArgs", 
                   u"varSuffix", u"args", u"functiondef", u"funcbody", u"parlist", 
                   u"tableconstructor", u"fieldlist", u"field", u"fieldsep", 
                   u"operatorOr", u"operatorAnd", u"operatorComparison", 
                   u"operatorStrcat", u"operatorAddSub", u"operatorMulDivMod", 
                   u"operatorUnary", u"operatorPower", u"number", u"string" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    T__32=33
    T__33=34
    T__34=35
    T__35=36
    T__36=37
    T__37=38
    T__38=39
    T__39=40
    T__40=41
    T__41=42
    T__42=43
    T__43=44
    T__44=45
    T__45=46
    T__46=47
    T__47=48
    T__48=49
    NAME=50
    NORMALSTRING=51
    CHARSTRING=52
    LONGSTRING=53
    INT=54
    HEX=55
    FLOAT=56
    HEX_FLOAT=57
    COMMENT=58
    LINE_COMMENT=59
    WS=60
    SHEBANG=61

    def __init__(self, input):
        super(LuaParser, self).__init__(input)
        self.checkVersion("4.5")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ChunkContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LuaParser.ChunkContext, self).__init__(parent, invokingState)
            self.parser = parser

        def block(self):
            return self.getTypedRuleContext(LuaParser.BlockContext,0)


        def EOF(self):
            return self.getToken(LuaParser.EOF, 0)

        def getRuleIndex(self):
            return LuaParser.RULE_chunk

        def enterRule(self, listener):
            if isinstance( listener, LuaListener ):
                listener.enterChunk(self)

        def exitRule(self, listener):
            if isinstance( listener, LuaListener ):
                listener.exitChunk(self)




    def chunk(self):

        localctx = LuaParser.ChunkContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_chunk)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.block()
            self.state = 69
            self.match(LuaParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BlockContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LuaParser.BlockContext, self).__init__(parent, invokingState)
            self.parser = parser

        def stat(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(LuaParser.StatContext)
            else:
                return self.getTypedRuleContext(LuaParser.StatContext,i)


        def retstat(self):
            return self.getTypedRuleContext(LuaParser.RetstatContext,0)


        def getRuleIndex(self):
            return LuaParser.RULE_block

        def enterRule(self, listener):
            if isinstance( listener, LuaListener ):
                listener.enterBlock(self)

        def exitRule(self, listener):
            if isinstance( listener, LuaListener ):
                listener.exitBlock(self)




    def block(self):

        localctx = LuaParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LuaParser.T__0) | (1 << LuaParser.T__2) | (1 << LuaParser.T__3) | (1 << LuaParser.T__4) | (1 << LuaParser.T__6) | (1 << LuaParser.T__7) | (1 << LuaParser.T__9) | (1 << LuaParser.T__13) | (1 << LuaParser.T__16) | (1 << LuaParser.T__17) | (1 << LuaParser.T__19) | (1 << LuaParser.T__26) | (1 << LuaParser.NAME))) != 0):
                self.state = 71
                self.stat()
                self.state = 76
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 78
            _la = self._input.LA(1)
            if _la==LuaParser.T__18:
                self.state = 77
                self.retstat()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StatContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LuaParser.StatContext, self).__init__(parent, invokingState)
            self.parser = parser

        def varlist(self):
            return self.getTypedRuleContext(LuaParser.VarlistContext,0)


        def explist(self):
            return self.getTypedRuleContext(LuaParser.ExplistContext,0)


        def functioncall(self):
            return self.getTypedRuleContext(LuaParser.FunctioncallContext,0)


        def label(self):
            return self.getTypedRuleContext(LuaParser.LabelContext,0)


        def NAME(self):
            return self.getToken(LuaParser.NAME, 0)

        def block(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(LuaParser.BlockContext)
            else:
                return self.getTypedRuleContext(LuaParser.BlockContext,i)


        def exp(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(LuaParser.ExpContext)
            else:
                return self.getTypedRuleContext(LuaParser.ExpContext,i)


        def namelist(self):
            return self.getTypedRuleContext(LuaParser.NamelistContext,0)


        def funcname(self):
            return self.getTypedRuleContext(LuaParser.FuncnameContext,0)


        def funcbody(self):
            return self.getTypedRuleContext(LuaParser.FuncbodyContext,0)


        def getRuleIndex(self):
            return LuaParser.RULE_stat

        def enterRule(self, listener):
            if isinstance( listener, LuaListener ):
                listener.enterStat(self)

        def exitRule(self, listener):
            if isinstance( listener, LuaListener ):
                listener.exitStat(self)




    def stat(self):

        localctx = LuaParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_stat)
        self._la = 0 # Token type
        try:
            self.state = 161
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 80
                self.match(LuaParser.T__0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 81
                self.varlist()
                self.state = 82
                self.match(LuaParser.T__1)
                self.state = 83
                self.explist()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 85
                self.functioncall()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 86
                self.label()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 87
                self.match(LuaParser.T__2)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 88
                self.match(LuaParser.T__3)
                self.state = 89
                self.match(LuaParser.NAME)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 90
                self.match(LuaParser.T__4)
                self.state = 91
                self.block()
                self.state = 92
                self.match(LuaParser.T__5)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 94
                self.match(LuaParser.T__6)
                self.state = 95
                self.exp(0)
                self.state = 96
                self.match(LuaParser.T__4)
                self.state = 97
                self.block()
                self.state = 98
                self.match(LuaParser.T__5)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 100
                self.match(LuaParser.T__7)
                self.state = 101
                self.block()
                self.state = 102
                self.match(LuaParser.T__8)
                self.state = 103
                self.exp(0)
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 105
                self.match(LuaParser.T__9)
                self.state = 106
                self.exp(0)
                self.state = 107
                self.match(LuaParser.T__10)
                self.state = 108
                self.block()
                self.state = 116
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==LuaParser.T__11:
                    self.state = 109
                    self.match(LuaParser.T__11)
                    self.state = 110
                    self.exp(0)
                    self.state = 111
                    self.match(LuaParser.T__10)
                    self.state = 112
                    self.block()
                    self.state = 118
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 121
                _la = self._input.LA(1)
                if _la==LuaParser.T__12:
                    self.state = 119
                    self.match(LuaParser.T__12)
                    self.state = 120
                    self.block()


                self.state = 123
                self.match(LuaParser.T__5)
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 125
                self.match(LuaParser.T__13)
                self.state = 126
                self.match(LuaParser.NAME)
                self.state = 127
                self.match(LuaParser.T__1)
                self.state = 128
                self.exp(0)
                self.state = 129
                self.match(LuaParser.T__14)
                self.state = 130
                self.exp(0)
                self.state = 133
                _la = self._input.LA(1)
                if _la==LuaParser.T__14:
                    self.state = 131
                    self.match(LuaParser.T__14)
                    self.state = 132
                    self.exp(0)


                self.state = 135
                self.match(LuaParser.T__4)
                self.state = 136
                self.block()
                self.state = 137
                self.match(LuaParser.T__5)
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 139
                self.match(LuaParser.T__13)
                self.state = 140
                self.namelist()
                self.state = 141
                self.match(LuaParser.T__15)
                self.state = 142
                self.explist()
                self.state = 143
                self.match(LuaParser.T__4)
                self.state = 144
                self.block()
                self.state = 145
                self.match(LuaParser.T__5)
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 147
                self.match(LuaParser.T__16)
                self.state = 148
                self.funcname()
                self.state = 149
                self.funcbody()
                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 151
                self.match(LuaParser.T__17)
                self.state = 152
                self.match(LuaParser.T__16)
                self.state = 153
                self.match(LuaParser.NAME)
                self.state = 154
                self.funcbody()
                pass

            elif la_ == 15:
                self.enterOuterAlt(localctx, 15)
                self.state = 155
                self.match(LuaParser.T__17)
                self.state = 156
                self.namelist()
                self.state = 159
                _la = self._input.LA(1)
                if _la==LuaParser.T__1:
                    self.state = 157
                    self.match(LuaParser.T__1)
                    self.state = 158
                    self.explist()


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RetstatContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LuaParser.RetstatContext, self).__init__(parent, invokingState)
            self.parser = parser

        def explist(self):
            return self.getTypedRuleContext(LuaParser.ExplistContext,0)


        def getRuleIndex(self):
            return LuaParser.RULE_retstat

        def enterRule(self, listener):
            if isinstance( listener, LuaListener ):
                listener.enterRetstat(self)

        def exitRule(self, listener):
            if isinstance( listener, LuaListener ):
                listener.exitRetstat(self)




    def retstat(self):

        localctx = LuaParser.RetstatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_retstat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            self.match(LuaParser.T__18)
            self.state = 165
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LuaParser.T__16) | (1 << LuaParser.T__22) | (1 << LuaParser.T__23) | (1 << LuaParser.T__24) | (1 << LuaParser.T__25) | (1 << LuaParser.T__26) | (1 << LuaParser.T__30) | (1 << LuaParser.T__42) | (1 << LuaParser.T__46) | (1 << LuaParser.T__47) | (1 << LuaParser.NAME) | (1 << LuaParser.NORMALSTRING) | (1 << LuaParser.CHARSTRING) | (1 << LuaParser.LONGSTRING) | (1 << LuaParser.INT) | (1 << LuaParser.HEX) | (1 << LuaParser.FLOAT) | (1 << LuaParser.HEX_FLOAT))) != 0):
                self.state = 164
                self.explist()


            self.state = 168
            _la = self._input.LA(1)
            if _la==LuaParser.T__0:
                self.state = 167
                self.match(LuaParser.T__0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LabelContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LuaParser.LabelContext, self).__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(LuaParser.NAME, 0)

        def getRuleIndex(self):
            return LuaParser.RULE_label

        def enterRule(self, listener):
            if isinstance( listener, LuaListener ):
                listener.enterLabel(self)

        def exitRule(self, listener):
            if isinstance( listener, LuaListener ):
                listener.exitLabel(self)




    def label(self):

        localctx = LuaParser.LabelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_label)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            self.match(LuaParser.T__19)
            self.state = 171
            self.match(LuaParser.NAME)
            self.state = 172
            self.match(LuaParser.T__19)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FuncnameContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LuaParser.FuncnameContext, self).__init__(parent, invokingState)
            self.parser = parser

        def NAME(self, i=None):
            if i is None:
                return self.getTokens(LuaParser.NAME)
            else:
                return self.getToken(LuaParser.NAME, i)

        def getRuleIndex(self):
            return LuaParser.RULE_funcname

        def enterRule(self, listener):
            if isinstance( listener, LuaListener ):
                listener.enterFuncname(self)

        def exitRule(self, listener):
            if isinstance( listener, LuaListener ):
                listener.exitFuncname(self)




    def funcname(self):

        localctx = LuaParser.FuncnameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_funcname)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self.match(LuaParser.NAME)
            self.state = 179
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LuaParser.T__20:
                self.state = 175
                self.match(LuaParser.T__20)
                self.state = 176
                self.match(LuaParser.NAME)
                self.state = 181
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 184
            _la = self._input.LA(1)
            if _la==LuaParser.T__21:
                self.state = 182
                self.match(LuaParser.T__21)
                self.state = 183
                self.match(LuaParser.NAME)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VarlistContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LuaParser.VarlistContext, self).__init__(parent, invokingState)
            self.parser = parser

        def var(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(LuaParser.VarContext)
            else:
                return self.getTypedRuleContext(LuaParser.VarContext,i)


        def getRuleIndex(self):
            return LuaParser.RULE_varlist

        def enterRule(self, listener):
            if isinstance( listener, LuaListener ):
                listener.enterVarlist(self)

        def exitRule(self, listener):
            if isinstance( listener, LuaListener ):
                listener.exitVarlist(self)




    def varlist(self):

        localctx = LuaParser.VarlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_varlist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            self.var()
            self.state = 191
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LuaParser.T__14:
                self.state = 187
                self.match(LuaParser.T__14)
                self.state = 188
                self.var()
                self.state = 193
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NamelistContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LuaParser.NamelistContext, self).__init__(parent, invokingState)
            self.parser = parser

        def NAME(self, i=None):
            if i is None:
                return self.getTokens(LuaParser.NAME)
            else:
                return self.getToken(LuaParser.NAME, i)

        def getRuleIndex(self):
            return LuaParser.RULE_namelist

        def enterRule(self, listener):
            if isinstance( listener, LuaListener ):
                listener.enterNamelist(self)

        def exitRule(self, listener):
            if isinstance( listener, LuaListener ):
                listener.exitNamelist(self)




    def namelist(self):

        localctx = LuaParser.NamelistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_namelist)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            self.match(LuaParser.NAME)
            self.state = 199
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 195
                    self.match(LuaParser.T__14)
                    self.state = 196
                    self.match(LuaParser.NAME) 
                self.state = 201
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExplistContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LuaParser.ExplistContext, self).__init__(parent, invokingState)
            self.parser = parser

        def exp(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(LuaParser.ExpContext)
            else:
                return self.getTypedRuleContext(LuaParser.ExpContext,i)


        def getRuleIndex(self):
            return LuaParser.RULE_explist

        def enterRule(self, listener):
            if isinstance( listener, LuaListener ):
                listener.enterExplist(self)

        def exitRule(self, listener):
            if isinstance( listener, LuaListener ):
                listener.exitExplist(self)




    def explist(self):

        localctx = LuaParser.ExplistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_explist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 202
            self.exp(0)
            self.state = 207
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LuaParser.T__14:
                self.state = 203
                self.match(LuaParser.T__14)
                self.state = 204
                self.exp(0)
                self.state = 209
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExpContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LuaParser.ExpContext, self).__init__(parent, invokingState)
            self.parser = parser

        def operatorUnary(self):
            return self.getTypedRuleContext(LuaParser.OperatorUnaryContext,0)


        def exp(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(LuaParser.ExpContext)
            else:
                return self.getTypedRuleContext(LuaParser.ExpContext,i)


        def number(self):
            return self.getTypedRuleContext(LuaParser.NumberContext,0)


        def string(self):
            return self.getTypedRuleContext(LuaParser.StringContext,0)


        def functiondef(self):
            return self.getTypedRuleContext(LuaParser.FunctiondefContext,0)


        def prefixexp(self):
            return self.getTypedRuleContext(LuaParser.PrefixexpContext,0)


        def tableconstructor(self):
            return self.getTypedRuleContext(LuaParser.TableconstructorContext,0)


        def operatorPower(self):
            return self.getTypedRuleContext(LuaParser.OperatorPowerContext,0)


        def operatorMulDivMod(self):
            return self.getTypedRuleContext(LuaParser.OperatorMulDivModContext,0)


        def operatorAddSub(self):
            return self.getTypedRuleContext(LuaParser.OperatorAddSubContext,0)


        def operatorStrcat(self):
            return self.getTypedRuleContext(LuaParser.OperatorStrcatContext,0)


        def operatorComparison(self):
            return self.getTypedRuleContext(LuaParser.OperatorComparisonContext,0)


        def operatorAnd(self):
            return self.getTypedRuleContext(LuaParser.OperatorAndContext,0)


        def operatorOr(self):
            return self.getTypedRuleContext(LuaParser.OperatorOrContext,0)


        def getRuleIndex(self):
            return LuaParser.RULE_exp

        def enterRule(self, listener):
            if isinstance( listener, LuaListener ):
                listener.enterExp(self)

        def exitRule(self, listener):
            if isinstance( listener, LuaListener ):
                listener.exitExp(self)



    def exp(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = LuaParser.ExpContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 18
        self.enterRecursionRule(localctx, 18, self.RULE_exp, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 223
            token = self._input.LA(1)
            if token in [LuaParser.T__42, LuaParser.T__46, LuaParser.T__47]:
                self.state = 211
                self.operatorUnary()
                self.state = 212
                self.exp(7)

            elif token in [LuaParser.T__22]:
                self.state = 214
                self.match(LuaParser.T__22)

            elif token in [LuaParser.T__23]:
                self.state = 215
                self.match(LuaParser.T__23)

            elif token in [LuaParser.T__24]:
                self.state = 216
                self.match(LuaParser.T__24)

            elif token in [LuaParser.INT, LuaParser.HEX, LuaParser.FLOAT, LuaParser.HEX_FLOAT]:
                self.state = 217
                self.number()

            elif token in [LuaParser.NORMALSTRING, LuaParser.CHARSTRING, LuaParser.LONGSTRING]:
                self.state = 218
                self.string()

            elif token in [LuaParser.T__25]:
                self.state = 219
                self.match(LuaParser.T__25)

            elif token in [LuaParser.T__16]:
                self.state = 220
                self.functiondef()

            elif token in [LuaParser.T__26, LuaParser.NAME]:
                self.state = 221
                self.prefixexp()

            elif token in [LuaParser.T__30]:
                self.state = 222
                self.tableconstructor()

            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 255
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 253
                    la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
                    if la_ == 1:
                        localctx = LuaParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 225
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 226
                        self.operatorPower()
                        self.state = 227
                        self.exp(8)
                        pass

                    elif la_ == 2:
                        localctx = LuaParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 229
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 230
                        self.operatorMulDivMod()
                        self.state = 231
                        self.exp(7)
                        pass

                    elif la_ == 3:
                        localctx = LuaParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 233
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 234
                        self.operatorAddSub()
                        self.state = 235
                        self.exp(6)
                        pass

                    elif la_ == 4:
                        localctx = LuaParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 237
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 238
                        self.operatorStrcat()
                        self.state = 239
                        self.exp(4)
                        pass

                    elif la_ == 5:
                        localctx = LuaParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 241
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 242
                        self.operatorComparison()
                        self.state = 243
                        self.exp(4)
                        pass

                    elif la_ == 6:
                        localctx = LuaParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 245
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 246
                        self.operatorAnd()
                        self.state = 247
                        self.exp(3)
                        pass

                    elif la_ == 7:
                        localctx = LuaParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 249
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 250
                        self.operatorOr()
                        self.state = 251
                        self.exp(2)
                        pass

             
                self.state = 257
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class VarContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LuaParser.VarContext, self).__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(LuaParser.NAME, 0)

        def exp(self):
            return self.getTypedRuleContext(LuaParser.ExpContext,0)


        def varSuffix(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(LuaParser.VarSuffixContext)
            else:
                return self.getTypedRuleContext(LuaParser.VarSuffixContext,i)


        def getRuleIndex(self):
            return LuaParser.RULE_var

        def enterRule(self, listener):
            if isinstance( listener, LuaListener ):
                listener.enterVar(self)

        def exitRule(self, listener):
            if isinstance( listener, LuaListener ):
                listener.exitVar(self)




    def var(self):

        localctx = LuaParser.VarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 264
            token = self._input.LA(1)
            if token in [LuaParser.NAME]:
                self.state = 258
                self.match(LuaParser.NAME)

            elif token in [LuaParser.T__26]:
                self.state = 259
                self.match(LuaParser.T__26)
                self.state = 260
                self.exp(0)
                self.state = 261
                self.match(LuaParser.T__27)
                self.state = 262
                self.varSuffix()

            else:
                raise NoViableAltException(self)

            self.state = 269
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 266
                    self.varSuffix() 
                self.state = 271
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PrefixexpContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LuaParser.PrefixexpContext, self).__init__(parent, invokingState)
            self.parser = parser

        def varOrExp(self):
            return self.getTypedRuleContext(LuaParser.VarOrExpContext,0)


        def nameAndArgs(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(LuaParser.NameAndArgsContext)
            else:
                return self.getTypedRuleContext(LuaParser.NameAndArgsContext,i)


        def getRuleIndex(self):
            return LuaParser.RULE_prefixexp

        def enterRule(self, listener):
            if isinstance( listener, LuaListener ):
                listener.enterPrefixexp(self)

        def exitRule(self, listener):
            if isinstance( listener, LuaListener ):
                listener.exitPrefixexp(self)




    def prefixexp(self):

        localctx = LuaParser.PrefixexpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_prefixexp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            self.varOrExp()
            self.state = 276
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 273
                    self.nameAndArgs() 
                self.state = 278
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FunctioncallContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LuaParser.FunctioncallContext, self).__init__(parent, invokingState)
            self.parser = parser

        def varOrExp(self):
            return self.getTypedRuleContext(LuaParser.VarOrExpContext,0)


        def nameAndArgs(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(LuaParser.NameAndArgsContext)
            else:
                return self.getTypedRuleContext(LuaParser.NameAndArgsContext,i)


        def getRuleIndex(self):
            return LuaParser.RULE_functioncall

        def enterRule(self, listener):
            if isinstance( listener, LuaListener ):
                listener.enterFunctioncall(self)

        def exitRule(self, listener):
            if isinstance( listener, LuaListener ):
                listener.exitFunctioncall(self)




    def functioncall(self):

        localctx = LuaParser.FunctioncallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_functioncall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 279
            self.varOrExp()
            self.state = 281 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 280
                    self.nameAndArgs()

                else:
                    raise NoViableAltException(self)
                self.state = 283 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VarOrExpContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LuaParser.VarOrExpContext, self).__init__(parent, invokingState)
            self.parser = parser

        def var(self):
            return self.getTypedRuleContext(LuaParser.VarContext,0)


        def exp(self):
            return self.getTypedRuleContext(LuaParser.ExpContext,0)


        def getRuleIndex(self):
            return LuaParser.RULE_varOrExp

        def enterRule(self, listener):
            if isinstance( listener, LuaListener ):
                listener.enterVarOrExp(self)

        def exitRule(self, listener):
            if isinstance( listener, LuaListener ):
                listener.exitVarOrExp(self)




    def varOrExp(self):

        localctx = LuaParser.VarOrExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_varOrExp)
        try:
            self.state = 290
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 285
                self.var()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 286
                self.match(LuaParser.T__26)
                self.state = 287
                self.exp(0)
                self.state = 288
                self.match(LuaParser.T__27)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NameAndArgsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LuaParser.NameAndArgsContext, self).__init__(parent, invokingState)
            self.parser = parser

        def args(self):
            return self.getTypedRuleContext(LuaParser.ArgsContext,0)


        def NAME(self):
            return self.getToken(LuaParser.NAME, 0)

        def getRuleIndex(self):
            return LuaParser.RULE_nameAndArgs

        def enterRule(self, listener):
            if isinstance( listener, LuaListener ):
                listener.enterNameAndArgs(self)

        def exitRule(self, listener):
            if isinstance( listener, LuaListener ):
                listener.exitNameAndArgs(self)




    def nameAndArgs(self):

        localctx = LuaParser.NameAndArgsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_nameAndArgs)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 294
            _la = self._input.LA(1)
            if _la==LuaParser.T__21:
                self.state = 292
                self.match(LuaParser.T__21)
                self.state = 293
                self.match(LuaParser.NAME)


            self.state = 296
            self.args()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VarSuffixContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LuaParser.VarSuffixContext, self).__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(LuaParser.ExpContext,0)


        def NAME(self):
            return self.getToken(LuaParser.NAME, 0)

        def nameAndArgs(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(LuaParser.NameAndArgsContext)
            else:
                return self.getTypedRuleContext(LuaParser.NameAndArgsContext,i)


        def getRuleIndex(self):
            return LuaParser.RULE_varSuffix

        def enterRule(self, listener):
            if isinstance( listener, LuaListener ):
                listener.enterVarSuffix(self)

        def exitRule(self, listener):
            if isinstance( listener, LuaListener ):
                listener.exitVarSuffix(self)




    def varSuffix(self):

        localctx = LuaParser.VarSuffixContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_varSuffix)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 301
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LuaParser.T__21) | (1 << LuaParser.T__26) | (1 << LuaParser.T__30) | (1 << LuaParser.NORMALSTRING) | (1 << LuaParser.CHARSTRING) | (1 << LuaParser.LONGSTRING))) != 0):
                self.state = 298
                self.nameAndArgs()
                self.state = 303
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 310
            token = self._input.LA(1)
            if token in [LuaParser.T__28]:
                self.state = 304
                self.match(LuaParser.T__28)
                self.state = 305
                self.exp(0)
                self.state = 306
                self.match(LuaParser.T__29)

            elif token in [LuaParser.T__20]:
                self.state = 308
                self.match(LuaParser.T__20)
                self.state = 309
                self.match(LuaParser.NAME)

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ArgsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LuaParser.ArgsContext, self).__init__(parent, invokingState)
            self.parser = parser

        def explist(self):
            return self.getTypedRuleContext(LuaParser.ExplistContext,0)


        def tableconstructor(self):
            return self.getTypedRuleContext(LuaParser.TableconstructorContext,0)


        def string(self):
            return self.getTypedRuleContext(LuaParser.StringContext,0)


        def getRuleIndex(self):
            return LuaParser.RULE_args

        def enterRule(self, listener):
            if isinstance( listener, LuaListener ):
                listener.enterArgs(self)

        def exitRule(self, listener):
            if isinstance( listener, LuaListener ):
                listener.exitArgs(self)




    def args(self):

        localctx = LuaParser.ArgsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_args)
        self._la = 0 # Token type
        try:
            self.state = 319
            token = self._input.LA(1)
            if token in [LuaParser.T__26]:
                self.enterOuterAlt(localctx, 1)
                self.state = 312
                self.match(LuaParser.T__26)
                self.state = 314
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LuaParser.T__16) | (1 << LuaParser.T__22) | (1 << LuaParser.T__23) | (1 << LuaParser.T__24) | (1 << LuaParser.T__25) | (1 << LuaParser.T__26) | (1 << LuaParser.T__30) | (1 << LuaParser.T__42) | (1 << LuaParser.T__46) | (1 << LuaParser.T__47) | (1 << LuaParser.NAME) | (1 << LuaParser.NORMALSTRING) | (1 << LuaParser.CHARSTRING) | (1 << LuaParser.LONGSTRING) | (1 << LuaParser.INT) | (1 << LuaParser.HEX) | (1 << LuaParser.FLOAT) | (1 << LuaParser.HEX_FLOAT))) != 0):
                    self.state = 313
                    self.explist()


                self.state = 316
                self.match(LuaParser.T__27)

            elif token in [LuaParser.T__30]:
                self.enterOuterAlt(localctx, 2)
                self.state = 317
                self.tableconstructor()

            elif token in [LuaParser.NORMALSTRING, LuaParser.CHARSTRING, LuaParser.LONGSTRING]:
                self.enterOuterAlt(localctx, 3)
                self.state = 318
                self.string()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FunctiondefContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LuaParser.FunctiondefContext, self).__init__(parent, invokingState)
            self.parser = parser

        def funcbody(self):
            return self.getTypedRuleContext(LuaParser.FuncbodyContext,0)


        def getRuleIndex(self):
            return LuaParser.RULE_functiondef

        def enterRule(self, listener):
            if isinstance( listener, LuaListener ):
                listener.enterFunctiondef(self)

        def exitRule(self, listener):
            if isinstance( listener, LuaListener ):
                listener.exitFunctiondef(self)




    def functiondef(self):

        localctx = LuaParser.FunctiondefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_functiondef)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 321
            self.match(LuaParser.T__16)
            self.state = 322
            self.funcbody()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FuncbodyContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LuaParser.FuncbodyContext, self).__init__(parent, invokingState)
            self.parser = parser

        def block(self):
            return self.getTypedRuleContext(LuaParser.BlockContext,0)


        def parlist(self):
            return self.getTypedRuleContext(LuaParser.ParlistContext,0)


        def getRuleIndex(self):
            return LuaParser.RULE_funcbody

        def enterRule(self, listener):
            if isinstance( listener, LuaListener ):
                listener.enterFuncbody(self)

        def exitRule(self, listener):
            if isinstance( listener, LuaListener ):
                listener.exitFuncbody(self)




    def funcbody(self):

        localctx = LuaParser.FuncbodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_funcbody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 324
            self.match(LuaParser.T__26)
            self.state = 326
            _la = self._input.LA(1)
            if _la==LuaParser.T__25 or _la==LuaParser.NAME:
                self.state = 325
                self.parlist()


            self.state = 328
            self.match(LuaParser.T__27)
            self.state = 329
            self.block()
            self.state = 330
            self.match(LuaParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ParlistContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LuaParser.ParlistContext, self).__init__(parent, invokingState)
            self.parser = parser

        def namelist(self):
            return self.getTypedRuleContext(LuaParser.NamelistContext,0)


        def getRuleIndex(self):
            return LuaParser.RULE_parlist

        def enterRule(self, listener):
            if isinstance( listener, LuaListener ):
                listener.enterParlist(self)

        def exitRule(self, listener):
            if isinstance( listener, LuaListener ):
                listener.exitParlist(self)




    def parlist(self):

        localctx = LuaParser.ParlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_parlist)
        self._la = 0 # Token type
        try:
            self.state = 338
            token = self._input.LA(1)
            if token in [LuaParser.NAME]:
                self.enterOuterAlt(localctx, 1)
                self.state = 332
                self.namelist()
                self.state = 335
                _la = self._input.LA(1)
                if _la==LuaParser.T__14:
                    self.state = 333
                    self.match(LuaParser.T__14)
                    self.state = 334
                    self.match(LuaParser.T__25)



            elif token in [LuaParser.T__25]:
                self.enterOuterAlt(localctx, 2)
                self.state = 337
                self.match(LuaParser.T__25)

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TableconstructorContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LuaParser.TableconstructorContext, self).__init__(parent, invokingState)
            self.parser = parser

        def fieldlist(self):
            return self.getTypedRuleContext(LuaParser.FieldlistContext,0)


        def getRuleIndex(self):
            return LuaParser.RULE_tableconstructor

        def enterRule(self, listener):
            if isinstance( listener, LuaListener ):
                listener.enterTableconstructor(self)

        def exitRule(self, listener):
            if isinstance( listener, LuaListener ):
                listener.exitTableconstructor(self)




    def tableconstructor(self):

        localctx = LuaParser.TableconstructorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_tableconstructor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 340
            self.match(LuaParser.T__30)
            self.state = 342
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LuaParser.T__16) | (1 << LuaParser.T__22) | (1 << LuaParser.T__23) | (1 << LuaParser.T__24) | (1 << LuaParser.T__25) | (1 << LuaParser.T__26) | (1 << LuaParser.T__28) | (1 << LuaParser.T__30) | (1 << LuaParser.T__42) | (1 << LuaParser.T__46) | (1 << LuaParser.T__47) | (1 << LuaParser.NAME) | (1 << LuaParser.NORMALSTRING) | (1 << LuaParser.CHARSTRING) | (1 << LuaParser.LONGSTRING) | (1 << LuaParser.INT) | (1 << LuaParser.HEX) | (1 << LuaParser.FLOAT) | (1 << LuaParser.HEX_FLOAT))) != 0):
                self.state = 341
                self.fieldlist()


            self.state = 344
            self.match(LuaParser.T__31)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FieldlistContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LuaParser.FieldlistContext, self).__init__(parent, invokingState)
            self.parser = parser

        def field(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(LuaParser.FieldContext)
            else:
                return self.getTypedRuleContext(LuaParser.FieldContext,i)


        def fieldsep(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(LuaParser.FieldsepContext)
            else:
                return self.getTypedRuleContext(LuaParser.FieldsepContext,i)


        def getRuleIndex(self):
            return LuaParser.RULE_fieldlist

        def enterRule(self, listener):
            if isinstance( listener, LuaListener ):
                listener.enterFieldlist(self)

        def exitRule(self, listener):
            if isinstance( listener, LuaListener ):
                listener.exitFieldlist(self)




    def fieldlist(self):

        localctx = LuaParser.FieldlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_fieldlist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 346
            self.field()
            self.state = 352
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,31,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 347
                    self.fieldsep()
                    self.state = 348
                    self.field() 
                self.state = 354
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,31,self._ctx)

            self.state = 356
            _la = self._input.LA(1)
            if _la==LuaParser.T__0 or _la==LuaParser.T__14:
                self.state = 355
                self.fieldsep()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FieldContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LuaParser.FieldContext, self).__init__(parent, invokingState)
            self.parser = parser

        def exp(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(LuaParser.ExpContext)
            else:
                return self.getTypedRuleContext(LuaParser.ExpContext,i)


        def NAME(self):
            return self.getToken(LuaParser.NAME, 0)

        def getRuleIndex(self):
            return LuaParser.RULE_field

        def enterRule(self, listener):
            if isinstance( listener, LuaListener ):
                listener.enterField(self)

        def exitRule(self, listener):
            if isinstance( listener, LuaListener ):
                listener.exitField(self)




    def field(self):

        localctx = LuaParser.FieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_field)
        try:
            self.state = 368
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 358
                self.match(LuaParser.T__28)
                self.state = 359
                self.exp(0)
                self.state = 360
                self.match(LuaParser.T__29)
                self.state = 361
                self.match(LuaParser.T__1)
                self.state = 362
                self.exp(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 364
                self.match(LuaParser.NAME)
                self.state = 365
                self.match(LuaParser.T__1)
                self.state = 366
                self.exp(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 367
                self.exp(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FieldsepContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LuaParser.FieldsepContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LuaParser.RULE_fieldsep

        def enterRule(self, listener):
            if isinstance( listener, LuaListener ):
                listener.enterFieldsep(self)

        def exitRule(self, listener):
            if isinstance( listener, LuaListener ):
                listener.exitFieldsep(self)




    def fieldsep(self):

        localctx = LuaParser.FieldsepContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_fieldsep)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 370
            _la = self._input.LA(1)
            if not(_la==LuaParser.T__0 or _la==LuaParser.T__14):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class OperatorOrContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LuaParser.OperatorOrContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LuaParser.RULE_operatorOr

        def enterRule(self, listener):
            if isinstance( listener, LuaListener ):
                listener.enterOperatorOr(self)

        def exitRule(self, listener):
            if isinstance( listener, LuaListener ):
                listener.exitOperatorOr(self)




    def operatorOr(self):

        localctx = LuaParser.OperatorOrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_operatorOr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 372
            self.match(LuaParser.T__32)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class OperatorAndContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LuaParser.OperatorAndContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LuaParser.RULE_operatorAnd

        def enterRule(self, listener):
            if isinstance( listener, LuaListener ):
                listener.enterOperatorAnd(self)

        def exitRule(self, listener):
            if isinstance( listener, LuaListener ):
                listener.exitOperatorAnd(self)




    def operatorAnd(self):

        localctx = LuaParser.OperatorAndContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_operatorAnd)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 374
            self.match(LuaParser.T__33)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class OperatorComparisonContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LuaParser.OperatorComparisonContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LuaParser.RULE_operatorComparison

        def enterRule(self, listener):
            if isinstance( listener, LuaListener ):
                listener.enterOperatorComparison(self)

        def exitRule(self, listener):
            if isinstance( listener, LuaListener ):
                listener.exitOperatorComparison(self)




    def operatorComparison(self):

        localctx = LuaParser.OperatorComparisonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_operatorComparison)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 376
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LuaParser.T__34) | (1 << LuaParser.T__35) | (1 << LuaParser.T__36) | (1 << LuaParser.T__37) | (1 << LuaParser.T__38) | (1 << LuaParser.T__39))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class OperatorStrcatContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LuaParser.OperatorStrcatContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LuaParser.RULE_operatorStrcat

        def enterRule(self, listener):
            if isinstance( listener, LuaListener ):
                listener.enterOperatorStrcat(self)

        def exitRule(self, listener):
            if isinstance( listener, LuaListener ):
                listener.exitOperatorStrcat(self)




    def operatorStrcat(self):

        localctx = LuaParser.OperatorStrcatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_operatorStrcat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 378
            self.match(LuaParser.T__40)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class OperatorAddSubContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LuaParser.OperatorAddSubContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LuaParser.RULE_operatorAddSub

        def enterRule(self, listener):
            if isinstance( listener, LuaListener ):
                listener.enterOperatorAddSub(self)

        def exitRule(self, listener):
            if isinstance( listener, LuaListener ):
                listener.exitOperatorAddSub(self)




    def operatorAddSub(self):

        localctx = LuaParser.OperatorAddSubContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_operatorAddSub)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 380
            _la = self._input.LA(1)
            if not(_la==LuaParser.T__41 or _la==LuaParser.T__42):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class OperatorMulDivModContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LuaParser.OperatorMulDivModContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LuaParser.RULE_operatorMulDivMod

        def enterRule(self, listener):
            if isinstance( listener, LuaListener ):
                listener.enterOperatorMulDivMod(self)

        def exitRule(self, listener):
            if isinstance( listener, LuaListener ):
                listener.exitOperatorMulDivMod(self)




    def operatorMulDivMod(self):

        localctx = LuaParser.OperatorMulDivModContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_operatorMulDivMod)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 382
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LuaParser.T__43) | (1 << LuaParser.T__44) | (1 << LuaParser.T__45))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class OperatorUnaryContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LuaParser.OperatorUnaryContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LuaParser.RULE_operatorUnary

        def enterRule(self, listener):
            if isinstance( listener, LuaListener ):
                listener.enterOperatorUnary(self)

        def exitRule(self, listener):
            if isinstance( listener, LuaListener ):
                listener.exitOperatorUnary(self)




    def operatorUnary(self):

        localctx = LuaParser.OperatorUnaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_operatorUnary)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 384
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LuaParser.T__42) | (1 << LuaParser.T__46) | (1 << LuaParser.T__47))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class OperatorPowerContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LuaParser.OperatorPowerContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LuaParser.RULE_operatorPower

        def enterRule(self, listener):
            if isinstance( listener, LuaListener ):
                listener.enterOperatorPower(self)

        def exitRule(self, listener):
            if isinstance( listener, LuaListener ):
                listener.exitOperatorPower(self)




    def operatorPower(self):

        localctx = LuaParser.OperatorPowerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_operatorPower)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 386
            self.match(LuaParser.T__48)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NumberContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LuaParser.NumberContext, self).__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(LuaParser.INT, 0)

        def HEX(self):
            return self.getToken(LuaParser.HEX, 0)

        def FLOAT(self):
            return self.getToken(LuaParser.FLOAT, 0)

        def HEX_FLOAT(self):
            return self.getToken(LuaParser.HEX_FLOAT, 0)

        def getRuleIndex(self):
            return LuaParser.RULE_number

        def enterRule(self, listener):
            if isinstance( listener, LuaListener ):
                listener.enterNumber(self)

        def exitRule(self, listener):
            if isinstance( listener, LuaListener ):
                listener.exitNumber(self)




    def number(self):

        localctx = LuaParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_number)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 388
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LuaParser.INT) | (1 << LuaParser.HEX) | (1 << LuaParser.FLOAT) | (1 << LuaParser.HEX_FLOAT))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StringContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LuaParser.StringContext, self).__init__(parent, invokingState)
            self.parser = parser

        def NORMALSTRING(self):
            return self.getToken(LuaParser.NORMALSTRING, 0)

        def CHARSTRING(self):
            return self.getToken(LuaParser.CHARSTRING, 0)

        def LONGSTRING(self):
            return self.getToken(LuaParser.LONGSTRING, 0)

        def getRuleIndex(self):
            return LuaParser.RULE_string

        def enterRule(self, listener):
            if isinstance( listener, LuaListener ):
                listener.enterString(self)

        def exitRule(self, listener):
            if isinstance( listener, LuaListener ):
                listener.exitString(self)




    def string(self):

        localctx = LuaParser.StringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_string)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 390
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LuaParser.NORMALSTRING) | (1 << LuaParser.CHARSTRING) | (1 << LuaParser.LONGSTRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx, ruleIndex, predIndex):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[9] = self.exp_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def exp_sempred(self, localctx, predIndex):
            if predIndex == 0:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 1)
         



