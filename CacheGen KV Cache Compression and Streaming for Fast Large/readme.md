# CacheGen KV Cache Compression and Streaming for Fast Large

# Questions
- what is  bitstream
- why  bitstream faster save bendwith and delay
- what is quatization
- how does the streaming adapt to different network conditions
- what is different compression level
- ho
- what is kv quantization
- what is load contextin text form
- f1 score and perplexity
- what is autoregressive manner
- how does CacheGen use the distributional properties of the KV cache
- how CacheGen adapt dynamic bandwidth
- how does CacheGen compute KV cache on demand
- what is layer and channel in LLM
- what is a token in LLM
- what is data loss, why apply it
- wha tis 2 dimension of kv cache, layers, channels and token position
- what is the relationship between context, kv cache and token

# Note
encoder
- a custom quatization arithmetic coding stretegy
    - to leverage the distributional properties of KV cache
decoding (decompression)
- accelerated using GPU-based implementation
- pipelined with transmission
    - further reduce teh impact on teh overall inference delay
    
cache streaming
- in low bandwidth, send text format

delta in this paper:
- difference between k tensors' values at the same layer and channel between every pair of consecutive tokens in the context
- v can be use in stead of k here

3 observation on KV cache the author:
1. 同一个layer和channel，相似token有相似的kv tensor values，相比tokens that are further apart 
    - token就是context里紧挨着的，文字的话就是紧挨着的词或者句子，他们转化成KV tensor value也更近
2. 越浅层apply loss，accuracy下降的越厉害
    - 基本原理是，高层数的时候有了higer level structure，低层数时候的损失更容易影响最终结果
3. kv cache可通过layers, channels and token position来index，用layer和channel比用token position来group value有更多的information gain
    - layer and channel capture varios features of the input

3 high level designkv cache encoder design
1. 相邻token算delta tensor
    - delta可能相比kv tensor更好压缩，因为上面的第一条（保存差值）
    - 每个chunk的第一个tensor算anchor tensor，完成保留，剩下的都和它计算差值
        - 不是相邻的计算，方便并行decode
2. 不同的layer，不同的quantization
3. arithmetic coder将同layer&channel的放在一起
    - 因为ac use fewer to encode more frequent symbols
    

# other thoughts
this paper has somehow good explaination on how transformer works in 2.1

# Task
1. reproduce CacheGen
    - Reproduce the authors' code.
2. Extend
3. Read and understand the paper. This may require reviewing other KV Cache-related literature
4. Consider potential improvements from a networking perspective 
    - attempt to implement them
        - Can the KV cache be distributed across different devices
        - Is it possible to implement wireless transmission for sharing KV between devices
        - What are the potential suitable application scenarios for such a networked implementation

5. other:
    - leveraging new tools like Claude or GPT-4 to assist you with 
        - environment setup
        - code comprehension
        - brainstorming

*** 把发现写成一个pdf

## 需要理解的点
- don't need you to fully understand or improve the code
- focus on the key aspect
    - sharing between networked devices rather than single-machine implementations

尝试从CacheGen出发，network方向找创新点


