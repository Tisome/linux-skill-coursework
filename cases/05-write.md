# 第六周 · 从 system_call 到返回检查

Linux 3.18.6 的 GDB 起初命中 `fd=0`、调用栈包含 initramfs 解包 `xwrite` 的路径。后续命中 `SyS_write`，`fd=1`、`count=18`，且 MenuOS 显示命令操作。C 断点以后无法完整跨越用户/内核边界回溯。已归档 `entry_32.S` 中分派和 `work_pending` 的源码截图。

任务：判断哪一次命中支持用户调用，解释源码中的返回前检查与条件调度。依据 [课程演进记录](../archive/course-evolution.md) 的实验五。
