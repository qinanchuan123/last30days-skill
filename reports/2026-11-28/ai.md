# AI 前沿

> 抓取窗口：2026-10-29 ~ 2026-11-28｜数据来源：instagram 0 条、tiktok 0 条、grounding 0 条、github 6 条、reddit 0 条、hackernews 12 条、youtube 0 条

**证据不足提示：** 本期可用证据很薄。reddit、tiktok、instagram、grounding 全部不可达，youtube 被限流。可用的只有 hackernews 12 条、github 6 条，以及 19 条 RSS 标题。多数条目只有标题，没有正文，下面只写标题能支撑的事实。

## 今天最值得知道的一件事

Google 研究博客称 DeepCrossAttention 在模型质量相当的情况下最高快 3 倍，这是本期唯一带明确技术数字的新条目。[来源](https://research.google/blog/supercharging-transformer-residual-connections/)

## 值得看的信号

**DeepCrossAttention：残差连接的改造**
Google 研究博客 11-27 发文，称该方法在模型质量可比时最高快 3 倍。标题只给出这一层结论，没有说明基准、模型规模或对比对象。如果数字成立，它指向的是架构层面的效率改进，而不是继续堆参数。[来源](https://research.google/blog/supercharging-transformer-residual-connections/)

**Context Scaling 被提为新的扩展维度**
arXiv cs.AI 11-27 收录一篇题为《Context Scaling: A New Frontier of AI Scaling》的论文。标题把上下文长度与 scaling 并列，暗示研究重心从参数规模转向上下文。只有标题，无法判断它提出的是方法还是综述。[来源](https://arxiv.org/abs/2611.33160)

**AutoformBench：面向高等数学的形式化基准**
arXiv cs.AI 11-27 收录 AutoformBench，标题称其为“面向高级数学的 Lean 形式化基准”。这是基准类新条目，指向用 Lean 检验模型数学形式化能力的方向。具体题目规模和评测结果未知。[来源](https://arxiv.org/abs/2611.33165)

**出口管制 GPU 的“指纹”取证**
Hacker News 上一条帖子称，中国前沿 AI 模型带有出口管制 GPU 的指纹。社区片段提到，中国公司可以远程使用位于新加坡或马来西亚的 GPU，这与美国出口管制并不冲突。这是取证方法层面的讨论，不是官方结论，需谨慎看待。[来源](https://unemploymentlabs.com/checkpoint-forensics)

## 数据面板

| 来源 | 条目数 | 互动 | 状态 |
|---|---|---|---|
| hackernews | 12 | — | ok |
| github | 6 | — | ok |
| reddit | 0 | — | unreachable |
| tiktok | 0 | — | error |
| instagram | 0 | — | error |
| youtube | 0 | — | rate-limited |
| grounding | 0 | — | unreachable |

## 阅读提醒

- 六个来源里四个是断的，youtube 被限流。本期没有社区热度和视频侧证据，判断“什么在发酵”的能力受限。
- DeepCrossAttention 的“3 倍”只有 Google 自家博客一个来源，且是标题级信息，没有第三方复现，先当作待验证的声明。
- 接下来值得盯：Context Scaling 那篇论文的正文、AutoformBench 的实际评测结果，以及 Nvidia 暂停对东南亚出货（11-26）是否影响后续算力叙事。[来源](https://techcrunch.com/2026/11/26/nvidia-hits-pause-on-chip-shipments-to-southeast-asia/)

---

由 last30days v4.6.0 引擎 + RSS 新闻源抓证据、deepseek-chat 合成；生成时间 2026-11-28 01:02。
