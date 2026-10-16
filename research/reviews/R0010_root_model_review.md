# R0010整合独审：actual f≡0、单层cap与非空true atlas

2026-10-17。root独立复核lifting_obstructions的R0010_zero_depth_counterexample_attack.md及其新增§8；统一随机标签稿由root编写，另经audit_four_dimensional在R0010_random_label_review.md独审，并经lifting_obstructions在模型稿§9独审RL4/RL5。此文不把自己对随机步骤的复述当成独立复核。

## 模型与真正的零深度密度

Q=tY2+Y1Y3=λ的恒等式逐项展开正确。λ,s,p,q的四参数grid等概率，单index权≈δ⁴，不能再误用R8的δ³。六visible系数加δ盒噪声、w0=cλ+e及W两维η盒给完整8维有限分段常density；(B1,V1,V3,B3)定位(s,p,q,λ)各O1格，重叠数统一有界。所有tables/widths是固定原始幂，tag实常数不受height限制，随机性在选定后不属于轨道law。

在selected内层t，exactY由Q定位O1 λ；每λ、每s再由x,z定位O1 p,q，故g_t≤δ^-1·δ^-3·δ⁴=C。每exactY上可贡献hidden bins数O1，因每层cλ只带η≪a_L的噪声。这直接给原observational support reference-volume≤C及全部深度G_r≤C，积分给µ{G_r<N^-τ}≤CN^-τ。故是实际f(r)=0，不是world平均或常数平移，也未假定support所有点有lower。

ρ≥δ的angular指数由O(ρ/δ)个s计数得Cρ；ρ<δ时eligibleindices O1，joint(Y,V) densityδ^-6乘权δ⁴与ρ³给δ^-2ρ³≤ρ。加hidden bin只减少upper。因而n(L)=1、S=1、固定depth range都真实满足；可取cap参数d=1/2（实际profile斜率0）。

## 全宽度几何与随机测试接口

固定λ∈[1,2]，diag(λ^-1/2,λ^-1,λ^-1/2)与其逆有统一常数界，参数缩放将Qλ化Q1，s范围仍是有正下界的固定compact。R7 QCAP证明只需这些非退化界，grid间距和noise宽也与δ固定可比。well-conditioned image用SVD包裹，ordered widths逐轴可比且体积只变常数；R8薄轴noise概率补偿仍适用全部正宽度。故conditional capδ^-1/2J正确，乘原πλ≈δ后是δ^1/2J，短块再付K³q^-3。

root的随机稿使用的是这项**单层未归一化**cap，以及混合g_t≤C的νvis(G)≤CK³J。没有假设tag与visible整个block独立；只在随机选择颜色表的存在性证明中独立抽cλ。复杂assignments扩大到固定维单chart几何与current tests，所以uniform pattern指数不依赖assignment复杂度或标签表长度。随机稿独审通过后，与真实floor比较得到H≥M/6；任意进一步selection及subsequence不能改变此固定幂。

## q=δ真实atlas的独核

在完全位于I0的δ块上，用midY的δ-cube Q及原w0的终端a-bin C分组。每Q定位O1 λ，故隐藏bin只O1个，全部pairs数≤Cδ^-3；每pair概率≤g_t ceiling×δ³≤Cδ³。删质量<τδ³的pairs至多失Cτ，goodpairs的原概率≥τδ³。D=C1δI的J=C1³δ³，与n(L)=1的原floor匹配。P=w−cC在整块small-value，Pw=1、curvature0。选整块assignments的全部incidences，m/q正是其原概率；总覆盖常数。

current exactY距midY为Oδ，current hidden a-bin与原w0 a-bin相差O1；所以own-depth/terminal列表O1。λ内部index不输出。所有assignments是原系数中的线性bin tests，goodpair table有限、总labels Oδ^-4、逆D为固定N幂。故H≤M，并非真系统集合为空导致的下界。

## 来源成本与结论

可见V=(p,−pq,q)+ζ。给定V1,V3仅O1个(p,q)grid centers，权δ²与ζ的δ^-3density给visible-slope ceiling≤Cδ^-1；其支撑在|V2+V1V3|≤Cδ的有界薄层、体积≤Cδ，概率为1，故最小ceiling也≥cδ^-1。这是实际方向来源缺失，n0=1不能删除它；full(V,W)还多η^-1成本。

因此在literal j3类中，actual f≡0、S1与d<1仍可有M/6≤H≤M，取M>6L即H>L。允许M任意大说明即使固定L=1、S=1及angular range、另限f0=0，原all-model supremum k(d)仍为∞（任意0<d<1）。不能通过限制f0为0重建原§4的有限k。此结论仅为形式模型障碍，原稿实际j2未受反驳；没有新维数下界、真实Kakeya反例或重大结果认证。
