# RT6 发布准备状态

> 更新日期：`2026-06-15`
> 作者：Yi Fu（付毅，ODDFounder，fuyi.it@live.cn）

## 1. 当前结论

> **RT6（共鸣与跃迁六步法）当前适合作为低风险行动承接框架进行内部使用和有限公开说明。**
>
> RT6 只有在 COP 未处于 FREEZE / REFER / UNKNOWN、用户同意且边界清楚时才可启动；它不治疗、不处方、不输出复诊结论或高风险强承诺。

> 2026-06-13 补充：RT6 已新增并细化 `AA-母版源层/README.md` 与 `SOURCE_OF_TRUTH.md`，母版导航、独立法源路径、canonical output、RT6-min ABI、历史原型边界和旧临床口径降级已固定。该状态表示可有限公开说明，不表示经验证实。
>
> 2026-06-15 补充：RT6.004 已补齐 LSM/WSH 到 RT6 的最小候选输入接口。`lsm_to_rt6_action_candidate` 与 `wsh_to_rt6_action_candidate` 只作为上游材料，不替代 COP 低风险分流、用户同意、边界说明、停止条件或回看机制。

## 2. 发布前需保持的边界

| 项目 | 状态 | 说明 |
|------|------|------|
| 六步结构 | 已形成 | 共鸣 / 命名 / 转译 / 执行 / 反馈 / 跃迁 |
| 外部比较 | 已补齐 | 已新增不可替代问题与外部比较文件 |
| 失败线 | 已补齐 | 已新增失败线与退出条件 |
| 母版源层导航 | 已补齐 | 2026-06-13 已新增 AA 母版入口与 SOURCE_OF_TRUTH |
| 标准输出 | 已固定 | canonical output 为 `non_clinical_action_plan` |
| RT6-min ABI | 已固定 | consent_scope / cop_clearance / boundary_notice / six_steps / review_loop / stop_condition / handoff_target |
| COP Clearance | 必须保留 | 风险未清、证据不足或需专业渠道时不启动 |
| 退出机制 | 必须保留 | 无效或越界时回到 COP / PFM / LSM / WSH 或专业渠道 |
| LSM/WSH 候选输入 | 已补齐 | 只作为行动候选材料；不得绕过 RT6-min 启动条件 |

## 3. 当前建议发布对象

- `README.md`
- `RT6-4AI.md`
- `SOURCE_OF_TRUTH.md`
- `AA-母版源层/README.md`
- `CC-独立理论层/RT6.007-不可替代问题与外部比较.md`
- `CC-独立理论层/RT6.008-失败线与退出条件.md`

## 4. 公开定位

RT6 是把已分流、已同意、低风险的问题转成可执行、可反馈、可退出行动的承接方法。它不越过 COP，不替代临床、法律、医疗或其他专业判断。

## 5. 当前不可公开声称

- 不声称 RT6 已经实证证明有效；
- 不声称 RT6 可处理临床、法律、医疗、投资或高影响责任问题；
- 不声称六步主链优于所有咨询、教练、服务设计或实施科学框架；
- 不声称案例库构成效果证明，案例只能作为走通示例和应用种子。
