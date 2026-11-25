# AI 周报

> 抓取窗口：2026-10-26 ~ 2026-11-25｜数据来源：grounding 5 条、hackernews 6 条、reddit 0 条

**证据不足提示：** 本期 reddit 完全不可达，实际可用条目仅 11 条，且多数为追踪器首页或标题级信息。以下结论只能当作线索，不能当作定论。

## 一句话结论
本周能确认的硬事实只有一条：上海 AI 实验室于 11 月 16 日开源了科学多模态 agent 模型书生 S2.1 Flash（MIT 许可）；其余“发布”信息均来自聚合追踪器，未经一手来源核实。

## 值得看的信号

**书生 S2.1 Flash 开源，许可宽松**
上海 AI 实验室的科学多模态 agent 模型于 2026 年 11 月 16 日发布并开源，采用 MIT License，在 Hugging Face 和 ModelScope 上提供 BF16 与 FP8 两种权重。这是本期唯一带具体日期、许可和分发渠道的条目，对需要本地部署或二次微调的团队有直接参考价值。[来源](https://www.llm-releases.com/)

**11 月发布量被追踪器量化为“37 家厂商、50 个模型”**
AIFOD 的实时追踪页称 2026 年 11 月有 37 家厂商发布 50 个模型，其中 25 个为开放权重，并点名 GPT-6.2 Astra、Gemini 4 Neon、Kimi K3。这些数字和型号只出现在该追踪器一处，没有厂商公告佐证，引用前需回查原始发布页。[来源](https://af.net/realtime/ai-model-releases-november-2026/)

**模型发布追踪器本身成了信息基础设施**
四个 grounding 条目都是追踪器：llm-releases.com、siliconainews 的 tracker（自称 60 条、覆盖 26 家公司）、scriptbyai 的发布日历、aireleasetracker（自称跟踪 343 个模型、11 家公司）。它们口径不一、互不引用，说明当前模型发布信息高度碎片化，质量岗若要做模型选型对比，得自己建一手清单。[来源](https://siliconainews.com/tracker/ai-model-releases)｜[来源](https://aireleasetracker.com/)

**agent 落地开始撞上制度边界**
美联航禁止 AI agent 代客订票；Signal 发文谈限制移动操作系统上的 AI agent 抓取数据。HN 讨论里有人直接质疑执行可行性（“他们打算怎么阻止我用 Claude in chrome”），也有人提到 Signal 正艰难阻止这类应用读取其数据。对制造业质量岗的启示：agent 接入外部系统时，对方平台的准入政策可能比技术能力更早成为约束。[来源](https://www.cbsnews.com/news/united-airlines-bans-ai-agents-booking-flights/)｜[来源](https://signal.org/blog/protecting-your-privacy/)

**审计场景出现 agent 对比实验，但只有标题级信息**
一条 HN 条目称“AI agents 在审计试验中比 KPMG 会计师提出更好的问题”。证据里只有标题，没有样本量、试验设计或评判标准，无法判断结论强度。若后续有一手报告，这类“提问质量”指标对质量审核、内审流程的 agent 评估有借鉴意义。[来源](https://europeanbusinessmagazine.com/ai-agents-better-questions-kpmg/)

## 数据面板

| 来源 | 条目数 | 互动 | 状态 |
|---|---|---|---|
| grounding | 5 | — | ok |
| hackernews | 6 | — | ok |
| reddit | 0 | — | unreachable（no path served；search blocked；brave/ddg/startpage 均被限流） |

## 阅读提醒

- **reddit 整条链路是断的**，本期没有任何社区一手讨论，HN 片段也只是零散评论，社区情绪类判断一律不要下。
- **发布类信息只有一处来源**：11 月的厂商数、模型数、GPT-6.2 Astra / Gemini 4 Neon / Kimi K3 等型号均出自单一追踪器，未经交叉验证，不要写进对外材料。
- **下期该盯**：书生 S2.1 Flash 的实际评测与采用情况；美联航禁令和 Signal 表态是否引发其他平台跟进；KPMG 审计试验是否有完整报告释出。

---

由 last30days v4.6.0 引擎抓取证据、deepseek-chat 合成；生成时间 2026-11-25 09:12。
