# 大概
# 3 Infrastructure
## 3.1 AI Accelerators
### 3.1.1 NVIDIA GPU
没啥内容
### 3.1.2 Other AI Accelerators
AMD, TPU 等

## 3.2 Network Infrastructure
### 3.2.1 Chip-to-Chip Communications
传统上用 PCIe 但是对LLM来说不够用 \
chip-to-chip 现在用 NVLink, 有很多 topology
- Cube-Mesh Topology
    - NVLink 1.0的， 每个平面四个全链接，可有两个平面，平面间四条线，160 GB/s
- Fully connected Topology
    - Switch-based
        - NVIDIA 用 NVSwitch, GPU 之间相互不连接，都连 NVswitch上；很快 900多
    - P2P
        - AMD，英特尔，华为都是全链接，受限于 bandwidth
- 2D/3D-Torus Topology  
    - 谷歌 TPU 用的, 每个 TPU 链接4个邻居 TODO 看看为啥好用
### 3.2.2 Node-to-Node Communications
Remote Direct Memory Access (RDMA)
- 能直接读对方的 memory, 不需要对面的 system 或者 cpu, 对 LLM 很适用
- 两个常见的是 InfiniBand(100-400 GB/s) 和 RDMA over Converged Ethernet (RoCE)

### 3.2.3 Network Topology
HPC network topology
- high performance computing 的常规 topology 都可以用，这里没具体讲 TODO 可看看链接里的文章
Training-Optimized Topology
- rail, 同一个pod里的 GPU 会和所有 leaf switch 全连接，这样他们 share index，可以视作整体使用
    - rail-Optimized 是多层 (core switch - spine switch - leaf switch - GPU) 每层都全连接，会造成资源浪费，因为大部分链接没啥通信
    - rail-only 是只有 (leaf switch) - GPU 全连接，其他的砍掉不必要的
Reconfiguable Topology
- 动态适应

### 3.2.4 Load Balancing & Congestion Control
load Balancing
- 传统的不好用，因为LLM训练的通信是 elephant flow, 周期性大批的
    - 一个解决方式是在通信量大的路径上，增加多个平行路径， Llama 3 405B 训练在两个GPU之间加了16个link
congestion Control
- 主要是根据流量，切块，还有根据layer不同，进行调整


## 3.3 Storage
### 3.3.1 Storage Systems for Checkpoint
存 checkpoint 一般用分布式 file system
### 3.3.2 Storage Systems for Training Data
training data 的使用一般是 file system + caching 


## 3.4 Scheduling
cluster-level scheduling 和 task-level scheduling 不同, 不看微小的 single-job optimization, 而是看全局
### 3.4.1 Workload Scheduling
有 3 个feature
- heterogenuous-aware scheduler
    - 适应不同的 GPU
- job-packing scheduler
    - enable fine-grained GPU sharing to fully facilitate hardware capability
    - 尽可能用满 GPU? TODO 没太看懂
- adaptive-scaling scheduler
    - 动态面对 GPU 的扩缩容

新的架构有 hybrid parallelism + heterogenuous hardware; scale down model; 将类似的 job 合在一起的
### 3.4.2 Resource Scheduling
schedule 的资源包括 
- bandwidth
    - Cassini 协调波峰波谷, 通过 GPU/job 之间的亲和
    - HIRE, in-network 计算资源协调, 减少 detour
- storage
    - SiloD, 将 data cache & remote io 视为第一级资源 TODO 没懂
- cpu & memory
    - CPU core allocations instead of relying on GPU-proportional allocation TODO 没懂
- energy
    - 让 GPU 的 SM 多使用, 减少 switch frequency; 为了 energy 改 batch size
    - efficient graph cut-based iterative algorithm to obtain the iteration time-energy Pareto front for large model training job TODO 没懂

# 4 PARALLELISM SCHEMES FOR LLM TRAINING
SPMD
- single program multiple data 
MPMD
- multiple program multiple data
## 4.1 Hybrid Parallelism
### 4.1.1 Data Parallelism
sharding 但是是针对 model parameter, 每个机器上都有一个完整的模型到每一机器上有一部分
### 4.1.2 Tensor parallelism
intra-layer model parallelism
- 主要还是单 GPU 用
### 4.1.3 Pipeline Parallelism
inter-layer model parallelism \
相比 tensor parallelism, less frequent; 两个问题：
- Pipeline Bubble
    - 在 pipeline 上等的时间
    - 可在一个 node 上放多个 stage, 可能会 higher bandwidth & memory consumption
- Memory Imbalance
    - 前面几层比后面的要用更多的 memory
    - 有常见的 re-allocation, 比较有意思的是从两个方向计算, 相对就 balance 了
    - activation recomputation TODO 没懂
### 4.1.4 Sequence parallelism
- 长 sequence, 可 split
- self-attention with ring-style communication
- 把 head dimension 分了 (DeepSpeed-Ulysses)
### 4.1.5 Expert Parallelism
针对 Mixture-of-Experts (MoE), 大概是几个 transformer, 每个 transformer 各自对各自的 input 做 self-attention; 第一个 res 好了后 第二个 res 是所有 transformer 相互交流, 各自是各自 input 的 expert, 所以叫 mixture of input
- expert 可以放在不同的机器上
- 可用上面的 load balancing

## 4.2 Auto Parallelism 
## 4.3 Heterogeneous Parallelism
各种各样的方法, 主要是两个方面
- 怎么 schedule
    - 各种优化算法 DP, RL等等
- 怎么分割机器
    - *** 第17页讲了远距离低带宽的情况
        - 主要是分块, 然后高 bandwidth 的块可以处理需要多沟通的
        - communication compression

# 5 COMPUTATION OPTIMIZATIONS
## 5.1 Operator Optimizations
### 5.1.1 Manually Optimized Attention Operator
就是那些经典 attention 优化
### 5.1.2 Automatic Optimizations via Compilers
很多重复前面的 moe, 改善 operator chain 啥的
## 5.2 Mixed-precision Training
### 5.2.1 16-Bit Floating Point
减训练精度来提高速度

# 6 MEMORY OPTIMIZATIONS
## 6.1 Activation Recomputation
discard certain activation, 然后 backward 的时候重新计算
- de facto
### 6.1.1 Static Evicting
FlashAttention
### 6.1.2 Dynamic Evicting
greedy / recomputation
## 6.2 Redundancy Reduction
### 6.2.1 Fully Sharding
### 6.2.2 Partially Sharding
看情况, 有的地方就直接计算, 不 shard 了
## 6.3 Defragmentation
去掉不可用的 fragment
### 6.3.1 Tensor-based Defragmentation
consider tensor's life and size; bin packing, heuristic algorithm
### 6.3.2 VMM-based Defragmentation
virtual memory management
## 6.4 Offloading
把一部分运算和 data 从 GPU 上下放
### 6.4.1 CPU Offloading
### 6.4.2 Dynamic Offloading
### 6.4.3 SSD Offloading

# 7 COMMUNICATION OPTIMIZATIONS
## 7.1 Collective Communication
Message Passing Interface (MPI)
### 7.1.1 Pre-Defined Collective Communication Algorithm
Ring Algorithm
- for AllReduce
Tree Algorithm
- 相比 ring, latency 更低
### 7.1.2 Synthesized Collective Communication Algorithm
## 7.2 Communication Scheduling
### 7.2.1 FIFO-based Scheduling
### 7.2.2 Priority-based Scheduling
### 7.2.3 Decomposition-based Scheduling
## 7.3 In-Network Aggregation
### 7.3.1 Ethernet-based Aggregation
### 7.3.2 Infiniband-based Aggregation

# 8 FAULT TOLERANC
## 8.1 LLM Failure Analysis
## 8.2 Anomaly Detection
### 8.2.1 Statistical Monitoring
### 8.2.2 Proactive Validation
## 8.3 Checkpoint-Based Recovery
### 8.3.1 Persistent Checkpointing
### 8.3.2 In-Memory Checkpointing
## 8.4 Checkpoint-Free Recovery
### 8.4.1 Live Migration
### 8.4.2 Module Redundancy

# Idea 华为的 远程 NVSwitch
- melage, 不同的机器融合
- 任务归类，方便pipeline
- RL 在训练一下，得到pipeline 和 不同机器怎么配合
