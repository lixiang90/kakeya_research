# 当前研究交接

更新：2026-10-16（Asia/Shanghai）。最近轮次：R0005。长期Goal：active。尚未解决高维Kakeya，也未取得经文献确认的重大中间结果。

## 宏观状态与恢复入口

R0004已同步0ff8d7ee7fbd130fb857714a7cc679ce4fd71108；R0005开轮工作树干净。本轮N5-ENT-01得到真实mixed-scale entropy rate，但无损传回原始W的通用桥接被明确d<1模型否定，已提前宏观审视：research/reviews/R0005_macro.md。

文献库6篇PDF、文本与关键源码保持；本轮无新下载。核心四维PDF与06-isotropic.tex已核对官方blob，但175页证明与外部plank输入未全面独立验证。不重复搭建、旧实验或已冻结等价写法。

## R0005实质结果

- ENT-002：固定同一parent-native world、同一ν°与嵌套网格，源码247–248的混合尺度cap ν°(A_p,C_r)≤Kp^j r^d π(V_p)，加fine participating floor，给H(C_p|C_r,A_p)≤dlog(r/p)+2logK。A=(y0,V)，C=(x0,x1,x2)。
- 同一概率律P≤Dν°、两端均参与时，总条件熵为dlog(1/p)+O(logK+logD+logR_y)，且I(C_r;A_p|A_r)≤logD+5logK+c_y。下界用正的velocity-reference KL，不要求affine边缘lower。参与支持及选择分母不可省略；完整ν°的非参与部分另付显式bad质量误差。
- NAT-001：P_*=w−StY3，V3=−e2/S、W=Sy03+e1、X=c+e1t+e2t²，c有限d-Cantor。full8有限半代数prior、真实d<1 profile、同prior(6.6)/(6.9)与fulltime trueatlas可同时成立。
- 同一最细native B_p内y03仍均匀，W_p最大原子≤1/S，所以L-list成功≤L/S、H(W_p|B_p)≥logS。需旧affine精度p/S。exact current Y3又恢复W至O(η)，显示遗漏的point互信息可达logS。
- 该反模型H=0有直接atlas证明，full raw slope density约η^-1，不保初始subpower来源；不是positive-horizon/critical/Kakeya反例。
- 同坐标bounded-W与affine cap给新几何界：对P_*=αw−β(tY3−Y1Y2)，目标prior质量≤C_R A_aff[p+(|α|M_W+M_x)/|β|]。必须核对同一坐标、同prior、0<p≤1和实际tuple；只覆盖此类shear，不是任意native全分类。
- KT2001对照确认：两时刻恢复本身只等同(y0,V)信息，改进需跨轨道重合。另一full-slope toy虽有参数d<1、mixed cap，真实profile却为d=1并缺strict physical support，不能当完整反例。

内部独立审查见R0005_entropy_rate_review.md、R0005_native_mass_review.md、R0005_native_review.md。native_entropy_probe.py精确恒等式与finite-bin计数已通过。无新改动不重跑。

## 当前冻结与真实缺口

G的“native熵率直接无损恢复W”版本冻结；正确ENT-002保留为工具。重开须有正horizon/真实source结构控制逆映射或point信息，或把NAT-001质量界闭合到实际归一化层。不能只给旧成本更换熵符号。

F小全局palette版本、朴素投影加一、native局部次数恢复、仅原始guards加细旧窗口均保持冻结。DIR-002真实floor预算仍有用，但既有Kh、branch f损失与source优化来源未闭合。

## 下一轮唯一优先任务：N5-FLAG-01

开轮先执行R0006固定宏观审视，再检验三维可见空间的真实两长一短flag几何；精读原稿10.2、2.13及narrowness优化。

具体目标：同一轨道在两个时刻的法向条带若独立，能否构造一长两短的fulltime known atlas，保留原始p_L列表、完整assignment质量、足够覆盖与可用floor，并在合法的flag/narrowness极值中给实际增益？

二维源稿两个非平行strip的交落小球；三维一般仍有一条长方向。只重述此线性代数障碍不算成功。须追踪第二短轴的宽度、外积/行列式预算、世界/时间权重和标签代价；det narrowness不等于每轴narrowness。

若投影丢短轴，必须计算hidden-test的敏感度及所丢标签数；NAT-001是必测反例，不能免费把短轴代入中心。已有full四维结论不自动给新投影的C(d)、native二次模型或列表。

验收：用于真实list/floor与原始质量的新几何引理，或满足被调用条件的严格反例；一个主轮只有“二维论证失效”则停止本版本并宏观重新选题。不把路线排除当长期Goal完成。

## 操作与边界

- 原稿version2 j=2；j=3是五维拟推广，几何准备与结构约化未证明。
- 初始raw full-slope来源不自动保留于对所有C(d)优化的maximizing sequences；跨世界须保留父标签。
- base R4五方向cubic2copy单射成立；ambient≥6 Hankel反例不能套到五维。
- 固定a=N^-s时真正统一绝对切线幂界足以控制S0/a；R0002过宽措辞已修正。
- 系统python有SymPy1.14.0，中文用python -X utf8。先读GOAL、STATE、ROADMAP、registry和最新轮次。
- R0005以R0004为父按PROTOCOL增量同步，核对完整tree、同一commit与干净树；回执tmp/sync/R0005.json。Git CLI网络不可用时用已连接GitHub API。
