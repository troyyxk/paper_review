星锟 这是我朋友最新的一项工作，涉及计算和通信的结合，蛮典型，和kv处理也有结合的可能，可以看一下：
论文：https://arxiv.org/abs/2410.00531
开源代码：https://anonymous.4open.science/r/tpi-llm/README.md

# Links:
https://www.reddit.com/r/LocalLLaMA/comments/1fu8ujh/serving_70bscale_llms_efficiently_on_lowresource/
https://github.com/Lizonghang/TPI-LLM

# To Figureout:
- Pipeline parallelism (same as model parallelism?)
- tensor parallelism
- layer weight
- attention head
- FFN (Feed Forward Network)
- allreduce (similar to mapreduce?)
    - star based allreduce
    - tree based allreduce

一直说link latency，只有公式里只有bandwidth是哥出了几起个数之外的可控变量？
是因为topology？
tlink为啥和bandwidth无关？
