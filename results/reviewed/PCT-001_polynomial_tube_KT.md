# PCT-001：离散有界次数向量曲线的 tube-KT 振幅界

2026-10-17，R0021。内部独立交叉审查的有限几何引理，未经外部同行评审，不宣称新颖性或重大结果。

固定 D,m。向量 polynomial P:[0,1]→R^m 次数≤D、全窗口振幅R≤1；原d-separated样本B有#B≥θ/d。若 e≥dR，P(B)⊂N_eY，且同一Y在所有 e≤e'≤L≤1 的任意方向细长tube内满足

    N_e'(Y∩tube)≤K(L/e')^{1−γ},

则

    R/e≤[C(D,m)Kθ^{-C(D,m)}]^{2/γ}.

证明保原有限样本，以scalar分量的导数sublevel及有限分支控制preimage重数，取domain长度sqrt(e/R)的一段，用真实polynomial Taylor余项将其放入短直管；同一管上的cover上下界相比较。离散坏集边界、D=1、近常P、非闭Y及fixed厚度倍数均已处理。

原草案把C放在2/γ幂外且要求其独立于γ，该**一致精确形式被严格有限反例否定**。取m=D=1、γ=1/(2n)、e=d=2⁻ⁿ、P(t)=t、B=Y为全二进网格、θ=1；半径r球cover的全部tube-KT查询可取K=2^γ，但原式要求2ⁿ≤4C。修正版常数必须保在幂内，或者先固定γ再允许依赖它。

证明：notes/40_multiscale/sticky_mixed/R0021_polynomial_tube_KT.md。独立反例/修正版独证：R0021_polynomial_counterattack.md。独审：research/reviews/R0021_polynomial_review.md。实际mixed32的条件应用见MIX-003；本引理本身不解决完整branch、Kakeya或新的维数下界。
