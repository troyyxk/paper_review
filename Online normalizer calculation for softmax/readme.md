# 前情提要
softamx公式很常见，这篇文章尝试减少IO操作，优化softmax公式

# 大概
本文一步一步讲解了他的优化
algorithm 1是基础的softmax，3个io，但是有overflow和underflow的风险 \
algorithm 2是一个safe softmax，但是4个io \
algorithm 3是作者提出的online algorithm，既safe，又只用了3个io，作者提供了证明，整体设计的很妙 \
algorithm 4，没看，有关top-k，之后看看

之前不是很理解 algorithm 3，在 get_softmax_algorithms.py 写了一半就发现问题了




# TODO
why is the original one unsafe and algorithm 2 safe
- 解释了上下溢出和为什么safe 
```
https://blog.csdn.net/qq_35054151/article/details/125891745
https://www.cnblogs.com/guoyaohua/p/8900683.html
```
- 摘要：
```
c 极其大，导致分子计算 ec 时上溢出
c 为负数，且  |c| 很大，此时分母是一个极小的正数，有可能四舍五入为0，导致下溢出

　　通过这样的变换，对任何一个 xi，减去M之后，e 的指数的最大值为0，所以不会发生上溢出；同时，分母中也至少会包含一个值为1的项，所以分母也不会下溢出（四舍五入为0）。所以这个技巧没什么高级的技术含量。
```

没看懂第三页的证明，需要多看看


# 相关视频
https://www.youtube.com/watch?v=D-vNLrZRvo0 \
https://www.youtube.com/watch?v=lpBJHUU4w6k

# playground
```
# index start at 1 and end at V, V = 3 here
input:
x = [1, 2, 3]

algorithm 1:
d = [2.718281828459045, 10.107337927389695, 30.19287485057736]
y = [0.09003057317038046, 0.24472847105479767, 0.6652409557748219]

algorithm 2:
d = [0.1353352832366127, 0.503214724408055, 1.5032147244080551]
y = [0.09003057317038046, 0.24472847105479764, 0.6652409557748218]

algorithm 3:
d = [1.0, 1.3678794411714423, 1.5032147244080551]
y = [0.09003057317038046, 0.24472847105479764, 0.6652409557748218]
```
