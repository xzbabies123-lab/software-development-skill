# 惠行用车 MVP 开发案例

## 项目背景

**用户画像**：非技术用户，关注UI/UX，一句话需求启动

**项目目标**：11项功能，2周上线

**技术栈**：uni-app + FastAPI + MySQL + Redis

---

## Phase 0：需求澄清

**用户原始需求**："做一个司机签到积分系统"

**AI苏格拉底提问**：

```
第1轮：签到的主要目的是？
  A. 提高司机活跃度
  B. 增加司机粘性
  C. 促进消费转化
用户选择：A

第2轮：签到奖励形式偏好？
  A. 积分（可兑换商品）
  B. 优惠券（直接抵扣）
  C. 现金红包（可提现）
用户选择：A

第3轮：连续签到奖励机制？
  A. 7天递增奖励
  B. 阶梯奖励（3天/7天/15天）
  C. 无额外奖励
用户选择：B

第4轮：签到方式？
  A. 点击签到
  B. 定位签到（需GPS）
  C. 扫码签到
用户选择：A

第5轮：需要签到日历展示吗？
  A. 需要（展示签到记录）
  B. 不需要
用户选择：A

第6轮：积分兑换方式？
  A. 兑换商品
  B. 兑换优惠券
  C. 兑换现金（需提现功能）
用户选择：C

第7轮：是否需要积分三级返利？
  A. 需要（推荐司机获得奖励）
  B. 不需要
用户选择：A

第8轮：确认需求？
用户选择：确认
```

**生成需求文档**：

```markdown
## 签到积分系统需求

### 核心功能
- 每日点击签到获得积分
- 连续签到阶梯奖励（3天/7天/15天）
- 签到日历展示签到记录
- 积分可兑换现金（需提现功能）

### 积分规则
- 每日签到：10积分
- 连续3天：额外30积分
- 连续7天：额外100积分
- 连续15天：额外300积分
- 断签重新计算

### 三级返利机制
- A分：个人积分，可兑换福利
- B分：推荐积分，可兑换现金
- 推荐1级：获得B分10%
- 推荐2级：获得B分5%
- 推荐3级：获得B分2%

### 风险提示
⚠️ 三级返利涉及合规风险，建议咨询法务
```

---

## Phase 1：UI/UX快速原型

**生成页面流程图**：

```
首页 → 签到页 → 积分页 → 提现页
  ↓       ↓       ↓
日收益   签到日历  积分记录
```

**生成UI设计稿**（使用豆包AI）：

- 首页：日收益核算 + 优惠速览双展示
- 签到页：签到日历 + 积分显示 + 连续签到提示
- 积分页：A分/B分分开显示 + 兑换按钮
- 提现页：提现金额输入 + 提现记录

**用户确认**："确认，这是我要的样子"

---

## Phase 2：技术设计

**数据库设计**：

```sql
-- 签到记录表
CREATE TABLE sign_records (
  id INT PRIMARY KEY AUTO_INCREMENT,
  user_id INT NOT NULL,
  sign_date DATE NOT NULL,
  continuous_days INT DEFAULT 1,
  points_awarded INT DEFAULT 10,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 积分表
CREATE TABLE user_points (
  id INT PRIMARY KEY AUTO_INCREMENT,
  user_id INT NOT NULL,
  a_points INT DEFAULT 0,  -- 个人积分
  b_points INT DEFAULT 0,  -- 推荐积分
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- 提现记录表
CREATE TABLE withdraw_records (
  id INT PRIMARY KEY AUTO_INCREMENT,
  user_id INT NOT NULL,
  amount DECIMAL(10,2) NOT NULL,
  status ENUM('pending', 'approved', 'rejected') DEFAULT 'pending',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

**API接口设计**：

```
POST /api/sign/daily       # 每日签到
GET  /api/sign/calendar    # 签到日历
GET  /api/points/balance   # 积分余额
POST /api/points/withdraw  # 提现申请
GET  /api/withdraw/history # 提现记录
```

---

## Phase 3：开发

**技术栈确认**：
- 前端：uni-app（支持抖音/微信小程序）
- 后端：FastAPI
- 数据库：MySQL
- 缓存：Redis（签到状态缓存）

**开发进度**：

```
【项目进度】
██████████ 100% Phase 3 开发完成

✅ Phase 0 需求澄清（已完成）
✅ Phase 1 UI设计（已完成）
✅ Phase 2 技术设计（已完成）
✅ Phase 3 开发（已完成）
🔄 Phase 4 验证（进行中）
⏳ Phase 5 上线（待开始）

当前任务：签到功能测试
预计完成：今天18:00
```

---

## Phase 4：验证

**验收标准验证**：

| 验收标准 | 状态 | 证据 |
|---------|------|------|
| 用户能正常签到 | ✅ PASS | `/screenshots/签到成功.png` |
| 连续签到积分正确计算 | ✅ PASS | `/screenshots/积分计算.png` |
| 签到日历正确显示 | ✅ PASS | `/screenshots/签到日历.png` |
| 积分兑换流程完整 | ✅ PASS | `/screenshots/积分兑换.png` |
| 提现功能正常 | ✅ PASS | `/screenshots/提现成功.png` |

**Dev↔QA Loop记录**：

```
第1次验证：❌ FAIL
- 失败项：连续签到积分计算错误
- 修复：修正积分计算逻辑
- 修复时间：2026-05-16 14:30

第2次验证：✅ PASS
- 全部验收标准通过
- 验证时间：2026-05-16 15:00
```

---

## Phase 5：上线

**上线检查清单**：

```
- [x] 所有功能已测试通过
- [x] 数据库已配置
- [x] Redis已配置
- [x] 小程序已提交审核
- [x] 服务器已配置监控
- [ ] 域名已备案（待完成）
```

**上线结果**：

- 抖音小程序：审核中（预计3-7天）
- 微信小程序：审核中（预计1-3天）
- 后端服务：已部署到云服务器

---

## 项目总结

**总耗时**：约5小时

**关键成功因素**：
1. Phase 0需求澄清充分，避免返工
2. Phase 1 UI原型快速确认，用户满意
3. Phase 4验证严格，截图证据完整
4. Dev↔QA Loop机制有效，bug及时修复

**风险提示**：
- 三级返利合规风险已标注
- 小程序审核时间不可控，需提前准备

---

## 对Hermes的借鉴价值

**可复用机制**：
- 苏格拉底式需求澄清
- UI原型优先展示
- 截图即证据验收
- Dev↔QA Loop质量保障
- 进度可视化追踪