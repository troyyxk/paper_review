# 文章链接
https://crfm.stanford.edu/2023/10/12/flashdecoding.html

# 大概
在 inference 的时候，Q的大小是1，导致导致只用了一个GPU的1 sm \
基于以上，FlashDecoding针对Key/Value sequence length进行切割，每块当作一个split，可以进行 parallel computing，最后对每一部分的结果reduce，得到一个最终的结果 \
有点类似 MapReduce  
