from antlr4 import *
from antlr4.tree import *
from LuaLexer import LuaLexer
from LuaParser import LuaParser
from LuaListener import LuaListener
from lxml import etree
import sys

# a lot of bad manner

keywords = set(["and","break","do","else","elseif","end","false","for","function","if","in","local","nil","not","or","repeat","return","then","true","until","while",
                "+","-","*","/","%","^","#","==","~=","<=",">=","<",">","=","(",")","{","}","[","]",":",";",",",".","..","..."])

# set of defaultFunctions
defaultFunctions = {"set": set(["assert","collectgarbage","dofile","error","getfenv","getmetatable","ipairs","load","loadfile","loadstring","next","pairs","pcall","print","rawequal","rawget","rawset","select","setfenv","setmetatable","tonumber","tostring","type","unpack","xpcall","module","require"]),
                    "argtable": {"assert": 1,
                                "collectgarbage": 0,
                                "dofile": 0,
                                "error": 0,
                                "getfenv": 0,
                                "getmetatable": 1,
                                "ipairs": 1,
                                "load": 1,
                                "loadfile": 0,
                                "loadstring": 1,
                                "next": 1,
                                "pairs": 1,
                                "pcall": 2,
                                "print": 0,
                                "rawequal": 2,
                                "rawget": 2,
                                "rawset": 3,
                                "select": 1,
                                "setfenv": 2,
                                "setmetatable": 2,
                                "tonumber": 1,
                                "tostring": 1,
                                "type": 1,
                                "unpack": 1,
                                "xpcall": 2,
                                "module": 1,
                                "require":1}}
defaultVariables = { "_VERSION", "_G", "_ENV", "coroutine", "package", "string", "table", "math", "io", "file", "debug", "os" }

mydebug = False

def getLxmlTree(tree, ruleNames):
    xmlchild = etree.Element(str(ruleNames[tree.getRuleIndex()]))
    if tree.children:
        for child in tree.children:
            if 'symbol' in child.__dict__:
                leaf = etree.SubElement(xmlchild, "leaf")
                leaf.text = str(child)
            else:
                xmlchild.append(getLxmlTree(child, ruleNames))
    return xmlchild

def calculateParams(root):
    if root.tag == "nameAndArgs":
        for child in root:
            if child.tag == "args":
                count = 0
                for c in child:
                    if c.tag == "explist":
                        for e in c:
                            if e.tag == "exp":
                                count += 1
                return count
    return -1

def generateUnionFuncTable(tables):
    unionTable = {"set": set(),  "argtable": {}}
    for table in tables:
        unionTable["set"] |= table["set"]
        unionTable["argtable"].update(table["argtable"])
    return unionTable
    
def report(message, root, informations):
    print message
    print "{"
    print etree.tostring(root.getparent().getparent().getparent(), pretty_print=True)
    for information in informations:
        print information
    print "}"

globalVarTable = set()
globalFuncTable = {"set": set(), "argtable": {}}
selfInsertHack = False  # There is no time to explain

# bad solution
def parseTree(root, topVarTable, bottomVarTable, topFuncTable):
    global selfInsertHack
    varTable = bottomVarTable
    if root.tag == "block" and selfInsertHack:
        varTable.add("self")
        selfInsertHack = False
    
    funcTable = {"set": set(), "argtable": {}}
    myBottomVarTable = set()
    for child in root:
        if child.tag == "leaf" and (not child.text in keywords):
            if root.tag == "var":
                unionFuncTable = generateUnionFuncTable([topFuncTable, funcTable, defaultFunctions, globalFuncTable])
                if root.getparent().tag == "varlist" or root.getparent().tag == "prefixexp":
                    if len(root) > 1 and root[1].tag == "varSuffix":
                        if not (child.text in (topVarTable | varTable | globalVarTable | defaultVariables | unionFuncTable["set"])):
                            if mydebug:
                                report("PROBLEMS with existance of variable: " + child.text, root, [topVarTable | varTable | globalVarTable, 
                                    topFuncTable["set"] | funcTable["set"] | globalFuncTable["set"]])
                            else:
                                raise Exception("Error with existance of variable: \"" + child.text + "\"")
                    globalVarTable.add(child.text)
                elif root.getparent().tag == "varOrExp":
                    if root.getparent().getparent().tag == "functioncall":
                        if len(root) > 1 and root[1].tag == "varSuffix":
                            if not (child.text in (topVarTable | varTable | globalVarTable | defaultVariables | unionFuncTable["set"])):
                                if mydebug:
                                    report("PROBLEMS with existance of variable: " + child.text, root, [topVarTable | varTable | globalVarTable, 
                                        topFuncTable["set"] | funcTable["set"] | globalFuncTable["set"]])
                                else:
                                    raise Exception("Error with existance of variable: \"" + child.text + "\"")
                            if (child.text in unionFuncTable["set"]):
                                count = calculateParams(root[1][0])
                                if count < 0:
                                    if mydebug:
                                        report("PROBLEMS with calculateParams: " + child.text, root, [topVarTable | varTable | globalVarTable, 
                                            topFuncTable["set"] | funcTable["set"] | globalFuncTable["set"], count])
                                    else:
                                        raise Exception("Error with calculateParams \"" + child.text + "\"")
                                elif not child.text in unionFuncTable["argtable"]:
                                    if mydebug:
                                        report("PROBLEMS with child.text in unionFuncTable: " + child.text, root, [unionFuncTable["set"]])
                                    else:
                                        raise Exception("Error with child.text in unionFuncTable: \"" + child.text + "\"")
                                elif count < unionFuncTable["argtable"][child.text]:
                                    if mydebug:
                                        report("PROBLEMS with arguments arg: " + child.text, root, [topFuncTable["set"] | funcTable["set"] | globalFuncTable["set"],
                                            topFuncTable["argtable"], funcTable["argtable"], count])
                                    else:
                                        raise Exception("Error with arguments count in function: \"" + child.text + "\"")

                        elif not (child.text in unionFuncTable["set"]):
                            if child.text not in (topVarTable | varTable | globalVarTable | defaultVariables):
                                if mydebug:
                                    report("PROBLEMS with existance of function: " + child.text, root, [topFuncTable["set"] | funcTable["set"] | globalFuncTable["set"]])
                                else:
                                    raise Exception("Error with existance of function \"" + child.text + "\"")
                        else:
                            count = calculateParams(root.getparent().getparent()[1])
                            if count < 0:
                                if mydebug:
                                    report("PROBLEMS with calculateParams: " + child.text, root, [topFuncTable["set"] | funcTable["set"] | globalFuncTable["set"], count])
                                else:
                                    raise Exception("Error with calculateParams \"" + child.text + "\"")
                            elif not child.text in unionFuncTable["argtable"]:
                                if mydebug:
                                    report("PROBLEMS with child.text in unionFuncTable: " + child.text, root, [unionFuncTable["set"]])
                                else:
                                    raise Exception("Error with child.text in unionFuncTable: \"" + child.text + "\"")
                            elif count < unionFuncTable["argtable"][child.text]:
                                if mydebug:
                                    report("PROBLEMS with arguments arg: " + child.text, root, [topFuncTable["set"] | funcTable["set"] | globalFuncTable["set"],
                                            topFuncTable["argtable"], funcTable["argtable"], count])
                                else:
                                    raise Exception("Error with arguments count in function: \"" + child.text + "\"")
                    else:
                        if not (child.text in (topVarTable | varTable | globalVarTable | defaultVariables | unionFuncTable["set"])):
                            if mydebug:
                                report("PROBLEMS with existance of variable: " + child.text, root, [topVarTable | varTable | globalVarTable, 
                                        topFuncTable["set"] | funcTable["set"] | globalFuncTable["set"]])
                            else:
                                raise Exception("Error with existance of variable: \"" + child.text + "\"")

            # create myBottomVarTable to pass it to the <block>
            elif root.tag == "stat" and root[0].text == "for":
                myBottomVarTable.add(child.text)
            elif root.tag == "namelist":
                if root.getparent()[0].text == "for" or root.getparent().tag == "parlist":
                    myBottomVarTable.add(child.text)
                else:
                    if not child.text in topVarTable or (root.getparent().tag == "stat" and root.getparent()[0].text == "local"): # or if local
                        varTable.add(child.text)
            elif root.tag == "funcname":
                if len(root) > 1:
                    if root[0] == child:
                        if not (child.text in (topVarTable | varTable | globalVarTable | defaultVariables)):
                            if mydebug:
                                report("PROBLEMS with existance of variable: " + child.text, root, [topVarTable | varTable | globalVarTable, 
                                        topFuncTable["set"] | funcTable["set"] | globalFuncTable["set"]])
                            else:
                                raise Exception("Error with existance of variable: \"" + child.text + "\"")
                        if root[1].text == ":":
                            selfInsertHack = True
                            continue
                        else:
                            continue
                else:
                    globalFuncTable["set"].add(child.text)
                    count = 0
                    if root.getparent()[2][1].tag == "parlist":
                        for c in root.getparent()[2][1][0]:
                            if c.text != ",":
                                count += 1
                    globalFuncTable["argtable"][child.text] = count
            elif root.tag == "stat" and root[0].text == "local":
                funcTable["set"].add(child.text)
                count = 0
                if root[3][1].tag == "parlist":
                    for c in root[3][1][0]:
                        if c.text != ",":
                            count += 1
                funcTable["argtable"][child.text] = count
        else:
            unionFuncTable = generateUnionFuncTable([funcTable, topFuncTable])
            if child.tag == "block":
                parseTree(child, varTable | topVarTable, myBottomVarTable, unionFuncTable)
            else:
                newVarTable, newFuncTable, newBottomVarTable = parseTree(child, varTable | topVarTable, set(), unionFuncTable)
                varTable = varTable | newVarTable
                myBottomVarTable = myBottomVarTable | newBottomVarTable
                funcTable["set"] = funcTable["set"] | newFuncTable["set"]
                funcTable["argtable"].update(newFuncTable["argtable"])

    if root.tag == "block":
        if len(varTable) > 0 or (len(varTable | globalVarTable) and root.getparent().tag == "chunk"):
            xmlVarTable = etree.Element("varTable")
            if root.getparent().tag == "chunk":
                xmlVarTable.text = str(varTable | globalVarTable)
            else:
                xmlVarTable.text = str(varTable)
            root.append(xmlVarTable)
        if len(funcTable["set"]) > 0 or (len(funcTable["set"] | globalFuncTable["set"]) > 0 and root.getparent().tag == "chunk"):
            xmlFuncTable = etree.Element("funcTable")
            if root.getparent().tag == "chunk":
                xmlFuncTable.text = str(funcTable["set"] | globalFuncTable["set"])
            else:
                xmlFuncTable.text = str(funcTable["set"])
            root.append(xmlFuncTable)
        return set(), {"set": set(), "argtable": {}}, set()
        
    return varTable, funcTable, myBottomVarTable

def main(argv):
    global mydebug
    if len(argv) < 2:
        print "Empty output"
        return
    ind = 1
    if argv[ind] == "-debug":
        print "Debug mod ON"
        ind += 1
        mydebug = True

    input = FileStream(argv[ind])
    if (len(argv) > 1 + ind):
        sys.stdout = open(argv[ind+1], 'w')
    try:
        lexer = LuaLexer(input)
        stream = CommonTokenStream(lexer)
        parser = LuaParser(stream)
        tree = parser.chunk()
        root = getLxmlTree(tree, parser.ruleNames)
        parseTree(root, set(), set(), {"set": set(), "argtable": {}})
        print(etree.tostring(root, pretty_print=True))
    except Exception as err:
        print err

if __name__ == '__main__':
    main(sys.argv)
