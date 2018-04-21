import sys

def main():
    print (sys.path)

if __name__ == '__main__':
    main()

convert_to_utf8 = open ('/Users/Love/Documents/GitHub/msds510/data/raw/avengers.csv', 'rb')
convert_to_utf8 = convert_to_utf8.read()
convert_to_utf8 = convert_to_utf8.decode('ISO-8859-1')

with open('/Users/Love/Documents/GitHub/msds510/data/interim/avengers_utf8.csv', 'w') as nf:
    nf.write(convert_to_utf8)

F = open ('/Users/Love/Documents/GitHub/msds510/data/interim/avengers_utf8.csv', 'r')
lines = F.readlines()
print (lines)

