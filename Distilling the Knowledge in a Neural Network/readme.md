# 讲解视频链接
https://www.youtube.com/watch?v=k63qGsH1jLo

# 相关文章
https://zhuanlan.zhihu.com/p/81467832

# 前情提要
训练和使用的模型需求不一样
- 训练的时候可以用大算力，不是很 time sensitive
- 使用的时候很 time sensitive
Insight
- using softmax, other than the largest probability answer, all other may be important as well

# 大概
temeprature T
- 用在softmax里，每个logit都除以T，这样结果会更smooth
Knowledge Distallation 主要做的是先训练一个大的模型作为teacher，一般还使用大的数据集 \
在一个小的数据集上，训练小的模型，拿大的模型的 inference result当作 label (soft label，相对真正label，hard label；他们的loss也分别叫做 soft loss 和 hard loss)，使得小模型接近大模型，更好使用 \
用softmax-T，是的除了one-hot的结果，别的也可以学习到 \
最终使用小模型，这就是 knowledge distallation

# Termiology
knowledge distallation
- the act of removing not needed information



