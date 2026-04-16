#!/usr/bin/env python3
"""
anti_gravity_suit_designer.py
反重力衣概念设计生成器 v1.0
问天计划 | Phase 4 工程化设计

生成多版设计方案，包含技术参数、可行性分析、制造路线图
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, FancyBboxPatch
import matplotlib.patches as mpatches

# 物理常数和材料参数
G = 9.81  # m/s^2
RHO_BSCCO = 6500  # kg/m^3, BSCCO密度
RHO_YBCO = 6300   # kg/m^3, YBCO密度
RHO_CU = 8960     # kg/m^3, 铜电极
RHO_KAPTON = 1420 # kg/m^3, 聚酰亚胺基底

# 设计约束
HUMAN_MASS = 70  # kg
HUMAN_HEIGHT = 1.7  # m
TARGET_LIFT = HUMAN_MASS * G * 1.1  # 10%安全余量

class AntiGravitySuitDesign:
    """反重力衣设计方案基类"""
    
    def __init__(self, name, concept_type):
        self.name = name
        self.type = concept_type
        self.specs = {}
        self.analysis = {}
        
    def calculate_performance(self):
        """计算性能指标"""
        raise NotImplementedError
        
    def generate_visualization(self):
        """生成概念图"""
        raise NotImplementedError

class DesignV1_WovenFabric(AntiGravitySuitDesign):
    """
    设计方案V1：超导织物背心
    概念：BSCCO超导纤维编织成可穿戴背心
    """
    
    def __init__(self):
        super().__init__("V1-超导织物背心", "柔性可穿戴")
        self.specs = {
            "material": "BSCCO-2212",
            "layer_count": 50,
            "layer_thickness": 0.001,  # 1mm/层
            "fiber_diameter": 0.0001,   # 100μm纤维
            "coverage_area": 0.3,       # 背部覆盖0.3m²
            "operating_temp": 20,       # 液氢温区20K
            "rotation_speed": 5000,     # rpm
            "rf_power": 5000,           # W/m²
            "total_mass": 0,            # 待计算
        }
        
    def calculate_performance(self):
        # 纤维体积计算
        fiber_volume = (self.specs["coverage_area"] * 
                       self.specs["layer_count"] * 
                       self.specs["layer_thickness"] * 
                       0.3)  # 30%填充率
        
        # 各组件质量
        sc_mass = fiber_volume * RHO_BSCCO
        substrate_mass = (self.specs["coverage_area"] * 
                         self.specs["layer_count"] * 
                         0.0002 * RHO_KAPTON)
        electrode_mass = self.specs["coverage_area"] * 0.0005 * RHO_CU * 2
        cryostat_mass = 5  # 液氢杜瓦瓶
        rf_system_mass = 3  # RF发生器和天线
        motor_mass = 2  # 旋转电机
        
        total_mass = sc_mass + substrate_mass + electrode_mass + cryostat_mass + rf_system_mass + motor_mass
        self.specs["total_mass"] = total_mass
        
        # SVS v2.0计算
        omega = self.specs["rotation_speed"] * 2 * np.pi / 60
        P_rf = self.specs["rf_power"]
        N = self.specs["layer_count"]
        
        # Δg/g = C_SVS × ω × P_RF × (1-P/Pc)^(-1) × N^γ
        C_SVS = 3.78e-7
        Pc = 1e4
        gamma = 1.5
        
        if P_rf >= Pc * 0.99:
            lift_ratio = 0
        else:
            lift_ratio = (C_SVS * omega * P_rf / (1 - P_rf/Pc) * 
                         (N ** gamma))
        
        lift_force = HUMAN_MASS * G * min(lift_ratio, 10)  # 最大10倍
        net_lift = lift_force - total_mass * G
        
        self.analysis = {
            "sc_mass": sc_mass,
            "total_mass": total_mass,
            "lift_ratio": lift_ratio * 100,  # %
            "lift_force": lift_force,
            "net_lift": net_lift,
            "payload_capacity": HUMAN_MASS - total_mass if net_lift > 0 else 0,
            "feasibility": "中等" if net_lift > 0 else "低",
        }
        
        return self.analysis
    
    def generate_visualization(self):
        fig, axes = plt.subplots(1, 2, figsize=(14, 6))
        
        # 左图：背心结构示意图
        ax = axes[0]
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.set_aspect('equal')
        ax.axis('off')
        ax.set_title('V1: 超导织物背心结构', fontsize=14, fontweight='bold')
        
        # 背心轮廓
        vest = FancyBboxPatch((2, 2), 6, 6, boxstyle="round,pad=0.1",
                              facecolor='lightblue', edgecolor='navy', linewidth=2)
        ax.add_patch(vest)
        
        # 分层示意
        for i in range(5):
            y = 2.5 + i * 1
            rect = Rectangle((2.2, y), 5.6, 0.8, 
                           facecolor=plt.cm.viridis(i/5), alpha=0.7)
            ax.add_patch(rect)
            ax.text(5, y+0.4, f'Layer {i+1}', ha='center', va='center', fontsize=8)
        
        # 标注
        ax.annotate('BSCCO超导纤维', xy=(5, 8.5), ha='center', fontsize=10)
        ax.annotate('液氢冷却\n20K', xy=(8.5, 5), ha='left', fontsize=9,
                   bbox=dict(boxstyle='round', facecolor='cyan', alpha=0.5))
        ax.annotate('RF天线阵列', xy=(1.5, 5), ha='right', fontsize=9,
                   bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.5))
        
        # 右图：质量分布饼图
        ax = axes[1]
        masses = [
            self.analysis["sc_mass"],
            5,  # cryostat
            3,  # RF
            2,  # motor
            self.analysis["total_mass"] - self.analysis["sc_mass"] - 10
        ]
        labels = ['BSCCO纤维', '液氢杜瓦', 'RF系统', '旋转电机', '其他']
        colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#ff99cc']
        
        wedges, texts, autotexts = ax.pie(masses, labels=labels, colors=colors,
                                          autopct='%1.1f%%', startangle=90)
        ax.set_title(f'质量分布\n总重: {self.analysis["total_mass"]:.1f}kg', 
                    fontsize=12, fontweight='bold')
        
        plt.tight_layout()
        plt.savefig('/Users/adminstrator/.qclaw/workspace-agent-10ad9760/research/anti-gravity/phase4-engineering/design_v1_fabric.png',
                   dpi=150, bbox_inches='tight')
        plt.close()

class DesignV2_DiskArray(AntiGravitySuitDesign):
    """
    设计方案V2：分布式碟片阵列
    概念：多个小型超导碟片分布在全身关键点
    """
    
    def __init__(self):
        super().__init__("V2-分布式碟片阵列", "模块化")
        self.specs = {
            "disk_count": 12,           # 12个碟片
            "disk_diameter": 0.08,      # 8cm直径
            "disk_thickness": 0.005,    # 5mm厚
            "material": "YBCO",
            "layer_per_disk": 20,
            "placement": ["背部x4", "腰部x4", "大腿x4"],
            "operating_temp": 77,       # 液氮温区
            "rotation_speed": 3000,
            "rf_power": 3000,
        }
        
    def calculate_performance(self):
        # 单碟参数
        disk_area = np.pi * (self.specs["disk_diameter"]/2)**2
        disk_volume = disk_area * self.specs["disk_thickness"]
        
        # 总质量
        sc_mass = (disk_volume * RHO_YBCO * self.specs["disk_count"] * 
                  self.specs["layer_per_disk"] * 0.4)  # 40%填充率
        
        structure_mass = self.specs["disk_count"] * 0.2  # 每个碟片支撑结构
        cryostat_mass = 8  # 12个小型液氮杜瓦
        rf_system_mass = 4  # 分布式RF
        motor_mass = 3  # 多个小型电机
        control_mass = 2  # 控制系统
        
        total_mass = sc_mass + structure_mass + cryostat_mass + rf_system_mass + motor_mass + control_mass
        self.specs["total_mass"] = total_mass
        
        # SVS计算（每个碟片独立工作）
        omega = self.specs["rotation_speed"] * 2 * np.pi / 60
        P_rf = self.specs["rf_power"]
        N = self.specs["layer_per_disk"]
        
        C_SVS = 3.78e-7
        Pc = 1e4
        gamma = 1.5
        
        single_disk_lift = (C_SVS * omega * P_rf / (1 - P_rf/Pc) * 
                           (N ** gamma))
        total_lift = single_disk_lift * self.specs["disk_count"]
        
        lift_force = HUMAN_MASS * G * min(total_lift, 10)
        net_lift = lift_force - total_mass * G
        
        self.analysis = {
            "sc_mass": sc_mass,
            "total_mass": total_mass,
            "lift_ratio": total_lift * 100,
            "lift_force": lift_force,
            "net_lift": net_lift,
            "payload_capacity": HUMAN_MASS - total_mass if net_lift > 0 else 0,
            "feasibility": "高" if net_lift > HUMAN_MASS * G * 0.5 else "中",
        }
        
        return self.analysis
    
    def generate_visualization(self):
        fig, ax = plt.subplots(figsize=(10, 12))
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 14)
        ax.set_aspect('equal')
        ax.axis('off')
        ax.set_title('V2: 分布式碟片阵列', fontsize=14, fontweight='bold')
        
        # 人体轮廓（简化）
        # 头
        head = Circle((5, 12), 0.8, facecolor='peachpuff', edgecolor='black')
        ax.add_patch(head)
        # 躯干
        torso = Rectangle((3.5, 7), 3, 4, facecolor='peachpuff', edgecolor='black')
        ax.add_patch(torso)
        # 手臂
        ax.plot([3.5, 2], [10, 11], 'k-', linewidth=3)
        ax.plot([6.5, 8], [10, 11], 'k-', linewidth=3)
        # 腿
        ax.plot([4.2, 4], [7, 2], 'k-', linewidth=4)
        ax.plot([5.8, 6], [7, 2], 'k-', linewidth=4)
        
        # 碟片位置
        disk_positions = [
            (4, 9), (6, 9), (3.5, 8), (6.5, 8),  # 背部
            (3.5, 7.5), (6.5, 7.5), (3.2, 7), (6.8, 7),  # 腰部
            (4, 4.5), (6, 4.5), (4, 3), (6, 3),  # 大腿
        ]
        
        for i, (x, y) in enumerate(disk_positions):
            color = plt.cm.plasma(i / 12)
            disk = Circle((x, y), 0.4, facecolor=color, edgecolor='darkred', linewidth=2)
            ax.add_patch(disk)
            ax.text(x, y, str(i+1), ha='center', va='center', fontsize=7, color='white', fontweight='bold')
        
        # 图例
        ax.text(5, 0.5, f'12个超导碟片 × {self.specs["layer_per_disk"]}层', 
               ha='center', fontsize=10, 
               bbox=dict(boxstyle='round', facecolor='lightyellow'))
        
        plt.tight_layout()
        plt.savefig('/Users/adminstrator/.qclaw/workspace-agent-10ad9760/research/anti-gravity/phase4-engineering/design_v2_disk_array.png',
                   dpi=150, bbox_inches='tight')
        plt.close()

class DesignV3_ExoskeletonFrame(AntiGravitySuitDesign):
    """
    设计方案V3：外骨骼框架式
    概念：刚性外骨骼支撑大型超导环
    """
    
    def __init__(self):
        super().__init__("V3-外骨骼框架式", "高功率")
        self.specs = {
            "ring_diameter": 0.5,       # 50cm主环
            "ring_count": 3,            # 3个同心环
            "material": "REBCO带材",
            "tape_width": 0.004,        # 4mm带材
            "operating_temp": 20,       # 液氢
            "rotation_speed": 10000,    # 高速旋转
            "rf_power": 8000,           # 高功率
            "power_source": "背包式燃料电池",
        }
        
    def calculate_performance(self):
        # 环参数
        ring_circumference = np.pi * self.specs["ring_diameter"]
        ring_volume = (ring_circumference * self.specs["tape_width"] * 
                      0.0001 * self.specs["ring_count"])  # 100μm厚
        
        sc_mass = ring_volume * RHO_YBCO * 3  # 3个环
        
        frame_mass = 15  # 钛合金外骨骼
        cryostat_mass = 12  # 大型液氢系统
        rf_system_mass = 8  # 高功率RF
        motor_mass = 5  # 高速电机
        power_mass = 10  # 燃料电池+液氢
        control_mass = 3
        
        total_mass = sc_mass + frame_mass + cryostat_mass + rf_system_mass + motor_mass + power_mass + control_mass
        self.specs["total_mass"] = total_mass
        
        # SVS计算
        omega = self.specs["rotation_speed"] * 2 * np.pi / 60
        P_rf = self.specs["rf_power"]
        N = 100  # 等效层数（带材绕制）
        
        C_SVS = 3.78e-7
        Pc = 1.2e4  # REBCO更高淬灭阈值
        gamma = 1.5
        
        lift_ratio = (C_SVS * omega * P_rf / (1 - P_rf/Pc) * (N ** gamma))
        
        lift_force = HUMAN_MASS * G * min(lift_ratio, 15)
        net_lift = lift_force - total_mass * G
        
        self.analysis = {
            "sc_mass": sc_mass,
            "total_mass": total_mass,
            "lift_ratio": lift_ratio * 100,
            "lift_force": lift_force,
            "net_lift": net_lift,
            "payload_capacity": HUMAN_MASS * 2 if net_lift > HUMAN_MASS * G else 0,
            "feasibility": "高" if net_lift > HUMAN_MASS * G else "中",
            "notes": "高功率设计，可搭载额外载荷",
        }
        
        return self.analysis
    
    def generate_visualization(self):
        fig, ax = plt.subplots(figsize=(10, 10))
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.set_aspect('equal')
        ax.axis('off')
        ax.set_title('V3: 外骨骼框架式（高功率版）', fontsize=14, fontweight='bold')
        
        # 外骨骼框架
        frame_outer = Circle((5, 5), 4, facecolor='none', edgecolor='darkblue', linewidth=4)
        ax.add_patch(frame_outer)
        
        # 同心超导环
        for i, r in enumerate([3.5, 3.0, 2.5]):
            color = plt.cm.coolwarm(i/3)
            ring = Circle((5, 5), r, facecolor='none', edgecolor=color, linewidth=8)
            ax.add_patch(ring)
            ax.text(5, 5+r+0.3, f'Ring {i+1}', ha='center', fontsize=9, color=color)
        
        # 中心载人舱
        capsule = Circle((5, 5), 1.5, facecolor='lightyellow', edgecolor='orange', linewidth=3)
        ax.add_patch(capsule)
        ax.text(5, 5, '乘员舱', ha='center', va='center', fontsize=10, fontweight='bold')
        
        # 支撑结构
        for angle in [0, 45, 90, 135, 180, 225, 270, 315]:
            rad = np.radians(angle)
            x1, y1 = 5 + 1.5*np.cos(rad), 5 + 1.5*np.sin(rad)
            x2, y2 = 5 + 4*np.cos(rad), 5 + 4*np.sin(rad)
            ax.plot([x1, x2], [y1, y2], 'k-', linewidth=2)
        
        # 系统标注
        annotations = [
            (8.5, 8.5, '液氢冷却\n20K'),
            (1.5, 8.5, '高功率RF\n8kW/m²'),
            (1.5, 1.5, '燃料电池\n背包'),
            (8.5, 1.5, '高速电机\n10000rpm'),
        ]
        for x, y, text in annotations:
            ax.text(x, y, text, ha='center', va='center', fontsize=9,
                   bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7))
        
        plt.tight_layout()
        plt.savefig('/Users/adminstrator/.qclaw/workspace-agent-10ad9760/research/anti-gravity/phase4-engineering/design_v3_exoskeleton.png',
                   dpi=150, bbox_inches='tight')
        plt.close()

class DesignV4_WearableRing(AntiGravitySuitDesign):
    """
    设计方案V4：可穿戴环形腰带
    概念：腰部环绕式超导环，最轻量化设计
    """
    
    def __init__(self):
        super().__init__("V4-可穿戴环形腰带", "极简")
        self.specs = {
            "ring_diameter": 0.35,      # 35cm（腰围尺寸）
            "ring_cross_section": 0.02, # 2cm×2cm截面
            "material": "Ni基超导",
            "layer_count": 30,
            "operating_temp": 45,       # 液氖或制冷机
            "rotation_speed": 2000,
            "rf_power": 2000,
            "cooling": "斯特林制冷机",
        }
        
    def generate_visualization(self):
        """生成V4概念图"""
        fig, ax = plt.subplots(figsize=(8, 8))
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.set_aspect('equal')
        ax.axis('off')
        ax.set_title('V4: Wearable Ring Belt (Minimal)', fontsize=14, fontweight='bold')
        
        # 人体腰部示意
        waist = Circle((5, 5), 3, facecolor='none', edgecolor='gray', linewidth=2, linestyle='--')
        ax.add_patch(waist)
        
        # 超导环
        ring = Circle((5, 5), 2.5, facecolor='none', edgecolor='purple', linewidth=12)
        ax.add_patch(ring)
        
        # 分层示意
        for i in range(3):
            r = 2.5 - i * 0.3
            circle = Circle((5, 5), r, facecolor='none', 
                          edgecolor=plt.cm.plasma(i/3), linewidth=3)
            ax.add_patch(circle)
        
        # 中心标注
        ax.text(5, 5, 'Ni-based\nSC Ring\n30 layers', ha='center', va='center', 
               fontsize=10, fontweight='bold', color='white')
        
        # 系统标注
        ax.text(5, 1, 'Stirling Cryocooler + RF System', ha='center', fontsize=10,
               bbox=dict(boxstyle='round', facecolor='lightyellow'))
        
        plt.tight_layout()
        plt.savefig('/Users/adminstrator/.qclaw/workspace-agent-10ad9760/research/anti-gravity/phase4-engineering/design_v4_ring_belt.png',
                   dpi=150, bbox_inches='tight')
        plt.close()
        
    def calculate_performance(self):
        # 环参数
        ring_circumference = np.pi * self.specs["ring_diameter"]
        ring_volume = (ring_circumference * self.specs["ring_cross_section"]**2 * 
                      self.specs["layer_count"] * 0.5)
        
        sc_mass = ring_volume * 5000  # Ni基密度较低
        
        structure_mass = 3  # 碳纤维环架
        cryocooler_mass = 8  # 斯特林制冷机
        rf_system_mass = 2  # 低功率RF
        motor_mass = 1.5  # 小型电机
        battery_mass = 5  # 锂电池
        
        total_mass = sc_mass + structure_mass + cryocooler_mass + rf_system_mass + motor_mass + battery_mass
        self.specs["total_mass"] = total_mass
        
        # SVS计算
        omega = self.specs["rotation_speed"] * 2 * np.pi / 60
        P_rf = self.specs["rf_power"]
        N = self.specs["layer_count"]
        
        C_SVS = 3.78e-7
        Pc = 5e3  # Ni基较低淬灭阈值
        gamma = 1.5
        
        if P_rf >= Pc * 0.95:
            lift_ratio = 0
        else:
            lift_ratio = (C_SVS * omega * P_rf / (1 - P_rf/Pc) * (N ** gamma))
        
        lift_force = HUMAN_MASS * G * min(lift_ratio, 5)
        net_lift = lift_force - total_mass * G
        
        self.analysis = {
            "sc_mass": sc_mass,
            "total_mass": total_mass,
            "lift_ratio": lift_ratio * 100,
            "lift_force": lift_force,
            "net_lift": net_lift,
            "payload_capacity": max(0, HUMAN_MASS - total_mass),
            "feasibility": "中" if net_lift > 0 else "低",
            "notes": "极简设计，适合部分减重而非完全悬浮",
        }
        
        return self.analysis

def generate_comparison_table(designs):
    """生成设计方案对比表"""
    fig, ax = plt.subplots(figsize=(14, 8))
    ax.axis('off')
    
    # 表头
    headers = ['方案', '类型', '总质量(kg)', '减重比(%)', '净升力(N)', '载荷(kg)', '可行性']
    
    # 数据
    data = []
    for d in designs:
        data.append([
            d.name,
            d.type,
            f"{d.analysis['total_mass']:.1f}",
            f"{d.analysis['lift_ratio']:.1f}",
            f"{d.analysis['net_lift']:.0f}",
            f"{d.analysis['payload_capacity']:.1f}",
            d.analysis['feasibility']
        ])
    
    # 创建表格
    table = ax.table(cellText=data, colLabels=headers,
                    cellLoc='center', loc='center',
                    colWidths=[0.2, 0.12, 0.1, 0.1, 0.12, 0.1, 0.1])
    
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1, 2)
    
    # 表头样式
    for i in range(len(headers)):
        table[(0, i)].set_facecolor('#4CAF50')
        table[(0, i)].set_text_props(weight='bold', color='white')
    
    # 行样式
    colors = ['#E8F5E9', '#FFF3E0', '#E3F2FD', '#FCE4EC']
    for i, color in enumerate(colors):
        for j in range(len(headers)):
            table[(i+1, j)].set_facecolor(color)
    
    ax.set_title('反重力衣设计方案对比', fontsize=16, fontweight='bold', pad=20)
    
    plt.tight_layout()
    plt.savefig('/Users/adminstrator/.qclaw/workspace-agent-10ad9760/research/anti-gravity/phase4-engineering/design_comparison.png',
               dpi=150, bbox_inches='tight')
    plt.close()

def generate_roadmap():
    """生成制造路线图"""
    fig, ax = plt.subplots(figsize=(14, 10))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 12)
    ax.axis('off')
    ax.set_title('反重力衣制造路线图（预估5-10年）', fontsize=16, fontweight='bold')
    
    # 阶段
    phases = [
        (1, 'Phase 1\n材料研发\n(1-2年)', '#FFCDD2'),
        (3, 'Phase 2\n原型验证\n(2-3年)', '#FFE0B2'),
        (5, 'Phase 3\n系统集成\n(2-3年)', '#FFF9C4'),
        (7, 'Phase 4\n安全测试\n(1-2年)', '#C8E6C9'),
        (9, 'Phase 5\n量产准备\n(1年)', '#BBDEFB'),
    ]
    
    for x, text, color in phases:
        box = FancyBboxPatch((x-0.8, 9), 1.6, 2, boxstyle="round,pad=0.1",
                            facecolor=color, edgecolor='black', linewidth=2)
        ax.add_patch(box)
        ax.text(x, 10, text, ha='center', va='center', fontsize=10, fontweight='bold')
    
    # 里程碑
    milestones = [
        (1, 7, 'BSCCO纤维\n拉丝成功'),
        (2, 5, '单层\nSVS验证'),
        (3, 7, '10层\n堆叠测试'),
        (4, 5, '50层\n原型机'),
        (5, 7, '冷却系统\n集成'),
        (6, 5, 'RF-旋转\n协同优化'),
        (7, 7, '人体\n安全测试'),
        (8, 5, '长时间\n运行验证'),
        (9, 6, '成本优化\n$10万/套'),
    ]
    
    for x, y, text in milestones:
        ax.plot(x, y, 'o', markersize=15, color='red')
        ax.text(x, y-0.8, text, ha='center', va='top', fontsize=8,
               bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
    
    # 连接线
    ax.plot([1, 9], [7, 6], 'k--', alpha=0.3, linewidth=1)
    
    # 关键技术挑战
    challenges = [
        (2, 2, '🔬 材料挑战\nBSCCO柔性纤维\n临界电流密度>1MA/cm²'),
        (5, 2, '⚡ 系统挑战\nRF-旋转同步\n液氢冷却小型化'),
        (8, 2, '🛡️ 安全挑战\n淬灭保护\n辐射屏蔽'),
    ]
    
    for x, y, text in challenges:
        ax.text(x, y, text, ha='center', va='center', fontsize=9,
               bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.9))
    
    plt.tight_layout()
    plt.savefig('/Users/adminstrator/.qclaw/workspace-agent-10ad9760/research/anti-gravity/phase4-engineering/manufacturing_roadmap.png',
               dpi=150, bbox_inches='tight')
    plt.close()

def main():
    """主程序：生成所有设计方案"""
    print("="*60)
    print("反重力衣概念设计生成器 v1.0")
    print("="*60)
    
    # 创建设计方案
    designs = [
        DesignV1_WovenFabric(),
        DesignV2_DiskArray(),
        DesignV3_ExoskeletonFrame(),
        DesignV4_WearableRing(),
    ]
    
    # 计算和可视化
    for d in designs:
        print(f"\n📐 {d.name}")
        print("-" * 40)
        d.calculate_performance()
        d.generate_visualization()
        
        print(f"类型: {d.type}")
        print(f"总质量: {d.analysis['total_mass']:.1f} kg")
        print(f"减重比: {d.analysis['lift_ratio']:.1f}%")
        print(f"净升力: {d.analysis['net_lift']:.0f} N")
        print(f"可搭载: {d.analysis['payload_capacity']:.1f} kg")
        print(f"可行性: {d.analysis['feasibility']}")
        if 'notes' in d.analysis:
            print(f"备注: {d.analysis['notes']}")
    
    # 生成对比表
    generate_comparison_table(designs)
    print("\n✅ 设计方案对比表已生成")
    
    # 生成路线图
    generate_roadmap()
    print("✅ 制造路线图已生成")
    
    print("\n" + "="*60)
    print("设计完成！所有文件已保存至 phase4-engineering/")
    print("="*60)
    
    # 推荐方案
    print("\n🏆 推荐方案:")
    feasible = [d for d in designs if d.analysis['net_lift'] > 0]
    if feasible:
        best = max(feasible, key=lambda x: x.analysis['net_lift'])
        print(f"   {best.name} - 净升力最大 ({best.analysis['net_lift']:.0f}N)")
    
    lightweight = min(designs, key=lambda x: x.analysis['total_mass'])
    print(f"   {lightweight.name} - 最轻量化 ({lightweight.analysis['total_mass']:.1f}kg)")

if __name__ == "__main__":
    main()
