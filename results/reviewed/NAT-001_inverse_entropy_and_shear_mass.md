# NAT-001：原生逆映射的残余熵与大剪切质量界

日期：2026-10-16，R0005。内部独立复核见research/reviews/R0005_native_review.md与R0005_native_mass_review.md；未经外部同行评审，不声称新颖性。

## 1. d<1的同精度逆映射反例

完整构造见notes/50_counterexamples/R0005_native_coefficient_inverse.md。取P_*=w−StY3，V3=−e2/S、W=Sy03+e1、w0=c，c为有限层d-Cantor，e1,e2∈[η,2η]且η≪所有prepared p。

精确X=c+e1t+e2t²，全八系数prior Jacobian绝对值1/S，有限半代数、原始多项式高度。可验证真实d<1隐藏profile、同一ν°的(6.6)/(6.9)、完整长线与unit-time true atlas。

给定一个最细native B_p=(y0,V,x0,x1,x2)_p，y03在其p-cell内仍均匀，所以W_p每个原子的条件概率≤1/S。于是任意L列表的成功率≤L/S，H(W_p|B_p)≥logS；恢复要求y03精度p/S。

exact current Y3会取回这份信息：W=SY3+e1+te2，误差O(η)。因此该模型没有否定加入exact point后的恢复；它说明I(W_p;point|B_p)可达logS，不能被原生系数熵率删除。

必要边界：H=0有直接true-atlas证明；完整raw full-slope密度约η^-1，不是初始subpower来源。它不是positive-horizon/critical/Kakeya反例。

## 2. 同坐标bounded-W给真实几何质量限制

对P_*=αw−β(tY3−Y1Y2)，同一未归一化prior中假设y0,V∈[-R,R]^3、|W|≤M_W、|x1|≤M_x；在一个prepared 0<p≤1网格有

ν(y0 p-cell,V p-bin J)≤A_aff p³π(J)，ΣJπ(J)≤1。

一次项恒等式为x1=αW−β(y3−y1V2−y2V1)。固定V-bin与前两个位置cells后，允许的y3 cells数≤C_R[1+(|α|M_W+M_x)/(|β|p)]，故

ν(目标轨道)≤C_R A_aff [p+(|α|M_W+M_x)/|β|]。

这是真实位置—方向薄带质量界。它不要求细到β^-1以下；但只适用于所列原生式及同prior affine cap，不能代替任意二次native的全分类。原稿父归一化更换test并改B、时间和坐标，必须重新核对完整tuple，不能沿用初始W范围。

尚未把此质量界闭合到全部真实临界路径。ENT-002与本结果都没有给新Kakeya维数下界。
