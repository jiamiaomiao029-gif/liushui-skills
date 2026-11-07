# liushui Skills | 首批可安装原型 V0.2

这是 liushui 系列的**前两个独立 Skill**：

- `skills/liushui-persona/`：人设考古，从授权的历史记录或对话中找人物行为模式和事件证据。基于用户先前提供的通用原型调整名称，保留材料/访谈双工作流。
- `skills/liushui-ip/`：个人IP定位顾问。基于真实能力、受众任务、差异化、可持续性、资源约束，输出多个定位假设和14天验证计划。

## 如何安装

### 通过 skills CLI（推荐）

```bash
npx -y skills add jiamiaomiao029-gif/liushui-skills -g --all
```

也可以只安装一个：

```bash
npx -y skills add jiamiaomiao029-gif/liushui-skills -g --skill liushui-persona
npx -y skills add jiamiaomiao029-gif/liushui-skills -g --skill liushui-ip
```

### 手动安装

分别将两个文件夹复制到支持 Agent Skills 的工具的 Skill 目录，确保每个文件夹下都直接有 `SKILL.md` 和 `references/`。具体目录因 Claude Code、Codex 等使用环境而不同；请按目标工具官方文档操作。

可**仅安装一个**；`liushui-ip` 不依赖 `liushui-persona`，只是可以接收其已完成、已经脱敏的人物发现。

## 提问示例

- `请用 liushui-persona 分析我授权的两年日记，找5条有行为证据的人物模式和反例。`
- `请用 liushui-ip 帮我在“摄影教学”和“AI影像成长记录”之间做定位取舍。我的作品和可投入时间如下……`
- `我运营半年，播放还行但几乎没有目标客户咨询，请先判断我的定位问题在哪里。`

## 已做与尚未做

已做：可安装文件结构、执行规则、参考资料、模板、测试任务、链接和基本静态检查；快速回答/标准诊断/完整定位的分档交付；大规模材料的覆盖度协议；人设考古到IP定位的脱敏交接简报。

未做：在 Claude/Codex 等实际宿主环境运行、与通用AI盲评、真实账号/客户结果验证。`V0.2` 仍是候选测试版本，不宣称已经通过线上效果验证。

## 版权与隐私

此安装包不附带外部培训原文、整本书、真实客户咨询报告或可识别的私人日记。公开材料为项目自行归纳的流程与规则，实际咨询时只分析用户授权的输入。
