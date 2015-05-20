from antlr4 import *
from antlr4.tree import *
from LuaLexer import LuaLexer
from LuaParser import LuaParser
from LuaListener import LuaListener
import sys

def dfs_print(tree, ruleNames, spaces=0):
    print ' '*spaces + '<' + str(ruleNames[tree.getRuleIndex()]) + '>'
    for child in tree.children:
        if 'symbol' in child.__dict__:
            print ' '*(spaces+4) + '<leaf>' + str(child) + '</leaf>'
        else:
            dfs_print(child, ruleNames, spaces+4)
    print ' '*spaces + '</' + str(ruleNames[tree.getRuleIndex()]) + '>'

def main(argv):
    input = FileStream(argv[1])
    lexer = LuaLexer(input)
    stream = CommonTokenStream(lexer)
    parser = LuaParser(stream)
    t = parser.chunk()
    #print(t.toStringTree(parser.ruleNames))
    dfs_print(t, parser.ruleNames)

if __name__ == '__main__':
    main(sys.argv)