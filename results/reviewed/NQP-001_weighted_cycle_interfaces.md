# NQP-001：保原时间先验的非二次四环接口

2026-10-17，内部交叉审查；未经外部同行评审，不主张新颖性或重大性。证明见 notes/40_multiscale/sticky_mixed/R0023_weighted_cycle_concentration.md；互补强共同线版本见 R0023_rank_and_prior_counterattack.md，实际尺度见 R0023_nonquadratic_source_audit.md。

同一有限time prior ν有interval cap K_t|I|（长度≥d），所有vector quadratic h-fits质量≤a。对于原S的四差Q，任意g₀≥d、e≤g₀h、任意0≤c≤1且∫c=D，

    Pr_c{|Q−q|≤e}≤[a+2K_tg₀]/D，
    N_e(Q(supp c))≥D/[a+2K_tg₀]。

若c支撑于原H-cycles、Q距固定affine line≤e，g₀≥d、2K_tg₀≤D/8、e/g₀≤h/4，则提取T质量m≥3D/4，normal F|T在e/g₀内为scalar quadratic；along-line F|T的scalar h/4-nonfit质量≤a/m。原H每row degree≥√D/4，若H由E_A g≥λ生成，则原g restriction绝对mean≥3λD^{3/2}/16；新time cap为K_t/m。重新生成cycles原质量≥9D⁴/4096，但不保证仍nearline，也不保证原c在T²保持质量。

在实际mixed32 small-τ中，可直接从原L boundedg的heavy-H使用点球cap。δ/ρ≤ρ³，w/h≤K^C[ρ^{1−2ε₁−ζ₁}+ρ^{ε₀−4ε₁−ζ₁}]，按正幂先固定、所有retention/η损失后取小，排direct-H全部Q落一个working-ball。无需vectorBSG或强制coarse time代表。

未证：二维cover/translation gain、Q共同线→S共同线、任意scalar projection保Y维数缺口、完整mixed32非二次、其他五维case或Kakeya。此为elementary original-mass接口，不是重大中间结果。
