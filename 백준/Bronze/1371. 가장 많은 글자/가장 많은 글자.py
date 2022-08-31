# 가장 많은 글자

import sys
from collections import Counter

counter = Counter(sys.stdin.read())
counter['\n'] = -1
counter[' '] = -1
print("".join(key for key in sorted(counter.keys()) if counter[key] == max(counter.values())))