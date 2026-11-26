# AI 前沿

> 抓取窗口：2026-10-27 ~ 2026-11-26｜数据来源：instagram 0 条、tiktok 0 条、grounding 0 条、github 5 条、reddit 0 条、hackernews 12 条、youtube 0 条

**证据不足提示：** 本期可用证据以 Hacker News 和 arXiv 标题为主，多数条目只有标题、没有正文。Reddit、TikTok、Instagram、YouTube、grounding 五个来源全部不可用，因此本期无法交叉验证任何一条消息，以下信号均按“单一来源”看待。

## 今天最值得知道的一件事

最近 48 小时内，可确认的新变化集中在“模型身份推测”和“智能体安全基准”两条线上：有博客称一个代号 Jev 的模型可能是 Qwen3.5-35B-A3B，arXiv 同日出现多篇针对智能体间接提示注入与训练分解的论文。除此之外，没有可确认的重大架构或权重发布。

## 值得看的信号

**Jev 被推测为 Qwen3.5-35B-A3B**
一篇博客以延迟特征为线索，推断代号 Jev 的模型可能是 Qwen3.5-35B-A3B。这是推测性结论，不是官方确认，也没有权重或技术报告佐证。同日 Hacker News 另有一条“Bare Metal Qwen”，指向在裸机环境跑 Qwen 的汇编项目，两件事放在一起看，说明社区对 Qwen 系列小模型的部署兴趣在升温。[原文](https://modaic.dev/blog/latency-doesnt-lie)｜[Bare Metal Qwen](https://github.com/alesha-pro/llm.asm/tree/main/02-baremetal-os)

**智能体安全：间接提示注入被单独拿出来做基准**
arXiv 11-25 收录《ContextLure: Exploiting Benign Conversation History for Indirect Prompt Injection》，研究如何利用看似无害的对话历史实施间接注入。同批还有一篇攻击改写绕过清洗器的论文（Antares-Smaug）。两篇都指向同一个问题：智能体的输入清洗在未见过的泛化样本上会失效。[ContextLure](https://arxiv.org/abs/2611.31424)｜[Antares-Smaug](https://arxiv.org/abs/2611.31347)

**智能体训练被拆成“学什么”和“学怎么用”**
《Learning What vs. Learning How: Decomposing Task and Interface Competence in Agentic Training》把智能体能力拆成任务能力与接口能力两部分分别考察。这是训练方法层面的分解，不是新模型发布。同批还有一篇多智能体治理结构的论文，讨论公平分配与策略防操纵。[Learning What vs. Learning How](https://arxiv.org/abs/2611.31427)｜[治理结构](https://arxiv.org/abs/2611.31284)

**基准侧：多模态与图表交互成为新方向**
11-25 的 arXiv 批次里出现两个新基准：MOZAIC 做音视频深度伪造检测，另一个做多模态大模型的交互式图表转代码生成。另有一个人际对话中“选择不说”的细粒度信息操纵基准。三个基准都指向“模型在真实交互中的行为”而非静态问答。[MOZAIC](https://arxiv.org/abs/2611.31301)｜[图表转代码](https://arxiv.org/abs/2611.31345)｜[信息操纵](https://arxiv.org/abs/2611.31346)

## 数据面板

| 来源 | 条目数 | 互动 | 状态 |
|---|---|---|---|
| hackernews | 12 | — | ok |
| github | 5 | — | ok |
| reddit | 0 | — | unreachable |
| tiktok | 0 | — | error |
| instagram | 0 | — | error |
| youtube | 0 | — | rate-limited |
| grounding | 0 | — | unreachable |

## 阅读提醒

- 五个来源（reddit、tiktok、instagram、youtube、grounding）本期全部断供，社区讨论面几乎空白。上面所有信号都只有单一来源，没有第二方印证。
- “Jev 是 Qwen3.5-35B-A3B”只是博客作者的推断，不是官方信息，不要当作已确认的模型发布。
- 接下来值得盯：Qwen 系列是否有官方权重或技术报告放出；arXiv 上智能体注入类论文是否出现配套的防御基准；以及 Hacker News 上 Edge0-145B 这类“本地跑前沿能力”的说法能否得到独立复现。

---

由 last30days v4.6.0 引擎 + RSS 新闻源抓证据、deepseek-chat 合成；生成时间 2026-11-26 00:33。
