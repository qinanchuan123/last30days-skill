# AI 周报

> 抓取窗口：2026-10-26 ~ 2026-11-25｜数据来源：grounding 5 条、hackernews 6 条、reddit 0 条

**证据不足提示：** 本期 reddit 完全不可达（0 条），hackernews 仅 6 条且多为单条新闻，grounding 5 条全是“发布追踪器”类页面而非具体发布事件。以下信号只能反映“有哪些话题在冒头”，不能当作完整发布清单。

## 一句话结论
本周没有可核实的单一重大模型发布，信号集中在两件事：AI agent 被外部平台限制（航司、移动操作系统），以及模型安全顾虑被内部员工公开化。

## 值得看的信号

**航司开始封堵 AI agent 代订机票**
United Airlines 禁止 AI agent 代替旅客订票。HN 讨论里有人质疑执行难度，提到用 Claude 浏览器插件或 computer-use agent 照样能操作，并形容自己与商家已形成“对抗关系”。对质量管理岗的意义：外部平台的 agent 准入规则正在变成合规变量。[来源](https://www.cbsnews.com/news/united-airlines-bans-ai-agents-booking-flights/)

**Signal 呼吁限制移动 OS 上的 AI agent 抓数据**
Signal 发文谈保护用户隐私，指向 AI agent 在移动操作系统层面获取过多设备数据。HN 评论引用 Meredith Whittaker 的访谈，称 Signal 正努力阻止这类应用读取 Signal 内容。这是 agent 权限边界问题的又一实例。[来源](https://signal.org/blog/protecting-your-privacy/)

**审计场景：AI agent 提问质量被拿来和 KPMG 会计师对比**
一则报道称在审计试验中 AI agent 提出的问题优于 KPMG 会计师。仅此一条来源，试验规模、方法、评审标准均未在证据中给出，结论需保留。[来源](https://europeanbusinessmagazine.com/ai-agents-better-questions-kpmg/)

**Anthropic 与 OpenAI 员工担忧未发布模型“不安全到不能发”**
报道称两家公司员工对尚未发布的模型存在安全顾虑。这是内部人视角的说法，证据中无具体模型名、无时间点，只能作为风险氛围信号。[来源](https://tech.yahoo.com/ai/claude/articles/scoop-anthropic-openai-employees-fear-104505580.html)

**DeepL 发布语音翻译模型 Aure**
DeepL 称 Aure 是其“最逼真”的语音 AI 翻译模型。证据只有官方新闻稿标题与一句描述，无参数、无评测数据。[来源](https://www.deepl.com/en/press-release/aure-voice-ai-model)

## 数据面板

| 来源 | 条目数 | 互动 | 状态 |
|---|---|---|---|
| grounding | 5 | — | ok |
| hackernews | 6 | — | ok |
| reddit | 0 | — | unreachable（搜索与多个引擎被限流） |

## 阅读提醒

- reddit 整条链路断掉，社区侧只有 HN 一个窗口，且 HN 条目多为单条新闻、无热度数字，不能据此判断话题真实热度。
- grounding 的 5 条都是发布追踪器首页，不是具体发布事件；本期无法给出“某模型某日发布”这类可核实条目，涉及发布的结论一律保留。
- 下期重点盯：agent 在消费平台与移动 OS 的准入规则是否有正式条款落地；两家实验室的安全顾虑报道是否出现具名模型或官方回应。

---

由 last30days v4.6.0 引擎抓取证据、deepseek-chat 合成；生成时间 2026-11-25 09:04。
