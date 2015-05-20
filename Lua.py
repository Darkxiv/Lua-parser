from antlr4 import *
from antlr4.tree import *
from LuaLexer import LuaLexer
from LuaParser import LuaParser
from LuaListener import LuaListener
from lxml import etree
import sys
import pdb

def dfs_print(tree, ruleNames, spaces=0):
    print ' '*spaces + '<' + str(ruleNames[tree.getRuleIndex()]) + '>'
    for child in tree.children:
        if 'symbol' in child.__dict__:
            print ' '*(spaces+4) + '<leaf>' + str(child) + '</leaf>'
        else:
            dfs_print(child, ruleNames, spaces+4)
    print ' '*spaces + '</' + str(ruleNames[tree.getRuleIndex()]) + '>'

def tree_to_xml(tree, ruleNames):
    if 'symbol' in tree.__dict__:
        xml_node = etree.Element('leaf')
        xml_node.text = str(tree)
    else:
        xml_node = etree.Element(ruleNames[tree.getRuleIndex()])
        for child in tree.children:
            child_node = tree_to_xml(child, ruleNames)
            xml_node.append(child_node)
    return xml_node

def main(argv):
    input = FileStream(argv[1])
    lexer = LuaLexer(input)
    stream = CommonTokenStream(lexer)
    parser = LuaParser(stream)
    t = parser.chunk()
    #pdb.set_trace()
    #print(t.toStringTree(parser.ruleNames))
    root = tree_to_xml(t, parser.ruleNames)
    s = etree.tostring(root, pretty_print=True)
    print s
    #print(t.toStringTree(parser.ruleNames))
    #dfs_print(t, parser.ruleNames)

if __name__ == '__main__':
    main(sys.argv)
