# 前情提要
针对 FlashDecoding 的 load balancing 问题

# 大概
和其他论文一样，基本都把 softmax， 特别是其中非 matmul 的部分， 放到最后做

FlashDecoding 是 fixed-split partition，在一些情况下，会造成GPU浪费
- Lean Attention采用了 stream-K 风格 decomposition

分块确保有 GPU 的 SM 被用满

# 相关文章
https://zhuanlan.zhihu.com/p/713810021
