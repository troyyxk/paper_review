LLM的layers中有lazy layers，他们的kv cache是相对redundent的
SimLayerKV 减少lazy layer的KV cache，缩小KV cache总体的体积

lazy layer是只关注开头和结尾，吧attention都给它们的layer，一般还是固定的几个layer

TODO KV cache和transfomer layer的关系是啥？
TODO what is the differnece between inter and intra-layer redundancy

缩小KV cache大小的技术：
- pruning
- quantization
- eviction


一直压缩，直到出现大不同
lazy layer也算上
