# 四维稿的部分原始源码

归档日期：2026-10-16。作者：OpenAI。稿名：*Every Four-Dimensional Kakeya Set Has Full Hausdorff Dimension*，2026-09-24。

本目录保存本轮精读的 `build/sections/06-isotropic.tex` 原文，用于核对§6的公式、共同方向误差和次数恢复。这里只是部分源码，不是完整、可独立编译的LaTeX项目；完整PDF另存于 `literature/primary/openai_2026_four_dimensional_kakeya.pdf`。

- [原仓库文件](https://github.com/openai/math/blob/main/preprints/Every-four-dimensional-Kakeya-set-has-full-Hausdorff-dimension-September-24-2026/build/sections/06-isotropic.tex)
- [不可变Git blob](https://api.github.com/repos/openai/math/git/blobs/9ca69ce86ca1b4c4dd5eea7f879dcd74f8412d29)
- Git blob SHA-1：`9ca69ce86ca1b4c4dd5eea7f879dcd74f8412d29`
- UTF-8，86878字节；由GitHub connector读取，内容未改写，已验证本地 `git hash-object` 与官方blob一致。

原仓库许可见 [LICENSE](https://github.com/openai/math/blob/main/LICENSE)。审计见 `notes/10_source_audit/R0002_尺度与共同方向接口.md`；归档不代表完整证明已审计。


R0036补入两个官方源文件，均通过本地git hash-object与官方Gitblob及bytes逐一比对：

- 07-finite-narrowness.tex：77895 bytes，Gitblob 2d2367cb50b9136dbc810dd5d64f5b13c84a3ebe，SHA256 e0b7915fcdfab73c800aa40837659682e13ac1dbbfde540b64a1512e9aa96e69；[原文件](https://github.com/openai/math/blob/main/preprints/Every-four-dimensional-Kakeya-set-has-full-Hausdorff-dimension-September-24-2026/build/sections/07-finite-narrowness.tex)。本轮只读/审其Theorem8.2；其余positivefinite分支仍未认证。
- 09-unbounded-narrowness.tex：54169 bytes，Gitblob b620f35d37507fae84860d27b5c1623cd212f8a5，SHA256 02e6e98f25c5945fa2af0b46b5a123034d5ab357abeba9b4ec0ba3ccddcf397b；[原文件](https://github.com/openai/math/blob/main/preprints/Every-four-dimensional-Kakeya-set-has-full-Hausdorff-dimension-September-24-2026/build/sections/09-unbounded-narrowness.tex)。对应PDF§10；章节文件编号与PDF节号相差1，不能混用。

当前目录仍是部分源码，不是完整可编译项目。原PDF身份复核仍同上述OAI4版本；取回源码不证明其数学正确，完整read/audit范围见metadata/R0036_source_check.json。
