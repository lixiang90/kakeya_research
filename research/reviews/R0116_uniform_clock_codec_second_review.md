# R0116：uniform全clock codec的第二份独立逐步审查

2026-10-26，new_projection_gate。实际先读 `research/rounds/R0116_uniform_clock_codec_working_spec.md`；主稿落盘后实际全文读 `notes/50_counterexamples/R0116_actual_direction_construction_gate.md` 九节，再读回末三节并fresh核SHA256。随后作者补§8的dense像inf未达到处理，本人又实际全文读最终九节并fresh核下列最终SHA256。未参与该codec机制提出或证明施工；此前本人Li文献接口稿与此机制不同。不改作者文件/controls/Git。

本次审查的主稿SHA256为：

    b044a044e23e32bcb32c2b383964cfd40dff1fd3d0a4118b857a0f5cbc31f331

此前实际审过的raw hash为33a257aa73e1c334cd89f4a0911902514bae51d19ab7497479b7ff7b1c59037e；本通过结论以已实读的上述最终版为准。

**结论：锁定量词下全部证明与范围通过，未发现必修数学缺口。** 这是uniform intertwining的有限certificate障碍，不是ordinary Kakeya维数结果、完整source排除或major，未经外部同行评审。以下核查针对实际主稿，不以working预推导代替实读。

## 1. 定义、有限tuple与odd p下界

Z_p确为p-adic整数环。−1、2对全部p合法；odd p时2是unit，所以1/2∈Z_p，p2则无此元素。主稿T₁=(a,b,t)=(0,−1,−1)的输入为1，实RHS为c(−1)²；T₂=(1,0,−1)的输入为2，RHS为1−c(−1)。两式都没有交换tuple坐标顺序。

令q=c(−1)、r=c(2)，当0≤ε<1且所有defects≤ε时，range与端点给

    q≥sqrt(1−ε)≥1−ε,
    r≤1−q+ε≤2ε.

odd p的T₃=(0,1/2,2)输入为1，给1≤r c(1/2)+ε≤r+ε≤3ε。因此ε≥1/3。所用三个tuple完全在域内，未借可测性/连续性、field embedding或加法同态。

若ε≥1，所求lower已平凡；若sup不达到，任取ε>D(c)且在非平凡范围内应用再下降即可。D(c)本身有限，因为两端皆在[0,1]。这些论证也适用于每个δ另选的任意函数，没有先取极限函数的隐含前提。

## 2. p2的range门及exact parity全tuple核

每个even z∈Z₂唯一写成2b，b∈Z₂；每个odd z写成1+2b，b∈Z₂。主稿的T_even=(0,b,2)及T_odd=(−1,b,2)分别确有这些输入，后者的实RHS为(1−r)q+r c(b)。因此

    c(2b)≤r+ε≤3ε,
    c(1+2b)≥q−r−ε≥1−4ε.

第二式用(1−r)q≥q−r及c(b)≥0，方向正确。若有|c(z)−1/2|≤ζ<1/2，even与odd分别给ε≥(1/2−ζ)/3和ε≥(1/2−ζ)/4，统一lower与working一致。没有在p2用非法1/2时钟。

exact ε=0迫even值0、odd值1。唯一候选parity确满足**所有**a,b,t：t even时输入residue为a、real weights为(1,0)；t odd时输入residue为b、weights为(0,1)。输出只取0/1，因此mod2判断在这一步真给real等式。c(2)=0而c(1)+c(1)=2也确证它不是到R的unital ring homomorphism。主稿没有先把hyp误认成ring homomorphism而删掉合法例外。

## 3. 任意向量H的归约与三个误差

主稿任意d,n≥1，固定非塌陷P₀,Q₀及D₀=||H(Q₀)−H(P₀)||>0。v为该**real输出差**的单位向量，L(a)=P₀+a(Q₀−P₀)合法落在Z_p^d，不需要Q₀−P₀有unit坐标，也不需要L覆盖整个ambient。

从原全称向量式在(P₀,Q₀,a)处得到|h(a)−c(a)|≤e；这使用投影norm≤1及除以同一D₀。h可以落在[−e,1+e]，**不要求h本身在[0,1]**；scalar定理最终应用于c。实际主稿正是这样使用。

再次在(L(a),L(b),t)使用原uniform-all-pairs假设，p-adic恒等式

    (1−t)L(a)+tL(b)=L((1−t)a+t b)

精确成立。投影后的中间误差≤e；将左h改成c损≤e，将右两h改成c因非负权重和为1仅再损≤e，故D(c)≤3e。不是四个误差，也没有把一般h的range作为额外hyp。

所以odd p的e≥1/9和p2 midclock时e≥(1/2−ζ)/12均正确。H任意非coordinatewise、非连续、不可测亦不影响有限运算；按tuple改clock或只在固定端点pair上有近似则不满足所用hyp。D₀是固定pair的归一尺度，不按tuple变化，缩小全部输出不会绕过相对下界。

exact parity下只依模2 residue vector的任意finite-image H确能满足向量式：输入residue随t的parity选P或Q，real系数也作同一选择。此为合法反攻校准，不是完整H分类；主稿没有误称它供应正长度实线段。constant H塌陷例也说明D₀>0必要。

## 4. 连续compact full-clock校准确成立

主稿M_p(x)将x的唯一p-adic digits倒读为real base-p小数，c_p(t)=M_p(−t)。若x,x′同余mod p^k，则实tail差≤Σ_(j≥k)(p−1)p^{−j−1}=p^{−k}，故连续性成立。Z_p compact，输出在[0,1]；每个real y可选一个base-p展开，按同digits定义p-adic −t，遂满射。y=1使用全p−1，端点没有被漏掉；实展开不唯一无碍存在性。

−1的所有digits为p−1，故c_p(1)=1；c_p(0)=0；而c_p(−1)=M_p(1)=1/p。T₁真实误差1−p^{−2}≥3/4，与有限certificate一致。因此这是同一compact输入上的连续、normalized、满实clock而defect大的显式例，没有以非紧/端点失败替代主结论。

该例未造Euclidean Kakeya低维集合，主稿只用它区分clock满射与保直线关系，范围准确。

## 5. δ依赖、sup与actual稀疏关系的边界

每个δ可任意重选c_δ,H_δ，只要端点/range及原uniform inequalities逐δ成立，有限certificate就逐δ成立；不需收敛、可测选择或先取极限函数。像ζ_δ-dense且ζ_δ→0时，若distance inf不达到，最终§8先对任意ζ'>ζ_δ、ζ'<1/2选近似见证，再令ζ'下降到ζ_δ，正确返回同一下界。它也处理ζ_δ=0的dense非满像。p2下界趋近1/8，vector版本趋近1/24，均不可能为o(1)。这里只核锁定常数，不作最佳化。

结论控制sup，不控制average。有限tuple在Haar乘积测度下可为零测，删去它们或只保相关选线子族会失去certificate。主稿明确不反sparse actual Kakeya transfers、line-dependent codec或其它多尺度方法；也没有从一条line的两端近似赠所有line内部anchors的hyp。

此处未产生真实Euclidean T/marks，因而不可能仅凭数值defect lower读出原volume或Hausdorff。主稿保管q/保I比例p的λ'=(p/q)λ是未来应用的另项责任，未声当前codec theorem已付平均/逐管密度。

## 6. 旧闭包、验收与最终版本

另实际定向读R92主稿的原真实管、短整数代表、Haar density、weighted mod采样和precision ceiling。R92的hyp是一个共同Euclidean h格/完整finite orbit的具体转移，其必要precision与direction预算不要求本稿单一c保全部Z_p affine tuples。当前有限certificate也没有反向构造R92原T/方向/marks。因此不是把R92全称statement统一重调用后重名，但两者都只是所列接口的资格门，不是新的general Kakeya理论。

working要求的exact分类、定量scalar certificate、非coordinatewise向量归约和compact full-clock显式校准全部实付，范围无越权。未发现必修项。作者的dense-inf补充已实际全文读回，最终hash与root冻结版一致，审查通过；本结论不预认证未来版本或Git。

本审查不认证新颖性/最优常数或外部同行评审，不改变长期Goal完成门槛。主稿达到本轮有限资格任务的内部审查标准，ordinary/完整source正gain仍为零。
