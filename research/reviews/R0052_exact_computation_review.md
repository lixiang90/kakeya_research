# R0052正式独审：精确计算、有限type图与范围

2026-10-17，A。实际全文读root《R0052_six_point_exact_refutation_of_R46》8节、B type稿最终9节、macro6节、next6节、本轮spec及A source稿7节；另逐行读root程序/输出和自己的全部独立程序/输出。A的自身实现不算自身独立审查，root/B另有实读；本review独立核root的计算与B的图/tensor论证。未执行来源notebook，不认证尚未整合的metadata/registry/Git。

**结论：六点Q12的严格weighted反例、n240有限整数证书及排除任意统一C的图/编码/tensor链通过，可按原scope归档。该law没有复现SDfour≥1.668，也不满足更强的四个SD>5/3测试；不产生欧氏Kakeya反例、高维新界或重大成果。未经外部同行评审。**

## 1. 来源分层与独立性

本轮A实际全读两个官方notebook的全部source cells。旧results repo默认main且不是GGSWT算术数据；真正配套repo的两个small notebooks已由root保存字节，A独算SHA与root一致。小本漏∞且无获1.668表，大本含不同的三controlled evaluator、改变边际的difference修正和不完整的代码片段，最终只是报告。problem30的raw HTML包含JS `problemData`及正确Colab URL，静态文本空白不能当没有statement。

因此root将“强报告仍未复现”与“独立六点weighted反例已经证明”分开，正确。六点law的来历已标为B手推自然整数权，七点浮点探索未作证明，来源代码未运行。没有伪称复现原作者的表，也不据notebook缺表反驳其论文报告。

## 2. 原jointlaw、五个边际及strict熵差

A在读取root聚合实现前已用排序groupby独立重算输入六行，Q=12；D/A/B/A+B/A+2B的counts分别为(1,2,3,3,2,1)、(1,5,5,1)、(3,6,3)、(6,6)、(2,4,4,2)。D在原支持单射。程序还重新聚合x=B−A、y=A+B之后四forms的全部加权law，与2B/2A/A+B/2(A+2B)精确一致，未将π₂或目标entropy配错。

独立从counts素因数分解得exp(12Δ)=5^100/(2^140·3^54)>1，与root直接乘幂结果一致。另用纯Fraction 48项atanh级数及正尾上界，向外格化每个log后组合，得自然log的Δ∈[381510198078314233860016127054,381510198078314233860016127055]/10^30。上下界没有依赖二进制浮点或非有向Decimal；负系数组合已交换上下端。

强测试输出中只有A+B通过3HD>5HC，其余三个失败；尤其A+2B对应2^40/3^42<1。root/B/macro据此明确仅反特定weighted候选，不将其升级为更强SD证书，范围通过。

## 3. n240的实际有限计算及代码审查

root用Counter/整数乘幂/阶乘；独立程序不导入root，以排序groupby、独立素因数汇总、Fraction对数及另写factorial计算。输入SHA均为9cd70f44b310b15f353a09a829c340853cd14e2c16c1123c36af2360af6f4326；所有边际、N及四个K的完整整数逐项相符。

对k=20、n=240，独立严格计算N²¹>(K_AK_BK_(A+B))¹⁰K_(A+2B)⁵，左12011bits、右11971bits，且比值>2³⁹。这里N来自D-type/联合type的一一对应，K只用作实际投影的安全upper。没有由upper推N lower、没有虚称K就是实际投影数，也不需要枚举巨大字集。

root代码已检查每行整数正权/不同支持、Q、D单射、multinomial整除和strict有限比较；其simple ratio由实际products再次比较，非只打印预设常数。A实现额外reject重复支持/变元law失配并保存各边际和strict interval。最终.py/.md/.json均LF，独立输出的verifier/input SHA已对最终源bytes回查相符；本项核字节不等于认证Git staged/remote。

## 4. B的完整type、有效误差与整数图

独核B一般版：按difference值逐位置分配joint计数，恰覆盖全部D-type words；每目标字留一pair后x=−D给M1。四forms如§2，marginaltype仅用upper。一般显式误差由积分界jlogj−j+1≤log(j!)≤jlogj−j+1+logj推出logN≥nHD−s(1+logn)，而logK_r≤nHC_r。故nΔ−21s(1+logn)的下界及k≥(84s/g)²/Q的有效选择正确。

最终B新增的解析备份也已读并独算：5^100−2^140·3^58给其所列正整数；比值>81、e<3迫Δ>1/3。e>8/3与8⁹>4800·3⁹给log4800<9，n4800时误差余量>340，成立。这是独立备份，不取代较小n240的exact证书，也未开启最小长度优化。

本实例D支持已单射，因此不需删代表，全部jointtype直接为M1图。单坐标x/y/全部forms的abs≤6，base14最高非零差位压倒低位总和12(14^h−1)/13，负digit无漏洞。编码与整数forms交换，保所有等值类、N和M；并未声称保几何尺度或angular rank。

## 5. 任意统一C、闭包与停止

一个strict C1 seed确不能单独反任意C；root/B均用Cartesian t次幂，使N、Sj准确乘幂、M仍1，再在长度240t用同一base14编码回Z²。其比值r^t无界，排除固定G=Z上任一有限统一C，原命题量词被完整击中。不是只反sharp常数或仅给概率不等式。

本构造从全部type字直接计数，无restriction保N的偷换。几何平均/逐管shading均未被推出。root/macro停止R46的q/权重/近邻slopes、保旧655350有限枚举在其覆盖范围内正确、不增同义ID/major，恰当。长期Goal仍未解决。

## 6. 唯一后继的范围审查

已全文读next最终6节，含§3新增fiber-integral拟证机制。Q3明确仅regular exact-contained R4 quadric单位直线、原physical方向bin权α、任意平均λ，目标δ^ε λ³δ³W/α；真实3D任意密度输入与旧nearfull种子的强弱分明。超平面Fubini校准的额外δ因子与n4管体积归一方向一致；非平面quadric的whole-line分类、normal/kernel双横截、全部direction charts/奇direction、纤维厚度及原质量均列作待证，不是已获得。

next同时明确exact contained不同于R5实际近切variety，regularity不可免费删奇点，phase光滑也不能自动用3D companion§11；尚无保原方向/质量的通用quadric嵌入。它要求先判旧闭包/等价，一主轮无新信息即停，未自动解冻整个HRZ/旧matrix或许诺n5增益。本review只通过其具体可检验量词和停止范围，不预认证Q3可行、独立新颖或任何高维桥。root可完成本轮统一归档；无待补的本轮计算/有限反例数学缺口。
