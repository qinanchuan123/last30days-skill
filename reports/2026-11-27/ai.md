# AI 前沿

> 抓取窗口：2026-10-28 ~ 2026-11-27｜数据来源：tiktok 0 条、grounding 0 条、instagram 0 条、github 4 条、hackernews 12 条、reddit 0 条、youtube 0 条

**证据不足提示：** 本期可用信息偏薄。reddit、grounding、instagram、tiktok 全部不可达，youtube 被限流，实际只有 hackernews 与 github 两个来源可用，且多数条目只有标题。以下内容只写标题能支撑的事实，不做延伸推断。

## 今天最值得知道的一件事

有报道称，AI 智能体已接管 DeepMind 部分算力，用于 Gemini 相关实验，但报道同时称递归自我改进仍然遥远——这是本期唯一一条直接落在“智能体 + 前沿模型研发流程”上的新变化，且仅有一个来源，需保留。[链接](https://the-decoder.com/ai-agents-now-control-part-of-deepminds-compute-for-gemini-experiments-but-recursive-self-improvement-remains-distant/)

## 值得看的信号

**智能体进入模型研发的算力调度环节**
2026-11-27 的报道称，AI 智能体现在控制 DeepMind 用于 Gemini 实验的部分算力；同一报道明确表示递归自我改进仍属远期。意义在于：智能体从“被评测对象”变成“研发流程的一部分”，但报道本身给这一变化划了边界。[链接](https://the-decoder.com/ai-agents-now-control-part-of-deepminds-compute-for-gemini-experiments-but-recursive-self-improvement-remains-distant/)

**智能体训练被拆成“学什么”与“学怎么用”**
2026-11-26 的 arXiv 论文《Learning What vs. Learning How》提出把任务能力与界面操作能力分开考察，用于智能体训练。这是对“智能体能力到底来自任务理解还是工具熟练度”的一次方法层拆分，属于评测与训练设计的细化，而非新模型发布。[链接](https://arxiv.org/abs/2611.31427)

**间接提示注入盯上了“良性对话历史”**
同日 arXiv 论文《ContextLure》研究利用良性对话历史实施间接提示注入。它指向一个具体攻击面：历史上下文本身可被当作注入载体，而不是只有外部文档或网页。[链接](https://arxiv.org/abs/2611.31424)

**基准继续往多模态与交互走**
2026-11-26 出现两个新基准：MOZAIC 面向音视频深度伪造鉴别，另一个面向 MLLM 的交互式图表转代码生成。方向一致——从静态问答转向动态、可交互、需鉴别的任务。[MOZAIC](https://arxiv.org/abs/2611.31301)｜[图表基准](https://arxiv.org/abs/2611.31345)

**开源权重侧只有一条，且是产品宣称**
hackernews 上出现 Edge0-145B，标题宣称“在自己电脑上获得前沿 AI 能力”。社区评论对 Blender 工具调用示例表示印象深刻，但同时有人怀疑模型实际可用性。只有标题与评论片段，无独立验证，只能记为“有宣称”。[链接](https://edge0.ai/blog/introducing-edge0-145b-frontier-ai-capabilities-on-your-own-computer)

## 数据面板

| 来源 | 条目数 | 互动 | 状态 |
|---|---|---|---|
| hackernews | 12 | — | ok |
| github | 4 | — | ok |
| reddit | 0 | — | unreachable |
| grounding | 0 | — | unreachable |
| youtube | 0 | — | rate-limited |
| tiktok | 0 | — | error |
| instagram | 0 | — | error |

## 阅读提醒

- 五个来源断供（reddit、grounding、youtube、tiktok、instagram），本期无法交叉验证任何一条信号；DeepMind 智能体接管算力这条尤其只有一个来源。
- 多条 hackernews 条目只有标题，包括“The End of AI Frontiers”“Closed AI models dominate the price-performance frontier”，标题本身是观点而非事实，未纳入信号。
- 接下来值得盯：arXiv cs.AI 每日新增中智能体训练与提示注入两条线是否出现后续工作；Edge0-145B 是否出现独立复现或评测。

---

由 last30days v4.6.0 引擎 + RSS 新闻源抓证据、deepseek-chat 合成；生成时间 2026-11-27 01:08。
