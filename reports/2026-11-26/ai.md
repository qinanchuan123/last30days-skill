# AI 前沿

> 抓取窗口：2026-10-27 ~ 2026-11-26｜数据来源：tiktok 0 条、grounding 0 条、instagram 0 条、github 5 条、hackernews 12 条、reddit 0 条、youtube 0 条

**证据不足提示：** 本期可用证据几乎全部来自 Hacker News 与 arXiv 标题列表。Reddit、YouTube、TikTok、Instagram、grounding 五个来源全部不可用，因此无法交叉验证任何一条消息的热度或真实性。以下内容只反映“有报道/有帖子”，不代表已确认的重大进展。

## 今天最值得知道的一件事

最近 48 小时内没有可确认的重大模型或架构发布；唯一带日期的技术性信号，是一篇博客推测某匿名模型“Jev”可能是 Qwen3.5-35B-A3B，属于推测而非官方发布。（[modaic.dev](https://modaic.dev/blog/latency-doesnt-lie)）

## 值得看的信号

**匿名模型“Jev”被推测为 Qwen3.5-35B-A3B**
11 月 25 日的博客从延迟特征反推模型身份，认为 Jev 大概率是 Qwen3.5-35B-A3B。这是推断，不是厂商公告，模型参数与归属都未经证实。同日 Hacker News 上还有一条“Bare Metal Qwen”，把 Qwen 跑在汇编级裸机环境里，说明围绕 Qwen 系列的工程实验在活跃。（[modaic.dev](https://modaic.dev/blog/latency-doesnt-lie)、[GitHub](https://github.com/alesha-pro/llm.asm/tree/main/02-baremetal-os)）

**Edge0-145B 宣称在本地机器上跑出前沿能力**
项目博客称 145B 模型可在个人电脑上提供“前沿 AI 能力”，社区片段特别提到 Blender 工具调用案例，认为工具使用的复杂度已到能替代人数天工作量的程度。但同一片段也明确表达怀疑：实际模型是否可用存疑。这是单来源、无日期的宣传性内容，只能当作待验证的说法。（[edge0.ai](https://edge0.ai/blog/introducing-edge0-145b-frontier-ai-capabilities-on-your-own-computer)）

**智能体方向的新论文集中在治理、注入与训练分解**
11 月 25 日 arXiv cs.AI 出现多篇相关标题：自主智能体系统的治理结构设计、间接提示注入（ContextLure，利用良性对话历史）、以及把智能体训练拆成“学什么”与“学怎么用接口”两类能力。另有交互式图表转代码的多模态基准。这些只有标题，没有摘要结论，不能推断效果好坏。（[治理结构](https://arxiv.org/abs/2611.31284)、[ContextLure](https://arxiv.org/abs/2611.31424)、[Learning What vs. Learning How](https://arxiv.org/abs/2611.31427)、[图表基准](https://arxiv.org/abs/2611.31345)）

**出口管制与算力地理成为前沿模型的讨论背景**
一篇取证分析称中国前沿模型的训练痕迹带有出口管制 GPU 的“指纹”，并指出中国企业可远程使用位于新加坡、马来西亚的 Nvidia GPU，这与美国出口管制并不冲突。另一篇 CSA 研究笔记讨论中国商务部 2026 年第 48 号公告，即中国首套前沿 AI 出口管制。两条都无明确发布日期，只能算背景材料。（[checkpoint-forensics](https://unemploymentlabs.com/checkpoint-forensics)、[CSA](https://labs.cloudsecurityalliance.org/research/csa-research-note-china-ai-export-controls-announcement-48-2/)）

## 数据面板

| 来源 | 条目数 | 互动 | 状态 |
|---|---|---|---|
| hackernews | 12 | — | ok |
| github | 5 | — | ok |
| reddit | 0 | — | unreachable |
| youtube | 0 | — | rate-limited |
| tiktok | 0 | — | error |
| instagram | 0 | — | error |
| grounding | 0 | — | unreachable |
| 外部 RSS | 32 | — | 正常返回 |

## 阅读提醒

- 五个来源（Reddit、YouTube、TikTok、Instagram、grounding）全断，本期判断建立在极窄的证据面上，任何“趋势”结论都应保留。
- Edge0-145B 与“Jev 是 Qwen3.5-35B-A3B”都只有单一来源，且前者是宣传博客、后者是延迟推断，均不可当作已确认事实。
- 接下来值得盯：Qwen 系列是否有官方发布确认；Edge0 是否放出可复现的权重或评测；arXiv 上 ContextLure 一类提示注入工作是否给出可量化的攻击成功率。

---

由 last30days v4.6.0 引擎 + RSS 新闻源抓证据、deepseek-chat 合成；生成时间 2026-11-26 01:04。
