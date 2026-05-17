# 软件架构 (含 应用架构 / 系统架构 / 分布式 后端架构 / 前后端 数据流 与 数据模型 设计 / API 边界 / 可扩展性 / 演进式架构 — 不含 硬件架构 / 纯企业架构 / 纯 DevOps / 纯安全架构) CLI

把 软件架构 (含 应用架构 / 系统架构 / 分布式 后端架构 / 前后端 数据流 与 数据模型 设计 / API 边界 / 可扩展性 / 演进式架构 — 不含 硬件架构 / 纯企业架构 / 纯 DevOps / 纯安全架构) master skill 的认知 OS 物化成 bash 工具。
不替代 SKILL.md（思维顾问），是它的「执行端」：交互问询 → 应用 playbook / protocol → 输出结构化报告。

## 用法

所有脚本支持 `--help` / `--explain` / `--dry-run` / `--json` 四个标准 flag。

```bash
# 拿到新问题时, 按 N 个研究维度做功课
./protocol/agentic.sh

# 决策树评估 (基于 playbook)
./decision/topic-1.sh


# 看背后的心智模型 / playbook (不交互)
./protocol/agentic.sh --explain
```

## 脚本清单

| 脚本 | 作用 |
|------|------|
| `protocol/agentic.sh` | Agentic Protocol (7 维度) — 拿到新问题时按这一行的研究维度做功课 |
| `decision/topic-1.sh` | 架构 决策树 (1 条规则) |
| `decision/service.sh` | Service 决策树 (3 条规则) |
| `decision/adr.sh` | Adr 决策树 (4 条规则) |
| `decision/general-playbook.sh` | 通用 Playbook 决策树 (2 条规则) |

## 设计与生成

CLI 子树由 `tools/cli_writer.py` 自动从 `references/synthesis.md` (Section 2 Playbook + Section 9 Agentic Protocol) 和 `references/research/03-workflows.md` 生成。

完整 spec 在 master-skill 仓库 `references/cli-spec.md`。

## 重新生成

如果 synthesis.md 或 03-workflows.md 更新了, 重跑:

```bash
python3 <master-skill>/tools/cli_writer.py emit \
  --skill-dir <this-skill-dir> \
  --synthesis references/synthesis.md \
  --workflows references/research/03-workflows.md \
  --industry-cn "软件架构 (含 应用架构 / 系统架构 / 分布式 后端架构 / 前后端 数据流 与 数据模型 设计 / API 边界 / 可扩展性 / 演进式架构 — 不含 硬件架构 / 纯企业架构 / 纯 DevOps / 纯安全架构)"
```
