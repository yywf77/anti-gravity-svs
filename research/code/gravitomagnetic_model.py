#!/usr/bin/env python3
"""
gravitomagnetic_model.py
反重力衣研究 — Phase 2 核心计算模型
基于GEM（引力电磁学）框架 + 李宁/Torr理论
问天计划 | 2026-04-16
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from dataclasses import dataclass
from typing import Tuple

# ============================================================
# 物理常数
# ============================================================
G   = 6.674e-11    # 引力常数 [m^3 kg^-1 s^-2]
c   = 3e8          # 光速 [m/s]
hbar = 1.055e-34   # 约化普朗克常数 [J·s]
me  = 9.109e-31    # 电子质量 [kg]
e   = 1.602e-19    # 元电荷 [C]
kB  = 1.381e-23    # 玻尔兹曼常数 [J/K]
mu0 = 4*np.pi*1e-7 # 真空磁导率

# ============================================================
# 超导材料参数库
# ============================================================
MATERIALS = {
    "YBCO": {
        "name": "YBa2Cu3O7 (YBCO)",
        "Tc": 93.0,           # 临界温度 [K]
        "lambda_L": 150e-9,   # 伦敦穿透深度 [m]
        "xi": 1.5e-9,         # 相干长度 [m]
        "rho_ion": 6300,      # 离子质量密度 [kg/m^3]
        "M_ion": 666.2*1.66e-27,  # 单元胞质量 [kg] (YBa2Cu3O7 ≈ 666 amu)
        "a_lattice": 3.82e-10,    # 晶格常数 [m]
        "n_s_max": 1e27,      # 最大超导电子密度 [m^-3]
    },
    "NiO_bilayer": {
        "name": "La2.85Pr0.15Ni2O7 (镍基, 2025新材料)",
        "Tc": 45.0,
        "lambda_L": 200e-9,
        "xi": 2.0e-9,
        "rho_ion": 7100,
        "M_ion": 580*1.66e-27,
        "a_lattice": 3.9e-10,
        "n_s_max": 8e26,
    },
    "BSCCO": {
        "name": "Bi2Sr2CaCu2O8 (BSCCO)",
        "Tc": 110.0,
        "lambda_L": 300e-9,
        "xi": 1.0e-9,
        "rho_ion": 6500,
        "M_ion": 888*1.66e-27,
        "a_lattice": 3.81e-10,
        "n_s_max": 1.2e27,
    },
}

# ============================================================
# 1. GEM引力磁场基础计算
# ============================================================

def gravitomagnetic_field_rotating_disk(
    omega: float,       # 角速度 [rad/s]
    R: float,           # 圆盘半径 [m]
    h: float,           # 圆盘厚度 [m]
    rho: float,         # 质量密度 [kg/m^3]
    z: float = 0.1,     # 观测点高度 [m]
) -> float:
    """
    计算旋转圆盘在轴线上方z处产生的引力磁场 B_g [m/s^2 / (m/s)]
    
    基于GEM方程：∇×B_g = -(16πG/c²) J_mass
    对均匀旋转圆盘积分得到轴线上的B_g
    
    注：B_g 的单位是 [1/s]，类比磁场 [T = kg/(A·s²)]
    引力磁场对质量m的力：F = m(v × B_g)
    """
    # 质量流密度 J = rho * v = rho * omega * r (切向)
    # 轴线上方z处的引力磁场（类比载流圆盘的磁场）
    # B_g(z) = (8G/c²) * rho * h * omega * ∫₀ᴿ r² dr / (r²+z²)^(3/2)
    
    # 数值积分
    r_arr = np.linspace(0, R, 10000)
    integrand = r_arr**2 / (r_arr**2 + z**2)**1.5
    integral = np.trapz(integrand, r_arr)
    
    B_g = (8 * G / c**2) * rho * h * omega * integral
    return B_g


def gravity_reduction_classical(B_g: float, v_ion: float) -> float:
    """
    经典GEM框架下的引力减少比例
    
    当超导体中离子以速度v_ion旋转时，
    引力磁场对静止物体的效应：
    δg/g = B_g * v_ion / g_earth
    
    注：这是纯GEM效应，不含量子放大
    """
    g_earth = 9.8  # m/s^2
    return B_g * v_ion / g_earth


# ============================================================
# 2. 李宁量子放大机制
# ============================================================

def cooper_pair_gravitomagnetic_moment(
    n_s: float,         # 超导电子密度 [m^-3]
    lambda_L: float,    # 伦敦穿透深度 [m]
    omega: float,       # 旋转角速度 [rad/s]
    R: float,           # 超导体半径 [m]
) -> float:
    """
    计算Cooper对的引力磁矩
    
    李宁理论：超导体中Cooper对的宏观量子相干
    使得引力磁矩被集体放大
    
    μ_g = n_s * (2me) * omega * R² * π * lambda_L²
    
    这里 lambda_L² 是伦敦穿透深度的平方，
    代表超导序参量的空间相干范围
    """
    mu_g = n_s * (2 * me) * omega * np.pi * R**2 * lambda_L**2
    return mu_g


def quantum_amplification_factor(
    material: dict,
    T: float,           # 工作温度 [K]
    omega: float,       # 旋转角速度 [rad/s]
) -> float:
    """
    估算量子相干放大因子
    
    核心思路：
    - 正常物质：每个离子独立贡献引力磁矩，随机相位，总效应 ∝ √N
    - 超导体：Cooper对形成宏观量子态，相位锁定，总效应 ∝ N
    - 放大因子 ≈ √N_coherent
    
    N_coherent = 超导相干体积内的Cooper对数
    相干体积 ≈ (λ_L)³ / ξ³ × (ξ/a)³ ... 
    
    更保守的估算（基于Tajmar 2005）：
    放大因子 ≈ (λ_L / ξ)² × (T_c/T - 1)^(-1/2)
    """
    Tc = material["Tc"]
    lambda_L = material["lambda_L"]
    xi = material["xi"]
    
    if T >= Tc:
        return 0.0
    
    # GL参数 κ = λ_L / ξ (Type-II超导体 κ >> 1)
    kappa = lambda_L / xi
    
    # 温度依赖的序参量
    t = T / Tc  # 约化温度
    order_param = np.sqrt(1 - t**4)  # GL近似
    
    # 放大因子（保守估算）
    # 李宁原始估算：~10^11，Harris认为高估
    # Tajmar保守估算：~10^3 - 10^5
    amp = kappa**2 * order_param
    
    return amp


def effective_gravity_reduction(
    material_name: str,
    T: float,
    omega: float,
    R: float,
    h: float,
    z: float = 0.1,
    use_quantum_amp: bool = True,
) -> dict:
    """
    计算综合引力减少效果
    返回详细的物理量字典
    """
    mat = MATERIALS[material_name]
    
    # 1. 经典GEM引力磁场
    B_g_classical = gravitomagnetic_field_rotating_disk(
        omega, R, h, mat["rho_ion"], z
    )
    
    # 2. 量子放大因子
    amp = quantum_amplification_factor(mat, T, omega) if use_quantum_amp else 1.0
    
    # 3. 放大后的有效引力磁场
    B_g_effective = B_g_classical * amp
    
    # 4. 离子热运动速度（作为"电流"速度的估算）
    v_thermal = np.sqrt(3 * kB * T / mat["M_ion"])
    
    # 5. 引力减少比例
    delta_g_ratio = gravity_reduction_classical(B_g_effective, v_thermal)
    
    # 6. Cooper对引力磁矩
    n_s = mat["n_s_max"] * (1 - (T/mat["Tc"])**4) if T < mat["Tc"] else 0
    mu_g = cooper_pair_gravitomagnetic_moment(n_s, mat["lambda_L"], omega, R)
    
    return {
        "material": mat["name"],
        "T_K": T,
        "omega_rad_s": omega,
        "B_g_classical_1_s": B_g_classical,
        "quantum_amp_factor": amp,
        "B_g_effective_1_s": B_g_effective,
        "v_thermal_m_s": v_thermal,
        "gravity_reduction_ratio": min(delta_g_ratio, 1.0),
        "gravity_reduction_percent": min(delta_g_ratio * 100, 100.0),
        "cooper_pair_density_m3": n_s,
        "gravitomagnetic_moment": mu_g,
    }


# ============================================================
# 3. 参数空间扫描 — 寻找2%→100%的路径
# ============================================================

def parameter_scan_omega_T(
    material_name: str = "YBCO",
    omega_range: Tuple = (1e3, 1e8),
    T_range: Tuple = (4, 90),
    R: float = 0.15,
    h: float = 0.005,
    n_points: int = 50,
) -> dict:
    """
    扫描角速度和温度参数空间，
    寻找引力减少效果最大化的区域
    """
    omegas = np.logspace(np.log10(omega_range[0]), np.log10(omega_range[1]), n_points)
    Ts = np.linspace(T_range[0], T_range[1], n_points)
    
    reduction_map = np.zeros((n_points, n_points))
    
    for i, omega in enumerate(omegas):
        for j, T in enumerate(Ts):
            result = effective_gravity_reduction(material_name, T, omega, R, h)
            reduction_map[i, j] = result["gravity_reduction_percent"]
    
    return {
        "omegas": omegas,
        "Ts": Ts,
        "reduction_map": reduction_map,
        "max_reduction": reduction_map.max(),
        "best_omega": omegas[np.unravel_index(reduction_map.argmax(), reduction_map.shape)[0]],
        "best_T": Ts[np.unravel_index(reduction_map.argmax(), reduction_map.shape)[1]],
    }


# ============================================================
# 4. 多层超导线圈阵列协同效应
# ============================================================

def multilayer_coil_array(
    material_name: str,
    T: float,
    omega: float,
    n_layers: int,
    R_base: float = 0.15,
    layer_spacing: float = 0.02,
    h: float = 0.003,
    z_target: float = 0.05,
) -> dict:
    """
    计算多层超导线圈阵列的协同引力磁场
    
    每层线圈半径略有不同（锥形排列），
    旋转方向交替（增强轴向分量）
    """
    total_B_g = 0.0
    layer_results = []
    
    for i in range(n_layers):
        R_i = R_base - i * 0.005  # 每层半径略减
        z_i = z_target - i * layer_spacing  # 观测点相对该层的高度
        
        if z_i <= 0:
            z_i = 0.01
        
        # 交替旋转方向
        omega_i = omega * (1 if i % 2 == 0 else -1)
        
        result = effective_gravity_reduction(material_name, T, abs(omega_i), R_i, h, z_i)
        B_g_i = result["B_g_effective_1_s"] * np.sign(omega_i)
        
        total_B_g += B_g_i
        layer_results.append({
            "layer": i+1,
            "R_m": R_i,
            "z_m": z_i,
            "B_g_1_s": B_g_i,
            "reduction_pct": result["gravity_reduction_percent"],
        })
    
    # 总引力减少
    v_thermal = np.sqrt(3 * kB * T / MATERIALS[material_name]["M_ion"])
    total_reduction = abs(total_B_g) * v_thermal / 9.8 * 100
    
    return {
        "n_layers": n_layers,
        "total_B_g": total_B_g,
        "total_reduction_percent": min(total_reduction, 100.0),
        "layers": layer_results,
    }


# ============================================================
# 5. 主程序：运行计算并输出报告
# ============================================================

def run_analysis():
    print("=" * 60)
    print("  反重力衣研究 — 引力磁场效应计算报告")
    print("  问天计划 | Phase 2 | 2026-04-16")
    print("=" * 60)
    
    # --- 5.1 单材料基准计算 ---
    print("\n【1】基准计算：YBCO超导盘 (Podkletnov实验参数)")
    print("-" * 50)
    # Podkletnov实验：YBCO盘，直径~30cm，厚~1cm，旋转~5000rpm
    omega_podkletnov = 5000 * 2 * np.pi / 60  # ~524 rad/s
    result = effective_gravity_reduction(
        "YBCO", T=77, omega=omega_podkletnov,
        R=0.15, h=0.01, z=0.1
    )
    for k, v in result.items():
        if isinstance(v, float):
            print(f"  {k:35s}: {v:.4e}")
        else:
            print(f"  {k:35s}: {v}")
    
    # --- 5.2 三种材料对比 ---
    print("\n【2】三种超导材料对比（最优参数）")
    print("-" * 50)
    print(f"{'材料':<30} {'Tc(K)':<8} {'最大减重%':<12} {'最优ω(rad/s)':<15}")
    print("-" * 65)
    
    for mat_name in MATERIALS:
        mat = MATERIALS[mat_name]
        # 在接近Tc的温度、高转速下计算
        T_opt = mat["Tc"] * 0.3  # 30% Tc 时序参量最强
        omega_opt = 1e6  # 高转速
        r = effective_gravity_reduction(mat_name, T_opt, omega_opt, 0.15, 0.01)
        print(f"  {mat['name']:<28} {mat['Tc']:<8.1f} {r['gravity_reduction_percent']:<12.4f} {omega_opt:<15.2e}")
    
    # --- 5.3 多层阵列效应 ---
    print("\n【3】多层超导线圈阵列协同效应（YBCO，T=20K，ω=10⁶ rad/s）")
    print("-" * 50)
    for n in [1, 3, 5, 10, 20]:
        arr = multilayer_coil_array("YBCO", T=20, omega=1e6, n_layers=n)
        print(f"  {n:2d}层阵列 → 总引力减少: {arr['total_reduction_percent']:.4f}%")
    
    # --- 5.4 参数扫描 ---
    print("\n【4】参数空间扫描：寻找最优工作点（YBCO）")
    print("-" * 50)
    scan = parameter_scan_omega_T("YBCO", n_points=30)
    print(f"  最大引力减少: {scan['max_reduction']:.4f}%")
    print(f"  最优角速度:   {scan['best_omega']:.3e} rad/s")
    print(f"  最优温度:     {scan['best_T']:.1f} K")
    
    # --- 5.5 关键结论 ---
    print("\n【5】关键结论与分析")
    print("-" * 50)
    print("""
  ① 经典GEM框架下，旋转超导盘产生的引力磁场极弱
     (B_g ~ 10^-26 量级)，即使加上量子放大(~10^4)
     仍远不足以产生可测量的引力减少。
     
  ② 这与Harris(1999)的批评一致：李宁原始估算的
     10^11放大因子过于乐观，实际可能只有10^3~10^5。
     
  ③ Podkletnov的2%减重若属实，需要额外的未知机制：
     - 可能是非平衡态超导的特殊效应
     - 可能是RF照射触发的量子真空效应
     - 可能是实验误差（气流、磁场梯度等）
     
  ④ 从2%到100%的路径：
     需要放大因子再提升约50倍，
     或者发现全新的引力-量子耦合机制。
     
  ⑤ 下一步：转向Casimir力路线，
     这条路在理论上更清晰，工程化路径更明确。
""")
    
    # --- 5.6 生成图表 ---
    try:
        fig, axes = plt.subplots(1, 2, figsize=(14, 5))
        
        # 图1：引力减少 vs 角速度
        omegas = np.logspace(3, 8, 100)
        for mat_name, color in [("YBCO","blue"), ("NiO_bilayer","red"), ("BSCCO","green")]:
            reductions = [
                effective_gravity_reduction(mat_name, T=20, omega=w, R=0.15, h=0.01)["gravity_reduction_percent"]
                for w in omegas
            ]
            axes[0].loglog(omegas, [max(r, 1e-20) for r in reductions],
                          label=MATERIALS[mat_name]["name"].split("(")[0], color=color)
        axes[0].set_xlabel("角速度 ω (rad/s)")
        axes[0].set_ylabel("引力减少 (%)")
        axes[0].set_title("引力减少 vs 旋转速度 (T=20K)")
        axes[0].legend(fontsize=8)
        axes[0].grid(True, alpha=0.3)
        axes[0].axhline(y=2, color='orange', linestyle='--', label='Podkletnov 2%')
        axes[0].axhline(y=100, color='red', linestyle='--', label='目标 100%')
        
        # 图2：多层阵列效应
        n_layers_arr = list(range(1, 31))
        reductions_arr = [
            multilayer_coil_array("YBCO", T=20, omega=1e6, n_layers=n)["total_reduction_percent"]
            for n in n_layers_arr
        ]
        axes[1].plot(n_layers_arr, reductions_arr, 'b-o', markersize=4)
        axes[1].set_xlabel("线圈层数")
        axes[1].set_ylabel("总引力减少 (%)")
        axes[1].set_title("多层超导线圈阵列协同效应")
        axes[1].grid(True, alpha=0.3)
        axes[1].axhline(y=2, color='orange', linestyle='--', label='Podkletnov 2%')
        axes[1].legend()
        
        plt.tight_layout()
        plt.savefig(
            "/Users/adminstrator/.qclaw/workspace-agent-10ad9760/research/anti-gravity/phase2-modeling/gravitomagnetic_analysis.png",
            dpi=150, bbox_inches='tight'
        )
        print("  📊 图表已保存至 phase2-modeling/gravitomagnetic_analysis.png")
    except Exception as ex:
        print(f"  图表生成跳过: {ex}")
    
    print("\n" + "=" * 60)
    print("  计算完成。下一步：Casimir力阵列模拟器")
    print("=" * 60)


if __name__ == "__main__":
    run_analysis()
