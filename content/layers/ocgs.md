---
status: AA-mother-source-entry
purpose: AI 协作者单文件入口
scope: OCGS的定位、核心概念、推导链、关键命题、跨层接口与术语
audience: AI协作者、自动化代理
canonical_sources:
  - SOURCE_OF_TRUTH.md
  - AA-母版源层/
  - CC-独立理论层/
  - DD-体系增强层/
  - PUBLISH_READINESS.md
required_reads:
  - 00-索引与导航/AI修改必读-理论体系治理原则-4AI.md
  - SOURCE_OF_TRUTH.md
  - PUBLISH_READINESS.md
inputs: SOURCE_OF_TRUTH.md + AA-母版源层 + CC-独立理论层 + DD-体系增强层 + PUBLISH_READINESS.md
outputs: 结构化总览、术语映射、接口声明
non_outputs: 不产生新理论命题、不替代母版正文、不替代独立法源、不发布放行
mandatory_rules:
  - SOURCE_OF_TRUTH、AA/CC/DD 源层与 PUBLISH_READINESS 是法源，本文件只是压缩入口
  - 不得产生比 SOURCE_OF_TRUTH、母版、独立法源、体系增强或发布准备文件更强的主张
forbidden_actions:
  - 不得修改母版正文的主张强度
  - 不得把 OCGS 包装成法律认证、安全认证、工程放行、责任终裁或完整系统安全保证
  - 不得把 OCGS.gate_state=PASS 写成 ODD PASS、TAT 阈值满足或现实发布授权
update_checklist:
  - 母板有新命题时同步更新
  - 每次发布前校验一致性
handoff_note: 修改后通知各下游层-4AI文件维护者
---

# ai能力有序治理论总览

> **2026-06-02 canonical status**：本文是完整 OCGS 理论的 AI 单文件总览，用于保留母体理论、独立理论层、Profile / Extension 与工程特化全貌。OCGS-min 的最小能力调用接口入口是 `EE-学术发表层/OCGS桥接规范-OCGS-Bridge-Spec.md`；独立理论法源入口是 `CC-独立理论层/`。本文不替代 OCGS-min ABI，也不替代独立理论层母板。本文中的十子集、StrongInv3Q、SealSet、AccountabilitySet、FREEZE、责任闭合等内容按完整 OCGS 理论、特化 Profile、下游证据包或候选扩展读取。
>
> 用途：面向 AI 与协作者的 `OCGS` 单文件入口。
> 目标：让读者一次性理解完整 OCGS 理论；若只需要机器接口或 DOI 最小转交字段，再读取 `EE-学术发表层/OCGS桥接规范-OCGS-Bridge-Spec.md`。
> 版本：v1.0
> 作者：Yi Fu（付毅，ODDFounder，fuyi.it@live.cn）

---

## 〇、法源矩阵与边界

| 层级 | 法源入口 | 作用 | 非输出 |
|------|----------|------|--------|
| Source of Truth | `SOURCE_OF_TRUTH.md` | canonical output、OCGS-min ABI、Kernel/Profile 边界、发布阻塞项 | 不替代 AA/CC/DD 正文 |
| OCGS-min ABI | `EE-学术发表层/OCGS桥接规范-OCGS-Bridge-Spec.md` | 对外最小能力调用接口：`ability / purpose / due / gate / evidence / audit_trail` | 不输出安全认证、法律合规、工程放行或责任终裁 |
| 独立理论层 | `CC-独立理论层/` | OCGS 脱离一元论总体系也能独立成立、审查、投稿和引用的法源 | 不要求读者先接受 DM/ASTO/一元论总体系 |
| Kernel | `CC-独立理论层/OCGS.069-OCGS-Kernel与Profile机制.md` | 最小判断核心：BJ-1/BJ-2、Kernel 不变量、核心操作和最低证据要求 | 不包含完整 DueSet 十子集或场景 Profile |
| Full Theory | `CC-独立理论层/` + `AA-母版源层/` + `DD-体系增强层/` | D1-D12、DueSet 十子集、WeakInv3Q、AI 隐式治理、组织层级、激励相容、三层继承契约等完整理论资产 | 不得反向加重 OCGS-min 必填项 |
| Profile / Extension | `AA-母版源层/OCGS.081-OCGS Profile设计规范.md`、`AA-母版源层/OCGS.082-OCGS-AI Profile.md` 等 | AI、SE、Org、Delphi、F 等场景化实现规范 | 不得改写 Kernel，不得声称代表所有 OCGS |
| Non-output | `CC-独立理论层/OCGS.090-确权声明-Claim-and-Boundary-Statement.md` | 固定 OCGS 的确权范围与不可外推边界 | 不输出法律、医疗、投资、财务审计、安全认证、代码正确性证明 |

AI 协作者必须先按本矩阵判断材料属于哪一层，再决定能否外发、能否加重主张、是否需要转交 TAT/ODD/COP 或其它相邻层。

---

## 一、定位

`OCGS`（能力有序治理系统 / Ordered Capability Governance Set）是能力有序治理的独立方法论。OCGS-min 可与 ASTO-min 结构上下文相容，但最低独立读法不要求先接受完整上游链。

最短句：

> **能力调用必须能说明 ability、purpose、due、gate 与 evidence。**

OCGS 不是：
- 能力生产系统（它不生产能力，而是治理既有能力）
- 软件框架（软件是重要落地场景，但不是全部）
- 组织咨询话术（不是简单告诉公司如何开会、分工、考核）
- ODD / ContractSet / 流程管理系统（那些是下游应用或 DueSet 子集）

更准确地说：

> **OCGS 是 capability-call governance（能力调用治理模型）。它不生产能力，而是为既有能力的显现、组织、调用、验证、放行、封存与承责提供前置门禁和证据输入。组织治理、软件工程、AI Agent 治理和 Delphi 是 OCGS 的 Profile / Extension 场景，不是 OCGS 本身。**

### 三条边界

1. OCGS 治理的是已存在的能力如何有序显现、组织、调用、验证、放行与承责；不治理能力本身的获取、生产、学习、进化
2. OCGS 不替代具体行业的专业判断标准，不预设任何特定的组织形态或软件架构
3. OCGS 是实用主义判断体系，不是先验分析命题或纯经验归纳；其正当性来自解释力、预测力与干预力

### OCGS-min 最小可保留内核

若 OCGS 受压，首先缩到以下三条：

1. **能力不自动入序**（BJ-1：能≠序）
2. **目的不替代合当**（BJ-2：为≠当）
3. **可治理行动需要 A↔P↔D 三层可区分、可追踪**
4. **OCGS-min 六字段 ABI：`ability / purpose / due / gate / evidence / audit_trail`**；前五个是治理判断字段，`audit_trail` 是必需输出元数据

> OCGS 若受压，首先失去的是更精细的十子集展开与特化方向的工程细节，而不是核心判断。

**不属于 OCGS-min 的内容**：十子集是 high-risk profile 常见 due families，不是 min 必填；`StrongInv3Q` / `FullInv3Q` 是 OCGS-F profile 扩展；`SealSet` 只作为 ODD 输入候选；`AccountabilitySet` 只作为 TAT 责任证据接口。

### 弱依赖定位

本文件不依赖强 DM/ASTO/ARBT/TAT/ODD 才能成立。OCGS 从能力治理现实出发，承认能力、目的、合当、门禁、证据之间必须被区分和追踪。

- **独立生存条件**：OCGS-min 的六字段 ABI 可在不接受完整本体论的前提下使用。
- **上层失效时**：若上游理论被质疑，OCGS-min 仍可作为能力调用治理接口继续使用。
- **reject/defer/escalate**：超出能力治理范畴的问题（临床诊断、法律终裁、工程放行）必须转交对应层；OCGS 不越权承接。

---

## 二、核心概念

OCGS 的概念体系围绕以下核心概念展开，构成从本体到治理的统一语法：

| 概念 | 最低稳定义 | OCGS 差异点 |
|------|-----------|------------|
| **AbilitySet（能力集）** | 主体已拥有或可调用的能力集合 | 分类标准是功能性的（可被调用、可被治理），而非本体论的；OCGS 不主张不同范畴的能力在本体论上同类 |
| **PurposeSet（目的集 / 为集）** | 把能力组织到某个目标、任务、角色或状态变迁中的属集 | 不是 Intent（主观心理意图），而是能力为何显现、如何显现的组织结构 |
| **DueSet（合当集 / 当集 / Due Governance Constraints）** | 对能力行动施加合当性治理的属集总层 | 不仅是 ContractSet；包含 Boundary / Output / Acceptance / Gate / Evidence / Seal / Accountability / Risk / Remediation 十个子集 |
| **↔（互约束）** | 三层之间存在持续的双向相互制约和调整关系 | 不是单向管道，也不是静态对齐，而是四通道动态反馈网络 |
| **GateSet（门禁集）** | 能力进入与阻断机制 | 放行/阻断是治理的可执行端点，不是惩罚 |
| **EvidenceSet（证据集）** | 留证机制 | 留证不是普通日志，而是可追溯、可封存、可审计的治理证据 |
| **SealSet（封存证据接口）** | ODD 输入候选 | 只提供封存证据接口，正式 seal / rollback 由 ODD 裁定 |
| **AccountabilitySet（责任证据包）** | TAT 输入候选 | 记录责任线索与指定方，责任阈值与后果承接由 TAT 决定。TAT 是相邻责任协议，读取 OCGS 证据但不属于 OCGS 子集 |
| **BoundarySet（边界集）** | 治理可识别性的前提条件 | 遇到禁元突破、核心约束冲突时输出 `DEFER/BLOCKED/ESCALATE_*` |
| **RemediationSet（补救集）** | 事后修正的兜底机制 | 覆盖冻结、回滚、召回、修正、追责 |

### 场域比喻

```
AbilitySet = 水库（储什么水、有多少水）
PurposeSet = 渠道（水往哪里引、为什么引）
DueSet     = 水闸（什么时候放、放多少、谁来管）

水库没有渠道，水只能漫溢（能力裸奔）；
渠道没有水闸，水可能冲毁下游（目的失当）；
水闸没有水库，闸门空转（治理僵化）。
```

### 复数性约束与维度零

**复数性约束**：OCGS 治理不得消除被治理者的不可替代性、对话可能性与行动空间。违反这三项的"治理"是控制，不是治理。

**维度零声明**：任何 OCGS 治理结构中，人先于治理结构存在，人不可被完全编码，人有权改变治理结构。当 OCGS 规则与人的基本尊严冲突时，规则让步。

---

## 三、推导链 / 命题体系

### 引用公理（从 ASTO 借力）

OCGS 不独立发明公理，以下来自 ASTO（20层）：

| 编号 | 名称 | 核心句 |
|------|------|--------|
| RA-1 | 序是历史实践沉淀 | 序不是先验的、不是人为设计的，而是在历史实践中自然沉淀的场域结构 |
| RA-2 | 场域比喻 | A=势能库，P=方向舵，D=调速器 |
| RA-3 | 属集变迁 | 治理对象是 S_t → S_t+1 的状态变迁，不是静态实体 |
| RA-4 | 实践回路 | 结构有效性由实践回路检验，不由自洽决定 |
| RA-5 | 边界与例外 | 边界是结构可识别性的条件，例外是当前处理不了的剩余 |
| RA-6 | 低阻抗合规 | 合规必须被设计成低阻抗路径 |
| RA-7 | 人的位置 | 人是感知张力、定义边界、修订规约、裁决例外的不可约主体 |
| RA-8 | 认知不对称 | 当产出速度超过审阅速度，必须转向结果验证 |

### 基本判断（OCGS 自己的起点）

OCGS 只有两条基本判断，它们是全部定理的起点：

**BJ-1：能≠序（能力不等于秩序）**

> 任何能力的存在，都不自动生成正确的使用秩序。

能力只是可行动的可能性。有能力不等于有秩序。能力必须被治理。

**BJ-2：为≠当（目的不等于合当）**

> 有目的（为），不等于合当（当）。目的可能是错误的、越界的、短视的、无人承责的。

完成不等于合格，流程完成不等于治理完成。目的不能替代合当性审查。

**BJ-1 与 BJ-2 独立性**：二者正交且不可互推——BJ-1 关注结构维（有没有序），BJ-2 关注规范维（该不该做）。四个象限（有序+合当 / 有序+失当 / 无序+合当 / 无序+失当）都有真实组织案例。

**认识论地位**：两条判断是实用主义判断，不是先验分析命题。正当性来自解释力、预测力与干预力；可证伪性来自反例系统的存在。

### 推导命题与设计原则（D1-D12）

从 BJ-1 和 BJ-2 推导出的命题体系分为两类：

**分析性推论（D1-D8）**：从公理定义出发的逻辑展开，不依赖经验事实。
**设计原则（D9b, D10-D12）**：基于理论洞察的实践推荐，可经验调整。

| 命题 | 名称 | 核心句 | 依赖 | 类型 |
|------|------|--------|------|------|
| D1 | 能力裸奔定理 | 未经目的组织与合当约束的能力，具有裸奔风险 | BJ-1 + BJ-2 | 分析性推论 |
| D2 | 三层互约束定理 | 可治理行动需要 A↔P↔D 三层双向互约束成立 | BJ-1 + BJ-2 | 分析性推论 |
| D3 | A-P失衡定理 | A 过强而 P 过弱，导致能力错配 | BJ-1 | 分析性推论 |
| D4 | P-D失衡定理 | P 过强而 D 过弱，导致目的失当 | BJ-2 | 分析性推论 |
| D5 | D-AP失衡定理 | D 过强而 A/P 过弱，导致治理僵化 | BJ-1 + BJ-2 | 分析性推论 |
| D6 | 流程≠治理 | 流程通常位于 P，不等于 D 成立 | BJ-2 | 分析性推论 |
| D7 | UI可操作性≠门禁通过 | 按钮可点击不等于门禁通过 | BJ-2 | 分析性推论 |
| D8 | 契约≠治理 | ContractSet 不能代表整个 DueSet | BJ-2 | 分析性推论 |
| D9a | AI不豁免治理 | AI 能力调用不豁免 OCGS 治理逻辑 | BJ-1 + BJ-2 | 演绎结论 |
| D9b | 推荐D-P-A顺序 | D-P-A 调用顺序是实践推荐，非唯一可行路径 | D9a | 设计原则 |
| D10 | OutputSet中心 | ODD 场景中被治理对象中心是 OutputSet | BJ-2 | 设计原则 |
| D11 | 责任锚点 | 没有责任证据包的高风险能力调用不是完整 OCGS 治理对象 | BJ-2 | 设计原则 |
| D12 | 风险分级 | 不同风险等级不应使用同一强度的 DueSet | BJ-2 | 设计原则 |

#### D1-D12 适用范围与降级口径

| 定理 | 适用范围 | 证据类型 | 反例 | 降级口径 |
|------|----------|----------|------|----------|
| D1 | 所有能力调用场景 | 能力登记缺失、调用无目的记录 | 低风险内部工具可降级为"事后审查" | 裸奔风险极低时可豁免前置门禁 |
| D2 | 需要治理判定的场景 | A/P/D 三层是否可区分 | 单一角色执行时三层可合并为"自查" | 降为单层自审+事后审计 |
| D3 | A 资源丰富的组织 | 能力清单 vs 实际调用频次 | 能力过强但不调用则无实际损害 | 不调整 A，只监控 P 路径 |
| D4 | 目的驱动型组织 | 目的声明 vs 实际执行偏差 | 紧急情况下可临时豁免 Due 全检 | 启用临时 Due 快速通道 |
| D5 | 治理成熟度高的组织 | 审批周期、审批否决率 | 治理强度压过执行效率时需降级 | D 级别降为"抽查"而非"全检" |
| D6 | 流程驱动型组织 | 流程文档 vs 治理证据 | 流程本身即含治理逻辑时可合并 | 流程与治理合并审计 |
| D7 | UI 交互场景 | UI 状态 vs 门禁状态日志 | 非高风险操作可简化为 UI 层校验 | 低风险操作允许 UI 层隐式门禁 |
| D8 | 契约管理场景 | 契约覆盖度 vs DueSet 全集 | 契约已覆盖核心 due 项时可豁免 | 契约覆盖率≥80%时可简化 Due |
| D9a | AI 调用场景 | AI 调用链 vs OCGS 注册链 | 非自主 AI 调用可降级为人工确认 | 非自主调用仅需人工确认+记录 |
| D9b | AI 调用场景 | 调用顺序 vs 治理效果 | D-P-A 非唯一路径，可按场景调整 | 设计时推荐 D-P-A，运行时可预编译为 P-D-A |
| D10 | ODD 工程场景 | OutputSet 中心度 | 非 ODD 场景不适用 | 仅在 ODD 对接时激活 |
| D11 | 高风险能力调用 | 责任证据包完整性 | 低风险调用可豁免责任证据 | 风险≤medium 时可降级为普通证据 |
| D12 | 多风险等级组织 | 风险分级与 Due 强度匹配 | 组织只有单一风险等级时可统一 | 统一 Due 但保留风险标签 |

### 三条不变量（所有特化方向必须遵守）

| 不变量 | 母体表达 | 当前可操作性 |
|--------|---------|-------------|
| **Inv-1：能力不得裸奔** | AbilitySet 的存在不自动构成秩序 | 半形式化（时间模型待补） |
| **Inv-2：目的不得替代合当** | PurposeSet 的存在不自动构成 DueSet 满足 | 半形式化（精确表述待补） |
| **Inv-3：三层必须可追踪** | 可治理行动必须能追踪 A→P→D 的引用链 | Weak-Inv3 为简化启发式指标；Strong-Inv3 为理论理想，当前不可操作 |

### 四个反馈通道

↔ 的完整含义 = 四通道动态反馈网络：

1. **D→P**：合当约束反向塑造目的（DueSet 拒绝 → PurposeSet 必须修改）
2. **P→A**：目的需求反向驱动能力建设（P 有需求 → A 需补充）
3. **D→A**：治理活动消耗能力（审批/验收消耗能力预算）
4. **治理自反馈**：执行 DueSet 本身需要接受 OCGS 治理

### 范围声明 R-1

```
OCGS 治理的是：已存在的能力如何有序显现、组织、调用、验证、放行与承责。
OCGS 不治理：  能力本身的获取、生产、学习、进化。
OCGS 不替代：  具体行业的专业判断标准。
OCGS 不预设：  任何特定的组织形态或软件架构。
```

### 操作原则

- **OP-1**：OCGS 可独立使用，不需要先理解 ASTO
- **OP-2**：从诊断入手（找失序点），不从设计入手（不先画完整架构图）
- **OP-3**：治理强度与风险匹配——低风险轻门禁，高风险强门禁

---

## 四、三个特化方向

OCGS 采用"母体理论 → 多场景特化"的继承结构。母体定义通用治理理论，三个特化方向将其落地到不同场景。

### 4.1 OCGS-se（软件工程特化）

| 项 | 内容 |
|----|------|
| 定位 | 把 A↔P↔D 特化为软件运行时和开发过程 |
| 核心产出 | AbilityRegistry / PurposeMap / DueGovernanceEngine / Runtime / Evidence / Seal / 成熟度模型 |
| 不承担 | 不替代 Clean Architecture、CQRS、权限系统或测试框架 |
| 关键文件 | OCGS-se.001 ~ OCGS-se.025 |

母体概念到 se 的映射：

| 母体 | OCGS-se | 说明 |
|------|---------|------|
| AbilitySet | AbilityRegistry / Capability Provider | 能力来源、登记与调用边界 |
| PurposeSet | PurposeMap / PurposeResolver | 能力为何显现、从哪里进入 |
| DueSet | DueGovernanceEngine | 合当约束总入口 |
| GateSet | GateResolver / GateStateMachine | 能力进入与阻断机制 |
| EvidenceSet | EvidenceRecorder | 留证（不是普通日志） |
| SealSet | Seal evidence interface | ODD 输入候选 |

### 4.2 OCGS-Delphi（Delphi 工程落地）

| 项 | 内容 |
|----|------|
| 定位 | 把 OCGS-se 落到 Delphi 的事件、Action、控件、路由、证据和测试门 |
| 核心产出 | TAction / EventBridge / ActionGrid / OCGSRuntime / AccessGate / Projection / DeepBaseGovernance |
| 不承担 | 不替代 VCL/FMX、TActionList、DataModule 或业务代码 |
| 关键约束 | S2/S3 行为不得从 UI 事件直接调用 NativeRoutine，必须经 EventBridge / Runtime / AccessGate |

Delphi 层额外规定了符合性测试（Conformance Test CT-01 至 CT-15）和迁移案例模板。

### 4.3 OCGS-F（前线运行时特化）

| 项 | 内容 |
|----|------|
| 定位 | 把 A↔P↔D 微分为单次能力调用（Invocation）的运行时校验 |
| 核心产出 | WeakInv3Q / APD 三比特向量 / 失衡模式诊断 / 跨链绑定协议 / 例外处理机制 |
| 不承担 | 不生产法源、不提供物理封存、不做战略级慢性偏移诊断 |
| 核心句 | OCGS-F 不造车也不修路，它只管在踩下油门的那一毫秒，校验驾照、目的地和行车记录仪是否同时在线 |

**OCGS-F 是工程规格提供者，工程实现不在理论文档范围。**

#### 核心公式：WeakInv3Q

```
WeakInv3Q(i) = validAbility(i) ∧ validPurpose(i) ∧ dueClosed(i)
```

输出保留完整 APD 三比特向量 `(A, P, D) ∈ {0,1}³`，而非仅标量 AND。三比特向量支持失衡模式诊断。

#### 三级治理强度

| 级别 | 名称 | 条件 | 含义 |
|------|------|------|------|
| S0 | 失衡 | WeakInv3Q = False | 调用被阻断 |
| S1 | 弱闭合 | WeakInv3Q = True | 最低合规，可执行但需监控 |
| S2 | 强闭合 | StrongInv3Q = True（+ sealed + reviewed + noUpstreamAlert） | 证据封存 + 人工复核 |
| S3 | 下游候选闭合 | FullInv3Q = True（+ ecetCleared + tatEscalationReady） | 下游责任/治理审查候选（profile extension，TAT/ODD/PFM/LSM/ARBT 依赖不进入 OCGS 母体定义） |

```
StrongInv3Q(i) = WeakInv3Q(i) ∧ sealEvidenceReady(i) ∧ reviewed(i) ∧ noUpstreamAlert(i)
FullInv3Q(i)   = StrongInv3Q(i) ∧ ecetCleared(i) ∧ tatChainClosed(i)
```

#### APD 八态完整状态空间

| A | P | D | 状态名称 | 处置 |
|---|---|---|----------|------|
| 1 | 1 | 1 | 弱闭合 | 放行 |

> **警告**：`OCGS.gate_state=PASS` 只表示本层入序证据足够，不等于安全、合法、可发布、可免责，也不等于 ODD PASS 或 TAT 高阈值满足。
| 1 | 1 | 0 | Due Deficiency（条件缺失） | 阻断，触发爆发型处置 |
| 1 | 0 | 1 | Purpose Void（目的悬空） | 阻断，转交 TAT 确权 |
| 1 | 0 | 0 | Naked Capability（裸能力） | 阻断，最高优先级告警 |
| 0 | 1 | 1 | 静默授权 | 不构成调用，记录备案 |
| 0 | 1 | 0 | 虚授权 | 记录为组织债务 |
| 0 | 0 | 1 | 孤立记录 | 审计异常 |
| 0 | 0 | 0 | 空转 | 系统空闲态 |

#### 跨链依赖

| 依赖层 | OCGS-F 从该层获取 |
|--------|------------------|
| TAT（40层） | Purpose 授权合法性（`subject` 主体字段）、Due 兜底（`fuse` / `compensation` / `review` 字段） |
| ODD（50层） | Ability 契约注册、Due 证据封存（Seal）、门禁校验 |
| PFM（52层） | Purpose 辅助显影（痛点场域识别，不作为合法性来源） |
| COP（51层） | 风险评级与异常模式检测 |
| LSM（53层） | 失衡模式的体感映射（割裂型/爆发型） |
| ARBT（30层） | FullInv3Q 中的伦理校验 |

---

## 五、跨层接口

OCGS 的跨层位置（可选背景，非使用前提）：

```
DM（10层）→ ASTO（20层）→ OCGS（25层）→ ARBT（30层）→ TAT（40层）→ ODD（50层）
                                        ↘ COP（51层）
                                        ↘ PFM（52层）
                                        ↘ LSM（53层）
```

| 层 | 职责 | 从 OCGS 接收什么 | 向 OCGS 提供什么 |
|----|------|-----------------|-----------------|
| **ASTO**（20层） | 属集变迁语法 | — | 公理体系（RA-1 至 RA-8）、属集/变迁/边界概念 |
| **OCGS**（25层） | 能力有序治理 | — （本层） | — |
| **ARBT**（30层） | 文明与伦理判断 | A/P/D 治理结构 | FullInv3Q 的伦理校验（ecetCleared） |
| **TAT**（40层） | 责任阈值 | OCGS 责任证据包 / audit trail | 责任阈值、`subject` 主体字段与 `fuse` 熔断字段 |
| **ODD**（50层） | 工程闭环 | A/P/D 经翻译后的可执行协议 | 契约注册、Seal 封存、门禁校验 |
| **COP**（51层） | 认知计算 | 风险分级需求 | 风险评级与异常模式检测 |
| **PFM**（54层） | 前线显影 | Purpose 辅助 | 痛点场域识别（不作为合法性来源） |
| **LSM**（52层） | 人生察局 | 失衡模式 | 五局体感映射（急性失衡诊断） |

**防火墙纪律**：OCGS 可独立使用（OP-1），不需要先理解 ASTO。OCGS 若受压，首先失去的是特化方向的工程细节，不自动拖垮上游公理或下游工程层。

---

## 六、术语表

| 术语 | 定义 |
|------|------|
| OCGS | Ordered Capability Governance Set，能力有序治理系统 |
| AbilitySet | 主体已拥有或可调用的能力集合。"能" |
| PurposeSet | 把能力组织到某个目标或状态变迁中的方向性属集。"为" |
| DueSet | 对能力行动施加合当性治理的属集总层。"当" |
| ↔（互约束） | A/P/D 三层之间持续双向制约与调整的关系，通过四通道反馈网络实现 |
| GateSet | 能力进入与阻断机制 |
| EvidenceSet | 留证机制（不是普通日志） |
| SealSet | ODD 封存证据接口 |
| AccountabilitySet | TAT 责任证据包 |
| BoundarySet | 治理可识别性的前提条件；遇到禁元突破时输出升级信号 |
| RemediationSet | 事后修正的兜底机制（冻结/回滚/召回/修正/追责） |
| RiskSet | 治理强度匹配风险的分级机制 |
| ContractSet | 管道约定，DueSet 的子集之一 |
| BJ-1 | 基本判断一：能≠序（能力不自动入序） |
| BJ-2 | 基本判断二：为≠当（目的不替代合当） |
| Inv-1 | 不变量一：能力不得裸奔 |
| Inv-2 | 不变量二：目的不得替代合当 |
| Inv-3 | 不变量三：三层必须可追踪 |
| D1-D12 | 从 BJ-1/BJ-2 推导的十二条结构定理 |
| OCGS-se | OCGS 的软件工程特化方向 |
| OCGS-d / OCGS-Delphi | OCGS 的 Delphi 工程落地方向 |
| OCGS-F | OCGS 的前线运行时特化方向 |
| Invocation | OCGS-F 的最小分析单位——单次能力调用 |
| WeakInv3Q | 前线调用最小闭合公式：validAbility ∧ validPurpose ∧ dueClosed |
| StrongInv3Q | 强闭合：WeakInv3Q ∧ sealed ∧ reviewed ∧ noUpstreamAlert |
| FullInv3Q | 完备闭合：StrongInv3Q ∧ ecetCleared ∧ tatChainClosed |
| APD 三比特向量 | (validAbility, validPurpose, dueClosed) ∈ {0,1}³，失衡诊断的最小充分统计量 |
| 能力裸奔 | 能力未经过目的组织与合当约束，直接显现或调用 |
| 目的失当 | 有目的但缺少合当约束（Purpose 过强、Due 过弱） |
| 治理僵化 | 合当约束过强但能力/目的不足（Due 过强、A/P 过弱） |
| 复数性约束 | 治理不得消除不可替代性、对话可能性与行动空间 |
| 维度零 | 人先于治理结构存在，人不可被完全编码 |
| TAT | 责任架构理论（40层），可读取 OCGS 的责任证据包并独立决定责任阈值 |
| ODD | 产出物驱动开发（50层），OCGS 在 AI 产出物治理中的具体展开 |
| ARBT | 伦理计算理论（30层），提供最高道德/文明尺度的校验 |
| ASTO | 属集变迁存在论（20层），OCGS 的公理来源层 |

### 最易混淆的区分

| 不应混淆 | 区分要点 |
|---------|---------|
| 能力 / 秩序 | 有能力 ≠ 有秩序；能力只是可行动的可能性 |
| 目的 / 合当 | 有目的 ≠ 合当；目的可能错误、越界、无人承责 |
| 流程 / 治理 | 流程通常在 PurposeSet；治理还需要 DueSet（验收、证据、封存、责任） |
| 契约 / 治理 | ContractSet 只是 DueSet 十个子集之一 |
| UI可操作性 / 门禁通过 | 按钮可点击 ≠ 门禁 PASS |
| 序（描述性）/ 当（规范性） | 序回答"有没有结构"，当回答"该不该做"；一个系统可以有序但失当 |
| OCGS / ODD | OCGS 是通用治理理论，ODD 是其在 AI 产出物治理中的具体展开 |
| OCGS / TAT | OCGS 治理能力如何入序，TAT 治理能力后果如何承责 |

---

## 七、阅读与下钻路径

**理论路径**：
1. `SOURCE_OF_TRUTH.md`
2. `PUBLISH_READINESS.md`
3. `DD-体系增强层/OCGS.000-三层总架构与继承契约.md`
4. OCGS.001（OCGS 本体论）
5. OCGS.011（核心公理与命题）
6. OCGS.055（整合白皮书）

**软件工程路径**：
1. `DD-体系增强层/OCGS.000-三层总架构与继承契约.md` → `FF-工程执行层/OCGS-se.001-从功能生产到能力治理.md` → `FF-工程执行层/OCGS-se.011-OCGS-se运行时架构.md` → `FF-工程执行层/OCGS-se.017-OCGS-se成熟度模型.md` → `FF-工程执行层/OCGS-se.023-AI协作指令.md`

**Delphi 工程路径**：
1. `DD-体系增强层/OCGS.000-三层总架构与继承契约.md` → `FF-工程执行层/docs/quickstart.md` → `FF-工程执行层/OCGS-d.O01.OCGS-se-Delphi概述.md`

**前线运行时路径**：
1. `DD-体系增强层/OCGS.000-三层总架构与继承契约.md` → `FF-工程执行层/001.OCGS-F-AI前线能力治理理论总览.md` → `FF-工程执行层/002.OCGS-F-前线能力治理理论白皮书.md` → `FF-工程执行层/003.OCGS-F-失衡模式与边界案例分流.md` → `FF-工程执行层/004.OCGS-F-跨链映射与ODD兜底协议.md` → `FF-工程执行层/005.OCGS-F-例外处理与破窗机制.md`

**状态核查**：`PUBLISH_READINESS.md` 是根层当前发布状态入口；工程执行层内部状态文件只约束对应工程分支。

---

## 八、最短压缩

> **OCGS 的核心命题：能力不自动入序（BJ-1），目的不替代合当（BJ-2）。能力只有经过目的组织与合当约束（A↔P↔D 三层互约束），才成为可治理行动。**

> **OCGS 是 ASTO 在能力治理方向上的选题聚焦，通过母体理论 + 三个特化方向（OCGS-se / OCGS-Delphi / OCGS-F），覆盖从通用本体到软件工程、Delphi 工程、前线运行时的全场景能力治理。**

> **暂无 Zenodo DOI。**

---

---

## 十、失败线总声明

> 详见 `CC-独立理论层/OCGS.089.[失败线]-失败线总声明-Failure-Lines-General-Statement.md`

### 前提失效

| 编号 | 失效条件 | 后果 |
|------|---------|------|
| F1 | Kernel 和 Profile 的边界在 ≥ 3 个独立案例中无法稳定划设 | 核心区分（Kernel vs Profile）不可操作——降级为"能力治理启发式分类" |
| F2 | 能力无法被形式化注册 | Register 前提消失 |
| F3 | 门禁/证据/封存机制不可执行 | 治理闭环断裂 |

### 三层失效

| 层 | 失效条件 |
|----|---------|
| A（能力注册） | 能力描述不可形式化；Kernel/Profile 边界持续漂移 |
| P（目的组织） | 目的无法独立于能力描述；目的之间不可比较 |
| D（合当约束） | 合当条件不可独立于目的；due 语句不可验证 |

### 降级路径

- Kernel/Profile 不可区分→降级为"能力治理启发式分类"
- A↔P↔D 三层互约束不可维持→降级为"注册-门禁"两层
- OCGS-min 不可操作→降级为普通 ABAC/PBAC

---

## 最短压缩句（补充）

> **OCGS 的可证伪性入口：Kernel/Profile 边界可稳定划设；三层互约束可独立验证；能力入序的全链路可审计。**

---

## 外部近邻

OCGS 与以下外部框架有近邻关系，但 OCGS 不等于其中任何一个：

| 近邻框架 | 与 OCGS 的共享点 | OCGS 的差异 |
|----------|-----------------|------------|
| **UCON** (Usage Control) | 使用控制模型，ABAC 扩展 | OCGS 不限于访问控制；覆盖能力入序全链路 |
| **PBAC** (Policy-Based Access Control) | 策略驱动的权限管理 | OCGS 增加目的组织与合当约束，不限于策略判定 |
| **Capability Security** (Capability-based security) | 能力作为权限令牌 | OCGS 治理能力的入序，不只是权限传递 |
| **OPA / ZTA** (Open Policy Agent / Zero Trust) | 策略引擎、零信任 | OCGS 提供能力治理框架，不限于策略执行 |
| **NIST AI RMF** | AI 风险管理 | OCGS 是能力调用治理，不是风险管理全框架 |
| **ISO/IEC 42001** | AI 管理体系 | OCGS 聚焦能力调用入序，不替代管理体系标准 |
| **COBIT** | IT 治理框架 | OCGS 是能力治理微内核，不替代 IT 治理全栈 |

### OCGS-min 最小案例

**案例 A：AI tool call**

```yaml
ability: "web_search_tool"
purpose: "查询用户问题相关的前沿论文"
due: "查询范围限于公开学术数据库；不得查询私人信息"
gate: "PASS"
evidence: "查询日志已记录；结果来源已标注"
audit_trail: "2026-05-23T10:00:00Z | caller=chat_agent | action=search | query='...' | result_count=5"
```

**案例 B：非 AI 组织权限调用**

```yaml
ability: "财务审批权限"
purpose: "批准部门季度预算"
due: "单笔≤50万；超过需双人会签"
gate: "PASS"
evidence: "预算表已附；审批人身份已验证"
audit_trail: "2026-05-23T14:30:00Z | caller=张三 | action=approve | amount=300000 | counter_sign=李四"
```
