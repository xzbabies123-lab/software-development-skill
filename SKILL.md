---
name: software-development-for-non-technical-users
description: 完整软件开发流程skill — 面向非技术用户，一句话需求启动，UI/UX优先展示，代码化约束强制执行
version: 1.0.0
author: Hermes Agent
license: MIT
triggers:
  - 载入软件开发skill
  - 软件开发
  - 开发软件
  - 做一个软件
  - 开发一个功能
  - 软件开发流程
  - 开发流程
dependencies:
  - brainstorm-focus
  - reflective-execution
---

# Software Development for Non-Technical Users

> 完整软件开发流程，面向非技术用户。一句话需求启动，UI/UX优先，代码化约束强制执行。

---

## 适用场景

- 非技术用户（不懂代码、不懂技术术语）
- 中小型项目（MVP、个人工具、小程序）
- 快速迭代（2周内上线）
- 一个人+AI协作
- 技术栈：uni-app + FastAPI + MySQL（抖音/微信小程序）

---

## 核心特点

1. **一句话需求启动** — 不需要写长文档
2. **UI/UX优先展示** — 第一时间看到效果
3. **苏格拉底式澄清** — 像做选择题，不是填表
4. **代码化约束** — 不靠AI自觉，靠脚本强制
5. **截图即证据** — 验收必须有截图，不接受口头声称
6. **进度可视化** — 随时知道做到哪了
7. **风险预警** — 提前告知可能的问题
8. **失败自动回滚** — 出问题可回退

---

## 流程概览

```
Phase -1: 环境检查（快速检查核心依赖）
    ↓
Phase 0: 需求澄清（苏格拉底式提问）
    ↓
Phase 1: UI/UX快速原型（优先展示视觉效果）
    ↓
Phase 2: 技术设计（数据库+API）
    ↓
Phase 3: 开发（写代码）
    ↓
Phase 4: 验证（截图即证据+Dev↔QA Loop）
    ↓
Phase 5: 上线（部署+监控）
```

---

## Phase -1: 环境快速检查

**目的**：确保核心依赖可用，避免项目跑到一半卡住。

**执行时机**：skill载入后立即执行，秒级完成。

**检查内容**：

| 类别 | 检查项 | 失败处理 |
|-----|-------|---------|
| 核心工具 | todo可用 | ❌ 停止，必须修复 |
| 核心工具 | terminal可用 | ❌ 停止，必须修复 |
| 核心工具 | Python环境 | ❌ 停止，必须修复 |
| Phase 0依赖 | brainstorm-focus skill | ⚠️ 提示安装或降级 |
| Phase 1依赖 | browser_vision | ⚠️ 降级为文字描述 |
| Phase 1依赖 | vision_analyze | ⚠️ 降级为文字描述 |

**执行脚本**：`python scripts/env_check_quick.py`

**输出格式**：

```
【环境检查】
✅ todo工具可用
✅ terminal工具可用
✅ Python环境可用
⚠️ brainstorm-focus skill未安装 → 降级为普通提问
✅ browser_vision可用

环境检查通过，开始Phase 0。
```

---

## Phase 0: 需求澄清

**目的**：一句话需求 → 结构化需求文档。

**核心机制**：苏格拉底式提问（每轮1问题+3选项+建议）。

**执行步骤**：

1. 加载 `brainstorm-focus` skill
2. 执行苏格拉底式提问（5-8轮）
3. **强制验证**：调用 `python scripts/phase0_validator.py`
4. 如果验证失败，打印错误并重新执行
5. 验证通过后，生成需求文档
6. **门控检查**：调用 `python scripts/gate_checker.py --phase=0`
7. 向用户展示需求文档，等待确认
8. 用户确认后，调用 `todo` 改状态为 `completed`

**验证规则**（由脚本强制执行）：

- 每轮只问1个问题
- 每个问题至少3个选项
- 每轮必须提供建议
- 必须生成需求文档
- 必须等待用户确认

**输出格式**：

```markdown
# 需求文档

## 项目名称
[项目名]

## 功能清单
1. [功能1] — [描述]
2. [功能2] — [描述]
...

## 优先级排序
| 功能 | RICE评分 | 优先级 |
|-----|---------|--------|
| [功能1] | [分数] | P0 |
| [功能2] | [分数] | P1 |
...

## 技术栈
- 前端：uni-app（抖音/微信小程序）
- 后端：FastAPI
- 数据库：MySQL
- 缓存：Redis

## 时间预估
- Phase 1 UI设计：[时间]
- Phase 2 技术设计：[时间]
- Phase 3 开发：[时间]
- Phase 4 验证：[时间]
- Phase 5 上线：[时间]
总计：[时间]

## 风险预警
⚠️ [风险1] — [建议]
⚠️ [风险2] — [建议]

## 确认
请确认需求文档（回复"确认"或提出修改意见）
```

---

## Phase 1: UI/UX快速原型

**目的**：第一时间展示视觉效果，用户确认后才开始开发。

**执行步骤**：

1. **开始前检查**：调用 `python scripts/env_check_phase.py --phase=1`
2. 基于需求文档，生成页面流程图
3. 生成UI设计稿（豆包AI或HTML）
4. **强制截图**：调用 `browser_vision` 截图
5. **强制验证**：调用 `python scripts/phase1_validator.py`
6. 向用户展示截图，等待确认
7. 用户确认后，调用 `todo` 改状态为 `completed`
8. **门控检查**：调用 `python scripts/gate_checker.py --phase=1`

**验证规则**：

- 必须生成页面流程图
- 必须生成UI设计稿
- 必须有截图证据
- 必须等待用户确认

**输出格式**：

```
【Phase 1完成】
生成了[N]个页面：
- [页面1]：[描述]
- [页面2]：[描述]
...

截图证据：
![页面1](/tmp/ui_page1.png)
![页面2](/tmp/ui_page2.png)

确认？（回复"确认"或"修改"）
```

---

## Phase 2: 技术设计

**目的**：设计数据库结构、API接口。

**执行步骤**：

1. **开始前检查**：调用 `python scripts/env_check_phase.py --phase=2`
2. 设计数据库表结构
3. 设计API接口文档
4. **强制验证**：调用 `python scripts/phase2_validator.py`
5. 生成设计文档
6. **门控检查**：调用 `python scripts/gate_checker.py --phase=2`

**验证规则**：

- 必须有数据库表结构（CREATE TABLE语句）
- 必须有API接口文档（路径、参数、返回值）
- 设计文档必须完整

**输出格式**（简化版，用户不用看细节）：

```
【Phase 2完成】
技术方案已设计：
- 数据库：[N]张表
- API接口：[N]个接口
- 技术栈：uni-app + FastAPI + MySQL

（技术细节已保存，用户无需关注）
```

---

## Phase 3: 开发

**目的**：写代码，实现功能。

**执行步骤**：

1. **开始前检查**：调用 `python scripts/env_check_phase.py --phase=3`
2. 环境搭建（创建项目、安装依赖）
3. 核心功能开发
4. 单元测试
5. **强制验证**：调用 `python scripts/phase3_validator.py`
6. 状态标记为 `NEEDS VERIFICATION`
7. **门控检查**：调用 `python scripts/gate_checker.py --phase=3`

**验证规则**：

- 代码必须可运行（无语法错误）
- 核心功能必须实现
- 单元测试必须通过

**并行开发**（可选）：

如果功能之间无依赖，可派subagent并行开发：

```
Phase 2结束后，分析功能依赖：
- [功能A]（独立）→ Subagent 1
- [功能B]（独立）→ Subagent 2
- [功能C]（依赖A）→ 等待A完成
```

**输出格式**：

```
【Phase 3完成】
开发完成：
- [功能1] ✅
- [功能2] ✅
- [功能3] ✅

状态：NEEDS VERIFICATION（待验证）
```

---

## Phase 4: 验证

**目的**：功能测试，截图即证据，Dev↔QA Loop。

**核心机制**：

1. **截图即证据** — 每个验收标准必须有截图
2. **Dev↔QA Loop** — 发现bug→修复→再验证，最多3次
3. **默认NEEDS WORK** — 只有通过验证才能标记COMPLETE

**执行步骤**：

1. **开始前检查**：调用 `python scripts/env_check_phase.py --phase=4`
2. 功能测试（逐项验收标准）
3. **强制截图**：调用 `browser_vision` 截图
4. **强制验证**：调用 `python scripts/phase4_validator.py`
5. 如果验证失败：
   - 修复bug
   - 重试（最多3次）
   - 3次失败 → 升级告知用户
6. 验证通过后，状态改为 `COMPLETE`
7. **门控检查**：调用 `python scripts/gate_checker.py --phase=4`

**验证规则**：

- 每个验收标准必须有截图
- 所有验收标准必须通过
- Dev↔QA Loop次数 ≤ 3

**输出格式**：

```markdown
# 测试报告

## 验收标准
| # | 标准 | 状态 | 截图证据 |
|---|------|------|---------|
| 1 | [标准1] | ✅ PASS | ![截图](/tmp/test1.png) |
| 2 | [标准2] | ✅ PASS | ![截图](/tmp/test2.png) |
| 3 | [标准3] | ✅ PASS | ![截图](/tmp/test3.png) |

## Dev↔QA Loop
- 第1次测试：PASS
- 重试次数：0/3

## 结论
所有验收标准通过，进入Phase 5。
```

**失败升级格式**：

```
【Phase 4失败】
经过3次重试，以下验收标准仍未通过：
- [标准1] ❌ — [问题描述]

建议：
1. 人工介入排查
2. 或降低验收标准
3. 或延后处理

请决定下一步。
```

---

## Phase 5: 上线

**目的**：部署到线上，配置监控。

**执行步骤**：

1. **开始前检查**：调用 `python scripts/env_check_phase.py --phase=5`
2. **上线检查清单**：
   - [ ] 所有功能已测试通过
   - [ ] 支付功能已配置真实商户号（如有）
   - [ ] 域名已备案（如有）
   - [ ] 小程序已提交审核（如有）
   - [ ] 服务器已配置监控报警
   - [ ] 数据库已备份
3. 部署配置
4. 数据迁移
5. 监控报警配置
6. **强制验证**：调用 `python scripts/phase5_validator.py`
7. **门控检查**：调用 `python scripts/gate_checker.py --phase=5`

**输出格式**：

```
【Phase 5完成】
上线成功：
- 访问地址：[URL]
- 小程序：[小程序名]（审核中）

监控配置：
- 性能监控 ✅
- 错误报警 ✅
- 数据库备份 ✅

项目完成！
```

---

## 进度追踪

**每个Phase结束，自动更新进度条**：

调用 `python scripts/progress_tracker.py`

**输出格式**：

```
【项目进度】
███████░░░ 70% Phase 3 开发中

✅ Phase -1 环境检查（已完成）
✅ Phase 0 需求澄清（已完成）
✅ Phase 1 UI设计（已完成）
✅ Phase 2 技术设计（已完成）
🔄 Phase 3 开发（进行中，预计2小时）
⏳ Phase 4 验证（待开始）
⏳ Phase 5 上线（待开始）

当前任务：[任务名]
预计完成：[时间]
```

**用户随时可问**："进度"、"做到哪了"、"还要多久"

---

## 失败回滚

**每个Phase结束，自动保存快照**：

```
Phase 0 完成 → 保存：.snapshots/phase0_requirement.md
Phase 1 完成 → 保存：.snapshots/phase1_ui/
Phase 2 完成 → 保存：.snapshots/phase2_tech.md
Phase 3 完成 → 保存：.snapshots/phase3_code/
Phase 4 完成 → 保存：.snapshots/phase4_test.md
```

**失败时自动回滚**：

```
Phase 4 验证失败（第3次）
    ↓
自动回滚到 Phase 3 快照
    ↓
重新开发
```

---

## 里程碑确认

**每个Phase结束，强制用户确认关键产出**：

| Phase | 确认内容 | 确认方式 |
|-------|---------|---------|
| Phase 0 | 需求文档 | AI总结关键点，用户回复"确认"或"修改" |
| Phase 1 | UI设计稿 | 展示截图，用户回复"确认"或"修改" |
| Phase 2 | 技术方案 | 简化版（只告诉用什么技术），用户回复"确认" |
| Phase 3 | 功能演示 | 展示功能截图，用户回复"确认"或"修改" |
| Phase 4 | 测试结果 | 展示测试报告，用户回复"确认" |

---

## 调用方式

**启动新项目**：

```
"载入软件开发skill"
"做一个签到功能"
"开发惠行用车MVP"
```

**中途查询**：

```
"进度" → 显示进度条
"还要多久" → 显示时间预估
"当前Phase" → 显示当前阶段详情
"跳过Phase 2" → 直接进入Phase 3（如果设计已存在）
"重新执行Phase 4" → 重新验证
```

---

## 致谢

本skill的设计思路参考了以下开源项目：

- **agency-agents** (MIT License)
  - 借鉴：NEXUS框架、Dev↔QA Loop、交接模板设计、"截图即证据"方法论
  - 原项目：https://github.com/agency-agents

---

## License

MIT License

Copyright (c) 2026 Hermes Agent

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.