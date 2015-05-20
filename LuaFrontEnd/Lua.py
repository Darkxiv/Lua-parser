from antlr4 import *
from antlr4.tree import *
from LuaLexer import LuaLexer
from LuaParser import LuaParser
from LuaListener import LuaListener
from lxml import etree
import sys

def lxmlPrint(tree, ruleNames):
    xmlchild = etree.Element(str(ruleNames[tree.getRuleIndex()]))
    for child in tree.children:
        if 'symbol' in child.__dict__:
            leaf = etree.SubElement(xmlchild, "leaf")
            leaf.text = str(child)
        else:
            xmlchild.append(lxmlPrint(child, ruleNames))
    return xmlchild

def main(argv):
    input = FileStream(argv[1])
    lexer = LuaLexer(input)
    stream = CommonTokenStream(lexer)
    parser = LuaParser(stream)
    tree = parser.chunk()
    root = lxmlPrint(tree, parser.ruleNames)
    print(etree.tostring(root, pretty_print=True))

if __name__ == '__main__':
    main(sys.argv)
