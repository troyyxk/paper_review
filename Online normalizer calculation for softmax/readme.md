# *** NOT FINISHED ***


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