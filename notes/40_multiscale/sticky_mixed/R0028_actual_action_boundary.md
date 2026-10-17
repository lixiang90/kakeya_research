# R0028：真实有限网格、作用闭包及数字乘法边界

2026-10-17，root整合。唯一main为actual ell3 AFF₃/>2增长；本稿没有证明main，也没有完整factorized反模型。新有限信息来自保原reference的box提取和平均carry门槛。与R0018同一observed/W归一化本身不再记新结果。独审见research/reviews/R0028_original_action_review.md与R0028_carry_and_boundary_review.md。

## 1. 原变量及source措辞修正

保A⊂R²x×R²ξ、概率μ_A、同一原time概率ν、H的原标签概率μ_H、原bounded g(a,t,s,u,v)∈[0,1]，mean m>0。定义ψ=v−u及

    L_ts ψ=((t−s)ψ,−[M(t)−M(s)]ψ)。

当g>0时a+L_tsψ距A至多E₀=Kr（K为已记录small-loss费用）。所有相关性留在g内。π=(v−u)_*(μ_H×μ_H)只假定原slab upper Kπ q^γ，q≥qbase；ν只在长度≥d有interval upper Ktℓ。原used-H已核有κ-cover/Frostman-upper/slab，不自动有逐点κ-AD lower。R27 next/spec曾将它简称κAD过强，本轮明确纠正；R27 OBS001、OBS002和本轮有限证明均未使用这个未付lower。

## 2. 保同一base的全十六边box

给定a，四变量box Cauchy–Schwarz给

    E_{t0,t1,s0,s1,u0,u1,v0,v1}
      ∏_{i,j,k,l∈{0,1}}g(a,ti,sj,uk,vl)
          ≥(E_{t,s,u,v}g(a,t,s,u,v))^16。

在a上Jensen得总box质量≥m^16。概率均为原产品reference，a只出现一次，没有先固定angle再借用条件边际。该不等式由对四个变量逐次CS得到（完整展开见A稿§2）；非负g保证剩余因子可按≤1删去。

令V=u1−u0、W=v1−v0。这两个变量独立且各有原π或其反射的slab upper。对λ≥qbase，事件|V|<λ可用一个坐标slab付CKπλ^γ；在|V|≥λ上，|V∧W|<λ²蕴含W落入法向V的宽λ slab，另付CKπλ^γ。故

    Pr(|det[V W]|<λ²)≤CKπλ^γ。

若CKπλ^γ≤m^16/4，删退化角后仍有≥3m^16/4 box质量。若还需删六对time碰撞，取b≥d、CKt b≤m^16/4，则余质量≥m^16/2。这里存在合法λ、b是显式预算条件；实际任意小source损失层级可使qbase、d低于所选小幂。不能在不满足条件的任意有限图上断言横截box存在。

对每个保留box，每个(i,j,k,l)都有实际输出y_ijkl∈A，误差e_ijkl≤E₀且

    y_ijkl=a+L_tisj(vl−uk)+e_ijkl。

同一time-edge的三个输出给

    [y_ij00−y_ij10, y_ij01−y_ij00]
        = L_tisj [V W]+O(E₀)。

H有固定bound，det[V W]≥λ²，所以逆矩阵norm≤Cλ^-2，恢复L_tisj的误差≤CE₀λ^-2；若再除time-gap恢复secant，另付b^-1。横/纵blocks分别恢复(ti−sj)I与−(M(ti)−M(sj))。四条time-edge保同一个角basis；angle parallelogram和time C4均在O(E₀)误差内真实成立。

该证明付了原g上共同base/time/multiple-angle的有限质量，不能再说提取完全未付。但它只说明十六个各从a出发的输出在A；未说明其中一个输出又能支持下一个L或shear的密作用。任意固定大小box可由CS取得，不等于一个可随尺度迭代的Cartesian action域。

## 3. 自然线性化为何不满足现有作用增长假设

在t≠s时令S_ts=(M(t)−M(s))/(t−s)。图向量为(z,−S_ts z)，自然shear

    T_S(x,ξ)=(x,ξ−Sx),  T_S=[[I,0],[-S,I]]。

对所有S，V₀={0}×R²逐点固定，商R⁴/V₀上也作用恒等。故自然shear群的Jordan–Hölder constituents全是平凡作用。即使S遍历全部Mat2,2，He–de Saxcé的相应nontrivial-constituent假设也不成立；He的irreducible-linear-map形式同样被共同不变V₀阻断。这个失败是表示本身的结构事实，不能由whole-M nonaffine或OBS001 plane cap消除。A稿逐项对照原定理，未重新证明这些高级源。

加入真实dilation可能改变商作用，但必须从原g提取实际operator×input密域及迭代闭包，不能先把任意dilation或free matrix algebra加入。作用定理可能有别的适配形式；本稿只冻结上述自然shear直接调用，未排除全部非线性/群论策略。

## 4. 平均真实carry门槛及责任边界

B稿完整证明：B≥B₀(γ)固定、N偶、r=B^-N，d≤r、qbase≤sqrt(r)。对固定j，X=frac(|t−s|)、Y=frac(|ψ_j|)，其标准非负base-B digits d_i,c_i满足

    Z= #{i≤N/2: d_i c_i≥B},
    Pr_{ν²×π}(Z≤γN/8)≤CKtKπ r^(γ/4)。

time N-prefix law被CKt倍uniform words支配；angle N/2-prefix各word质量≤CKπB^(-γN/2)。固定angle digit的time无overflow比例≤w(c)=min(1,2/c)，w(0)=1，Σw≤C logB。允许至多θN/2个例外，求和得[2B^θ ClogB/B^γ]^(N/2)，θ=γ/4即得结论。原g任意相关只付1/m；不是给条件angle law虚构独立digits。

每个d_i c_i≥B都在实际非负乘积raw coefficient第2i位迫向上carry，至少正比例位置必须overflow。故完全无carry或o(N) raw-overflow策略不能以任意小幂质量实现R27数字mask。这个结论没有从carry数量推出carry修正熵、输出card、可见纤维增长或M affine-fit；修正值可相关或相消。平衡符号digits等其它算法没有被本证明排除。

## 5. main结论与停止

两项新增有限门槛保真实原质量，内部审查后可存档，但均属初等有限结构补全，未做新颖性或重大性认证。仍无AFF₃、N_r(A)>r^-2固定增益、完整factorized反例或任何高维dimension新界。原source高级计数、四维175页proof仍未全面独审。

提前macro停止无新输入的observed/BSG/自然shear/仅carry数量局部迭代。重开须实际small-doubling/action闭包、可证carry-correction熵或其它不同source机制；不能再做box大小/常数改良。下一主任务转定量四维种子能否进入KT高维递推，详见notes/20_dimension_lifting/finite_seed_transfer/R0028_next_finite_seed_target.md。长期Goal保持active。
