# R0011整合独审：实际可见方向有界仍有任意大horizon

2026-10-17。root复核两个独立代理的R0011主稿与接口稿；level-dependent shear最初由audit_four_dimensional提出，由lifting_obstructions独立确认。统一随机标签引理的作者是root，其R0010独立逐步审查仍见R0010_random_label_review.md及R0010模型稿§9；此处不将root对自己随机引理的复述充作独审。本轮两位代理另互审新模型。

## 新输入而非旧反例的改名

逐项展开新系数b=(s,−sq−λp/s,λ/s)，u=(p,αλ−pq,q)，得到tY₂+Y₁Y₃=λ(1+αt²)。固定α=1/10，因此exact(t,Y)在δ噪声后仍只定位O(1)个λ。另一方面，给定实际V，V₁,V₃分别定位O(1)个p,q，再由V₂定位O(1/α)个λ。每个三参数权≈δ³、速度noise density≈δ⁻³，所以f_V≤C/α，不依赖M,U,N₀。这是原概率分布的Lebesgue ceiling，不是bin cap或条件归一化。

这是相较HOR-002的实质差别：旧visible law的ceiling≈δ⁻¹，现在κ=0。λ被空间point定位与λ被速度定位可以同时成立；不能凭混合层数直接断言profile变d=1。

## 其余全部条件仍来自同一law

四参数λ,s,p,q均匀grid，每index权δ⁴；六visible系数δ噪声加w₀、W各η噪声给full8有限分段常density。用B₁,V₁,V₃,B₃依次定位四格点，重叠统一有限，故非仅低维推前law。piece数、noise倒尺度及density都是固定原始幂。tag表选择后是实常数，不属于重采样随机变量。

selected time I₀=[1/2,3/4]使t有固定正下界；exactY定位O(1)个λ后，每s只留O(1)个p,q。故g_t≤δ⁻¹δ⁴δ⁻³=C。η≪a_L使每exactY所有贡献的hidden bins共O(1)个，因此每depth G_r≤C且其reference support体积≤C。积分给µ{G_r<N₀⁻τ}≤CN₀⁻τ，实际f≡0。无须错误地要求support处处有pointwise lower。

ρ≥δ的angular计数把s缩到O(ρ/δ)格，给Cρ；ρ<δ的joint(Y,V) per-index densityδ⁻⁶乘原权δ⁴与ρ³，给Cδ⁻²ρ³≤Cρ。指定hidden bin只降低upper。可固定S=1和同一angular范围，cap参数取d=d₀=1/2。

## uniform lower的合法复用

在每λ内，新轨道只是旧轨道Y_old+αλt e₂。任意whole/short-block spatial fit向旧模型拉回时，center改为y_c−αλt e₂，D及J完全不变。旧cap对所有affine centers统一成立，所以原π_λ cap仍是CK³δ^(1/2)q⁻³J。混合g_t≤C另给global cap CK³J。

R0010随机引理不要求visible law与λ独立，只要求各Π_λ在选颜色之前固定、H⊂G且G不含颜色、固定维有界次数tests、tag对w的系数为1平移，以及上述两项cap。新模型全部满足；为新Π_λ重选一张forall-chart的好tag表，不沿用旧表。任意复杂assignment扩大为whole-fit/current-test事件后，未进入θ维数。得到同样

    m/q ≤ K^C[a_L+(log N₀)²δ^(1/2)q⁻³]J + N₀^(-ω(1)).

与同prior true floor及tempered J固定幂倒界比较，给q³≤N₀^o(1)δ^(1/2)，所以H≥M/6。进一步逆subpower incidence restriction保同prior domination、profile exponent及固定幂lower。没有调用DIR-003或四维主证明来证明此模型。

## 非空true atlas与边界

q=δ时，midY的δ-cube定位O(1)个λ，因而原w₀终端bin的pairs共O(δ⁻³)。删原质量<τδ³的pairs仅失Cτ；goodpair用D=CδI、P=w−c_C，whole fit、small value与Pw=1成立。其m/q≥τδ³匹配原n(L)J≈δ³。当前Y及当前hidden bin恢复mid-cube和w₀-bin的O(1)列表，不输出λ。因此H≤M、常量覆盖，真实系统非空。

W仍独立均匀于[η,2η]，完整(V,W) density ceiling≈η⁻¹=N₀^U。只证明了可见方向成本κ=0，并没有真实五维完整方向来源。故N5-DIR-COST-01的uniform有限常数不存在，甚至在实际可见density有界子类；形式j3的all-model k仍无限。原j2四维稿、欧氏Kakeya猜想均未被反驳，没有新维数界或重大中间结果认证。
