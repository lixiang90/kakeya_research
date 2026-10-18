# R0090：原point-star的polar补全与超平面端点闭包

2026-10-18，root。完整κ1/ordinary目标未证未否。新的超平面文献引出一个可付的原法向转换，但在实际可接的端点被二点计数复得；按排重门拒作新gain方向。以下实际原质量证明、范围和反攻待两份全文独审，未经外部同行评审。

## 1. 完整原任务与本轮资格结论

取原Wang–Zakharov Def17.2–17.4的bounded d5/k=ell3/κ1配置，不添新假设：whole T joint4-AD/CW，Z近满δ-time，Y_t为1-AD，X_(y,t)近满二维，原point的selected ξ和Φ为1-AD/slab并有coarse coherence。令K≥δ^-η吸收全部原小幂，L=1+log(1/δ)。原N在[K^-Cδ^-4,K^Cδ^-4]。

本轮原待接结论是从这个完整配置取得矛盾/真实branch saving，继而仍须ordinary桥；没有得到。阶段I先拒直接line→hyperplane和随point改offset法，再实际做polar补全，发现其正向端点是旧二点闭包，故不锁phaseII新gain，不把已知应用当major或新数学ID。

## 2. 新primary的准确输入和直接编码失败

Csörnyei–Stull2609.38742v1 Th1.1：point cubes相对t-Frostman，每point有同M个相对s-Frostman δ-hyperplanes相交，d−2<s≤d−1、0<t≤d；则全hyperplane族至少δ^[-min(t,(s+t−d+2)/2,1)+ε]M。原定义是dual参数网格，非带重数标签。root实际原PDF1–5、完整§4.1 physical18–21，view1/20；高级whole33页proof未本轮新独证。

R5原line在通常projective dual里是3-flat，不是hyperplane。H_(p,v)法向取v虽通过p，却沿unit clock产生δ^-1种offset，未付输出upper。此失败不排别的编码。下面采用**包含同一原axis的全部超平面**，保同一个全局集合；所需逐star法向law将由原Φ证明，不以假设赠送。

## 3. 原点集的relative4-Frostman与原访问账

原E_t={(x,y+F_tx,t):y∈Y_t,x∈X_(y,t)}。每个固定t，physical r-ball限制x至Cr-ball和native y至Cr-ball，F_t有界；故点数至多K^C(r/δ)^3。δ分离Z在r-interval内至多C(r/δ)个time，因此

    #E∩B_r≤K^C(r/δ)^4， |E|≥K^-Cδ^-4。                (1)

这里|E|表示有限点数，不是Lebesgue体积。下界用#Z≥K^-1δ^-1、#Y_t≥K^-1δ^-1、每X≥K^-1δ^-2；原E为δ分离。若只沿source allowed coarse尺度记上界，取相邻上尺度≤Kr并在F_t漂移中付K^C亦够。由(1)得normalized relative4 upper，不从ordinary小Lebesgue union免费推出它。

每p按原Φ的δ-bin选一个真实witness T，方向v=(φ,ξ_p+F_tφ,1)归一。相同tube只可对应固定个相近φ-bin，原jointAD upper还控制同point/同direction bin重数为K^C。于是所选原tube-point访问I_*与δ^-1|E|相差K^C；若取固定比例points，至少保K^-C原访问。它不授删后每原tube保原nearfull shading，平均/逐管分母仍须另算。

## 4. 原1-AD方向经polar bands成为近满法向支持

对每p令μ_p为其实际witness方向的normalized counting law。bounded图坐标中φ→v为定量bi-Lipschitz，Oδ方向误差可吸入网格，故μ_p(B_r)≤K^C r，r≥δ。v最后坐标同号且离0，避免antipodal歧义。

以S4面积dw归一，设 f_p(w)=δ^-1∫1_{|w·v|≤cδ}dμ_p(v)。每条band面积≈δ，故∫f_p≈1。两band在S4的面积≤Cδ²/(|v∧v′|+δ)，由坐标旋转可直接看为两个线性薄条；近乎平行时上界退到Cδ。于是

    ∫f_p²≤C∬ (|v∧v′|+δ)^-1 dμ_p(v)dμ_p(v′)≤K^C L。   (2)

末步按dyadic角annuli用1-Fst，最细diagonal亦≤K^C。取A=C K^C L足大，∫f_p1_{f_p>A}≤A^-1∫f_p²≤一固定小常数；余支持Ω_p的面积≥c/A。故它占至少cδ^-4/A个normal δ-cells。

这是直接L2/Fubini证明，不是把filled X维数加到同一point的Φ上；不需Φ给s>3，不假generic star。仅critical κ1范围，不把(2)字面改成κ<1时的多尺度normal Frostman定理。

## 5. 同一个原axis超平面族、统一M与去重

对每原axis a_T+t v_T，定义polar超平面 w·z=w·a_T，w⊥v_T；在固定有限normal charts离散δ参数，并添固定相邻参数cells得到H^+。它完全由原T定义，不随访问p改axis/offset。若f_p(w)>0，选实际v_T使|w·v_T|≤cδ，投到v_T⊥得w′，|w−w′|≤Cδ。该H确包含原axis，且距p≤Cδ；有限邻cell padding确保source的δ-cube incidence。所有Oδ扰动的normal/offset去重只损固定数，不把同一H复制成独立标签。

在有限normal charts中取共同chart及固定比例point子族P，仍保(1)的K^C-Fst及K^-C原I_*。每point有至少cδ^-4/A个不同H^+参数bins，且可令其normal bins不同。统一取

    M= floor(cδ^-4/A)。                              (3)

由于所有H(Q)通过同Q的固定加厚，offset由normal及Q确定至Oδ；参数r-ball中至多C(r/δ)^4个这种bins。**任取**同M个不同normal bins便有relative4-Fst常数≤C/(Mδ4)≤CA。无需假随机或把weights复制成几何集合。有限chart、颜色和padding均固定，source的[0,1]^5参数/physical box可共同固定缩放处理，原δ只变常倍。

## 6. 新source给出的饱和端点与独立二点证明

接受Th1.1并先定ε后选原η足小，K^C L落在其δ^-η_CS阈值，d5/s=t4给 #H^+≳δ^-1+ε M。下面不用该定理，直接得同强度且保实际K/log。

两个point cubes Q,R距离r，在同bounded chart内，同时交它们的δH参数cells至多Cδ^-3/(r+δ)：normal δ-bins须落在相对Q−R的宽δ/(r+δ)薄带，offset每normal只有O1格。r≈δ时即Cδ^-4。由(1)的relative4 upper，对每p分annuli得到

    Σ_(p,q)∈P² (|p−q|+δ)^-1≤K^C|P|²。              (4)

diagonal项|P|/δ由|P|≥K^-Cδ^-4吸收。令d_H=# {Q:H∈H(Q)}，新PH边总数=|P|M，而

    Σ_H d_H²≤Cδ^-3 Σ_(p,q)(|p−q|+δ)^-1
              ≤K^Cδ^-3|P|²。

CS给

    #H^+≥cM²δ³/K^C≥cδ^-5/(K^C L²)。                (5)

因此本轮实际可接的超平面端点是初等二点/Fubini闭包，不需新primary的高级归纳输入；不能以换成hyperplane名注册新gain。这不否原Th1.1在别的指数区间的实质内容。

## 7. 原N/I没有因三个自由法向参数产生增益

单根unit axis的polar normals为S3，故fixed bounded chart中每原T只产生Oδ^-3个H^+；全局还受ambient五维参数上界。于是

    #H^+≤C min(δ^-5,Nδ^-3)，
    Σ_H # {T:H来自T的polar}≤CNδ^-3。                 (6)

原N≈K^Cδ^-4时，(5)与(6)相容。原selected tube-point访问约K^Cδ^-5，新PH访问约δ^-8/K^C；多出的δ^-3是补全的自由normal参数，不能当新的physical marks或小union矛盾。若从(5)的near-full H平均(6)，每H natural tube数上界仅K^Cδ^-2，不是调用原R4 full三参数方向网所需δ^-3。即使有很多H，也没付其内部direction cap、marks density、unit clock、真实体积和重计。

两点证明只用point和normal law，其本身不控制原T在同一个H内的分布。把‘有某个H承载足够好R4族’加作前提会把未付质量藏进成功输入。完整κ1源尚可能另有更强几何，但本接法没有得到。

## 8. 具体校准：full五维H不强迫三维tube纤维

只反(5)→每H高degree这一无附加推断，不反完整source。取v=(v1,…,v4)在固定小四维盒的δ网，a(v)=(v1²,…,v4²)，原axis为(x,t)=(a(v)+tv,t)，0≤t≤1。方向δ分离、joint参数为有界光滑四维graph。看hyperplane chart

    x1+b2 x2+b3 x3+b4 x4+c t=h。

包含axis等价c=−v1−b2v2−b3v3−b4v4，h=v1²+b2v2²+b3v3²+b4v4²。取b2近1，b3,b4近0，v1/v2在两个相距固定量的小interval，(v1,v2)→(c,h)的Jacobian=2b2(v1−v2)离0；另三个b是自由参数。故此chart的polarH有≈δ^-5 bins，而固定H后每(v3,v4)至多O1对(v1,v2)网格解，总tube数≤Cδ^-2。小盒内统一inverse-function/二次根数控制给这些离散upper/lower，不是数值猜测。

底层**连续v盒**的axis union在(v,t)→(a(v)+tv,t)的Jacobian ∏j(2vj+t)非零处含开集，故有正五维体积。对所用**有限δ网**，axes并本身测度零；对应roundδtube并仍有与δ无关的正体积下界。具体取固定内部t小区间，使各2vj+t在适当缩小的v盒上都离0，slice map v→a(v)+tv统一bi-Lipschitz；δ网image中δ-balls的重叠度为O1，N≈δ^-4使每slice四维体积≥c，沿该t区间积分即得。这没有构造原pointΦ1AD或critical E。它不是full κ1或Kakeya反例，也不否原source加全部条件后可能有别的高degree机制。它只校准所用H饱和计数单独不够。

## 9. 四完整路径、闭包和停止

ordinary仍缺原smallfootprint与jointADlower同时提取，directHRZ仍缺原parent/terminal/coarse全部费用，sticky临界及其余mixed和ordinary桥仍open，真反例仍须同一集合全方向和Hausdorff上界。DIM001/R38/R80已付链不重排；本轮新normal输入不是给ordinary任意star的免费规律。

whole-label/marks删选须分别重算N/I/CW/ADlower，平均不授逐管；本轮只在完整source原E上取chart点，没有自动生成新allowed配置。CP/PM/PW全称gain的旧双向正幂闭包不变。本次polar→新hyperplane端点→R4接法停止，不续κ、normal厚度、M、richH公设或更多补全模板；不宣所有hyperplane/双曲方法无用。无qualified下一gain，保守ordinary/fullbranch-saving streak13。

## 10. 文献、审查和结果层级

新Csörnyei–Stull原PDF33页/542683bytes，SHA256 99253cd4975331a8efec4f1e5bf89c1d1e2ce541525b040a04f47fbf6a803daa，blob0e411d67ede40709bc3083f61d217d317d91083d。root实际原Th/definitions和完整§4.1，B另实际§3.3/3.4及proof，A实际statement/definitions；全33页高级算法/距离集proof未新独证。wholebytes身份与数学正确性分开。

两份actual全文formal后有限范围才内部reviewed，非外部peer。预计66PDF/70sources/78IDs，无新实验/ID/ordinary新界/完整branch-saving/full方向反例/major。实际原质量转换和endpoint排重是资格信息，不降低完整Goal；Goal active。
