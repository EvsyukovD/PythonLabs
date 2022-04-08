from bloomfilter import BloomFilter
import countmodule as c
import managermodule as manager
import argparse
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f',help='The name of file with text')
    parser.add_argument('-p',help='The name of file with patterns')
    parser.add_argument('-l', help='The len of one pattern')
    args = parser.parse_args()
    manager.work(args.f,args.p,int(args.l))

if __name__ == '__main__':
    main()