# R0097正式审查：原质量与scalar参数的局部Segre门

2026-10-19，A。以下有限范围全文通过，无未解决强制项；未经外部同行评审。结论只排明列small-loss直接输入，不是完整mixed42排除或ordinary增益。

## 1. 实际全文对象、primary与审查层次

已实际全文读root `R0097_scalar_Segre_local_spreadout_gate.md`12节、A原稿`R0097_adapted_projection_primary_and_mass_gate.md`10节、B稿`R0097_rough_adaptation_counteraudit_and_routes.md`8节、reselection/working两spec各5节及终macro/next/source各6节。root§7最后新增的E_t/Φ计数、K^C参数格重数和不同time可有不同witness均已fresh读回。A本人参与原source质量推导，不把自己的稿再算一份独审；该部分已由root/B实际全文核对。本审重点独立检查root/B的局部几何、primary量词、反攻及整合范围。

实际primary为库存CSWZ2610.13682v1：引言及Def1.4–1.5、Th1.2/1.6/1.7和所需big-cell声明已读，官方abs/history fresh核仍2026-10-09 v1。原45页高级§3和companion paper未本轮独证。WZ Def3.6–3.9及普通/dyadic管替换说明本轮实际读回；Def17两grain/Φ等输入沿R96实际读取范围核对。既有R14、R76固定Schubert范围与R96exact观测商保持，不冒新增PDF、官方核心wholebytes或外部proof认证。

## 2. 正确维数、原visited质量与nearfull条件用途

F_tλ在重排后为π_(θ_t)(x,y)=x+θ_t y，θ_t=(-β_t,-tβ_t,t)∈R7。Th1.7取d=8、kernel k=7、output1，spread-out下标(8,1)；scalar模型H是全部affine hyperplanes。Th1.6对kernel7-planes用transpose/负号参数，仍是同一个R7几何，不能混同output4的旧配置。有限输出near-full t_P，强度确实足够，不是half-plus或dim/8。

root§7已补的原计数成立：第一套global grain给#E_t≥K^-Cδ^(-4+κ)，逐p的scalar Φκ给≥K^-Cδ^-κ个分离角。固定time一根bounded graph tube只遇O(1)个原分离位置，固定p/tube也只容O(1)个φ；于是实际visited T_t≥K^-Cδ^-4≥K^-C N。原N是bounded全T分母，不是used族。取原joint参数δ-grid P；每格重数保守付K^C，故#P≥K^-C N、#P_t≥K^-C#P，UniformP的ball upper≤K^Cr⁴。不同time可用不同原T见证同一格，因它们参数相距Oδ，每time scalar target误差仍仅Oδ。

取t_P=1−κ/4和输出loss ζ<κ/4，原η在定理ε之后小。若额外spread-out输入真成立，则K^C≤δ^-ε、P_t达到robust大小阈值；θ最后坐标t保证原time到参数格碰撞O(1)，保留参数有实际time见证。Th1.7会给某个真实P_t输出≥δ^(-1+κ/4+ζ)，与原Ỹ_t的upper K^Cδ^(-1+κ)冲突。固定点/参数rounding、[0,1]^8归一及target baseline只损固定邻格，不需β Lip或g独立。

若改Th1.6，原总边到point-heavy并统一M≈K^-Cδ^-1需另付质量；所定义kernel7-plane的offset来自实际F_tλ。总affine-plane cover≤K^Cδ^(-2+κ)，nearfull lower δ^(ζ−t_P)M亦足矛盾，但仍要求逐point shading spread-out。root/B没有把这些条件正链当已取得该假设；平均、逐point和逐tube的分母明确分开。

## 3. 精确局部恒等式与真实cell厚化

原θ无论β多粗糙都在Σ={z=(u,v,w):v=wu}。在z_0∈Σ，H_i的法向g_i=(-w_0e_i,e_i,-u_(0,i))有norm≥1，且

    g_i·(z−z_0)=(w−w_0)(u_i−u_(0,i))， z∈Σ。

故Σ∩B(z_0,r)距H_i≤Cr²。H_i是合法scalar model H，随basepoint变动，不需一个global H包含整个族。此步没有β导数、clock gap或小singular值分母。

root§4/B§4对family的union而非仅精确curve作了必要检查：任意非空𝒥′、θ∈∪𝒥′，选同cell的z_0∈Σ；局部ω再选其cell内z∈Σ。两次误差≤Cδ、|z−z_0|≤r+Cδ，得到dist(ω,H_i)≤C(r²+δ)。因source Def1.5的centre可在cube内部，不能省这项；现证明已覆盖角点、内部及所有非空子家族。

固定b∈(0,1]，先取c小、A大，则Aδ/b≤r≤cb保证上述误差严格小于br。常数只依固定chart/dimension；fixed b、δ最后小保证区间非空。H可随中心，Def1.5允许此量词；实际同一H_i对该中心所有这些r已够。

## 4. 尺度数、删选、ε边界及chart限制

dyadic尺度数至少s_δ≥log₂(1/δ)−2log₂(1/b)−C。对任何非空家族取其自身全子族，Def1.5迫

    C_spread≥2^(b s_δ)≥c_bδ^-b。

因此固定b且C_spread=δ^-ε、ε<b时，所有原time子选和逐point非空shading都不能满足该small-loss输入。这个几何事实不需要保留比例；不因heavy、权层或正常restriction消失，也未假删后ADlower。

关键边界准确保留：该必要式不排ε=b或ε>b；不能用定理‘可缩小ε’冒对所有较大参数版本的反证。b若随δ变，定理cutoff/ε依赖同样不能免费固定。root/A/B、macro/next均没有扩大此范围。

固定有界可逆ambient变换在远离projective pole、C²及逆规范受控的chart内，把Σ变成正codimension smooth图形；切H/δ厚化仍同阶。scalar模型包括所有affine H，所以局部证书只改固定常数。一般δ病态变换和非可逆有效商不在此uniform结论内；非线性压平Σ也不自动保原πθ作用和model定义。没有将chart选择当新全局归约。

## 5. Global-cap校准、原商与旧失败区别

独立核root§10/B§5的moment例：β=(t²,t⁴,t⁶)使θ为t,…,t⁷的signed permutation。任意unit-normal global H对应degree≤7多项式，某非恒项系数≥1/√7。若sublevel长m，在其中取8个gap≥cm的点，Lagrange系数upper≤Crm^-7，迫m≤Cr^(1/7)；sublevel至多15个interval/point组件，均匀δ网额外误差Oδ。因此r≥δ有统一global H cap≤Cr^(1/7)，parameter-cell舍入只改常数。full span8及full moment jet也同时成立，却仍有第3–4节的全部local singular scales。

B的真实unit bush可保joint4AD/angular separation/whole-CW并有正五维tube-union体积；它没有所需small native labels/point-Φ/双grain，不能冒fullsource counter。moment例同样只分离global与local假设，R96已排其完整source实现，不反GGW或本轮原观测商。

R96exactspan的point-law upper不是parameter law的局部离H比例；不能填作Def1.5或approxspan/conditional lower。R14/R76是fixed global model-H/Schubert退化，当前即使所有global H均有power cap仍local退化，具体审查责任不同。但本证书只是一个primary输入门，不是已证明新的point-adapted投影定理，也未建立与旧CP/PM的双向正幂等价；旧冻结保持。

## 6. 最终实际scope、宏观后继与结论

终macro、next和source各6节已实际全文读，root§7的K^C重数/原点角计数及跨time不同witness修订亦已读回。它们一致保留：CSWZ scalar nearfull强度够、原质量可转移，但原参数族在fixed b/ε<b的small-loss要求下失败；ε≥b、有效非可逆商和真正relative-point theorem仍未由本证书排除，也未获正用途。保守ordinary/fullrough时钟20与实际finite数学信息分列，没有宣称无工作进展。

无未解决强制项。对原质量条件桥、局部Segre/cell/全子族证书、global-cap分离和明列停止范围，全文通过。完整rough mixed42及四完整路线仍未解决，本轮不增数学ID、不宣ordinary界、major或Goal完成。停止b/ε/局部曲率/chart常数续轮，不能以desired adaptive hyp重开同一gain。

CSWZ高级wholeproof仍具名；本审为项目内部逐步独立审查，未经外部同行评审。自身A的source证明由root/B独审，不自算独审；不预认证未来metadata、Git、验证、同步或来源计数，完成后停止编辑检索。
