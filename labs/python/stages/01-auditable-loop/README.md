# 实验 01：可审计 Agent 循环

使用确定性 Fake Model 运行“模型提议—工具执行—观察—终止”循环。运行时掌握最大步数和终止权；轨迹只记录模型结果、工具调用与状态变化，不保存隐藏推理。

```bash
PYTHONPATH=labs/python/src python3 labs/python/stages/01-auditable-loop/main.py
```
