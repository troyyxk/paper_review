# 前情提要
FlashAttention
- 介绍了FalshAttention如何利用 Online Softmax 将计算划分为block全部在SRAM中进行， 避免了昂贵的HBM IO
和FlashAttention一样，FlashAttention是为了解决LLM输入long sequence的问题，专注于通过优化优化 Memory Access Cost 而不是优化 Floating Point Operations Per Second (FLOPS) 来做到的

# 大概
相较于 FlashAttetion ，有以下三个改进：
1. 减少 non-matmul FLOP，因为GPU计算乘法更好
2. 在 sequence length 是长的时候，in addition to batch and head dimesion，用sequence去 parallelize forward and backward pass
3. 同一 block of attention of block computation 内，也partition给不同的 thread blocks

### 如何减少 non-matul FLOP 
减少 non-matmul FLOP是通过减少过程中的diag运算，将他们尽量合并到尾部

### 新的并行
- GPU上的基本计算单元是 streaming multiprocessor
- 基于FlashAttention v1，更换了算法的内外循环
- v1 每个streaming multiprocesor 一个 batch/attention head
- v2 基于long sequence batch size比较小， 可能无法利用一个gpu里所有的sm的情况，分割 sequence length，更加的并行
- 具体参考一下 https://zhuanlan.zhihu.com/p/642962397 写的太好了

### work partitioning
- 矩阵乘法本身是可分块计算的
- v2 相比 v1，对Q而不是KV分块，得到的临时结果直接拼接就是最终的O

# Termiology
batch dimension
- the number of input in a batch
batch size
- the number of input sequences processed simultaneously by the model during training
- long sequence的时候，batch size会小

# TODO
what is the "diag" operation?

# Useful links
```
https://zhuanlan.zhihu.com/p/642962397

https://zhuanlan.zhihu.com/p/664061672
https://zhuanlan.zhihu.com/p/4264163756
```
