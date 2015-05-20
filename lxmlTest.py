from lxml import etree
import sys

def main(argv):
    with open (argv[1], "r") as myfile:
        data=myfile.read()
    root = etree.fromstring(data)
    print(etree.tostring(root, pretty_print=True))

if __name__ == '__main__':
    main(sys.argv)