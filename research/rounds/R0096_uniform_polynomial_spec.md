# R0096补充锁题：原coarse标签闭包与统一bounded-degree分支

2026-10-19，以下新增施工在落主证明前明确锁定。原两spec保留；新候选来自原Def17.2的coarse union上界与native filled三轴，不是追加desired smoothness。

## 1. 命题与完整范围

固定D、B、0<κ<1、γ>0。拟证存在η0(κ,D,B,γ)>0及δ0(κ,D,B,γ)>0：不存在完整bounded WZ mixed42 source、CW≤δ^-η，且native βδ(t)为degree≤D、monomial系数≤B的R3多项式row；允许该多项式依赖δ且所有非零singular values任意小。原T/N、jointAD、原time、两grain、ξ/Φ/coherence和原allowedρ全部保留。不排全部dyadicLip β；不得称完整Kakeya证明或major，优先权另查。

## 2. 必先支付的原coarse标签上界

对每个原allowed ρ≫δ及dyadicρ-time窗口J，拟证Nρ(∪_(t∈J∩Z)Ytilde_t)≤K^Cρ^(-1+κ)。原global f在窗内Oρ变动，原global Y_union是(ρ,3−κ,K)-AD，故空间union E_J ρ-cover≤K^Cρ^(-4+κ)。另一方面native βδ的uniform polynomial C1 bound使各label对应的filled三轴点在统一window-normal坐标下保持Oρ误差；每label至少K^-1ρ^-3个实际horizontalρ格，分离label着色后不重叠，推出所需upper。须真证而非默认Def17.4额外coherence。此步只用actual点数/上界，不声删后nativeADlower。

## 3. 谱gap与近kernel压缩

Cδ:R8→R^(D+2)为native相位系数map，norm≤C_D,B。取固定小ε*≪κ及大M(依R74半代数compression幂c*)，固定目标exponent a_j=a0(ε*/(4M))^j，j=0..8。每个a_j就近取原allowed尺度ρ_j，exponent在[a_j,2a_j]（η最后小）；对应开band(ρ_j^M,ρ_j^ε*)两两不交，最多8个singular values，某band空。把Cδ截为Cstrong+Cweak，strong非零smin≥ρ^ε*，weak norm≤ρ^M。

K=kerCstrong上physical evaluation pencil近rank≤3：F_t|K=p_D(t)Cweak|K，故全部4minors系数O_D(ρ^M)。R74固定维半代数稳定compression给K1/E泄漏≤Cρ^(M c*)；M先大使此≪ρ。一个Cstrong输出r-ball(r≥ρ)参数近affineK at rρ^-ε*，whole凸box/补格求和给原μstrong(B_r)≤K^C ρ^-ε* r。小dimK≤3可直接全K网格；ker0另核。ρ mollify后任意α<1的cα≤K^Cρ^-ε*。不需要曲线Cδ非退化或Cδ inverseuniform。

## 4. 原clock到finite GGW与参数顺序

原平均visits先heavy，逐管≥K^-Cδ^-1。fine原t round到ρ网时一个cell至多Cρ/δ个原times，故每管仍≥K^-Cρ^-1个不同coarse times；βδ/Cstrong相位Lipuniform，误差Oρ，§2付coarse目标每time≤K^Cρ^-1+κ，weak phase≤ρ^M支付。用literal fixed fullmomentR^(D+2) Th2.1，spatialρmollify和真实plates全support参与给lower≥K^-Cρ^ε*ρ^-1−α+L√ε_th，对比upper K^Cρ^-2+κ。先α=1−κ/4、ε*≪κ，ε_th足小，M/九target尺度固定，再η≪min_j a_j·min(κ,ε_th)，δ最后小。必须完整证明actualρallowed取整、时间邻格/label聚合、plate常数和所有原分母。

## 5. 分工、独立反攻及停止

A在原assigned稿追加独立§2原coarse标签闭包与§4 finite用途；B在原assigned稿独立§3 SVD/近compression常数与既有反攻scope；root另写统一主稿并检索primary是否已有同结论。若任一原coarse上界、谱gap或稳定wholeCW账失败，则只保已付fixed-poly结果，不将uniform theorem登记成功；不靠重命名/degree阈值续轮。即使统一bounded-degree分支通过，也须明确一般rough β提取仍未付、非ordinary/fullbranch或major自动认证。formal待真实全文逐式互审，未经外部同行评审；元数据/Git统一root。
