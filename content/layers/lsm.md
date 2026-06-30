---
status: AA-mother-source-entry
purpose: AI协作者单文件入口
scope: LSM 的定位、核心概念、推导链、关键命题、跨层接口与术语
audience: AI协作者、自动化代理
canonical_sources:
  - SOURCE_OF_TRUTH.md
  - AA-母版源层/
  - CC-独立理论层/
  - PUBLISH_READINESS.md
required_reads:
  - 00-索引与导航/AI修改必读-理论体系治理原则-4AI.md
  - SOURCE_OF_TRUTH.md
  - PUBLISH_READINESS.md
inputs: SOURCE_OF_TRUTH.md + AA-母版源层 + CC-独立理论层 + PUBLISH_READINESS.md
outputs: lsm_pattern_hypothesis、结构化总览、术语映射、接口声明
non_outputs: 不产生新理论命题、不替代母版正文、不替代独立法源、不发布放行
mandatory_rules:
  - SOURCE_OF_TRUTH、AA/CC 源层与 PUBLISH_READINESS 是法源，本文件只是压缩入口
  - 不得产生比 SOURCE_OF_TRUTH、母版、独立法源或发布准备文件更强的主张
  - 高风险、临床、法律、医疗、投资、责任或工程放行问题必须转介到对应层或专业渠道
forbidden_actions:
  - 不得修改母版正文的主张强度
  - 不得把 LSM 包装成诊断、人格分类、命运判断、道德终裁、责任终裁或工程放行系统
  - 不得跳过 COP/PFM 复核直接进入 TAT 责任裁决
update_checklist:
  - AA/CC 有新命题时同步更新
  - 每次发布前校验 PUBLISH_READINESS
  - 每次路径迁移后校验真实文件路径
handoff_note: 修改后通知各下游层 4AI 文件维护者
---

# AI 人生察局学总览（LSM）

> **层序**：第 7 层（编号 52），实践链第 2 层
> **定位**：前线结构识别 + 责任流向观察 + 识局假设方法
> **术语说明**：公开口径统一为“识局 / 察局 / 责任流向观察 / 行动假设”；“判局/诊断”为历史内部词
> **本质**：一套把上游结构语言转写为前线可调用识局语言的方法论；不等于人格学，不等于成功学

---

## 一句话定义

**LSM 先回答“责任现在正沿哪条错误路径在流”，再形成最低止流动作和转交建议。**

---

## 核心概念

| 概念 | 含义 |
|------|------|
| 责任流向 | 责任在组织/协同系统中如何从源头移动到承压点 |
| 承压点 | 责任最终落到的节点；谁在承受后果 |
| pattern_hint | 当前信号更像哪类责任流向原型的可撤回假设 |
| action_blockage | 当前行动被责任错位、权责割裂或灰区沉积阻塞的位置 |
| minimum_stop_flow_action | 在不越权的前提下，先阻断错误责任流动的最低动作 |
| handoff_target | COP / PFM / RT6 / professional_channel / none |
| escalation_hint | TAT / ODD / professional_channel / none；只作提示，不直接裁决 |

---

## 推导链

```text
可观测信号 -> 承压点 -> 责任流向 -> pattern_hint -> action_blockage
           -> minimum_stop_flow_action -> handoff_target / escalation_hint
```

| 步骤 | 输入 | 输出 | 核心问题 |
|------|------|------|----------|
| 定位承压点 | 任务、冲突、责任、后果信号 | 承压角色/节点 | 这件事最终压在谁身上 |
| 追溯流向 | 承压点与上下游关系 | responsibility_flow | 责任是怎么流到这里的 |
| 标注原型 | 流向证据 | pattern_hint + confidence | 当前更像哪类责任流向失衡 |
| 找行动阻塞 | 权限、资源、信息、边界 | action_blockage | 为什么动不了或越动越错 |
| 设最低动作 | 风险、置信度、边界 | minimum_stop_flow_action | 先阻断什么，不做什么 |
| 转交 | 风险与越界条件 | handoff_target / escalation_hint | 是否转 COP、PFM、RT6 或专业渠道 |

---

## 五类责任流向原型

| 原型 | 中文名 | 核心流向 | 最低识别句 |
|------|--------|----------|------------|
| downward | 下行型 | 责任从应负责者滑向不应负责者 | “没人明确负责，最后落到最能扛的人身上。” |
| diffuse | 扩散型 | 临时补位、善意帮忙或能力者默认接盘逐渐变成长期责任 | “帮一次，后来就成了你的固定职责。” |
| explosive | 爆发型 | 平时不定责，事故或冲突时责任突然集中释放 | “平时没人签，出事第一个找最近执行者。” |
| accumulative | 堆积型 | 灰区任务、历史债务、例外事务长期沉积 | “没人清理的杂事慢慢都堆到同一人身上。” |
| split | 割裂型 | 结果责任与决策权、资源、信息或控制权被切开 | “要你负责结果，但不给你决定权。” |

五局是当前责任流向原型集，不是人格类型、命运分类、临床诊断或封闭完备分类。

---

## 关键命题

1. LSM 的价值不在于它总能给出答案，而在于它让前线先看出“责任现在正沿哪条错误路径在流”。
2. 许多协同困局不是能力问题，而是责任流向在结构中发生失衡。
3. 看信号不看性格；信号是可观察事件，不是人格归因。
4. 识局不是算命；它是可撤回的责任流向假设。
5. 先止流再谈优化；阻断错误流向优先于改造整个结构。
6. `confidence=high` 只表示当前假设更稳，不等于事实确定、低风险证明或责任裁决。
7. TAT 只能作为 `escalation_hint` 或 `requires_tat_review`，实际升级必须经 COP、PFM 边界承接或专业复核。

---

## 固定边界

LSM 不负责：

- 不替代 ASTO 的桥接职责与状态语言；
- 不替代 COP 的冻结与转介协议；
- 不替代 TAT 的责任门槛、补偿、追责或责任闭合判断；
- 不替代 PFM 的问题显影、低阻自检、边界承接、转交或停止；
- 不替代 RT6 的个人技能提升承接；
- 不替代 ODD 的审计封存、工程承诺和回滚；
- 不做人格分类、命运判断、临床诊断、心理治疗、道德评判、法律/医疗/投资建议、责任终裁或工程放行。

### 弱依赖定位

本文件不依赖强 DM/ASTO/ARBT/TAT/COP 才能成立。LSM 从协同实践出发，承认责任流向不清、承压点反复出现、权责割裂、灰区任务堆积是组织/协同场景常见的结构问题。

---

## 跨层接口

| 方向 | 接口内容 |
|------|----------|
| <- PFM | PFM 在用户说不清“卡在哪”时调用 LSM 识局能力 |
| <- COP | COP 在 FREEZE / UNKNOWN / 结构困惑场景请求 LSM 提供责任流向假设 |
| -> COP | 高风险、低置信、混合信号、危机或专业超界转 COP |
| -> PFM | 低中风险问题显影、前线接引和现实承接 |
| -> RT6 | 只通过 `lsm_to_rt6_action_candidate` 提供行动承接候选输入；RT6 必须复核 COP 低风险、用户同意、边界、停止条件和回看机制 |
| -> TAT | 只允许 `escalation_hint` / `requires_tat_review`，不直接裁决 |
| -> ODD | 涉工程执行、审计封存、证据留痕或回滚需求 |

---

## 不可替代问题与失败线

> 不可替代问题详见 `CC-独立理论层/LSM.007-不可替代问题与外部比较.md`
> 失败线详见 `CC-独立理论层/LSM.008-失败线与不可替代补充论证.md`

LSM 解决的独特问题是：人在组织中反复“卡住”，不一定因为不够努力或不够聪明，而可能是责任在结构中沿错误路径流动，且当事人看不见这个流动。

整体失效条件：

| 编号 | 失效条件 | 后果 |
|------|---------|------|
| F1 | 五类原型无法覆盖足够比例的协同困局案例 | 原型集需扩展或降级 |
| F2 | 多个独立判别者对同一案例识局不一致 | 识局方法不可复述 |
| F3 | 五局被人格化、命理化或用于贴标签 | 结构语言失效，必须退出 |

---

## 当前阅读入口

1. `SOURCE_OF_TRUTH.md` — 当前唯一真相源、canonical output、non-output 和发布阻塞项。
2. `PUBLISH_READINESS.md` — 当前可发布状态和禁止外发边界。
3. `AA-母版源层/README.md` — 母版主链导航。
4. `AA-母版源层/LSM.001-人生察局学-核心理论文章.md` — 核心理论主文。
5. `AA-母版源层/LSM.004-与COP及PFM的接口规范.md` — 转接纪律。
6. `CC-独立理论层/README.md` — 独立成立口径。
7. `CC-独立理论层/LSM.007-不可替代问题与外部比较.md`。
8. `CC-独立理论层/LSM.008-失败线与不可替代补充论证.md`。
9. `FF-工程执行层/LSM-kappa-test-framework.md` — 评判者一致性测试入口。

---

## 前线最短输出格式

```yaml
lsm_pattern_hypothesis:
  source_layer: LSM
  pattern_hint:
    primary_pattern: downward | diffuse | explosive | accumulative | split | unknown
    secondary_pattern: downward | diffuse | explosive | accumulative | split | none
  responsibility_flow: ""
  action_blockage: ""
  confidence: low | medium | high
  minimum_stop_flow_action: ""
  handoff_target: COP | PFM | RT6 | professional_channel | none
  escalation_hint: TAT | ODD | professional_channel | none
  requires_tat_review: false
```

---

## 术语表

| 缩写 | 全称 | 中文 |
|------|------|------|
| LSM | Life Situational Methodology | 人生察局学 |
| COP | Cognitive Computing Protocol | 认知计算协议 |
| DM | Differential Monism | 差异一元论 |
| ASTO | Attribute-Set Transition Ontology | 属集变迁存在论 |
| TAT | The Accountability Threshold | 责任锚定与阈值理论 |
| PFM | Problem Framing Method | 问题显影方法 |
| WSH | Whole Self Harmony | 和悦论 |
| RT6 | Resonance & Transition 6-Step | 共鸣与跃迁六步法 |
| ODD | Output-Driven Development | 产出物驱动开发 |

---

## LSM-min 与完整 LSM 的关系

LSM-min 是完整 LSM 的识局假设 ABI，只保留 `pattern_hint`、`responsibility_flow`、`action_blockage`、`confidence`、`minimum_stop_flow_action`、`handoff_target` 等跨层转交字段。它不替代完整 LSM 的五局模型、识局四步法、弱测量纪律、主局/次局标注、交叉局型、止流/边界/升级行动原则和跨层转接纪律。

当 `handoff_target=RT6` 时，LSM 可附带 `lsm_to_rt6_action_candidate`。该对象只表示责任流向观察、行动阻塞和最低止流动作可供 RT6 复核，不等于 RT6 的 `non_clinical_action_plan`。

当前验证等级为 C1-C2。不得声称真实世界有效、稳定识别五局或认证级可靠。需建设 30+ 匿名案例、多人一致性测试和误判成本矩阵。
