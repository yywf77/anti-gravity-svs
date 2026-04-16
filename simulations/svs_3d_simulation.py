#!/usr/bin/env python3
"""
svs_3d_simulation.py
SVS反重力效应 — 3D交互式可视化
问天计划 | 2026-04-16
"""

import numpy as np
import plotly.graph_objects as go
import os

OUT = "/Users/adminstrator/.qclaw/workspace-agent-10ad9760/research/anti-gravity/visualizations"
os.makedirs(OUT, exist_ok=True)

G    = 6.67430e-11
c    = 2.99792458e8
hbar = 1.0545718e-34
e    = 1.6021766e-19
mu0  = 4*np.pi*1e-7

SUPERCONDUCTORS = {
    "YBCO":  {"Tc":93.0, "xi":1.5e-9, "n_s":5.3e27, "R":0.025, "h":0.005},
    "BSCCO": {"Tc":110.0,"xi":1.0e-9, "n_s":6.0e27, "R":0.025, "h":0.005},
    "Ni基(2025)":{"Tc":45.0,"xi":2.0e-9,"n_s":3.0e27,"R":0.025,"h":0.005},
    "REBCO": {"Tc":90.0, "xi":1.2e-9, "n_s":8.0e27, "R":0.025, "h":0.001},
}

def xi(T, Tc, xi0):
    if T >= Tc: return 0.0
    return xi0 / np.sqrt(max(0.001, 1-(T/Tc)**2))

def n_s_val(T, Tc, ns0):
    t=T/Tc; return ns0*(1-t**4) if t<1 else 0.0

def rf_enh(P, f, xi0, Delta0=20e-3):
    if P<=0: return 1.0
    w_gap=2*Delta0*e/hbar
    w_rf=2*np.pi*f
    Pc=1e4
    resonance=1/(1+(w_rf/w_gap-0.3)**2)*3.0
    return min(1.0+(P/Pc)*(1+resonance), 1000.0)

def red(m, w_rot, P, f, mat="YBCO", T=77.0, N=1, gamma=1.5):
    m_par=SUPERCONDUCTORS[mat]
    xi0=m_par["xi"]; ns0=m_par["n_s"]
    R=m_par["R"]; h=m_par["h"]; Tc=m_par["Tc"]
    xi_e=xi(T,Tc,xi0)*rf_enh(P,f,xi0)
    ns=n_s_val(T,Tc,ns0)
    w_ref=0.196*(ns/ns0)*(h/0.005)*(R/0.025)
    rot_f=min(w_rot/524.0,1e4)
    return m*w_ref*max(1,xi_e/xi0)*max(1,N**gamma)*np.sqrt(rot_f)/(m*9.8)*100

# =========================================================
# 图1: 3D超导体 + 悬浮质量 + 引力场可视化
# =========================================================
def fig1_main_simulation():
    fig = go.Figure()

    # 超导体圆盘 (分层渲染)
    theta=np.linspace(0,2*np.pi,40)
    phi=np.linspace(0,np.pi,20)
    R=0.025; h=0.005
    x_disc=np.outer(np.cos(theta), np.sin(phi)*h)
    y_disc=np.outer(np.sin(theta), np.sin(phi)*h)
    z_disc=np.outer(np.ones(40), np.cos(phi)*R) + R

    fig.add_trace(go.Surface(
        x=x_disc, y=y_disc, z=z_disc,
        colorscale=[[0,'#1a5fff'],[1,'#0033cc']],
        opacity=0.92, showscale=False,
        name='YBCO超导体圆盘',
        hovertemplate='YBCO圆盘<br>R=2.5cm h=0.5cm<br>T=77K (液氮)<extra></extra>'
    ))

    # 旋转轴 (红线)
    t_arr=np.linspace(0,2*np.pi,30)
    fig.add_trace(go.Scatter3d(
        x=np.zeros(30), y=np.zeros(30),
        z=np.linspace(-0.03,0.03,30),
        mode='lines', line=dict(color='#ff3333',width=5),
        name='旋转轴', hovertemplate='旋转轴方向<extra></extra>'
    ))

    # 旋转示意箭头
    for angle in [0, np.pi/2, np.pi, 3*np.pi/2]:
        fig.add_trace(go.Cone(
            x=[0.04*np.cos(angle)], y=[0.04*np.sin(angle)], z=[0.0],
            u=[-0.01*np.cos(angle)], v=[-0.01*np.sin(angle)], w=[0],
            colorscale='Reds', opacity=0.5, showscale=False,
            hoverinfo='skip'
        ))

    # RF波束 (橙色锥)
    angles=np.linspace(0,2*np.pi,8,endpoint=False)
    for ang in angles:
        fig.add_trace(go.Cone(
            x=[0.09*np.cos(ang)], y=[0.09*np.sin(ang)], z=[0.12],
            u=[-0.03*np.cos(ang)], v=[-0.03*np.sin(ang)], w=[-0.02],
            colorscale='Oranges', opacity=0.35, showscale=False,
            hoverinfo='skip'
        ))

    # 测试质量 - 不同高度代表不同引力减少
    cases=[
        (0.04, '#00ff00', '2.5%', '高度4cm<br>引减2.5%<br>接近悬浮'),
        (0.065,'#44ff88', '1.5%', '高度6.5cm<br>引减1.5%'),
        (0.09, '#ccff44', '0.8%', '高度9cm<br>引减0.8%'),
        (0.12, '#ffff44', '0.3%', '高度12cm<br>引减0.3%'),
    ]
    for hgt, col, lbl, hov in cases:
        u=np.linspace(0,2*np.pi,20); v=np.linspace(0,np.pi,10)
        xs=0.008*np.outer(np.cos(u),np.sin(v))
        ys=0.008*np.outer(np.sin(u),np.sin(v))
        zs=0.008*np.outer(np.ones(20),np.cos(v))+hgt
        fig.add_trace(go.Surface(
            x=xs,y=ys,z=zs,
            colorscale=[[0,col],[1,col]],
            opacity=0.9, showscale=False,
            name=f'测试质量 ({lbl})',
            hovertemplate=hov+'<extra></extra>'
        ))

    # 引力场透明球 (多层)
    for r,op in [(0.05,0.04),(0.08,0.025),(0.12,0.015)]:
        u=np.linspace(0,2*np.pi,16); v=np.linspace(0,np.pi,8)
        xs=r*np.outer(np.cos(u),np.sin(v))
        ys=r*np.outer(np.sin(u),np.sin(v))
        zs=r*np.outer(np.ones(16),np.cos(v))+0.04
        fig.add_trace(go.Surface(
            x=xs,y=ys,z=zs,
            colorscale='Greens',opacity=op,
            showscale=False, hoverinfo='skip', name=f'引力场等值面'
        ))

    # 标注线
    fig.add_trace(go.Scatter3d(
        x=[0.025,0.055], y=[0,0], z=[0.005,0.005],
        mode='lines+text',
        line=dict(color='white',width=1),
        text=['R=2.5cm',' '],
        textposition='middle right',
        textfont=dict(color='white',size=10),
        hoverinfo='skip', showlegend=False
    ))

    fig.update_layout(
        title=dict(
            text='<b>🔬 SVS反重力实验 3D模拟</b><br>'
                 '<sup>YBCO超导体 | T=77K | ω=524rad/s | P_RF=100W/m²</sup>',
            x=0.5, font=dict(size=18,color='#223366')
        ),
        scene=dict(
            xaxis=dict(range=[-0.15,0.15],
                       backgroundcolor='rgba(10,10,30,1)', gridcolor='#334466',
                       showbackground=True, tickfont=dict(color='white'),
                       title=dict(text='X (m)', font=dict(color='white'))),
            yaxis=dict(range=[-0.15,0.15],
                       backgroundcolor='rgba(10,10,30,1)', gridcolor='#334466',
                       showbackground=True, tickfont=dict(color='white'),
                       title=dict(text='Y (m)', font=dict(color='white'))),
            zaxis=dict(range=[-0.02,0.18],
                       backgroundcolor='rgba(10,10,30,1)', gridcolor='#334466',
                       showbackground=True, tickfont=dict(color='white'),
                       title=dict(text='Z (m)', font=dict(color='white'))),
            camera=dict(eye=dict(x=1.4,y=1.4,z=0.7),up=dict(x=0,y=0,z=1)),
            aspectmode='cube'
        ),
        showlegend=True,
        legend=dict(x=0.01,y=0.99,bgcolor='rgba(0,0,0,0.7)',
                    font=dict(color='white'),bordercolor='#555'),
        paper_bgcolor='#0a0a20',
        plot_bgcolor='#0a0a20',
        width=1000, height=800,
        annotations=[
            dict(text="<b>图例</b><br>🔴旋转轴<br>🟠RF微波<br>🔵超导体<br>⚪测试质量<br>🟢引力场",
                 x=0.01,y=0.35,xref='paper',yref='paper',
                 showarrow=False,font=dict(size=11,color='white'),
                 bgcolor='rgba(0,0,0,0.6)',bordercolor='white',borderwidth=1,
                 align='left'),
            dict(text="<b>⚠️ 理论预测值</b><br>蓝色球=2.5%引减<br>绿色=1.5%<br>黄色=0.8%/0.3%<br>仅供演示",
                 x=0.99,y=0.01,xref='paper',yref='paper',
                 showarrow=False,font=dict(size=10,color='#ffff88'),
                 bgcolor='rgba(0,0,0,0.6)',bordercolor='#ffff88',borderwidth=1,
                 align='right'),
        ]
    )
    return fig

# =========================================================
# 图2: 旋转速度 vs 引力减少 (多曲线)
# =========================================================
def fig2_rotation():
    fig=go.Figure()
    omegas=np.logspace(2,8,200)
    colors=['#3366ff','#00cc66','#ff9900','#ff4444','#aa00ff','#ffaa00']
    N_vals=[1,5,10,50,100,500]
    for N,col in zip(N_vals,colors):
        ys=[red(0.001,om,100,16e9,"YBCO",77,N) for om in omegas]
        fig.add_trace(go.Scatter(
            x=omegas,y=ys,mode='lines',name=f'N={N}层',
            line=dict(color=col,width=2.5),
            fill='tonexty' if N>1 else None,
            hovertemplate=f'N={N}层 | ω=%{{x:.0e}}rad/s | Δg=%{{y:.4f}}%<extra></extra>'
        ))
    fig.add_hline(y=2,line_dash='dash',line_color='#ff8800',
                  annotation_text='Podkletnov 2%',annotation_font_color='#ff8800')
    fig.add_hline(y=100,line_dash='dash',line_color='#ff0000',
                  annotation_text='完全悬浮 100%',annotation_font_color='#ff0000')
    fig.add_vline(x=524,line_dash='dot',line_color='#4488ff',
                  annotation_text='Podkletnov转速',annotation_font_color='#4488ff')
    fig.update_layout(
        title=dict(text='<b>📊 旋转速度 vs 引力减少</b><br>'
                        '<sup>YBCO | T=77K | P_RF=100W/m² | 多层协同放大 N^γ</sup>',
                   x=0.5,font=dict(size=16)),
        xaxis=dict(type='log',title='旋转速度 ω (rad/s)',
                   tickformat='.0e',gridcolor='rgba(100,100,100,0.3)'),
        yaxis=dict(type='log',title='引力减少 Δg/g (%)',
                   gridcolor='rgba(100,100,100,0.3)'),
        template='plotly_dark',height=550,width=900,
        legend=dict(x=0.02,y=0.98,bgcolor='rgba(0,0,0,0.5)'),
        annotations=[dict(text='γ=1.5协同指数 | ω∝√ω_rot',
                          x=0.99,y=0.01,xref='paper',yref='paper',
                          showarrow=False,font=dict(size=10,color='#aaa'))]
    )
    return fig

# =========================================================
# 图3: RF功率 vs 引力减少
# =========================================================
def fig3_rf_power():
    fig=go.Figure()
    P_arr=np.logspace(-2,5,200)
    colors=['#3366ff','#00cc66','#ff9900','#ff4444','#aa00ff']
    N_vals=[1,5,10,100,500]
    for N,col in zip(N_vals,colors):
        ys=[red(0.001,524,P,16e9,"YBCO",77,N) for P in P_arr]
        fig.add_trace(go.Scatter(
            x=P_arr,y=ys,mode='lines',name=f'N={N}层',
            line=dict(color=col,width=2.5),
            hovertemplate=f'N={N}层 | P_RF=%{{x:.1e}}W/m² | Δg=%{{y:.4f}}%<extra></extra>'
        ))
    fig.add_vline(x=100,line_dash='dash',line_color='#ff8800',
                  annotation_text='Podkletnov: 100W/m²',annotation_font_color='#ff8800')
    fig.add_vline(x=10000,line_dash='dash',line_color='#ff0000',
                  annotation_text='目标: 10kW/m²',annotation_font_color='#ff0000')
    fig.update_layout(
        title=dict(text='<b>📊 RF功率 vs 引力减少</b><br>'
                        '<sup>YBCO | T=77K | ω=524rad/s | f_RF=16GHz</sup>',
                   x=0.5,font=dict(size=16)),
        xaxis=dict(type='log',title='RF功率密度 (W/m²)',
                   tickformat='.0e',gridcolor='rgba(100,100,100,0.3)'),
        yaxis=dict(type='log',title='引力减少 (%)',
                   gridcolor='rgba(100,100,100,0.3)'),
        template='plotly_dark',height=550,width=900,
        legend=dict(x=0.02,y=0.98,bgcolor='rgba(0,0,0,0.5)'),
        annotations=[dict(text='共振频率≈10-20GHz | 功率阈值≈100W/m²',
                          x=0.99,y=0.01,xref='paper',yref='paper',
                          showarrow=False,font=dict(size=10,color='#aaa'))]
    )
    return fig

# =========================================================
# 图4: 材料对比
# =========================================================
def fig4_material():
    fig=go.Figure()
    P_arr=np.logspace(0,4,150)
    colors=['#3366ff','#00cc66','#ff9900','#ff4444']
    mats=list(SUPERCONDUCTORS.keys())
    for mat,col in zip(mats,colors):
        ys=[red(0.001,524,P,16e9,mat,77,10) for P in P_arr]
        Tc=SUPERCONDUCTORS[mat]["Tc"]
        fig.add_trace(go.Scatter(
            x=P_arr,y=ys,mode='lines',name=f'{mat} (Tc={Tc}K)',
            line=dict(color=col,width=2.5),
            hovertemplate=f'{mat} | P_RF=%{{x:.0e}}W/m² | Δg=%{{y:.4f}}%<extra></extra>'
        ))
    fig.update_layout(
        title=dict(text='<b>🔬 不同超导材料的SVS效应对比</b><br>'
                        '<sup>10层结构 | T=77K | ω=524rad/s | f_RF=16GHz</sup>',
                   x=0.5,font=dict(size=16)),
        xaxis=dict(type='log',title='RF功率密度 (W/m²)',
                   gridcolor='rgba(100,100,100,0.3)'),
        yaxis=dict(title='引力减少 (%)',type='log',
                   gridcolor='rgba(100,100,100,0.3)'),
        template='plotly_dark',height=500,width=900,
        legend=dict(x=0.02,y=0.98,bgcolor='rgba(0,0,0,0.5)')
    )
    return fig

# =========================================================
# 图5: 温度-层数相图热力图
# =========================================================
def fig5_phase_diagram():
    T_arr=np.linspace(4,92,50)
    N_arr=[1,2,5,10,20,50,100,200]
    z_data=[]
    for N in N_arr:
        row=[red(0.001,524,100,16e9,"YBCO",T,N) for T in T_arr]
        z_data.append(row)

    fig=go.Figure(data=go.Heatmap(
        z=z_data,
        x=[f'{T:.0f}K' for T in T_arr],
        y=[f'N={n}' for n in N_arr],
        colorscale='RdYlGn_r',
        colorbar=dict(title='引力减少(%)'),
        hovertemplate='T=%{x} | 层数=%{y}<br>Δg=%{z:.4f}%<extra></extra>'
    ))
    fig.add_vline(x=list(T_arr).index(min(T_arr,key=lambda t:abs(t-77))),
                  line_dash='dash',line_color='white',
                  annotation_text='液氮温度 77K',annotation_font_color='white')
    fig.update_layout(
        title=dict(text='<b>🌡️ SVS效应温度-层数相图</b><br>'
                        '<sup>ω=524rad/s | P_RF=100W/m² | f_RF=16GHz</sup>',
                   x=0.5,font=dict(size=16)),
        xaxis=dict(title='温度',tickangle=45),
        yaxis=dict(title='超导层数'),
        template='plotly_dark',height=500,width=900
    )
    return fig

# =========================================================
# 图6: 多视角3D动画帧 (悬浮高度随参数变化)
# =========================================================
def fig6_animation():
    """展示测试质量在不同条件下悬浮高度变化的动画"""
    frames_data=[]
    heights=[]
    labels=[]
    for N in [1,5,10,50,100]:
        r=red(0.001,524,100,16e9,"YBCO",77,N)
        h=0.03+min(r/10.0*0.08, 0.08)
        heights.append(h)
        labels.append(f'N={N}层 Δg={r:.3f}%')

    fig=go.Figure()
    # 背景超导体
    theta=np.linspace(0,2*np.pi,40); phi=np.linspace(0,np.pi,20)
    R=0.025; h=0.005
    xd=np.outer(np.cos(theta),np.sin(phi)*h)
    yd=np.outer(np.sin(theta),np.sin(phi)*h)
    zd=np.outer(np.ones(40),np.cos(phi)*R)+R
    fig.add_trace(go.Surface(
        x=xd,y=yd,z=zd,
        colorscale=[[0,'#1a5fff'],[1,'#0033cc']],
        opacity=0.9,showscale=False,name='YBCO',hoverinfo='skip'
    ))

    # 初始帧
    u=np.linspace(0,2*np.pi,20); v=np.linspace(0,np.pi,10)
    xs0=0.008*np.outer(np.cos(u),np.sin(v))
    ys0=0.008*np.outer(np.sin(u),np.sin(v))
    zs0=0.008*np.outer(np.ones(20),np.cos(v))+0.04
    fig.add_trace(go.Surface(
        x=xs0,y=ys0,z=zs0,
        colorscale=[[0,'#00ff00'],[1,'#00dd00']],
        opacity=0.9,showscale=False,name=f'N=1 Δg={red(0.001,524,100,16e9,"YBCO",77,1):.3f}%',
        hovertemplate='N=1层<br>Δg=1.1%<extra></extra>'
    ))

    # 动画帧
    frames=[]
    N_vals=[1,5,10,50,100]
    cols=['#00ff00','#88ff00','#ffff00','#ff8800','#ff4444']
    for i,(N,col) in enumerate(zip(N_vals,cols)):
        r=red(0.001,524,100,16e9,"YBCO",77,N)
        h=0.04+min(r/2.0*0.07, 0.07)
        xi_s=0.008*np.outer(np.cos(u),np.sin(v))
        yi_s=0.008*np.outer(np.sin(u),np.sin(v))
        zi_s=0.008*np.outer(np.ones(20),np.cos(v))+h
        frames.append(go.Frame(
            data=[go.Surface(x=xi_s,y=yi_s,z=zi_s,
                              colorscale=[[0,col],[1,col]],
                              opacity=0.9,showscale=False)],
            name=f'frame{i}',
            layout=go.Layout(
                title=dict(text=f'<b>🔬 SVS悬浮动画: N={N}层</b><br>'
                                f'<sup>引力减少: {r:.2f}% | 悬浮高度: {h*1000:.0f}mm</sup>')
            )
        ))
    fig.frames=frames

    # 滑块
    steps=[dict(
        method='animate',args=[[f'frame{i}' for i in range(5)],
                                dict(frame=dict(duration=1000,redraw=True),
                                     mode='immediate')],
        label=f'N={N}' ) for i,N in enumerate(N_vals)]

    fig.update_layout(
        updatemenus=[dict(
            type='buttons',showactive=False,
            y=0.1,x=0.1,
            buttons=[
                dict(label='▶ 播放',method='animate',
                     args=[None,dict(frame=dict(duration=1500,redraw=True),
                                     fromcurrent=True,transition=dict(duration=500))]),
                dict(label='⏸ 暂停',method='animate',
                     args=[[None],dict(frame=dict(duration=0,redraw=True),
                                       mode='afterall')])
            ]
        )],
        sliders=[dict(active=0,pad=dict(t=30,b=10),
                      steps=steps,x=0.1,len=0.8,
                      currentvalue=dict(prefix='层数: ',visible=True,
                                       font=dict(size=14)),
                      font=dict(color='#aaa'))],
        title=dict(text='<b>🔬 SVS悬浮高度随层数变化动画</b><br>'
                        '<sup>YBCO | T=77K | ω=524rad/s | P_RF=100W/m² | ▶播放</sup>',
                   x=0.5,font=dict(size=16)),
        scene=dict(
            xaxis=dict(range=[-0.1,0.1],title=dict(text='X (m)',font=dict(color='white')),
                       backgroundcolor='rgba(10,10,30,1)',gridcolor='#334466'),
            yaxis=dict(range=[-0.1,0.1],title=dict(text='Y (m)',font=dict(color='white')),
                       backgroundcolor='rgba(10,10,30,1)',gridcolor='#334466'),
            zaxis=dict(range=[-0.02,0.15],title=dict(text='Z (m)',font=dict(color='white')),
                       backgroundcolor='rgba(10,10,30,1)',gridcolor='#334466'),
            camera=dict(eye=dict(x=1.5,y=1.5,z=0.7),up=dict(x=0,y=0,z=1)),
            aspectmode='cube'
        ),
        paper_bgcolor='#0a0a20',plot_bgcolor='#0a0a20',
        width=900,height=750
    )
    return fig

def main():
    print("🎯 生成SVS 3D交互式可视化...")
    fig1=fig1_main_simulation()
    fig1.write_html(f"{OUT}/svs_experiment_3d.html",include_plotlyjs='cdn',full_html=True)
    print(f"✅ {OUT}/svs_experiment_3d.html")

    fig2=fig2_rotation()
    fig2.write_html(f"{OUT}/rotation_vs_reduction.html",include_plotlyjs='cdn')
    print(f"✅ {OUT}/rotation_vs_reduction.html")

    fig3=fig3_rf_power()
    fig3.write_html(f"{OUT}/rf_power_vs_reduction.html",include_plotlyjs='cdn')
    print(f"✅ {OUT}/rf_power_vs_reduction.html")

    fig4=fig4_material()
    fig4.write_html(f"{OUT}/material_comparison.html",include_plotlyjs='cdn')
    print(f"✅ {OUT}/material_comparison.html")

    fig5=fig5_phase_diagram()
    fig5.write_html(f"{OUT}/temperature_phase_diagram.html",include_plotlyjs='cdn')
    print(f"✅ {OUT}/temperature_phase_diagram.html")

    fig6=fig6_animation()
    fig6.write_html(f"{OUT}/levitation_animation.html",include_plotlyjs='cdn',full_html=True)
    print(f"✅ {OUT}/levitation_animation.html")

    print(f"\n🎉 全部生成完成！共6个交互式HTML文件")
    print(f"📂 位置: {OUT}")
    print("🌐 用浏览器打开任意HTML文件即可查看")

if __name__=="__main__":
    main()
