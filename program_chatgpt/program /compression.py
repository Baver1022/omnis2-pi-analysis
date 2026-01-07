import gzip, lzma, sys
data=open(sys.argv[1],'rb').read()
print(len(data), len(gzip.compress(data)), len(lzma.compress(data)))
