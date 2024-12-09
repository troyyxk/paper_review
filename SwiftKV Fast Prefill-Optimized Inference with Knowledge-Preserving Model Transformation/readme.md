# 前情提要
常见的LLM workload里，input比output多得多，有的达到了10:1。单纯的KV cache减小体积在这作用没一般的大，因为和process input promts无关

# 大概
SingleInputKV
- 基于一个观察：layer越深，他们的input越类似
- 人工设定一个l，l之后的层的input直接不算，直接用l层的input

AcrossKV
- 直接一个KV给多层用
    - 不会出问题么？

Knowledge Recovery
- 对l之后的层的W_QKV find-tuning
- 一个开SwiftKV，一个不开
- 没有直接用standard LM loss，而是distillation
- 没完全看懂，要看看distilling

# 想法
路子真野， 基本是相似的直接忽略， 然后fine tune一下就可以用了

# Others
SwiftKV
- reducing inference computation during prompt processing 
- rather than just compressing memory
-
- model rewiring and knowledge-preserving self-distillation
- improvements in throughput, latency and cost efficiency for enterprise LLM workloads by up to 2x
- compute-quality tradeoffs
