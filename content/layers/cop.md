---
status: AA-mother-source-entry
purpose: AI协作者单文件入口
scope: COP 的定位、核心概念、推导链、关键命题、跨层接口与术语
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
outputs: 结构化总览、术语映射、接口声明
non_outputs: 不产生新理论命题、不替代母版正文、不替代独立法源、不发布放行
mandatory_rules:
  - SOURCE_OF_TRUTH、AA/CC 源层与 PUBLISH_READINESS 是法源，本文件只是压缩入口
  - 不得产生比 SOURCE_OF_TRUTH、母版、独立法源或发布准备文件更强的主张
  - 高风险、临床、法律、医疗、投资、责任或工程放行问题必须转介到对应层或专业渠道
forbidden_actions:
  - 不得修改母版正文的主张强度
  - 不得把 COP 包装成诊断、治疗、人格分类、法律/医疗/投资建议、责任终裁或工程放行系统
  - 不得跳过风险分流直接进入实践动作
update_checklist:
  - AA/CC 有新命题时同步更新
  - 每次发布前校验 PUBLISH_READINESS
  - 每次路径迁移后校验真实文件路径
handoff_note: 修改后通知各下游层 4AI 文件维护者
---

# AI 认知计算协议总览（COP）

> **层序**：第 6 层（编号 51），实践链第 1 层
> **定位**：结构分流（非临床）+ 风险分流 + 转介协议层
> **本质**：一套有界的认知计算协议；不等于问卷，不等于万能解释器
> **术语说明**：公开主词统一为“结构分流 / risk routing / triage”；“诊断”为历史兼容词，已 deprecated

---

## 一句话定义

**COP 先回答“当前是否清楚、是否安全、是否应继续”，再决定转 RT6、TAT、ODD 或专业渠道。**

---

## 核心概念

| 概念 | 含义 |
|------|------|
| 采样帧 | 原始现实信号经 P1 转换后的结构化输入单元 |
| 编码向量 | 采样帧经 P2 映射到 COP 编码空间的输出 |
| 结构标签 | 编码过程中附加的类型标记，不等于解释或诊断 |
| 分流状态 | P3 输出的 `triage_status`，决定后续动作权限 |
| 置信度 | `confidence`，结构分流的可靠程度，不等于低风险证明 |
| 结构风险 | `risk`，当前状态的系统性风险评级 |
| 证据缺口 | `evidence_gap`，继续判断前必须补齐或记录的不确定项 |

---

## 推导链：五协议管线

COP 由五份协议组成一条结构分流管线，每一步把前一步的输出转写为更可计算、可复核、可转介的形式：

```text
P1 输入采样 -> P2 状态编码 -> P3 分流判定 -> P4 转介与有限干预 -> P5 反馈校准
   ^                                                               |
   +--------------------- 校准结果回流到采样策略 ------------------+
```

| 协议 | 输入 | 输出 | 核心问题 |
|------|------|------|----------|
| P1 输入采样 | 原始现实信号 | 结构化采样帧 | 我们看到了什么 |
| P2 状态编码 | 采样帧 | 编码向量 + 结构标签 | 这接近什么状态 |
| P3 分流判定 | 编码向量 | 分流状态 + 置信度 + 风险 | 当前是否清楚、是否安全 |
| P4 转介与有限干预 | 分流状态 | 动作边界 + 转介路由 | 接下来该做什么，不能做什么 |
| P5 反馈校准 | 真实结果 | 协议参数更新与回滚记录 | 我们上次判断对了吗 |

P2 编码前须先继承 `AA-母版源层/COP.031-结构编码前置接口.md` 的结构编码纪律，而非跳过结构直接从表面标签起步。

---

## 五种分流状态

COP 输出的 `triage_status` 共五种，优先级从高到低：

```text
ESCALATE > FREEZE > UNKNOWN > REFER > CONTINUE
```

| 状态 | 含义 | 允许动作 | 必须转介 |
|------|------|----------|----------|
| ESCALATE | 紧迫风险或硬边界触发 | 停止一切自动推进 | 立即转有权限的决策者或专业渠道 |
| FREEZE | 冲突或高风险，不可继续压缩 | 停止推进，不做强引导 | 转人工；高影响时转 TAT/ODD |
| UNKNOWN | 信息不足，不能稳定判断 | 补材料、弱测量、延迟进入 | 回 COP 补证；必要时转人工 |
| REFER | 需外部专业判断 | 可做接引，不可做结论替代 | 转 TAT / 领域专家 / 专业渠道 |
| CONTINUE | 可安全进入下一步 | 允许推进到 RT6 或后续承接 | 高影响动作前仍过 TAT/ODD |

---

## 关键命题

1. COP 的价值不在于它总能回答，而在于它知道何时不该继续自动回答。
2. 采样只管“收进来”，不管“对不对”；判断留给后续协议。
3. 编码不是解释；编码是“这更接近 X”，不是“这是因为 Y”。
4. 置信度与结构风险必须分开编码，不得混成一个分数。
5. 误判成本不对称：假阴性（漏掉高风险）的代价通常高于假阳性（多冻结一次）。

---

## 固定边界

COP 不负责：

- 不重写 DM（本体论地基）；
- 不替代 ASTO（变迁语法）；
- 不接管 ARBT（权责边界）；
- 不越权替代 TAT（责任阈值）；
- 不替代 ODD（审计封存、工程回滚、产出物放行）；
- 不承担 PFM 的前线显影与接引；
- 不承担 RT6 的操作执行；
- 不承担临床诊断、治疗建议、人格分类、法律/医疗/投资建议、责任终裁或工程放行。

### 弱依赖定位

本文件不依赖强 DM/ASTO/ARBT/TAT/ODD 才能成立。COP 从风险分流实践出发，承认协同场景中需要置信度评估、风险分级、冻结和转介纪律。

- **独立生存条件**：COP-min 可在不接受完整本体论的前提下使用。
- **上层失效时**：若上游理论被质疑，COP-min 仍可作为非临床风险分流接口继续使用。
- **reject/defer/escalate**：FREEZE/REFER/UNKNOWN 时阻断 RT6/LSM/WSH 继续操作；临床风险转专业渠道；高责任转 TAT；工程承诺转 ODD。

---

## 跨层接口

| 方向 | 接口内容 |
|------|----------|
| <- PFM | 场域准入评分；BOS（历史别名）作为首次进入参考 |
| <- ASTO | 结构编码前置输入：当前结构状态、节律、位点和边界状态 |
| -> PFM | `triage_status + confidence + risk + evidence_gap` |
| -> TAT | FREEZE / REFER / ESCALATE 状态下的责任阈值转介 |
| -> RT6 | CONTINUE 状态下的非临床操作方法入口 |
| -> ODD | 分流留痕、证据封存、工程承诺和回滚需求 |
| <-> P5 校准 | 真实结果回流，更新采样策略与协议参数 |

---

## 不可替代问题与外部比较

> 详见 `CC-独立理论层/COP.035-不可替代问题与外部比较.md`

COP 解决的独特问题是：

> 一个高不确定问题被看见之后，谁能判断它能不能接、该不该接、接不了往哪转；不是靠直觉，而是靠结构化分流。

传统分流（客服初筛、热线接线、分诊）依赖个体经验，面对高维不确定、弱信号、多风险交叉时普遍失效。COP 提供可复述的五协议管线（P1-P5）和五种 canonical 分流状态。

| 维度 | COP | 传统分诊 | 纯规则引擎 | ML 分类器 |
|------|-----|----------|-----------|----------|
| 能冻结 | 内置 FREEZE/ESCALATE | 依赖人工判断 | 无 | 无 |
| 能承认未知 | 内置 UNKNOWN | 不内置 | 无 | 置信度低时仍可能输出 |
| 误判成本建模 | False Safe > Over Freeze | 无 | 无 | 依赖训练数据 |
| 转介纪律 | 内置转介路由 | 靠经验 | 无 | 无 |

---

## 分流失效条件与失败线

> 详见 `CC-独立理论层/COP.037-分流失效条件与失败线.md`

完全失效条件：

| 编号 | 失效条件 | 后果 |
|------|---------|------|
| F1 | 无可靠信号可采样 | 分流前提消失 |
| F2 | 编码空间无法区分五种分流状态 | 分类退化 |
| F3 | 假阴性率（漏掉高风险）持续高于可接受边界 | 冻结纪律崩溃 |

最危险失败模式：

1. **编码漂移**：标签含义随时间移动，但阈值未更新。
2. **过度冻结**：假阳性率过高，FREEZE 降为“跳过”。
3. **过度自信**：UNKNOWN 极少出现，但实际信息不足。
4. **虚假安全**：CONTINUE 后无后续监控。

---

## 当前阅读入口

1. `PUBLISH_READINESS.md` — 当前可发布状态和禁止外发边界。
2. `AA-母版源层/README.md` — 母版主链导航。
3. `AA-母版源层/COP.003-五协议主文.md` — 五协议框架。
4. `AA-母版源层/COP.029-诊断协议.md` — 风险分流协议 v1；“诊断”为历史名。
5. `CC-独立理论层/README.md` — 独立成立口径。
6. `CC-独立理论层/COP.035-不可替代问题与外部比较.md`。
7. `CC-独立理论层/COP.037-分流失效条件与失败线.md`。
8. `FF-工程执行层/COP-min-schema-and-fixtures.md` — 最小接口与样例入口。

---

## 术语表

| 缩写 | 全称 |
|------|------|
| COP | Cognitive Computing Protocol / 认知计算协议 |
| BOS | Business Opportunity Score / 场域评分（历史别名，现统一为 PFM 场评分） |
| DM | Differential Monism / 差异一元论 |
| ASTO | Attribute-Set Transition Ontology / 属集变迁存在论 |
| ARBT | Authority-Responsibility Boundary Theory / 权责边界理论 |
| TAT | The Accountability Threshold / 责任锚定与阈值理论 |
| ODD | Output-Driven Development / 产出物驱动开发 |
| PFM | Problem Framing Method / 问题显影方法 |
| RT6 | Resonance & Transition 6-Step / 共鸣与跃迁六步法 |

---

## COP-min 与完整 COP 的关系

COP-min 是完整 COP 的风险分流 ABI，只保留 `triage_status`、`confidence`、`risk`、`referral_target`、`evidence_gap` 等跨层转交字段。它不替代完整 COP 的 P1-P5 协议管线、误判成本管理、结构编码前置接口、反馈校准和失败线。

### canonical triage_status

`CONTINUE / FREEZE / REFER / ESCALATE / UNKNOWN`

- `RESOLVE` = `CONTINUE` 历史别名（deprecated）。
- `MIXED` 下沉为 `signal_composition: mixed`。

### 验证等级

当前为 C1-C2。不得声称真实世界有效、诊断准确或认证级安全。需建设 30-50 条 conformance fixtures。

### confidence 纪律

`confidence != risk`。必须记录 False Safe、Over Freeze、错误转介、补证成功率和人工复核一致性。

### HITL

人工复核者必须具备：信息、权限、责任、场景能力、复核窗口和交接记录。`referral_target = HUMAN` 时必须记录 `reviewer_role / authority_scope / domain_competence / evidence_access / conflict_of_interest / review_window / handoff_record`；字段缺失时不得视为已承接。

### 传播口径

**router, not advisor**。不做临床决策、治疗建议、人格分类、法律/医疗/投资建议、责任终裁或工程放行。

### 数据治理

同意、去标识、保留周期、删除、审计必须按场景 Profile 明确；高风险或心理健康相邻信号不得默认长期保留。
