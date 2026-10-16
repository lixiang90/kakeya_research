# 当前研究交接

更新：2026-10-16（Asia/Shanghai）。最近轮次：R0004。长期Goal：active。尚未解决高维Kakeya，也未取得经文献确认的重大中间结果。

## 宏观状态与恢复入口

R0003已同步b9099d1dda00682746aa7e241b7d9b672daf7a62；R0004开轮工作树干净。前三轮宏观审视后，本轮按N5-POLY-CAP-01推进一次真实方向预算。结果有新约束，但现有阈值不能完成排除，已执行预定停止规则。

文献库含6篇PDF、抽取文本及关键源码。核心四维PDF与06-isotropic.tex已核对官方blob，但175页证明和外部plank输入没有全面独立验证。本轮无新下载。不要重复搭建、旧代数实验或已冻结的等价改写。

## R0004新增约束

- DIR-002：同一prior真实饱和νA≥n(b)JA/K，方向换元FA=DA/q，给νbad/νA≤K Cvis Φ/[n(b)q^j]。JA及全层父数量均可消去，world/time权重与完整assignment分母不变。
- 特殊v2−v1²薄层体积O(η)；一般归一化二次式仅有O(sqrtη)。不能错用特殊横向非退化。
- 原稿方向Hessian在固定potential及截距/core/sign分支后才确定；branch质量仅≥hνQ f/K，f=(a2/a)^d。固定支内全部仍计数轨道可由统一三阶界得到Kh方向薄层，但不得推广到无该见证的完整prior。
- 原稿现有η=Kh，含branch成本后即使乐观线性体积也仅给h^(1-ed)/(a^d h^j)，j≥2不衰减；sqrt版本更弱。只说明该界不闭合，不证明真实bad质量大。
- Cor4.4只给相对profile与nearzero节点；Cvis/n(0)小是额外输入。真实父归一化把同一成本转进Cvis,new≤K Cvis/[n(b)q^j]。初始full-slope来源不自动附于对全部C(d)优化的maximizing sequence。
- BND-001：完整原始斜率密度1、真实assignments、own-depth常数列表、逐chart真实floor及总覆盖1/32可并存，而全局方向二次式palette需η^-1个。严格是d=1边界，H未计算，非native-Hessian或critical认证。
- ENT-001：固定law、同一原始方向网格的KL/pointwise-list选择成本及共同palette似然界成立。已有祖先信息、稀疏选择、隐藏W条件信息不能省略。

内部独立审查见R0004_direction_entropy_review.md、R0004_source_review.md、R0004_boundary_entropy_review.md。known_floor_probe.py精确符号验证已通过；无新改动不重复运行。

## 路线冻结

F的“小pointwise列表/true floors直接恢复小全局palette”版本完成一次主轮并冻结。DIR-002保留作工具。重新开启须有真实新输入：更强方向非集中/更细可付阈值、有效全局匹配、或保留raw full-direction来源并闭合极值过程。不得仅换写Cvis/[nq^j]或祖先代价再延长。

旧投影加一、native耦合局部次数恢复、仅用原始guards加细旧熵窗口也保持冻结。R0002幅度措辞已纠正：固定a=N^-s时真正统一绝对切线幂界足以给S0/a固定幂；缺的是这种统一切线控制。

## 下一轮唯一优先任务：N5-ENT-01

在同一原始分辨率、固定prior和完整祖先记录下，检验原生系数熵率是否能与全斜率隐藏W信息结合给实际几何增益。

新输入：Def2.1明确X(t)=x0+x1 t+x2 t²的三个系数为subpower有界；(6.6)给同一ν°的长期系数箱上下界。先严格导出H((x0,x1,x2)_p | (y0)_p,V_p)的有限尺度界及选择损失，再核查从原生系数回到原始W所需的分辨率、分支与坐标条件数。

必须保留H(Wδ|Vδ)的原始下界、已有祖先标签成本和I(Wδ;point/history|Vδ)。原稿可见V窗口的小增量不控制这些项。固定旧native系数虽有小窗口信息，父native信号重置/除a可能要求更细旧bins，不能免费当作同精度传输。

验收：适用于d<1真实路径的新增熵率/几何质量不等式，或满足被调用条件的明确反模型。仅写链式法则、得到方向与截距相关性下界、或重述小增量不等于小总量，不算成功。核对KT2001原稿中已有熵方法。一个主轮无新输入即冻结该版本并转2长1短flag投影。

## 操作与边界

- 原稿version2的j=2；j=3为五维拟推广，结构约化及几何准备尚未证明。
- ALG-004是局部障碍，PRI-001是有限网格prior兼容；均非完整高维critical/Kakeya反例。
- base R4五方向cubic2copy单射成立；ambient≥6的Hankel反例不能套到五维。
- 系统python有SymPy1.14.0，输出中文用python -X utf8。优先读GOAL、STATE、ROADMAP、registry及最新轮次。
- R0004按PROTOCOL只上传变化blob，以R0003为父，核验完整tree和同一commit；回执tmp/sync/R0004.json。Git CLI网络不可用时走已连接GitHub API。
- 下一次固定宏观审视R0006，关键命题失败时提前；Goal完成标准不变。
