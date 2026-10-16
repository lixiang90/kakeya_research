# 每轮 GitHub 同步

授权目标：`https://github.com/lixiang90/kakeya_research`，默认分支 main。

1. 在提交前确认当前文件属于本项目，不上传凭据或无关个人文件。保留文献原始文件及来源信息。
2. 读取远端当前分支。既有历史必须保留；远端前进时先安全整合，禁止强制覆盖。
3. 本地暂存快照并建立Git tree。常规网络与凭据可用时创建commit并使用普通fast-forward push，比较本地和远端HEAD。
4. Git CLI不可用但已连接GitHub可写时，允许通过GitHub connector创建blob、tree、commit和ref。上传精确文件字节，保留远端父提交；读取返回的commit并验证树与本地快照一致。初始空仓库可通过contents API创建首个文件。非空仓库不得重新初始化历史。
5. Connector创建的commit若不是本地git所建commit，必须把远端commit对象取回或按API中的原始payload重建并校验SHA，再fast-forward本地分支；不得伪称两个不同SHA相同。
6. 全部文献及代码上传后读取远端分支和tree，逐文件比较blob SHA、路径及文件模式。校验成功才报告同步完成。
7. 回执写 `tmp/sync/<round>.json`（避免把commit回执写入该commit产生自引用）。含远端commit/tree、验证时间和每文件哈希。下一轮记录可引用上一轮SHA。

命令式同步失败和认证失败是可恢复的基础设施问题，不构成数学结论，不以上传日志代替研究进展。
