# 讲解视频链接
- https://www.youtube.com/watch?v=0iDtRpBcXW8
- https://www.youtube.com/watch?v=blYpzQdzWlU

# 前情提要
- hallucination，幻觉，导致答案无法被使用的原因，unfaithful
- confabulation: 意思是wrong and arbitrary
    - 对不重要的细节敏感

# 大概
confabulation是LLM幻觉的一种，这篇文章提出了一种方式来检测幻觉。文章提出了sematic entropy，并在后面附上了计算办法，来针对一个答案，而不是一个一个token计算entropy，entropy越低，越不可能是confabulation。文章同时提出了一个方法 ，我在 [如何检测confaculatoin] 里写了。

文章不算很难，不论是公式还是方法，但是很有意思，很易用，能发在nature上，值得学习。

# 想解决的问题，做成了啥，咋做的
### 如何检测confaculatoin
- p2
- 先LLM1生成长答案 -> 把长答案分成多个factiod -> LLM2针对每个factoid生成该答案可能来自的问题 -> LLM1回答LLM2生成的问题 -> 针对原本的和新的factoid算semantic entropy，低的就认为不是confabulation，高的认为是
# 
- 看 semantic entropy 来看是否是 semantic uncertainty， high to high
- 因为 free-form generation 不同的文本也可能是同一个意思，所以不是 token-to-token, 而是 estimating the entropy of the distribution of the meanings free form answers
- 怎么看是否是正确的答案？生成几个，按照能否相互印证来生成cluster， k-mean？不在cluster里的就是有问题的错误答案

# TODO
how is semantic entropy measured? how is it different from naive entropy?
- p2的图
- 算entropy之前，cluster answers with same meaning
    - naive的会直接算entroypy

difference between hallucination and confabulation?
- confabulation a subset of hallucination, it is result of false training data

AUROC & AURAC

能用一个agent来代替一个单独的LLM来聚类semantic meaning么？
