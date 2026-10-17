# FSD-001：任意ambient的有限种子及稀疏族预算

2026-10-17。内部交叉独审通过，未经外部同行评审；新颖性/重大性未认证。完整证明notes/20_dimension_lifting/finite_seed_transfer/R0029_projection_and_prior_audit.md及R0029_conditional_seed_and_six_dimensional_bound.md，KT核对R0029_KT_seed_and_frontier_audit.md；两独审在research/reviews/R0029_projection_transfer_review.md、R0029_source_KT_review.md。

无条件有限几何部分：fixed ambient M,R、real s≥3、原δ-separated directions满足cap K(θ/δ)^s。任意m条原线可由bounded Gaussian projection到R4，保nonshort并经collision independentset留下≥c m/[Kδ^(3−s)(1+log)]个sep方向；原mark/clock/endpoint/cell-cover只付固定常数。输出allscale cap3由packing给，不假ADlower或自动投影Frostman。

**条件部分依赖既有DIR003→SRC001→完整OAI4 proof及全部输入正确。** 原平均mark densityλ先heavy，再投影，DIR003给

    #E ≥ c λ² m K^-1 δ^(s−4+ε_D)/(1+log(1/δ))。

任意原条数均可，两个λ分别来自heavy数及逐line marks。∀targetε∃sourceη，若K≤δ^-η、λ≥δ^η则#E≥c mδ^(s−4+ε)。饱和时条件给所有fixed real n=s+1≥4、任意fixed ambient的严格次临界K(n,4−ζ)。不声称input/output loss有线性模数，也不是任意λ的尖锐maximal。

未重证完整四维高级排除或KT全文。单独投影不证明维数下界；后续条件六维推论见DIM-001。无无条件新Kakeya界或重大性认证。
