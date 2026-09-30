# Optional model providers

真实模型适配器是显式 opt-in 依赖，不进入默认离线 CI。适配器只能实现公共 `ModelClient` 契约，不得绕过策略、状态或轨迹层。
