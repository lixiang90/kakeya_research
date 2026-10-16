# FLAG-002：外积目标夹逼与复合奇异子空间对齐

R0006；证明：`notes/70_flags/R0006_flag_objective.md`；独审：`research/reviews/R0006_exterior_flag_review.md`。初等条件工具，不声称新颖性，未外部同行评审。

归一化形状A=D/q中v(A)=−log_N|detA|精确可加，b_k(A)=−log_N||∧^kA||超可加。固定有限网格，若所有段有同一线性率的下界且总段有相配上界，则累计节点及连续块成本夹逼到该线性率，总拼接缺陷由全部误差之和控制。不能把超可加误写为可加。

若r=σ_{k+1}(A)/σ_k(A)<1且||∧^k(AB)||≥ρ||∧^kA||||∧^kB||，实际top-k左奇异plane的最大principal angle满足sinθ≤r/ρ。证明直接投影到∧^kA的top左奇异向量之正交补，无需把相对B-plane的像认作实际复合plane。

j=3且最大轴full时，节点体积率ℓ、外积率µ满足0≤µ≤ℓ/2；各谱隙分支可条件性区分稳定长轴、短法向或完整flag。真实Kakeya路径的同步二级极值、类闭合、共同列表及质量输入均未建立，故没有推出j=3 critical path或高维结构定理。
