import argparse
import re

def parseLic(rawLic):
    licPattern = re.compile(r'''\w{28}''')
    for item in rawLic:
        match = re.search(licPattern, item)
        if match:
            print('license add -license-code ' + match.group(0))

def main():
    parser = argparse.ArgumentParser(description='licparser - Copy/Paste raw license from NetApp support and get cDot commands to add licenses')
    args = parser.parse_args()

    print('Paste raw license content. Press CRTL-D or CTRL-Z (Windows OS) to save it.')
    rawLic = []
    while True:
        try:
            line = input()        
        except EOFError:
            break
        rawLic.append(line)
    
    print('\n')
    parseLic(rawLic)
    print('\n')

if __name__ == '__main__':
    main()