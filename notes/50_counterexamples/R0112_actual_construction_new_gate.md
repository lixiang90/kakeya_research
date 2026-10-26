# R0112：真实构造、全部含段直线与多纤维资格门

2026-10-26。分工 constructive_gate，仅编辑本文件；不修改公共状态、登记或 Git。结论是 **no qualified new mechanism**：本次取得新来源的实际量词核验，没有新的严格维数上界、ordinary gain 或重大中间结果。内部逐步审查尚待 root 安排，未经外部同行评审。

## 1. 原目标、读取范围与停止条件

目标仍为同一个实欧氏 (K\subset\mathbb R^n\)、每个方向的实际单位线段及严格 Hausdorff 上界，或者能推进该完整问题的非等价结构输入。部分方向、零 Lebesgue 体积、参数维数、不同尺度不同集合和任意 finite toy 均不能代替这些量词。

实际读 GOAL、STATE、R111 next gate；回读 R81 compact-family/Baire 归约、R82 完整端点/多纤维选择门与正角度无 Hölder 正则化、R85 midpoint/packing、R86 Du 构造与真实 completion、R106 原源失败；补读 R83 next 与 macro 的明确 acyclic 冻结，以及 R41 coordinate-separable/共同 clock 障碍、R93 真单位段乘积例、R94 真全方向满维例。未重跑 context 或旧计算。没有把来源身份当作正确性保证。

本轮停止条件：若新来源实际仍为共同 clock 的坐标乘积、已有源的重调用，或拓扑候选只排额外 acyclic/selector 子类而没有从完整原对象支付该输入，则拒绝锁 phase II，不追加 joint-law 公设。

## 2. 新 primary 的固定版本及实际读域

root 定位并下载 Lai–Wong，arXiv **2506.18142v2，2026-08-15**。本文实际打开[当前 v2 HTML](https://arxiv.org/html/2506.18142v2)，读 Definition 1.1、Propositions 2.1–2.3、3.2–3.3 的 statement/proof，及 §4 的 Lemma 4.1、Theorems 4.2–4.3 完整证明；随后回读本地 extracted 的上述 §4 和 intro 定义。PDF 是 [literature/primary/R0112_lai_wong_2506_18142_v2.pdf](../../literature/primary/R0112_lai_wong_2506_18142_v2.pdf)，本稿不冒称逐页视觉核验或自行完成字节核验。root 统一保版本和实际下载元数据。

来源声称的高维例是零体积而满 Hausdorff 维，并非 Kakeya 反例。“不是平面集合乘自由盒”的物理表述不授跨坐标耦合：§4.2 的生成参数仍为一个平面紧集的 ((n-1)) 次 Cartesian 乘积。下文分别核几何结论及生成标签/全部含段直线之别；不照搬一个未消歧的 intrinsic sticky 分类。

## 3. §4.1 的同一个真实集合、方向与单位长度

为避免源中 line/compact 的措辞歧义，按其 slice 证明取**连接端点的闭线段**，不取无限支持直线。记 (m=n-1)，

\[
 D=\left\{\sum_{j\ge1}\varepsilon_j4^{-j}:\varepsilon_j\in\{0,3\}\right\},
 \quad A=\tfrac12D^m,\quad B=D^m,
\]
\[
 K_0=\{((1-t)a+tb,t):a\in A,b\in B,0\le t\le1\}. \tag{1}
\]

这是紧参数域的连续像，所以紧且可测。每条生成段的速度为 ((b-a,1))，长度至少 1；在同一段中截取单位子段即可，不把 clock 长 1 误称弧长 1。生成 slope 集是 (B-A=[-1/2,1]^m)，有固定开角度内点。固定有限个物理旋转覆盖球面上的方向后，得到**同一个**紧全方向单位段集合；不是每个方向另换集合或拼 clock。

原 slices 为
\[
 (K_0)_t=\tfrac{1-t}{2}D^m+tD^m. \tag{2}
\]
当 (t\ne0)，正确的一维相对系数为 ((1-t)/(2t))。源证明在这里略去的固定 (1/2) 不改变参数映射在 ((0,1)) 中的非退化性，所以不改变其 a.e. 投影和 Fubini/slicing 结论；不把此措辞问题冒作高维反例。

## 4. 一个实际可检验的中间截面：含 (3/4) 盒

下列等式直接从 digits 验证，不依赖源的高级投影定理。(D+\tfrac12D) 的逐位数字为 (0,3/2,3,9/2)；其四个比例 (1/4) 的相似像把 ([0,3/2]) 分成四个首尾相接的闭区间。因此紧不动集唯一性给
\[
 D+\tfrac12D=[0,3/2]. \tag{3}
\]
也可用 (D=1-D) 与源列出的 (D-\tfrac12D=[-1/2,1]) 相互校验。(2) 在 (t=1/2) 给
\[
 (K_0)_{1/2}=\tfrac14D^m+\tfrac12D^m=[0,3/4]^m. \tag{4}
\]

这不是只有有限近似网的结论；是同一紧集中的确切盒。它不与 (n) 维 Lebesgue 零矛盾，因为只有一个 clock 截面。(m\ge2) 时其最长弦为 (3\sqrt m/4>1)，因而它含有相对方向空间中一个非空开集的单位线段；不是只含零长度点或不足单位的短弦。

## 5. 生成 label 与全部含单位段直线不能相等

对物理集合 (K)，令
\[
 \mathcal L_1(K)=\{\ell:\ell\cap K\text{ 含一个实际单位线段}\}.
\]
这与指定生成参数族 (G=\{(b-a,a):a\in A,b\in B\}\) 是不同对象。生成族的 packing/Hausdorff 维数为 (m)：端点到 ((b-a,a)) 是固定可逆线性变换，且 (D^{2m}) 为强分离自相似集、维数 (m)。这能证明**指定 family** 小，不能推出 (mathcal L_1(K_0)=G)。

事实上，(4) 中的所有单位弦均属于 \(\mathcal L_1(K_0)\)，而它们方向满足 (v_n=0)，从而不是任何 (1) 的生成线。更强地，在 (m\)-维超平面内，所有穿过盒内部且弦长严格大于 1 的 affine lines 含一个 line-space 开集：方向有 (m-1) 个自由参数，垂直 offset 有 (m-1) 个自由参数。局部 canonical 线坐标是双 Lipschitz 的，故
\[
 \dim_H\mathcal L_1(K_0)\ge 2m-2=2n-4,
 \quad \dim_P\mathcal L_1(K_0)\ge2n-4. \tag{5}
\]
具体地，先取盒对角线方向、中心穿线；其弦长 (3\sqrt m/4>1)。方向与 offset 足小扰动仍有长度大于 1 的内部弦，支付上述真正开参数集。这里 (n\ge3)；(n\ge4) 时 (2n-4>n-1)。

源固定 chart ((v,a)\mapsto(a+tv,t)) 排除了横向 lines，不能直接在该 chart 中数 (4) 的 horizontal 家族。但对任意把该超平面倾斜成非水平的物理旋转 (R)，可在上述开集内保 \(|u_n|\ge c>0\) 的小方向帽。这时换到该 chart 的映射 (v=u_h/u_n\)、(a=x_h-x_nv\) 在紧子帽上局部双 Lipschitz，故同一 (2n-4\) 下界就在源的 chart 中成立。

特别地，可在任何有限旋转全方向 completion 上**再加入一份这样的固定倾斜 (RK_0)**；紧性、零体积、满 Hausdorff 维与全方向均保留，但其全部含段线空间具有 (5) 下界。若按源 Proposition 2.1 的标准方法只用生成方向 patch 完成球面覆盖，旋转族中也必须有倾斜 copy，因为仅保竖轴的旋转不能把任何生成方向变成 horizontal。未分类原集合的全部意外 lines，故不擅称“任何依赖其他意外 lines 的有限 completion 都必如此”。

因此，本稿只采用如下安全读法：生成标签族的低维计算有明确对象；若要声称**物理集合全部含单位段 lines** 的 intrinsic packing 维数等于该标签维数，仍需另证。intro 对单位圆盘的说明与 notation (a_v) 对“任选一根/全部含段 lines”的使用存在量词区别，本文不替作者选择解释，也不宣布其定理全 false。此处是一个可逐式检验的 source-application 限制，不是新的 Kakeya 维数结果。

## 6. 真正满维的原因与旧指纹

§4.1 的普通投影定理给 (2) 在 a.e. (t\) 具有 (m\) 维；§4.2 令平面参数 (F\) 为源 Proposition 3.3 的紧集后，实际 slices 是
\[
 \{a+tv:(v,a)\in F\}^{m}. \tag{6}
\]
平面投影在 a.e. 同一个 (t\) 有维数 1，有限次乘积给 slice 维数 (m\)，再 slicing 给集合维数 (n\)。不同坐标分别换成有限个这样的平面 (F_i\) 也没有新的脱同步：有限个 a.e. clock 集的交仍 conull。不能从零长度 a.e. slices 推严格 dimension upper。

这是对该新 primary 的实际归类，不是本项目新证明了一般坐标分离 Kakeya 定理。R41 已对同 clock 的 complete Cartesian direction combinations 给实际 log 邻域 lower；R93 已有经典数字参数族的同集/真单位段/全方向、零体积但满维例。新来源的“物理非 (K_2\times\) 自由盒”没有离开该共同 clock 坐标分离指纹。没有原跨坐标 joint-law 或比既有 DIM001 更强的初始化输入，不锁 gain。

## 7. 合法 restriction/shading 与反向强度

同一生成族的闭 label restriction 保紧、保原线段、保继承几何，但通常丢全部方向；任意可测阴影 restriction 可保体积/质量定义，却不保整段及 (2)/(6) 的 complete Cartesian slices。任意生成 label 子族均不删除物理并集中已经出现的其他方向线段；把 label 维数当 intrinsic 全部含段线维数不是 restriction 闭包。

有限真实 δ 管先给全管 marks (Y_i=T_i\)，逐管与平均都是 (\lambda=1\)。若原 (N\)、incidence (I\) 经删选分别剩 (N'=qN\)、(I'=pI\)，则平均密度为 (\lambda'=(p/q)\lambda\)，归一方向 cap upper 至少须按原上界除以 (q\)。逐管 lower 只在实际每管保留足够 marks 时继承；平均 positive mass 不授完整共同 clock，更不授 Cartesian completion、点上完整 pencil 或 WZ source 的原联合质量。不能靠选一个有限 δ 集再称其 packing 维为 0。

原全方向 compact Kakeya 结论若已知，并不推出指定生成 family 唯一或全部 contained-line 参数等于该 family。反过来，一个小参数 family 加方向内点只保证可作有限旋转的全方向几何，不给严格 Hausdorff upper。本文未证与旧 CP/PM/PW4 正幂 gain 的双向等价，也未发现可借这些统一闭包免费得到的新增 gain；没有因“未证等价”就自动准入。

## 8. 完整 compact 多纤维拓扑候选：按 R83 冻结拒选

另有限筛查 R81 原对象：canonical affine line space 中紧致 (C\)，方向满 (\mathbb{RP}^{n-1}\)，distinct whole lines 两两不交，不预设方向唯一、有限 fibres、section、流形或正则。R82 已实际支付 (R>\max|a|\) 的端点嵌入到球面闭像、近反极关系和 inclusion-minimal 子族的 residual singleton；它不授 full-direction section、幂模量或 nonzero degree。

曾考察以 Vietoris–Begle 将“每个方向 fibre 都 Čech-acyclic”转成顶上同调障碍。这个假设比连续 selector 的字面形式不同，但本项目**没有从完整原 (C\) 支付它**，不能把它当新输入。进一步 rg 实读 R83 next §4 与 macro §5，已明确冻结 continuous/acyclic/Hölder proper 类重开。故本稿不锁该题、不登记结构定理、不再下载其文献或以无环 fibre 成功公设收轮。

有界检索仅定位了 Kryszewski 1996 *Remarks to the Vietoris theorem* 的 Theorem 1.1（作者上传文字可读，官方 DOI 工具未达），以及扫描 Begle 1950 原 PDF（正文未实际读清）；它们都**未被采用为本轮数学输入**。没有宣称独立重证这些高级拓扑定理。完整 multifibre no-family 或真实 full compact 构造仍未取得；partial Cantor/端点图不能当其反例。

## 9. 反攻与本轮判定

(4)–(5) 保同一个真实欧氏集合与严格单位长度，所反的是“指定低维生成 labels 等于物理集合全部含单位段 lines”的免费等式；它不反 Kakeya 猜想，也不削弱源满维几何结论。不以两锚球面、Du 曲线零损失 lifting、更多 fixedtime、p-adic metric 或旧 digit 参数替换这一个反攻。

本轮新增证据是新 primary 的实际应用边界和明确 contained-line 压力测试；仍无可推进 ordinary (n\ge5\) 下界、完整原 source mass 或真 strict-Hausdorff 反例的 qualified mechanism。R83 acyclic 门保持冻结，R41/R93 product 指纹保持。没有新数学 ID、major、first/best 声明；完整 Goal 继续 active。root 负责独审、公共记录及同步，本稿不预认证这些后续操作。
