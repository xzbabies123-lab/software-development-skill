# Software Development Skill for Non-Technical Users

**为非技术用户设计的软件开发技能包** — 让不懂代码的人也能通过AI完成软件开发。

---

## 这是什么？

这是一套完整的软件开发流程规范，帮助非技术用户：
- 清晰表达需求（苏格拉底式提问）
- 快速看到UI原型（先看效果再开发）
- 确保质量（截图即证据）
- 避免项目烂尾（强制检查点）

---

## 核心特性

### 🎯 Phase 0: 需求澄清
- 苏格拉底式提问，把模糊想法变成清晰需求
- 强制输出需求文档，不靠口头约定

### 🎨 Phase 1: UI/UX快速原型
- **先看效果再开发** — 非技术用户最关心视觉
- 快速生成UI设计稿，确认后再进入开发

### 📋 Phase 2: 技术设计
- AI生成技术方案
- 用户确认技术选型

### 💻 Phase 3: 开发
- 代码实现
- 本地运行验证

### ✅ Phase 4: 验证
- **截图即证据** — 每个功能必须有截图证明
- Dev↔QA Loop — 开发和测试循环验证

### 🚀 Phase 5: 部署
- 上线发布
- 运维监控

---

## 文件结构

```
software-development-skill/
├── SKILL.md                    # 主技能文档（AI读取）
├── README.md                   # 本文件
├── scripts/                    # 验证脚本（强制约束）
│   ├── env_check_quick.py      # 环境快速检查
│   ├── env_check_phase.py      # Phase依赖检查
│   ├── phase0_validator.py     # Phase 0验证
│   ├── phase1_validator.py     # Phase 1验证
│   ├── phase2_validator.py     # Phase 2验证
│   ├── phase3_validator.py     # Phase 3验证
│   ├── phase4_validator.py     # Phase 4验证
│   ├── gate_checker.py         # Phase门控检查
│   └── progress_tracker.py     # 进度追踪
├── templates/                  # 文档模板
│   ├── requirement-doc.md      # 需求文档模板
│   ├── design-doc.md           # 技术设计模板
│   └── test-report.md          # 测试报告模板
└── examples/                   # 案例
    └── huixing-use-case.md     # 惠行用车MVP案例
```

---

## 如何使用？

### 对AI说这些关键词触发：
- "载入软件开发skill"
- "软件开发"
- "开发软件"
- "做一个软件"
- "开发一个功能"

### AI会自动：
1. 检查环境（Phase -1）
2. 苏格拉底式提问澄清需求（Phase 0）
3. 快速生成UI原型让你确认（Phase 1）
4. 技术设计 → 开发 → 测试 → 部署

---

## 核心方法论

### 1. 代码化约束
不靠AI自觉，用Python脚本强制验证每个Phase的输出。

### 2. 截图即证据
每个功能必须有截图证明，不接受口头"做完了"。

### 3. Dev↔QA Loop
开发 → 测试 → 修复 → 再测试，循环直到通过。

### 4. 质量门控
每个Phase结束必须通过验证，才能进入下一Phase。

---

## 参考来源

- [agency-agents](https://github.com/ao-data/agency-agents) (MIT License)
- NEXUS框架
- Dev↔QA Loop方法论

---

## License

MIT License — 自由使用，保留署名。
