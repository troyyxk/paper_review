# 前情提要
LLM多轮回话会导致 \
cache因为存子啊HBM里，HBM空间不够用会把他们清理了，下次会话的时候还要重新计算

# 大概
挑战
1. 访问存好的 KV cache的开销
2. 大量的 KV cache 存储容量需求
    - 上磁盘
        - 但是更慢了？
3. 放在更慢的存储介质怎么提高性能
    - 要尽量放在主机内存
4. 存的 KV cache 太长可能会超过限制
    - 直接截掉，反正本来 recompute 模式下，所用的也是有限制的相对新的 KV

### 挑战1
- 用layer-wise pre-loading scheme
- hbm to host memory
    - asynchronous saving scheme
    - overlap the saving with the inference computation

### 挑战2，3
- scheduler-aware fetching scheme
- scheduler-aware eviction scheme
- 上述两个是disk和host memory的交互 scheme

### 挑战4
- positional encoding decoupled truncation scheme
    - save the KV caches without positional encoding embedded

### layer-wise pre-loading scheme
文章里只说了，在last job结束之前，一层一层地load kv cache，这样执行第1...n层的时候，该层的kv cache是load好的
- 没load好的话要等一等，完全不用等的叫 perfect pre-loading with a customized larger buffer \
文章说具体咋做的

### Asynchronous Saving from HBMs to Memory
- prefill阶段并行快速产生大量 kv cache，decode阶段串行，一个一个地产生 kv cache
- asynchronous saving scheme 考虑到了两个阶段的不同，但是没有说具体的
- 逐层写，执行完就写
- 还保留了一个写入缓冲区，防止 block execution of the next job

### Hierarchical KV Cache Placement
- AttentionStore用了host memory和disk
- host快很多，最好放host里

#### scheduler-aware fetching scheme
- 执行一个的时候，就开始把后面两个的从disk load 到 host memory

#### scheduler-aware eviction scheme
- evict的顺序是 host memory -> disk -> 删除
- 按照 host memory 和 disk 所能保存的最多 kv cache，有一个 eviction window，假设大小为 n
- 即将执行的 job queue里，即将执行的 n 个在 window 里
    - 要删的时候不删这window里的
    - 要移到 disk 里的时候，越靠近末尾（越晚执行），越会被移到 disk里

### decoupled truncation scheme
- 使用 relative position embedding

# 相关文章
https://zhuanlan.zhihu.com/p/706249272
