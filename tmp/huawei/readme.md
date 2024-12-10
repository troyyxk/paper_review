

Huawei Cloud is the cloud brand of Huawei Group and curently ranks as the second larest cloud service provider in China and the fith inthe world. Computing and network innovation ab is exploring how to utilize Linggu and UB networks to connect geo-distributed data centersalming to provide large-scale cloud network services. This also includes cloud services for training and inference tasks. We are studyingnetwork transmission optimization technologies for Al large model training across regions (across data centers with a distance of 2000 km to3000 km).There are many technical challenges in this
Currently, we are looking for patners in this field to jointly research on the collaborative support of multimodal models by cloud datacenterslEdge-cloudidevices, as well as how cloud networks can iteratively support LLM (including long context and multimodal models)
am reaching out to see if we could schedule a one-hour online meeting at your convenience. l would appreciate the opportunity to discusspotential colaboration and share insights related to our work. lf it is convenient for you, could you please provide two time slots that areconvenient for you?
Thank you very much for your time and consideration. Looking forward to your reply
Best regards,
冷浕伶 /Leng Jinling(Ph.D.)
华为云计算技术有限公司 架构与技术创新部 技术规划团队Huawei Cloud Computing Technologies Co. td. Architecture & Technical Planning Dept, Technology Planning and Cooperation Team中国(China)-北京(Beiiing)-海淀区(Haidian)-华为北京研究所-华为大厦Huawei Beiing Research Center, Xinxi Road 3#, Haidian, Beiing. P.R.ChinaMobile/x:13190078478
E-mail:lengiinling@huawei.com

# ######################################################################################################

Professor Du, looking forward to seeing you next Monday. In prepration for our conversation, we have a few topics we would like to explore:
1. Building Super cluster for Al Training and Inference: How can we improve scale-up network performance? For instance, how to make a single server with perform better than two servers with 8 GPUs each(also totaling 16 GPUsGPUs)?

2. Technical Preparedness for Large Data Centers: What are the technological considerations for mLLM in large data centers in terms of network、 computing、 architecture？

3. Comparative Performance of Cloud Inference vs. On-Premise Servers: In what ways might cloud-based inference outperform self-hosted servers (in terms ofcompute power, networking, etc.)?

# ######################################################################################################

Related papers:
```
[1] Efficient   Training of Large Language Models on Distributed Infrastructures: A Survey
[2] Google Cloud demonstrates the world’s largest distributed training job for large language models across 50000+ TPU v5e chips
[3] Fine-Tuning Large Language Models: A Guide into Distributed Parallel Training with DeepSpeed, Ray, and Instruction Following
[4] Harnessing Distributed Training for LLMs: Single-Node and Multi-Node Configurations with UCX on InfiniBand
[5] Mélange Cost Efficient Large Language Model Serving by Exploiting GPU Heterogeneity
[6] AWS Migration Hub Documentation
    - https://docs.aws.amazon.com/migrationhub/latest/ug/whatishub.html
[7] 李沐 创业一年，人间三年
    - https://www.bilibili.com/opus/965508248739250195?spm_id_from=333.999.0.0
```

# ######################################################################################################

1. Building Super cluster for Al Training and Inference: How can we improve scale-up network performance? For instance, how to make a single server with perform better than two servers with 8 GPUs each(also totaling 16 GPUsGPUs)?
- 关于 cluster 扩容, 同等资源大 cluster 效率更高，怎么做到
### TODO 这个是 geo-distributed 么？
- 假设不是 geo-distributed:
    - [1] 3.2.1 Chip-to-Chip Communications
        - 保证内部bandwidth, 能学 NVlink么?
        - 谷歌的 2D/3D-Torus Topology, 没看懂为啥比全连接好 TODO
    - [1] 3.2.3 Network Topology
        - netowrk topology, 减少不必要的线路
            - 和16比2*8强关系不大
- [1] 3.2.2 Node-to-Node Communications
    - Remote Direct Memory Access (RDMA)
- [1] 4.1.1 Data Parallelism [1] 4.1.3 Pipeline Parallelism
    - sharding of model and data can utilize 

# ######################################################################################################

2. Technical Preparedness for Large Data Centers: What are the technological considerations for mLLM in large data centers in terms of network、 computing、 architecture？
### TODO mLLM 的 m 是 modelar 还是 multi-modal, training和普通 LLM 有啥区别么
- large data center 应该会有多种机器
    - 组合一起用更好
    - [5] 还能省钱
- 技术大纲可以从 [1] 里看

# ######################################################################################################

3. Comparative Performance of Cloud Inference vs. On-Premise Servers: In what ways might cloud-based inference outperform self-hosted servers (in terms ofcompute power, networking, etc.)?
- mostly form [6] AWS documentations
- easy scale up and down
- pay as needed
- larger variaty of machine
    - for LLM, different tasks
- do not need to worry about maintaince
- huawei control internal networking
    - can use huawei network, if they have any
- expertise in assemble and operate cluster
    - [7] 专业人士在组装上手的时候也会碰到问题
    - 而且华为是自己的硬件，内部沟通解决问题更方便

    

