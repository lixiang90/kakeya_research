# R0083：直接直线并集输入的原量词核验

2026-10-18，root。先锁research/rounds/R0083_working_spec.md，再实际读新一手原文。root/A/B及两formal已实际全文cross，原量词应用与停止判定内部通过；不是新高维维数定理，未经外部同行评审。

## 1. 原对象和已失败步骤

固定n=6，C为canonical affine unoriented line space中的非空compact集，方向投影π:C→RP5满射，distinctwholelines不交。S(C)为真实整线并集。R81具名最小维归约可能给dim_H S(C)<5，尚未排该对象。R82只否local open angularchart的无假设正测度Holder升级；不能将其proper方向集或有内点union冒作C反例。本文不续该模型。

## 2. Compact fibre的实际可测选择与原角度law

π连续，C compact，每方向fibre非空compact。可给出Borel selector而不授连续性：在C逐层取有限闭球覆盖，半径趋0；对已选compact前缀K，用条件D∈π(K∩B_j)取最小j。各π(K∩B_j)compact，故分支事件Borel。嵌套非空compact的diam趋0，极限s(D)唯一、Borel，且π(s(D))=D。首层可用C本身，后层对每个compact前缀用有限更小球覆盖，保证非空选择覆盖其每个fibre。

令σ为RP5规范角度概率、ν=s_*σ。则π_*ν=σ。canonical metric |a−a'|+||P−P'||下π Lipschitz，line-space球B(q,r)投到角球O(r)，故ν(B(q,r))≤C r^5（0<r≤1）。这是真5-Frostman upper，不是ADlower、任意更高维指数、position与direction独立或Holder selector。正σ质量方向restriction只将upper乘σ(E)^−1；其像未必compact且未必fullD。闭restriction保compact/不交，fullD需另核，不能把两个闭包混同。

## 3. Zahl一手定理的精确强度

Zahl arxiv2208.02913v1官方history仅v1，8页原PDF和全文实际已读。其Oberlin结论：dim_H L≥2(d−1)+β，1≤d≤n整数、0≤β≤1，则dim_H∪L≥d+β。Th1.2是line-space球计数下的δ-tube Lp估计，p'=d+β，不是原方向自动给任意参数维数。§3把Hausdorff cover、analytic line family、Frostman measure、dyadic scale/contact和finite sampling接回集合维数；高级CV multilinear theorem仍具名，本文没有新独证全部来源。

有限计数的自然尺度为r≥δ；原文Th1.2/式3.7的all balls不能按r<δ、RHS<1理解成允许非空原子。§3sampling的简述也不是本轮新完整随机证明，特别不能把‘exponentially small’当所有r~δ的字面统一概率。原定理作为具名已发表输入保持，与这些简写范围的项目重证责任分开，不声称主定理反例。

## 4. 原C的实际输出与缺少的放大

方向Lipschitz满射给dim_H C≥5，可取d=3,β=1，只得dim_H S(C)≥4。n5仅dimC≥4时该定理给3。对n6，s∈[6,7]才可取d=4,β=s−6，输出s−2；要超过17/4须s>25/4，要到5须s≥7。不存在把5连续插值成6或用packing维10替Hausdorff维的授权。

17/4仍是本项目列明四维finite seed及KT等具名输入的既有条件链，不在此升级无条件新界。Zahl的当前4也没有超出旧baseline。KM的典型line-collection Hausdorff维n−1/packing维2n−2可按其真实具名Baire范围与R81 residual比较，但不能相加；不以该文intro说明冒本轮wholeproof新独证。原满方向或不交尚未给所缺参数维数提升，当前不造此desired theorem。

## 5. HKM主定理实际删掉什么

HKM arxiv2106.09661v3，实际26页。root全文读§2和完整§3（3.1、3.2，没有3.3小节），未读/独证完整§5–7高级证明。Cor2.13/3.2可对非vertical line chart的Borel union B删Borel Γ1-null G，B'=B\G满足dim B'=1+esssup dim B_t；每原line仅删零H1长度。clock基底R为AD1，不能据此给label族ADlower。

B原为compact线族的union，canonical offset有界，S(C)闭/σcompact；非vertical closed有界slopechart可用标准countable exhaustion，实际方向full及质量在chart选择时另记。Γ1-null对每条原line给a.e.clock，Tonelli也给ν×Leb原product零损，但不赠任何预先指定的finite/dyadic clocks、完整line、非退化segment或compact subfamily。

## 6. Γ删选不能当整族restriction

仅由Γ1-null性质无法推出整线闭包：G=B∩(Q×R5)是Borel且Γ1-null，每条非vertical line恰失countable clock；B\G没有一条完整非vertical line或非退化segment。这个例子不反HKM所保证的特别G存在，更不是原C或Kakeya反例，只严格核删除类型的责任。取闭包可回B却可能增Hausdorff维；不能把a.e.clock改成全clock后仍保同一维数。

平均product零损和逐line H1零损在这里均真，但finite time law可能全部集中Q，因此该连续结论不授任意原离散source的质量。要把它用于finite shadedtube或R81wholefamily，必须另证实际闭包和原质量接口。

## 7. HKM投影应用和仍是猜想的结论

Th3.6/Cor3.10的维数等式只在line-family dim≤1（或union<2）适用。原n6 C的任何正angularmass restriction仍有参数dim≥5，删成1维不能说保原质量。Th3.8+Cor3.4、Cor3.16在bounded affine slope-code X上给a.e.t sectiondim≥dimX/2，故s≥5只给union≥1+s/2≥7/2；没有新超过4或17/4的读出。

Conj3.11才是一般line union的完整Fubini等式；Th3.12是条件应用：固定m的该猜想给Kakeya Hausdorff≥m−1，所有m才给full upper Minkowski。不能把condition删掉，不能把upper Minkowski写Hausdorff full。其projective graph-at-infinity证明已实际全文读；它解释为何未证等式不能偷作免费输入，未证明对pairwise-disjoint C的特例已满足。

## 8. 正gain旧闭包、双向核验与结论范围

原C本身compact analytic，Zahl任意集合的analytic enlargement在这里不是新优势，也不会保不交或fullD；只用任意族下界时无须这些性质，但不能把其新label集合当R81 C。HKM结果正向是删除后的维数等式，反向只能从B'低维推出其自身维数，不能无费恢复whole B。更高Frostman、full line-extension invariance或一般Fubini正是未付新输入，不能以新名称开方向。

本轮有界directline输入门至此没有合格phaseII：已取得两项真实可用来源及其原scope，却无完整C的新增矛盾/ordinary增益。不是证明所有line-union方法不可能；按预先stop应立即完整四路径macro，不接第二轮同family abstract检索，不以本节初等闭包核验立新ID/major。

## 9. 独立审查和下一选择责任

A独核Zahl完整文本和原measure；B独核HKM§2/完整§3；root实际全文读两源上述范围并视觉核Zahl6–7/HKM6–10。A/B/root稿及两formal已实际全文逐步核过，不以source身份保证正确性。归档一致性脚本只检路径/字节/状态，不认证数学。

终macro需比较ordinary初始化、directHRZ、实际matrix/mixed和真fullcompact构造；没有新匹配输入即诚实记没有合格主命题，不把缺口改成假设收轮。旧CP/PM/PW4/BSG/更多anchors/endpoint/h模板保持冻结。完整Goal active，高维未解，未产生新维数界或重大结果。

本文关于Fubini的conjectural状态限定于所核HKMv3原文与本轮未获证明的依赖状态，不认证2022以后全球文献仍未解决该猜想。
