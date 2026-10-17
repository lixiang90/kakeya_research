# R0052：来源定位与六点加权证书的独立精确核验

2026-10-17，A。已读固定恢复入口、registry78状态、本轮spec及R51完整来源分层。仅编辑本稿、独立verifier/输出与指定formal；无Git、无新代理、未执行远程notebook。目标是删除一个错误的固定算术候选，不是欧氏Kakeya反例、高维新界或重大成果。

## 1. 验收命题及这次实际取得的层次

R46全称候选要求对所有无挠交换群有限Z⊂G²，以N=|Z|、M=max_x|Z_x|、S_j分别为x+y、−x+y、y、x+3y的投影基数，有统一有限C满足 N≤C M^(1/3)(S₁S₂S₃)^(10/21)S₄^(5/21)。本轮允许的较弱且足够目标是同一有理jointlaw上的

    Δ=21H(A−B)−10[H(A)+H(B)+H(A+B)]−5H(A+2B)>0。

最终保存的是**独立构造的六点Q12加权law**、严格整数/有理区间及n240的有限阶乘证书；不是复现文献所报SDfour≥1.668。该law的强测试H(D)>(5/3)max_r H(C_r)事实上失败。两者严格分开，不因弱目标已足够就声称验证了强报告。

## 2. 官方数据入口与只读审查

实际打开[旧results repo](https://github.com/google-deepmind/alphaevolve_results)，其默认分支是main；旧master notebook链接不能当可用数据。实际web读取其10051行raw notebook，find未找到Kakeya/entropy/1.668；其中B.6是不同的和差集问题，不是本目标。随后实际打开[GGSWT配套repo](https://github.com/google-deepmind/alphaevolve_repository_of_problems)的experiments目录，定位两个相关notebook：

1. [arithmetic_kakeya.ipynb](https://raw.githubusercontent.com/google-deepmind/alphaevolve_repository_of_problems/main/experiments/arithmetic_kakeya/arithmetic_kakeya.ipynb)，root保存为 `literature/source_code/R0052_official_arithmetic_kakeya.ipynb`，5656字节。A独算SHA256为 `e7d2c2cdf86bb50da98cceb23358bf6c737b632880a24d75e71228790e19dbb5`。
2. [arithmetic_kakeya_conjecture.ipynb](https://raw.githubusercontent.com/google-deepmind/alphaevolve_repository_of_problems/main/experiments/arithmetic_kakeya_conjecture/arithmetic_kakeya_conjecture.ipynb)，root保存为同目录 `R0052_official_arithmetic_kakeya_conjecture.ipynb`，27270字节。A独算SHA256为 `59525c28704a5890c3e24f426a0179bb8e5aa0371896d203869b19f234a5cbb9`。

两个本地文件的全部11/6个source cells已实际读完，只作JSON解析，未exec、import或运行优化函数。root负责固定Git tree/blob/许可/metadata；A不把web访问当已核同一immutable bytes。

问题[30.html](https://raw.githubusercontent.com/google-deepmind/alphaevolve_repository_of_problems/main/problems/30.html)的静态可读页虽只显示空template，其raw HTML第198–215行的JavaScript `problemData`有完整statement和正确的第二notebook链接。故“静态解析空白”不等于原页面没有内容；只是页面本身仍未提供获1.668的概率表。

## 3. 为什么两个notebook不能充当strict四投影证书

小本cell6给未相关的离散Gaussian；cell10只查询0、1、2，遗漏∞，无保存的1.668表及严格误差。不能把这种示例的浮点score当本轮四controlled目标。

大本cell1 evaluator只处理A/B/一个额外slope，不是同时四controlled；`ensure_distinct_differences`把某difference纤维的质量移到最高权pair，这会改变其它marginals，不能免费拿变换前后熵拼接。其source含裸`) -> tuple[...]`语法残片，cell4又使用未定义的Gaussian helper，并把`best_joint_prob_xy`赋为scalar objective而非概率矩阵；这些是实际源码片段范围，不能按原样执行来获取合格表。最后markdown仅重复作者所报1.668，没有给对应的有限jointlaw。

这不反驳Tao/GGSWT的报告，也不认证完整notebook项目有误；只是本轮实际读到的这两个版本没有可直接验收的原强证书。本轮不无限搜索同一handle，不执行未审远程代码，而采用独立的较弱weighted反例。

## 4. 六点law与完全独立的聚合

保存输入为 `experiments/arithmetic/inputs/R0052_rational_counterlaw.json`，SHA256 `9cd70f44b310b15f353a09a829c340853cd14e2c16c1123c36af2360af6f4326`。六行(A,B,整数权)为

    (1,0,1),(0,0,2),(0,1,3),(−1,1,3),(−1,2,2),(−2,2,1)。

总权Q=12。A先手算、再用新程序从所有行的真实整数linear image排序，以`itertools.groupby`合并；未读/导入root的Counter聚合实现就完成首轮独立核算。得到：

| 变量 | 按值递增的整数权 |
| --- | --- |
| D=A−B，值−4,−3,−2,−1,0,1 | 1,2,3,3,2,1 |
| A，值−2,−1,0,1 | 1,5,5,1 |
| B，值0,1,2 | 3,6,3 |
| A+B，值0,1 | 6,6 |
| A+2B，值0,1,2,3 | 2,4,4,2 |

D在六行支持上单射。程序另外从变元x=B−A、y=A+B重新聚合四个原forms的**完整加权law**，与2B、2A、A+B、2(A+2B)逐项比较，避免只核基数而配错边际。全部通过。

## 5. 纯整数与可靠有理对数两条strict检查

独立verifier为 `experiments/arithmetic/R0052_independent_certificate_verify.py`，只用Python标准库。由输入count逐个素因数分解并合并加权指数，得到

    exp(12Δ)=5^100/(2^140·3^54)>1。

分子为7888609052210118054117285652827862296732064351090230047702789306640625，分母为81048904266647757416883177984820369473129355035761980948216119558144，直接整数比较严格大于，不借log浮点。

另独立给每个正整数m的自然log向外区间。写m=2^k(1+z)/(1−z)，0≤z<1/3；ln2使用z=1/3。取L=48项，

    log((1+z)/(1−z)) = 2Σ_(j=0)^(L−1) z^(2j+1)/(2j+1) + R，
    0≤R≤2z^(2L+1)/[(2L+1)(1−z²)]。

所有计算为精确Fraction；每个log再向外取整到10^(−48)格，然后按 H(C)=lnQ−Σc ln c/Q 及正负系数反向组合端点。最终自然log单位的Δ位于

    [381510198078314233860016127054,
     381510198078314233860016127055] / 10^30。

下端严格正。强SD四个3HD−5HC中A、B、A+2B均为负，输出明确 `all_four_SD_gaps_strictly_positive=false`；不能隐去该结果来称复现1.668。

## 6. n240的另写阶乘核验与真实图责任

输入k=20，n=kQ=240。独立程序另写`math.factorial`与整除检查，直接求目标type数N及各边际type upper K。D在支持单射，所以联合type数等于D-type数，无需先删代表；x=−D逐坐标唯一确定行字，M=1。

独立结果严格为 N²¹>(K_A K_B K_(A+B))¹⁰K_(A+2B)⁵；左12011bits、右11971bits，并且左/右>2³⁹。左/右unsigned-big-endian SHA256分别为 `fa49b3a72221e8bacbac5700c7f5e9c89a8d8159a11be33f21cb1b08cf0d2cc9`、`557e1b5189d24f61cdacdff6ad2af057c4bba5e475eb9d7b8dd61be69d2434e6`。程序只用实际投影包含于边际type类的upper；没有免费假定两者相等。

本次有限计算不代替图实现。已另核B/root：每个D-type word可按difference位置分配joint计数；本例每个D值只有一个pair，甚至直接唯一填充。四原forms为2B、2A、A+B、2(A+2B)，乘2不改变整数向量基数。所有x/y/forms的单坐标绝对值≤6，base14整数编码的最高差位压倒全部低位，精确保N、M和四投影。一个strict C1 seed经笛卡尔幂再编码，排除固定G=Z上的任意统一C。这里没有角度、单位段、shading或Hausdorff转移。

## 7. 实际运行、反攻与停止

实际命令为：

    python -X utf8 experiments/arithmetic/R0052_independent_certificate_verify.py experiments/arithmetic/inputs/R0052_rational_counterlaw.json

输出仅写 `experiments/arithmetic/outputs/R0052_independent_verification.json`，保存输入/自身SHA、全部边际、有理端点、整数比和有限阶乘证书。程序严格拒绝非整数/非正权、重复支持、总权不符、变元law不符、entropy两种strict检查不符或给定k的有限C1失败。没有执行来源notebook、调用root聚合、运行旧网格或以采样替proof。

之后实际读取root代码及输出逐行对照：root用Counter与直接整数乘幂/阶乘，A用排序groupby+素因数指数+Fraction对数/另写factorial；输入和全部边际/精确数值一致。此次rerun仅为独立代码scope修订后的自身hash更新，没有新增数学搜索。

本轮已经达到“严格否定旧固定weighted候选”的验收，不是强SD报告的完整复现。接下来停止此算术候选，不改q/权重/更多slopes，不优化有限图规模；正式review需再实际全文审root/B/macro/唯一next后完成。Goal active，未经外部同行评审，无major或新ordinary高维结果。
