# *** NOT FINISHED ***
具体需要去去实了解计算，需要去理解透彻transformer

# 前情提要
Transformer很多任务需要long context， 如输入一个完整的使用说明书，一个高精度的大号图片等。这部分的计算attention耗时主要在compute 和 memory两部分，文章中称主要是memory bond花时间多，从HBM读读写到更快速的SRAM需要时间。本文试图通过tiling和recomputation来解决这个问题

# 大概
tiling 

# TODO
what does "IO aware" mean here
what is tilling

# 相关链接
https://www.zhihu.com/question/611236756

https://zhuanlan.zhihu.com/p/664061672

# 视频讲解

https://www.youtube.com/watch?v=FThvfkXWqtE&t \
https://www.youtube.com/watch?v=gMOAud7hZg4&t
- 原作者讲的，正确，可以看看，感觉比较概括

https://www.bilibili.com/video/BV1UT421k7rA/?spm_id_from=333.337.search-card.all.click&vd_source=59c74a5a0818a21536380fdc275ad91b
- 有关于tiling部分非常好的图解