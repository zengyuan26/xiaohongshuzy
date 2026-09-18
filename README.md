# Xiaohongshu Carousel Creator

一套可同时用于Codex和Claude Code的小红书图文/轮播创作Skill。核心能力包括：判断题材是否适合图文、选择图文类型、分级研究对标与评论、核实事实、设计标题封面和逐页内容，以及交付标签和发布描述。

## 获取

仓库地址：

```text
https://github.com/zengyuan26/xiaohongshuzy
```

可以下载Release中的ZIP包并解压，也可以克隆仓库后，把整个目录复制到对应的Skills目录。

## 安装到Codex

个人全局使用：

```text
~/.agents/skills/xiaohongshu-carousel-creator/
```

也可以放入项目：

```text
<项目目录>/.agents/skills/xiaohongshu-carousel-creator/
```

部分Codex环境也支持`~/.codex/skills/`。安装后重新打开会话，让工具重新发现Skill。

## 安装到Claude Code

个人全局使用：

```text
~/.claude/skills/xiaohongshu-carousel-creator/
```

项目内使用：

```text
<项目目录>/.claude/skills/xiaohongshu-carousel-creator/
```

Claude Code会读取`SKILL.md`和`references/`；`agents/openai.yaml`是Codex可选界面元数据，Claude Code可以忽略。

## 使用

可以直接说：

```text
用xiaohongshu-carousel-creator判断这段内容是否适合做小红书图文，并给出封面、逐页内容、标题、5个标签和发布描述。
```

也可以显式调用：

```text
$xiaohongshu-carousel-creator
```

不同客户端对显式Skill语法的支持可能不同；即使不支持`$`语法，只要Skill已安装，直接描述任务即可。

## 能力与边界

- 不依赖小红书连接器；没有平台工具时仍可完成策划、文案和生图提示词。
- 有联网或平台工具时，会按授权研究公开样本；链接失效时不会假装已经看完。
- 不包含任何私人项目资料、账号密码、客户案例或本地绝对路径。
- 不会自动发布；登录、上传和发布必须另行明确授权。

## 包内验证

```bash
python3 -m unittest discover -s tests -v
```

## 版本与许可

- 当前版本：`1.0.0`
- 开源许可：MIT
