# 当前研究交接

更新：2026-10-16（Asia/Shanghai）。最近轮次：R0002。长期Goal：active。尚未解决高维Kakeya，也未取得经文献确认的重大中间结果。

## 上轮分类与既成状态

R0001属于实质进展，已同步commit为 affe0b0770a8c25aec46025f9bcd785b4c5d86d3；本轮开始时工作树干净。文献库存6篇PDF、文本及关键输入源码；核心四维PDF及本轮06-isotropic.tex与官方Git blob精确匹配。请保留既有证明与失败索引，不重复搭建或下载。

## R0002的新信息

ALG-004给出五维局部直纹三次模型：
- q=u0*u3-u1*u2非退化，k=u0*u2-u1²，r=u0*k，f=S q+a r，ε=a/S。
- p(u,θ)=(1,θ,θ²,θ³-ε[u2-2θu1+θ²u0])沿自身线不变；f沿完整直线严格仿射，native Ps=w-Sq沿线严格二次。
- 同一base点任意四方向的行列式精确为Vandermonde；不再仅是孤立张量反例。
- 任意二次Q若在base体积σ的集合上|Q(u,f)|≤E，则|Qw(u,f)|≤Cσ^-24 E/a，|Qww|≤Cσ^-24 E/S²。a2精度拟合无法保留隐藏导数下界；带a2见证误差仍有矛盾。
- 对事前给定有限网格，可随后选ε足够小并删很少θ，使方向bin只依θ。空间流Jac=1，独立未归一化d-Frostman截距给(6.7)型joint upper cap。
- 这不等于全部任意细尺度的固定palette联合乘积domination；ρ≪ε时相关性会暴露。正球状angular cap仍可成立，不能混淆。

证明与独立审查见ALG-004、R0002局部模型、尺度接口及R0002_coupling_adversarial.md。脚本 python experiments/algebra/ruled_cubic_probe.py 已通过全参数符号验证，无浮点阈值。

## 禁止过度解释

模型尚未验证Def2.2全部条件、(6.6)同prior系数箱上下界、历史list、真实嵌套packets、positive horizon或临界最优化。Cantor测度本身不是Def2.2有限半代数先验，需有限层近似与floor审计。没有完整Theorem6.1推广反例，更不是Kakeya反例。

冻结仅靠native耦合、真实长线、非退化q及一份预定网格upper cap的次数恢复。不得改写成“再多选方向”“再细一点”或只计算16点样例来重启，除非增加真实新输入。

## 下一轮唯一优先任务：N5-SCALE-02

审计原始guards能否使共同方向网格细到a2/S0，重点读Def2.2、Theorem2.17及§4.2–4.3的原始排除/窗口预算。

可检验目标：真实临界路径上是否有固定C，使 S0/a≤N^C，N=N0^ε_n，C不依赖n、N0、ε_n？若不能，明确哪些额外条件排除ALG-004，并证明不等式或核验反模型。

只知道S0绝对有界不等于比值受控；仅有N0^M上界会变成N^(M/ε_n)，也不是固定切线幂界。不能以局部upper caps代替真实临界路径。

验收：非循环的统一幅度/精度引理，或严格定位未控接口并验证至少一项此前未查的完整模型条件。两轮没有新增约束则冻结并转向全方向输入的多项式非集中/flag分支。

## 既有边界与操作

- 四维核心证明及plank输入未全面独立验证；依赖它的维数结论注明条件。
- GWZ v1/v2分开；投影下界4已在原文11.2，六维旧KT下界超过4。
- base R4五方向cubic2copy单射成立；n>=6的Hankel反例不能套到五维。
- 系统python有SymPy1.14.0。旧代数脚本无需无故重跑。
- Git CLI网络失败时用已连接GitHub API。只上传变化blob，保留既有文献对象和远端父提交；同一commit校验导入后fast-forward本地。

本轮回执在tmp/sync/R0002.json；读取Git refs确认同步。R0003结束须固定宏观审视；本轮局部方案失败已提前审视，见research/reviews/R0002_macro.md。
