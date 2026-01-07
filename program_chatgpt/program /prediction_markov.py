import sys, collections
digits=[int(c) for c in open(sys.argv[1]).read() if c.isdigit()]
cnt=collections.defaultdict(lambda:[0]*10)
for i in range(len(digits)-1): cnt[digits[i]][digits[i+1]]+=1
def p(d): return cnt[d].index(max(cnt[d]))
print(sum(p(digits[i])==digits[i+1] for i in range(len(digits)-1))/(len(digits)-1))
