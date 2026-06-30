---
status: AA-mother-source-entry
purpose: AI协作者单文件入口
scope: ODD的定位、核心概念、推导链、关键命题、跨层接口与术语
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
forbidden_actions:
  - 不得修改母版正文的主张强度
  - 不得把 ODD 包装成法律放行、安全认证、业务正确、责任终裁或完整软件工程替代系统
  - 不得把 `gate_status=PASS` 或 `SEALED` 写成现实发布授权
update_checklist:
  - 母板有新命题时同步更新
  - 每次发布前校验一致性
handoff_note: 修改后通知各下游层-4AI文件维护者
---

# ODD 产出物驱动开发总览

> 用途：这是面向 AI 与协作者的 `ODD` 单文件入口。
> 目标：只发这一份文件，也能快速看懂 `ODD` 是什么、解决什么问题、位于整套体系的什么位置、与上下游如何衔接。
> 状态：当前现行入口
> **Canonical 送审对象**：本文件 + `EE-学术发表层/ODD工程治理规范-ODD-Engineering-Governance-Spec.md` + `EE-学术发表层/ODD工程治理重发正文-ODD-Engineering-Governance-Reissue-Body.md`。旧论文、工具案例和 guide 层材料为 historical/full profile，不作为最小送审口径。
> 作者 / Author：Yi Fu（付毅，ODDFounder，fuyi.it@live.cn）

### ODD 法源矩阵

| 层级 | 内容 | 定位 |
|------|------|------|
| `ODD-min` | 五字段 ABI：`contract / validation / evidence / seal / rollback-recall` | 最低工程治理接口 |
| Core Theory | 产出物门禁、状态机、证据封存、回滚/召回 | 核心理论 |
| Pre-gate Methods | RSC / CTF / CAP / 多投影规格链 | 前置方法论 |
| Support Corpus | 论文、白皮书、工具案例、实践指南 | 辅助材料 |

**Non-output**：ODD 不输出法律放行、安全认证、业务正确、TAT 责任终裁、OCGS 能力合当终裁或完整软件工程替代结论。`gate_status=PASS` 只表示工程门禁证据充足。

**TAT/OCGS 硬约束（高影响 Profile）**：高影响产出物若缺 TAT 阈值或 OCGS 能力治理结论，ODD 不得 `PASS` 或 `SEALED`。`upstream.tat.threshold_met=false/unknown` 时，`gate_status` 只能是 `FAIL` 或 `FREEZE_WAITING_UPSTREAM`。

---

## 一、ODD 是什么

`ODD` 是”产出物驱动开发”。

最低独立读法不要求先接受完整上游链。

最短句：

> **`ODD` 是整套体系中的工程方法层，负责把高影响 AI 产出物的定义、验证、留痕、封存与追责压成可执行闭环。**

再压一句：

> **它关心的核心不是“AI 怎样写代码”，而是“哪些产出物允许进入系统，以及它们如何被验证、留痕、封存、召回与追责”。**

---

## 二、ODD 不是什么

`ODD` 不是：

- 对所有传统软件工程方法的简单替代宣言
- 对“完全无人负责自动化”的背书
- 只要用了 AI 就必须采用的唯一流程
- 脱离权责边界与责任结构的纯效率技巧

更准确地说：

> **`ODD` 更像高影响产出物治理框架，而不是泛化的软件工程万能方法。**

### 弱依赖定位

本文件不依赖强 DM/ASTO/ARBT/TAT 才能成立。ODD 从工程产出物治理实践出发，承认高影响产出物需要门禁、证据、审计封存与回退机制。

- **独立生存条件**：ODD-min 可在不接受完整本体论的前提下使用。
- **上层失效时**：若 DM/ASTO/TAT 被质疑，ODD-min 仍可作为产出物治理协议接口继续使用。
- **reject/defer/escalate**：超出工程产出物治理范畴的问题（法律终裁、临床诊断、责任终裁）必须转交对应层；ODD 不越权承接。

---

## 三、ODD 在整套体系中的位置

> 本节为体系接入参考（L2），独立使用 ODD 不需要阅读。

若看整套体系总链条，以 `ai一元论理论体系总览.md` 为准；
若看 `TAT / COP / ODD / Harness` 的治理执行链分工，以 `TAT-COP-ODD-Harness 接口白皮书（现行版）` 为准。

只需要记住两条局部关系：

- 在公开法源链里，`ODD` 可由 `TAT` 提供责任解释，但其最低独立读法不要求先接受完整上游链
- 在治理执行链里，`ODD` 位于 `TAT` 之后、`Harness` 之前

因此 `ODD` 的最稳角色是：

> **它负责把上游判断真正压到工程执行层。**

没有 `ODD`，很多关于责任、边界、治理的讨论会停留在概念层；
有了 `ODD`，这些要求才会变成：

- 契约
- 门禁
- 验证
- 证据链
- 封存
- 解封
- 回滚
- 召回

---

## 四、ODD 解决什么问题

`ODD` 当前优先解决 4 类问题：

### 1. 高影响产出物如何被定义

先把“什么算合格结果”写清楚，而不是先崇拜生成过程。

### 2. 高影响产出物如何被验证

当 AI 产出量远超人类逐行审查能力时，
验证不应再只靠传统代码审查。

### 3. 错误放行后如何留痕、封存与回滚

真正危险的不是模型偶尔出错，而是：

- 出错后没人知道是谁放行
- 没有可回放证据
- 没有回滚与召回能力

### 4. 人类责任如何保留在不可替代节点

`ODD` 不是取消人类责任，而是把人类责任集中在：

- 定义契约
- 裁定结果
- 授权放行
- 审议召回

这些不可替代的位置。

> **责任溯源**：ODD 的责任模型可回引 DM.P10「责任的拓扑」——"责任是对高损伤结果的可归属性标记"。ODD 把这一哲学定义操作化为工程闭环：谁定义契约、谁裁定结果、谁授权放行、谁审议召回，均须可审计、可追溯。（体系接入者详见 `DM.P10.伦理-责任的拓扑.md`）

---

## 五、ODD 的最小核心

如果压成 4 个核心动作，`ODD` 其实非常清楚：

1. `契约`
先定义什么结果才算合格。

2. `验证`
用系统化验证，而不是只靠主观感觉。

3. `证据`
把关键输入、输出、决策和放行记录留下来。

4. `封存 / 回滚 / 召回`
高影响结果一旦出问题，系统必须真能停下、撤回、复放与追责。

最短句：

> **`ODD` 的核心不是“更快生成”，而是“更稳放行”。**

---

## 六、ODD 内部的前置协议

ODD 不应从一句模糊需求直接跳到执行门禁。当前更稳的内部链条是：

> **门禁状态来源**：ODD 的门禁成熟度（开放受理/封闭审理/存档关闭/失衡量测）可回引 OCGS 的 S0-S3 四级治理强度。独立使用时可直接采用四级门禁而不必先接受 OCGS。（体系接入者详见 `OCGS-4AI.md` §三级治理强度）

```text
RSC：需求语义澄清
  -> CTF：可信规格建构
  -> ODD：契约验证、证据封存、回滚召回
```

三者分工：

- `RSC` 负责把模糊话语、缺省上下文和半成形想法澄清为 `RequirementFrame`
- `CTF` 负责把澄清后的需求、项目事实、代码证据和人类判断建构成 `SpecSnapshot / ContractCandidate`
- `ODD` 负责把候选契约落实为验证、证据、封存、回滚和召回闭环

最短句：

> **RSC 让需求可问清；CTF 让规格可信；ODD 让产出可验。**

---

## 七、ODD 的核心主张

`ODD` 当前最稳的公开主张可以压成 4 句：

1. 软件开发真正需要治理的是产出物，而不只是代码文本。
2. 在 AI 产出量超过人类审查能力的条件下，代码审查不应继续作为唯一主门禁。
3. 契约、验证、证据链与封存机制，比“解释 AI 如何想的”更适合承担工程控制功能。
4. `ODD` 的目标不是取消人类责任，而是把人类责任集中在不可替代的定义、裁决与授权节点。

---

## 八、ODD 与 `TAT / ARBT / ASTO` 的关系

> 本节为体系接入参考（L2），独立使用 ODD 不需要阅读。

### 1. 与 `TAT` 的关系

`TAT` 先回答：

- 谁来承接后果
- 哪些责任门槛已经成立
- 哪些合同、证据、熔断和补偿结构必须被配置

`ODD` 再回答：

- 这些要求如何落实到工程门禁与证据链
- 哪些结果可以放行
- 哪些结果必须冻结、召回或回滚

最短句：

> **`TAT` 定责任门槛，`ODD` 把门槛编译成工程规则。**

### 2. 与 `ARBT` 的关系

`ARBT` 处理的是更上游的文明与权责边界。
`ODD` 不直接做这些判断，只负责承接其结果。

最短句：

> **`ARBT` 负责治理判断，`ODD` 负责执行闭环。**

### 3. 与 `ASTO` 的关系

`ASTO` 提供结构门前语法。
`ODD` 在进入契约、验证、放行与回滚前，建议先读取 `ASTO` 的前置结构字段，而不是把门禁写成纯技术流程。

---

## 九、ODD 当前最稳的阅读方式

如果不先接受 `DM` 的强版本，`ODD` 仍然可以先被读成：

- 高影响产出物治理协议
- 工程审计与可回滚框架
- 契约驱动、验证驱动、证据驱动的执行闭环

也就是说：

> **即使上游哲学仍有争议，`ODD` 也可以先以契约、验证、证据与回滚能力站住。**

---

## 十、如果离开本文件后只继续读 5 份文件

建议顺序是：

1. `SOURCE_OF_TRUTH.md`
   作为当前唯一真相源、canonical output、non-output 和发布阻塞项阅读
2. `EE-学术发表层/ODD工程治理规范-ODD-Engineering-Governance-Spec.md`
   作为 `ODD-min` 工程治理规范阅读
3. `EE-学术发表层/ODD工程治理重发正文-ODD-Engineering-Governance-Reissue-Body.md`
   作为重发正文候选阅读
4. `EE-学术发表层/ODD-OCGS治理事件-ODD-OCGS-GovernanceEvent.md`
   作为 OCGS/TAT/ODD 上游治理事件接口阅读
5. `CC-独立理论层/ODD.P05-不可替代问题与外部比较.md`

如果还要继续深读，再进：

6. `CC-独立理论层/ODD.P06-失败线与反例手册.md`

补一句角色边界：

> **本文件是 `ODD` 的 AI 单文件入口；`EE-学术发表层/ODD工程治理规范-ODD-Engineering-Governance-Spec.md` 是当前 ODD-min 规范入口；`EE-学术发表层/ODD工程治理重发正文-ODD-Engineering-Governance-Reissue-Body.md` 是重发正文候选；两者分工不同，不互相替代。**

---

## 十一、当前最稳结论

如果把 `ODD` 压成一句话：

> **在 AI 辅助工程里，真正需要治理的不是“模型说了什么”，而是“哪些产出物被允许进入系统，以及它们能否被验证、留痕、封存和召回”。**

如果再压成更适合 AI 理解的一句：

> **`ODD` 是整套体系里的工程闭环层，负责把上游的责任与治理要求变成可执行的契约、门禁、证据链与回滚机制。**

---

## 十二、不可替代问题与外部比较

> 详见 `CC-独立理论层/ODD.P05-不可替代问题与外部比较.md`

### ODD 解决什么独特问题

> **AI agent 生成的产出物，如何被验证、封存、回滚——不是"看起来对不对"，而是"能不能被契约约束"。**

传统软件工程预设人类编写代码、人类审查代码。AI agent 成为主要生产者后，出现四个新问题：验证目标漂移、证据链断裂、回滚粒度失控、封存时效缺失。

### 为什么传统方法不够

| 问题 | 传统方法 | ODD |
|------|----------|-----|
| AI 修改了未授权模块 | Code review——AI 产出量远超人类审查带宽 | Contract `must_not_change`→违反即 Fail gate |
| spec 滞后于代码 | 非结构化 PR 讨论 | SpecSnapshot + stale 自动检测 |
| 两个月后审计 agent 修改 | git log——只有 diff | EvidenceRecord 封存 contract/spec/decision/artifact |
| agent 产出"看起来对"但数据漂移 | 功能测试不一定覆盖 schema | data-tree + migration 门禁 |
| 回滚不是 revert commit | git revert 不回滚"当时为什么接受" | Contract 绑定回滚路径 + recall 纪律 |

### 核心比较矩阵

| 维度 | ODD | CMMI | DevOps | SLSA |
|------|-----|------|--------|------|
| 核心关注 | AI 产出物契约验证 | 组织过程成熟度 | 交付速度 | 供应链完整性 |
| 粒度 | 产出物级 | 组织级/项目级 | 流水线级 | artifact 级 |
| AI 原生 | 是 | 否 | 否 | 否 |
| 验证方式 | 契约门禁+证据封存 | 过程审计 | 测试 | 来源验证 |

### 不可替代性声明

> 去掉 ODD，AI agent 工程仍可进行——但会失去：契约化验证、证据封存、结构化回滚纪律、人-AI 责任接口。ODD 不是"更好的 CI/CD"，而是一个新的问题域——AI 产出物治理——在当前工具链中不存在对应物。

---

## 十三、失败线与反例

> 详见 `CC-独立理论层/ODD.P06-失败线与反例手册.md`

### 完全失效条件

| 编号 | 失效条件 | 后果 |
|------|---------|------|
| F1 | AI 产出量小到人类可逐行审查 | ODD 过度设计——退化为普通 checklist |
| F2 | 测试完全覆盖所有"不该改的" | Contract 门禁多余 |
| F3 | 不需要"两个月后审计" | EvidenceRecord 无用户 |
| F4 | Agent 从不跨 concern 修改 | Rollback 纪律多余 |

### 门禁绕过条件

| 编号 | 绕过条件 | 机制漏洞 |
|------|---------|---------|
| B1 | Agent 绕过 Contract 直接修改文件 | 无门禁钩子→Contract 形同虚设 |
| B2 | `must_not_change` 太窄 | 门禁不保护真正需要保护的东西 |
| B3 | SpecSnapshot 过期 | stale 漏报——过期 spec 仍在放行 |
| B4 | EvidenceRecord 可篡改 | 证据链断裂 |

### 过度收紧模式

| 编号 | 条件 | 后果 |
|------|------|------|
| O1 | Contract 过宽 | Agent 无法工作 |
| O2 | EvidenceRecord 过详 | 审查者信息过载 |
| O3 | Seal 过严 | 工程速度归零 |

### 不使用 ODD 的条件

- AI agent 产出量很少（人类可逐行审查）→ 不需要
- 纯人类工程 → 问题域不存在
- 项目生命周期 < 1 周 → 成本 > 收益
- 无审计/合规要求 → EvidenceRecord 无需求

---

## 最小独立口径声明

ODD 的最低独立成立理由：AI/自动化系统产出高影响产出物时，必须回答"产出物是否契约化、是否可验证、是否有证据链、是否可封存、是否可回滚、是否可召回"。这个判断不需要先接受 DM/ASTO/ARBT/TAT/OCGS 的强理论版本。

---

## AA-母版源层文件清单

母版源层是 ODD 的理论生发层。以下列出当前 AA-母版源层全部文件及其状态。

| 文件 | 标题 | 状态 |
|------|------|------|
| `ODD.P01.结构门禁前置语法.md` | 结构门禁前置语法 | active |
| `ODD.P02.迁移对照指南.md` | 迁移对照指南 | active |
| `ODD.P03.CTF建构追溯可谬规格方法论.md` | CTF 建构追溯可谬规格方法论 | active |
| `ODD.P04.RSC需求语义澄清协议.md` | RSC 需求语义澄清协议 | active |
| `ODD.P05.验证策略矩阵.md` | 验证策略矩阵 | draft_recovered (D3) |
| `ODD.P06.管道组合模型.md` | 管道组合模型 | draft_recovered (D3) |
| `ODD.P07.车间管理模型.md` | 车间管理模型 | draft_recovered (D3) |
| `ODD.P08.状态机与门禁.md` | 状态机与门禁 | draft_recovered (D3) |
| `ODD.698-产出物分类学-L1L2L3.md` | 698 产出物分类学 | active |
| `ODD.CAP-契约对抗生成协议.md` | CAP 契约对抗生成协议 | active |
| `ODD.BugMap-Bug意向图与反模式库.md` | BugMap | active |
| `ODD.FuncTree-功能树与影响分析.md` | FuncTree | active |
| `ODD-理论推演母板.md` | 理论推演母板 | active |
| `ODD.发散推理笔记-2026-06-06.md` | 发散推理笔记 | working |
| `ODD.P07-操作化检查表.md` | 操作化检查表 | working |
| `ODD.698-分类学数据.json` | 分类学数据 | data |

> P05-P08 从 ZZ-归档与素材层回收（D3 批次），状态 `draft_recovered`，待与 L0 母板对齐后升级为 `consolidated_review_draft`。

---

## 强主张清理表与禁用句

| 强口径 | C 级 | 禁用表达 | 允许表达 |
|--------|------|----------|----------|
| 替代 code review | C5 | "ODD 替代 code review" | "ODD 将人工审阅重心从逐行检查迁移到契约定义、异常裁决、放行授权与召回审议" |
| 系统验证替代人工 | C5 | "系统验证替代人工" | "系统验证辅助人工审阅；人工保留异常裁决和放行授权" |
| seal 后无需复审 | C5 | "seal 后无需复审" | "seal 是版本-证据绑定，不是不可变真理；仍可被新证据触发解封" |
| PASS 即可发布 | C5 | "PASS 即可发布" | "PASS 表示工程治理证据充足；发布还需法律、安全、合规等渠道确认" |
| 领域无关 | C3 | "ODD 适用于一切领域" | "ODD 提供跨领域治理框架；领域特化需补充领域证据" |
| 已验证 | C0 | "ODD 已被验证" | "ODD 是候选研究纲领，正在积累案例" |
| 实证数字证明优越 | C3 | "172 任务证明 ODD 优越" | "172 任务/59.5%/p=0.029 是研发缓存/初步实验材料，不作为普适证据" |

> **实证数字降级声明**：`172 任务 / 59.5% / p=0.029` 证据强度不足以支撑普适优越性。降为"研发缓存/初步实验材料"，默认不得进入单理论主包；若进入论文，必须补方法、对照、复现包和外部验证。

> **未经经验验证声明**：ODD（含 RSC/CTF）是候选研究纲领，尚未经过系统性经验验证。所有核心命题（门禁有效性、契约降低返工率、stale 检测降低规格漂移等）均为待验证假说，不作为已证明结论。

---

## 外部近邻方法矩阵

| 方法 | 与 ODD 的共享点 | ODD 的差异 |
|------|-----------------|------------|
| **TDD** | 测试先行 | ODD 不限于测试；覆盖契约、证据、封存、回滚全链路 |
| **BDD/ATDD** | 行为驱动、验收标准 | ODD 增加产出物治理、封存和回滚机制 |
| **Design by Contract** | 契约化 | ODD 把契约扩展为可审计治理接口 |
| **Spec-driven** | 规格先行 | ODD 增加验证、证据、封存、回滚/召回闭环 |
| **Eval-driven** | 评估先行 | ODD 增加产出物生命周期治理 |
| **Requirements Traceability** | 需求追溯 | ODD 把追溯扩展为产出物全生命周期治理 |
| **Assurance Case** | 安全论证 | ODD 不限于安全；覆盖质量、责任、治理 |
| **CI/CD Gates** | 门禁 | ODD 把门禁扩展为契约化治理接口 |
| **Formal Methods** | 形式化验证 | ODD 不要求形式化；允许多种验证方式 |

**ODD 的新增性**：不在单个契约、测试、CI gate 或封存动作，而在 AI 高通量产出场景下，以产出物为中心，把契约、验证、证据、封存、回滚/召回组织成可审计治理接口。

## 学术对照

### Popper / Dijkstra / Falsification-Driven Verification

CTF 的"可谬"需要认识论和工程验证双重支撑。CTF 不是证明规格正确，而是提高规格错误被提前暴露的概率。对 TDD/BDD 的增量：TDD/BDD 多数时候验证"实现是否满足已给规格"，CTF 额外追问"规格本身是否已经不可信"。

### Pre-RS Traceability

传统 RTM 多在同一需求语义层内追溯。CTF 追溯跨越治理语言、需求语言、规格节点、验证证据和工程产出物。CTF 定位到需求规格化之前的追溯薄弱点。

### Safety Case / GSN / CAE

| GSN 元素 | ODD/CTF 映射 |
|----------|-------------|
| Goal / Claim | ODD contract 或 CTF governance requirement |
| Strategy / Argument | CTF mapping strategy / TrustSignal |
| Solution / Evidence | ODD evidence |
| Context / Assumption | RSC/CTF 边界条件 |

ODD 增量：前置 gate、可失效冻结、版本-证据封存、rollback/recall。不是替代 safety case，是 safety case 前的结构门禁和证据封存层。

### Stage-Gate / TRA / TRL

- Stage-Gate 问"项目是否进入下一阶段"
- TRA/TRL 问"技术是否足够成熟"
- ODD 问"这个产出物是否具备契约、验证、证据和回滚边界"

ODD 不宣称发现门禁思想。

### CMMI / ISO 过程合规

CMMI/ISO 管组织过程成熟度与管理体系；ODD 管单个高影响产出物进入系统前的契约、验证、证据和回滚条件。二者互补：过程体系提供组织纪律，ODD 提供产出物级门禁记录。ODD 不比过程合规"更高级"。

### ISO/IEC/IEEE 29148

29148 是需求工程和需求相关信息项的正式标准。RSC/CTF 必须承认它是近邻。ODD 的增量：在 AI 辅助高通量产出场景中，把需求澄清、规格可谬、验证证据、封存和召回组织成最小工程治理接口。

### RSC 与 LLM 目标提取自动化

LLM 可辅助生成候选目标、缺槽问题和风险提问，但 `ready_for_ctf` 必须由来源、置信度、未知项和人工确认边界共同决定。失败线：LLM 自动补槽不得直接冻结规格；未标注来源的补槽只能作为候选。

---

## ASTO 1-5-6-7-1 与 ODD-min 关系

ASTO 的 `1-5-6-7-1` 循环不进入 ODD-min。ODD-min 保持五个字段：`contract / validation / evidence / seal / rollback-recall`。`1-5-6-7-1` 只在 ODD-full / high-impact profile 中使用。

---

## claim_strength 字段模板

每个公开主张必须标：

```yaml
claim: "ODD 将人工审阅重心从逐行检查迁移到契约定义"
claim_strength: C1
evidence_source: "框架提案"
allowed_expression: "ODD 迁移审阅重心"
forbidden_expression: "ODD 替代 code review"
```

---

## seal 与 rollback 精确措辞

**seal（封存）**：封存是"版本-证据绑定"，不是不可变真理。新证据可以触发解封。

**rollback/recall（回滚/召回）**：成本、影响范围、补偿路径不由 ODD 自动解决。回滚/召回触发后，成本评估和补偿路径需转交 TAT / OCGS / 法律渠道。

---

## P91-P96 编号统一

ODD 工具层文件使用 P91-P96 编号（`ARBT.P91` 改为 `ODD.P91`），与 README 中的 P99 说法统一。具体映射：

| 旧编号 | 新编号 | 文件 |
|--------|--------|------|
| P91 | ODD.P91 | 工具层 |
| P92 | ODD.P92 | 工具层 |
| P93 | ODD.P93 | 工具层 |
| P94 | ODD.P94 | 工具层 |
| P95 | ODD.P95 | 工具层 |
| P96 | ODD.P96 | 工具层 |

---

## guide 层标识

guide 层（传播文案、教程、示例）保留时，必须加醒目标识：

> **非 canonical**：本文件为传播辅助材料，不作为 ODD canonical 送审口径。Canonical 入口见 `ODD-4AI.md`。
