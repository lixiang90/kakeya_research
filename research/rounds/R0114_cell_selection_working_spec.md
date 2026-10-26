# R0114 主 working：整δ格删选与实体载体初始化

2026-10-26，root。在macro_selection_spec的四出口审视及实际资格计算后锁本轮唯一主命题。rough grain候选已落原19.4更强cap闭包，反例/新finite输入尚无主幂；不以三角proper类续轮。本working是原平均shading类上的严格closure压力，不是新普通维数界、major或真实Kakeya反例。

## 精确命题与量词

固定n>=2、有界盒B、半开δ-grid及格式类H_{s,D}：每个H由至多s个实多项式（degree<=D）的符号作任意Boolean组合给出，s,D固定，系数不需有界。任意有限原真实单位δ管T_i⊂B，N<=Cδ^{−(n−1)}、原方向分离/全部角帽照旧，各自任意Lebesgue marks Y_i⊂T_i。记E=union Yi、f=Σ1Yi、I=∫f、λ=I/(Nδ^{n−1})>=δ^η，固定0<η<1。

对任意固定C>=1、0<θ<1，先选固定0<p<<θ/C，再对足够小δ证明：存在原multiplicity dyadic层A⊂E以及同一union of wholeδ-cells的mask M，使Y_i'=Yi∩A∩M满足

    I' >= c p I/(1+logN),
    |E'| <= 2p|A| <= 2p|E|,
    对所有H∈H_{s,D}、|H|<=C|E'|，∫_H Σ1Yi' <= θ I'。

绝不声每管保量；原N、axes、directions、clock不变，平均λ'按原N收费。若原E另有smallfootprint upper，此合法删选继续保该upper，属条件closure压力；没有在未解范围构造一个实际smallfootprint原族。

## 必须支付的证明链

先对任意非负g∈L1(B)、cell质量w_j证明uniform absolute discrepancy：E_ξ sup_H |∫g1_H(1_M−p)| <= C_{s,D,n} sqrt[(Σw_j²) log(2K)]，K为B中grid格数。每cell内按g/w_j取独立U_j，Jensen上界为conditional finite signpatterns随机和；格式给K^{O(s binom(n+D,n))}个patterns。需要给出该计数/最大值界，不借boundary-cell Oδ误差、不声任意小H的相对均匀。

dyadic层a<=f<2a上，用同一随机mask同时控制g=f1A及g=1A；小cell质量<=2aδ^n使相对误差r<=C sqrt(δ^n logK/|A|)。原|A|>=I/[2N(1+logN)]，λ>=δ^η使r→0。再由f<=2a和|H|约束得carrier质量比例<=4Cp+2r/p。

## 闭包与独立攻击

整cell mask对原cell-shading保持该性质，对任意measurable marks原样相交；但multiplicity层本身在非cell模型无需是格并，不能冒δ-cell regularity。几何wholeaxis containment和PW上界继承只是原几何事实，不由本命题变假。逐管density只对mask本身另可核，layer+mask仅保总量。一般q/p删选仍λ_new=(p_I/q)λ。

反攻须检查：uncountable H的sup可测性/稠密类或outer expectation；真实一份mask而非按H重选；同一原I分母；对C(λ')或C随δ增长的carrier不能用fixedC结论免费否；HV不授PW或原fixed-format轴carrier错误。若只证subδmask，或只证cell-boundary误差太大，停止/修正，不放宽目标。

## 停止与验收

完成此精确命题的自含证明、独立逐步审查和作用边界后停止。新source2609.06556v1仅作互补公式核验，主定理真假不得由literal输运失败决定。无普通高维新界不完成Goal；下一回完整原对象机制，不续本随机mask的p/degree参数作为主路线。
