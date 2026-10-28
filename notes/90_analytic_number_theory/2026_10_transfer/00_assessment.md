# 局部光滑的新结果与经典解析数论：应用排序和实际桥梁

2026-10-29，R0120，root 整合。用户要求思考 OpenAI 证明的思路和结果能用于哪些经典解析数论问题。本轮是有限应用研究，未恢复旧 Kakeya Goal，也未创建长期 Goal。固定输入为已存2026-10-25欧氏波稿；以下区分该文外部定理、严格下游推论、经典基准和未付的新方法输入。

判断：**有价值的接口很多，但本轮没有得到新的经典数论指数。最值得研究的是锥面 first-spacing 分布及 Dirichlet 多项式大值的正能量；直接套现成定理所得的二次均值，尚未优于已有离散 decoupling。** 关键在于保留目标要求的系数范数、算术相关与各向异性尺度。

## 1. 先把原稿已经给出的工具用足

源稿不止证明 wave local smoothing：§9 给 sphere/cone restriction，§10 给 Bochner–Riesz 及相应 maximal，§11 给 Stein square function，**§12 已给 compact paraboloid restriction 和 Schrödinger local smoothing**。因此不能把连续“波→抛物面”桥重新列为待证。

这些输出适合控制曲率相位的叠加、频率壳求和、参数平均与高值集合。数论中的平方系数预算、稀疏整数频率和固定原点取值，则需实际转移。输入密度原子化到半径η的小帽时，质量1对应L^a范数η^(-d(1−1/a))，不能无费用地将surface density换成delta masses。

## 2. 哪些经典问题值得优先考虑

| 问题 | 具体联系 | 还需的新输入及本轮判断 |
| --- | --- | --- |
| Gauss圆问题、Dirichlet除数问题 | Poisson/Bessel及Bombieri–Iwaniec将误差转成cone small-cap、first/second-spacing和large sieve | 最接近已有应用机器；需改善特定离散分布式，连续restriction不是同一输入。原2+1维local-smoothing幂范围早已有，不能直接把新全维范围说成圆问题新幂 |
| ζ零密度、短区间素数 | Dirichlet多项式大值→零密度/素数机器；Guth–Maynard已用Gram/离对角trace保干涉 | 新PDE思想有具体靶点；必须保l∞系数及不规则大值时刻，尚未建立相容的新能量 |
| ζ临界线点值、次凸 | Bourgain已有四维曲线decoupling→first-spacing→second-spacing→ζ的历史链 | 相位为(t,t²,t^(3/2),t^(1/2))，不是原二次超曲面；全盒关键均值幂已饱和，需改变实际瓶颈，不可直接声Lindelöf |
| 二次Weyl和、二次方程组、球面加性能量 | §12可严格周期化为二次指数和Lp均值 | 真正可立即写下的推论，但输入是初值Lp，不是系数l²；已知BD均值更强。单一整数球上该周期演化只是标量，不能由此改善能量 |
| Vinogradov均值、Waring | moment-curve decoupling与circle method已提供成熟路线 | VMVT主猜想早已证明且两项幂均sharp；新方法若适配高阶导数flag、权重/短区间或minor arcs才有新增内容。未取得新变量数阈值 |
| 凸体格点误差的平均、例外集、Riesz加权求和 | 半波相位与square-function/maximal天然相关 | 可作为稳妥应用场；先与ISS等旧radius-mean和Parseval shift-mean比较。一般凸体符号也不由欧氏球符号免费覆盖 |

排序有两种：若要立即可调用的定理，先做二次指数和及平滑/平均格点问题；若要争取新的经典问题改进，优先检验锥分布和大值估计的新正能量，而非重新证明已sharp的全盒VMVT。

## 3. 一条已完整支付的算术桥，以及它为何尚不改善旧纪录

取d≥1、p=2(d+1)/d、整数N≥2、任意复系数a_m，||m||_∞≤N，T^j=(R/Z)^j为概率空间。设

    P_a(x)=Σ a_m e(m·x)， F_a(x,t)=Σ a_m e(m·x+t|m|²)。

[01](01_discrete_restriction_gate.md) 从源Cor12.1(12.2)用大包络、Galilean恒等式和固定N后取极限，完整证明

    ||F_a||_(L^p(T^(d+1)))
      ≤C_d(log(2+N))^(2/p)||P_a||_(L^p(T^d))。      (3.1)

但等系数box给||P_a||_p/||a||_2≈N^(d/(2(d+1)))。因此它不是同尺度的l²离散restriction。将(3.1)配合L∞用于2s次矩，只得到log²N·N^(2ds−d)；已有BD可给N^ε max(N^(ds),N^(2ds−d−2))，大矩中差N²。人工随机化也会同时改变目标指数和，不能凭随机平均恢复原确定性算术off-diagonal。

d=1、p=4甚至已有精确式∫|F_a|⁴=2||a||_2⁴−||a||_4⁴。若频率限于|m|²=K，则F_a=e(tK)P_a，该演化路线完全无额外时间增益。这些测试说明真实缺口在哪里，不否定其他精细离散restriction或PDE重构的可能。

## 4. 圆/除数问题：把新思想落到一个有明确参数的门

[03](03_lattice_counting_and_PDE_routes.md) 实际核了CGZZ2610.21730v1 §6。其cone和为

    F_c(x)=Σ_(k≈K,l≈L)c_kl e(lx1+klx2+l√k x3)， |c_kl|≤1，
    1≤L<K≤η^(-1)≤KL， Z=ηK²。

观察盒B=[−1,1]²×[−(ηL√K)^(-1),(ηL√K)^(-1)]，归一化分布D(λ)的已有具名输入是

    D(λ)≲_ε(KL)^ε[(KL)^3λ^(-6)+K L²(L+Z)λ^(-4)]。

新PDE若能提供更强且保这些尺度/有界系数的分布式，就有已知double-large-sieve、second-spacing机器可承接。但取全c=1的小聚焦盒就迫D(c0KL)≳η/(KL²)；第四项中的Z恰支付它。L=K/2、η=1/K给出的测试排除全参数只保pure-sixth的错误愿望，不能借“更强restriction”删除实际必须的聚焦贡献。

CGZZ的209/670是2026-10-15预印本的外部声明，早于OpenAI新稿，不是本轮推论。本文未认证其全文或绝对最佳。BW1709.04340已撤回，不能把其旧指数作为现有效定理。ISS早已证明平面光滑正曲率凸体在h≥logR的半径均方根为R^(1/2)；[04](04_shifted_lattice_variance_benchmark.md)另自含给出平移均方∫|D(R,u)|²du≲R^(n−1)。这两个平均彼此不同，均不能直接变成固定原点的点态猜想。

## 5. 大值、零密度与短区间素数：一个原生复平移起点

Guth–Maynard v2在|b_n|≤1、1分离大值时刻集W⊂[0,T]、|Σb_n n^(it)|≥V时，有已有界

    |W|≤T^o(1)[N²V^(-2)+N^(18/5)V^(-4)+T N^(12/5)V^(-4)]。

这类结果已有零密度/短区间素数的下游机器；不是OpenAI新稿的应用成果。GM用Gram矩阵、奇异值和离对角trace，因而与“保留叠加干涉再取正能量”有值得检验的方法联系。v2明确l∞系数条件不可免费改成纯l²。

[05](05_dirichlet_holomorphic_seed.md) 写出一个确实可用的接口。令λ_n=log(n/N)、H(z)=Σb_n exp(izλ_n)，N<n≤2N，则实轴上|H(t)|=|Σb_n n^(it)|，而τ≥0时

    H(t+iτ)=Σb_n(n/N)^(-τ)exp(itλ_n)，
    Δ_(t,τ)|H|^(2s)=4s²|H|^(2s−2)|H′|²≥0，s∈N。

因此复平移保持有界系数类，且有真实次调和正性。它只是经典有限和的原生起点，尚不提供原证明的角向Gaussian、局部散度零PSD张量、Dirichlet/cofactor抵消或不规则W的算术相关能量。所有系数可在某一点完全对齐，因此单纯次调和不能强迫统一平方根点值。

有价值的下一步是固定GM的某个临界大值参数范围，检能否从该原生延拓构造真正改善已有trace预算、同时保l∞和离对角信息的能量。若成功，零密度和短区间素数才有可调用的新输入；本轮没有证明这一改进。对ζ点值，Bourgain的A6全盒均值已有对角下界4N6，单纯降低该幂不合法；须另找不同盒、权重或spacing瓶颈。

## 6. 认证与交接

01/04由未参与施工者全文逐式独审；02及05由另一未参与者审查自含算术接口；03的聚焦测试和候选门由未参与者独审。三份记录在research/reviews/R0120_*_review.md，各记实际raw版本。源OpenAI、BD/BDG、Bourgain、ISS、CGZZ、GM的高级全证仍是具名输入，未本机Lean重放、未全篇独证或认证外部peer/新颖性；不新增78项之外的数学ID。

本轮新增6篇PDF和7条明确web-only记录，共114PDF/129sources；版本、bytes/hash和实际读域见literature/metadata/R0120_source_check.json。Bourgain实际v2 PDF摘要13/84与abs旧53/342分开，GM实际52p与comments48p分开。恢复先读STATE和本文件；不要从正确但较弱的平均式继续作等价换名。旧Goal停止状态不变，下一步研究需另有用户授权。
