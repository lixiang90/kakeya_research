# R0007主代理对QCAP与输入范围的独立复核

日期2026-10-16。被审作者为lifting_obstructions，文件notes/50_counterexamples/R0007_weighted_plank_obstructions.md。root独立核对全部case与离散化；另由literature_frontier独审。未经外部同行评审，不声称新颖性。

## 1. 全框连续上界

固定参数盒与适度扩大盒。n_y较大时∂p(n·b)=−n_y/s；较小时n_x,n_z至少一个有常数大小，∂p(n·u)=n_x−n_yq或∂q(n·u)=n_z−n_yp统一非零。均是对选定参数严格一次，故任意边长r的参数cube内薄轴w1约束质量≤Cw1r²。

完整plank的两个端点约束使全部系数与固定参考线差O(w3)。逆坐标s=b_x,p=u_x,q=u_z直接给参数cube，得Cw1w3²，不需一般逆函数定理。

固定两短轴后，πM与πM0在affine coefficient norm差O(w2)。Q代入πM0+ζn后得Aζ²+Bζ+C；参考ζ0精确为根，另一ζ的残量O(w2)。两种情况覆盖全部单位n：

- |A|≥a0：完成平方后(R−R0)(R+R0)=O(w2)。固定degree1实多项式的归一化系数范数乘积有正下界，故每个R距R0或−R0之一O√w2。两分支是两个固定coefficient centers；若其中心不在参数图上，用固定线性读出s,p,q仍给两个参数cubes，足以积分。
- |A|<a0：A=n_xn_z。当A=0，L0=n_x(1/s0+q0t)+n_yt+n_z(s0+p0t)不能恒零：n_x=0迫n_z=0再迫n_y=0，另一情形同理。单位n和参考参数紧性给||L0||≥c；固定小a0确保||L0+A(ζ−ζ0)||≥c/2。乘积下界给ζ−ζ0=O(w2)。

因此参数分成至多两个O√w2 cubes，Fubini给Cw1w2。与首界合并得到QCAP，代数比值min(1/w3,w3/w2)≤w2^-1/2≤δ^-1/2正确。

这些证明没有漏掉相切框、null方向、特定仿射中心或参数盒边界，常数不依赖plank选择。大width只在固定C0内增加常数。

## 2. 离散全框cap、全阴影和反例

δ参数格点的互不相交cδ-cubes放在扩大Ω⁺内；映射在该盒Lipschitz，完整格点迹线在P则cube的全部迹线在各宽固定扩大的P⁺，宽度w_j≥δ吸收Oδ误差。连续估计的测度必须是扩大盒Ω⁺，定稿已明确，避免原边界cube遗漏。除以cube体积cδ³给全部离散planks计数上界。

每index固定权δ^1/2/Ccap将cap恰归一到A=1。全marks满足任何η门槛。x=s+pt≥.9，所以整个quadric patch为有界Lipschitz图z=(1−ty)/x，#E≤Cδ^-3；加权访问量≥cδ^-7/2。ε<1/2时矛盾，不依赖任何shading稀疏度或subsequence。

root另独立构造宽(δ,δ,√δ)坏框，证明完整未加权网格的cap loss下界δ^-1/2；符号恒等式及m=8,16,32精确有理数网格验证见quadric_plank_probe.py/json。该计算只辅助坏框下界，all-plank上界完全由本节连续证明负责。

## 3. 结论范围

WP4一般形式严格为假；这是已知quadric障碍的一项完整加权chart化验证，不是新Kakeya结果。方向u=(p,−pq,q)落在真二次曲面上，不能充作满方向来源。否定原greedy证明的新增输入，不等于否定另一种方法下j=3 H≤L。

Guth与Zahl综述数字差异另存源审计附记，本轮选用可直接验证的权重δ^1/2版本，不拼接未核验更强claim。四维原稿主证明及正向方向丰富有限尺度输入仍须单列条件，不由本复核认证。
