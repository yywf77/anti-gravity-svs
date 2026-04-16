# 反重力衣研发路线图（修订版） — 问天计划 v2.0

> 目标：研发可穿戴的反重力材料系统，实现人体在无约束条件下的自由悬浮
> 启动时间：2026-04-16 | 大修订：2026-04-16
> 负责人：问天

---

## 大修订说明

**Phase 1 结论（2026-04-16 完成）**：

- ❌ 纯超导引力磁场路线（GEM）：计算证明无效，Harris批评正确
- ❌ 纯Casimir排斥力路线：需要~10⁹倍未知放大，不可能靠现有机制
- ✅ **超导-真空协同效应（SVS）是唯一突破口**

---

## 总体策略

**超导-真空协同效应（SVS）**：两条死路交汇处，隐藏着未知的第三种力。

不是"对抗引力"，而是"用量子序重塑真空，让引力自己消失"。

---

## SVS核心理论框架

### 协同机制假设链

```
1. 旋转Cooper对（超导量子流）
     ↓ [GEM方程]
2. 引力磁场 B_g（修改时空几何）
     ↓ [边界条件改变]
3. 局部量子真空能谱重构
     ↓ [Casimir效应增强]
4. 真空排斥力 F_Casimir ↑↑↑
     ↓ [协同正反馈]
5. 净升力 F_net = F_Casimir_synergy - mg
     ↓
6. 引力减少 Δg/g = F_net / mg
```

**RF照射的关键作用**：
- 保持超导体处于非平衡态
- 防止Cooper对回到热平衡（抑制耗散）
- 创造持续的非平衡量子真空扰动
- 这可能是Podkletnov实验的"秘密配方"

---

## Phase 2：SVS理论建模（第1-4周）

### 2.1 协同效应数学模型
- [ ] 建立超导引力磁场→真空边界条件→Casimir力的完整方程链
- [ ] RF非平衡态的Ginzburg-Landau理论框架
- [ ] 协同放大因子的理论推导（目标：10⁸-10⁹倍）
- [ ] 写出 phase2-modeling/svs-synergy-model.py

### 2.2 RF-超导动力学
- [ ] 研究RF场对超导体Cooper对的影响
- [ ] 分析非平衡超导态的寿命和稳定性
- [ ] 找出RF频率、功率与协同效应的关系
- [ ] 写出 phase2-modeling/rf-superconductor-dynamics.py

### 2.3 参数空间优化
- [ ] 对SVS模型进行参数扫描
- [ ] 寻找协同效应的临界条件（非线性跃迁点）
- [ ] 确定最优材料、几何、RF参数组合
- [ ] 画出 phase3-simulation/svs-phase-diagram.png

### 2.4 里程碑交付物
- 📄 `phase2-modeling/svs-theory.md` — SVS协同效应完整理论
- 📄 `phase2-modeling/rf-dynamics.md` — RF超导动力学分析
- 💻 `code/svs-synergy-model.py` — SVS数值模型
- 💻 `code/svs-simulator.py` — SVS仿真器

---

## Phase 3：SVS实验设计（第5-8周）

### 3.1 可行性验证实验设计
- [ ] 微型SVS装置设计（克级测试）
- [ ] 测量方案：RF+旋转超导体的引力效应检测
- [ ] 所需仪器清单和成本估算
- [ ] 实验步骤的SOP（标准操作程序）

### 3.2 精确复现Podkletnov实验
- [ ] 基于原始参数设计复现实验
- [ ] 加入现代传感技术（原子干涉仪、扭转天平）
- [ ] 对比RF开/关的效果差异
- [ ] 写出 phase3-simulation/podkletnov-replication-plan.md

### 3.3 新型SVS材料探索
- [ ] 镍基高温超导（2026 Nature）的SVS潜力评估
- [ ] 拓扑超导材料的调研
- [ ] 超导-超材料复合材料的设计
- [ ] 室温超导突破后的SVS预期参数

### 3.4 里程碑交付物
- 📄 `phase3-simulation/experiment-design.md` — 微型验证实验设计
- 📄 `phase3-simulation/replication-plan.pdf` — Podkletnov复现方案
- 📄 `phase3-simulation/new-materials.md` — 新型SVS材料调研
- 📄 `phase3-simulation/cost-estimate.md` — 预算和资源规划

---

## Phase 4：工程化设计（第9-16周）

### 4.1 SVS织物原型设计
- [ ] 多层SVS织物架构（超导层+RF层+真空谐振层+隔热层）
- [ ] 柔性超导导线布局（编织方案）
- [ ] RF发生器的小型化集成
- [ ] 能量系统设计（电池+超导储能）

### 4.2 人体悬浮系统集成
- [ ] 70kg人体悬浮的总参数预算
- [ ] 稳定性控制（重心、姿态）
- [ ] 安全性设计（磁场暴露、热管理）
- [ ] 外形和可穿戴性设计

### 4.3 里程碑交付物
- 📄 `phase4-design/svs-garment-spec.md` — SVS衣规格书
- 📄 `phase4-design/engineering-drawings/` — 工程图纸
- 📄 `phase4-design/safety-assessment.md` — 安全性评估
- 📄 `phase4-design/prototype-roadmap.md` — 原型路线图

---

## Phase 5：协作与验证（持续）

### 5.1 寻找合作
- [ ] 接触有超导实验条件的大学实验室
- [ ] 联系国内高温超导研究团队（南方科技大学、清华大学）
- [ ] 探索与国际同行合作的可能性
- [ ] 申请相关科研基金

### 5.2 小规模验证
- [ ] 如果条件允许：制作并测试克级SVS原型
- [ ] 发表预印本论文（arXiv）建立优先权
- [ ] 申请核心专利

### 5.3 里程碑交付物
- 📄 `phase5-proof/collaboration-contacts.md` — 合作方联系记录
- 📄 `phase5-proof/patent-draft.md` — 专利草稿
- 📄 `research-report-final.md` — 最终研究报告

---

## 阶段性汇报节点

| 节点 | 预计时间 | 汇报内容 |
|------|---------|---------|
| M1 ✅ | Phase 1 完成 | 文献综述 + 理论 + 计算（已完成）|
| M2 | Phase 2 完成 | SVS理论 + RF动力学模型 |
| M3 | Phase 3 中期 | 实验设计 + 合作进展 |
| M4 | Phase 3 完成 | Podkletnov复现 + 新材料评估 |
| M5 | Phase 4 完成 | SVS织物原型设计 |
| M6 | Phase 5 完成 | 小规模验证 + 专利/论文 |

---

## 当前状态：Phase 2 — SVS理论建模 — 立即启动
