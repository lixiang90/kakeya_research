# R0057 specification：原joint law的带费用conditional-capacity组合

2026-10-17。context→tmp/R0057_context.txt、固定入口/78状态/latestR56/next/macro/receipt已实际恢复。上一turn progress，父HEAD=origin=remote1a9ae718dbd798e181f25705b273f6ce8c42112d/tree5228a6a01e4b0a454cf7236291d9da8192fcbc00/866files/clean。本轮先执行research/reviews/R0057_macro.md（周期点），以下先于证明。

## 1. 原目标及唯一机制

保持旧H5/full ordinary n≥5 Goal，不新增等价方向ID。检验新elliptic Th2.2的all-s singleblock估计，经真实base conditioning及weighted聚合能否产生joint(T,X1,X2)超过4的指数。原(δsep物理方向、位置、wholeunitclock、marks、可测性/权)保留，平均与逐管分开。

Th2.2全假设见R56next，固定0<s≤1、0<κ<1/10、finiteD；initialellipse floorM^-D、terminalM^-(D−1)，X_v用bin左端点。原source103页wholeproof未独证。本轮不另下载新paper或声最新最优。

## 2. 明确待测的带费用命题

δ=M^-1。固定有界chart，P=(U,V)∈R4×R4，U=(A,B)、V=(B,A)的原交换校准作为反攻，但主任务不是重复freecap失败。A,B在固定R2 square独立uniform，T独立uniform于共同固定clock。实际unit axes取direction(1,A,B)归一化、原midpoint(0,B,A)；共同clock嵌原unitaxes，不延长marks。有限δ方向网与Oδ jitter/固定邻格另核。

允许任意有限/可数可测base partition Γ_j，每项含于(U2,V2)的两个独立center、同shape ellipse E_j的乘积；δ≤w_j≤L_j≤C，orientation及scales可因j不同。Γ_j可严格小于该box，不假乘积/均匀。原prior masses p0_j；任意最终dominated law ν≤μ保总质量m，分项p_j=ν(Γ_j×clock)，time support A_j（按原δ bins或连续投影），time mass/timeprofile据实付，不能重置prior。

每conditional singleblock调用的jointellipse constant K_j必须适用于其实际normalized(U1,V1) prior。其输出仅通过sup-cap聚合到secondblock椭圆slab S_j={(t,x2):t∈A_j, x2∈a_j+t b_j+C E_j}，允许fixed δ增厚。检验该机制所需的最乐观费用

    C(t,x2)=Σ_j p_j K_j 1_(S_j)(t,x2)

能否uniform小到使singleblock δ^(1+2s_j−10κ−ε) cap变joint δ^(4+σ)。若真实调用前权≥p_j，其费用只更高。目标是证明/否定这个**具体带费组合**所需预算，并单独判断是否涵盖所有可能joint策略。不得把不足当H5反例。

## 3. 量词、闭包和独立攻击

所有δ充分小、固定κ/clock/geometry常数，任意上述partition、任意dominated保留（可time-dependent），欲有固定σ>0、小η及m≥δ^η的H5级预算。先检查至少一种交换law下的全partition、全retention费用下界，而不是某个固定分解失败。特别核ellipse Wκ(E)=L^(1+κ)w^(1−κ)、实space area Lw、sameclock权与p_j/p0_j。

ν删选后只有domination，条件time的support/maxweight不自动不变；本轮若能在更乐观的忽略time退化假设下仍否预算，其scope需明确。合法原shading删选保持原标签和domination，平均m与逐管密度不等价；逐管dense仅为被测子类，不能从global m假得。

CP/PM正gain全称闭包旧记录先比，当前仅同一旧H5的一次新source机制测试，不登记“conditional联合增益”新名。若所提命题可由旧统一gain直接再调用即得，注明非新数学；不以新标签重开。

## 4. 真几何/有限与continuous范围

反攻先连续law及全部可测partition，再核原finite方向网/真实wholeunitaxes/commonclock/端帽/Oδ误差。共同chart的positive-angle族可按固定rotations接全方向，但是否保所需每partition量词单独审；不得冒全局Kakeya counterexample。若仅该组相同coordinate-split的slab-envelope失败，不反adaptive charts、joint support计数、空间多packet或Th2.2原定理。

## 5. 分工和验收

A只编辑notes/40_multiscale/R0057_conditional_capacity_source_and_closure.md及research/reviews/R0057_source_and_closure_review.md，核Th2.2完整量词/合法原质量和旧等价。B只编辑notes/40_multiscale/R0057_joint_packet_budget_counteraudit.md及research/reviews/R0057_joint_budget_review.md，独立反攻任意partition/retention的费用、anisotropy/time和finiteaxis。root主稿/metadata/整合/Git，最多两代理、不spawn他人。formal最终全文root/A/B/macro/next实读再写。

## 6. 本轮停止条件

完整作至少一个实际weighted joint组合与严格预算证明/反攻；不能只抄source、只作顺序调用或重复freecap交换例。若无法产生H5收益，准确给uniform envelope的失败scope与尚未覆盖的联合信息，停止此source组合局部链，不续κ/s/partition常数。更新STATE/ROADMAP/registry及48PDF/49sources核验，安全同步同commit/fulltree/每blobSHA256。Goal active，不因本轮困难终止。
