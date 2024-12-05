# 相关视频
https://www.bilibili.com/video/BV1pu411o7BE/?spm_id_from=333.337.search-card.all.click&vd_source=59c74a5a0818a21536380fdc275ad91b

# 内容

这篇比较著名，我就不过多概括，毕竟基本全是精华。主要记录自己觉得需要记录的，即当时不明白，或者之后可能会忘的点。

layer norm相对于batch norm的
- batch norm是针对每一个输入的，比如输入一组图片，batch norm就针对同一个特征的norm，某一个像素点啥的。如果长度是变动的，那就用不了。
- layer norm是针对每一个输入进行norm，所以不关心总输入的长度。

decoder里mask是为了不让transformer在预测t的时候，看到t之后的，t+1, t+2...的输入

/(sqrt(dk))是因为不这么做，回更极端，更加只有1和0（接近），gradient会比较小

matmul就是乘

scale是啥
- /(sqrt(dk))

# TODO
what is dimension dk
- 向量的长度
