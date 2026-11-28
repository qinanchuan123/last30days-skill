# 芯片与算力

> 抓取窗口：2026-10-29 ~ 2026-11-28｜数据来源：grounding 0 条、instagram 0 条、tiktok 0 条、github 0 条、hackernews 0 条、reddit 0 条、youtube 0 条

**证据明显不足：本期没有任何一条落在半导体、先进制程、HBM、先进封装、GPU/ASIC 路线图、EDA 或出口管制主题上的证据。** 所有社区源（Reddit、YouTube、TikTok、Instagram、Hacker News、GitHub、grounding 搜索）均未返回条目；RSS 侧 10 条标题里，9 条是 Tom's Hardware 的黑五促销，1 条是 IEEE Spectrum 的人物报道，1 条是木星探测器任务。以下只写证据里确实存在的东西，不补任何数字或结论。

## 今天最值得知道的一件事

本期无重要变化——抓取窗口内没有出现任何与先进节点、HBM、先进封装、GPU/ASIC 路线图、EDA 或出口管制相关的可核实信号。

## 值得看的信号

**消费级 GPU 出现在整机促销里，仅此而已**
Tom's Hardware 报道一款联想 LOQ 笔记本搭载 Arc B390 显卡、Panther Lake 平台，黑五价 799 美元。这是本期唯一带具体芯片型号的条目，但属于零售促销，不构成产品路线图或产能信息。[链接](https://www.tomshardware.com/laptops/gaming-laptops/this-lenovo-loq-notebook-with-arc-b390-graphics-is-just-usd799-this-black-friday-get-a-gaming-ready-panther-lake-laptop-for-a-super-low-price)

**CPU 促销价，不是发布**
同一来源称 Ryzen 9 9950X3D2 降价 140 美元，9950X3D 降价 115 美元。只有价格事实，没有规格、出货量或架构变化的信息。[链接](https://www.tomshardware.com/pc-components/cpus/amds-ultimate-ryzen-9-9950x3d2-cpu-is-down-to-its-lowest-price-with-usd140-savings-single-cache-ryzen-9-9950x3d-is-also-on-a-deep-usd115-discount)

**存储侧只有 SSD 零售折扣**
SanDisk Optimus GX Pro 8100 2TB NVMe（PCIe 5.0）报道为 21% 折扣、每 GB 0.18 美元。这是消费级 SSD 的促销，与 HBM 或企业级存储供需无关，不能拿来推断存储周期。[链接](https://www.tomshardware.com/pc-components/sandisks-lightning-fast-optimus-gx-pro-8100-2tb-nvme-ssd-is-21-percent-off-and-usd0-18-cents-per-gb-usd349-for-a-pcie-5-0-m-2-ssd-is-about-as-good-as-it-gets-for-black-friday)

**非芯片主题，仅作来源状态参考**
IEEE Spectrum 一篇写某急诊医生成为医院首位临床 AI 工程师，一篇写木星冰卫星任务的工程设计。两条都不涉及算力硬件，列在此处只为说明 RSS 侧当天确实没有芯片选题。[临床 AI 工程师](https://spectrum.ieee.org/clinical-ai-engineer-dinesh-rai)｜[木星任务](https://spectrum.ieee.org/jupiter-europa-clipper-mission-jpl)

## 数据面板

| 来源 | 条目数 | 互动 | 状态 |
|---|---|---|---|
| grounding | 0 | — | unreachable（无密钥搜索不可用） |
| reddit | 0 | — | unreachable（无路径、搜索被限流） |
| youtube | 0 | — | rate-limited（需登录验证） |
| tiktok | 0 | — | error（oss discovery 为空） |
| instagram | 0 | — | error（oss discovery 为空） |
| hackernews | 0 | — | no-results |
| github | 0 | — | no-results |
| RSS（Tom's Hardware + IEEE Spectrum） | 10 | — | 正常返回，但无主题相关条目 |

## 阅读提醒

- 七个抓取源里五个是断的（grounding、reddit、youtube、tiktok、instagram），两个是空结果（hackernews、github）。本期等于只有 RSS 一条腿在跑，且 RSS 当天被黑五促销占满。任何“本期无芯片新闻”的判断都受这个采集缺陷限制，不能当成行业真的没动静。
- 唯一带芯片型号的两条（Arc B390 / Panther Lake、Ryzen 9 9950X3D2）都来自促销标题，只能确认“这些型号在售”，不能推出发布时间、产能或路线图。不要据此写产品节奏。
- 接下来该盯：先把 grounding 和 reddit 的抓取修好（doctor 提示已给出），否则先进节点、HBM、出口管制这类信息基本抓不到；RSS 侧建议加半导体专业源，避开促销季的消费硬件噪音。

---

由 last30days v4.6.0 引擎 + RSS 新闻源抓证据、deepseek-chat 合成；生成时间 2026-11-28 01:03。
