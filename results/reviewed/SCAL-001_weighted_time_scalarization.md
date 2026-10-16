# SCAL-001：保留时间的有限weighted scalarization

2026-10-17，R0022。内部独立交叉审查的自包含有限引理，未作新颖性/重大性认证。

有限原时间概率ν满足：所有长度≥d的interval质量≤K_t长度。向量F的直径≤M，任意vector vertical h-affine fit的原质量≤a。λ在[1,2]^m均匀，Π_λ(t,F)=(t,λ·F)。当b≥C_mK_t(d+w)时，

    Prλ[存在Euclidean w-line tube，原ν质量≥b]
      ≤C_m[a/b³+(1+M)K_t w/(h b⁴)].

ordered middle residual的convex weights避免了残差中的gap逆；Euclidean tube垂直化的gap费用仍保在b⁻⁴中。原time weights全保留，一次统计控制所有自适应直线，无无限union bound。若另有真正Euclidean Lip，可有较强版本；source仅dyadicLip时用本bounded-range版。

任意set-theoretic graph免费保Π_λ的cover cardinality为假；原observed A若另有每coarse observable-x最多K fibres，则对所有boundedλ可保cover到K倍，这个正向接口在同稿证明，不冒充一般集合定理。

证明：notes/40_multiscale/sticky_mixed/R0022_scalarization_counterattack.md。独审：research/reviews/R0022_scalarization_review.md；实际应用：AFF-001。有限引理不等于Kakeya或新的维数结果。
