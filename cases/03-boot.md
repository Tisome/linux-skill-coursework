# 第四周 · 从内核入口到 PID 1

归档记录为 Linux 3.18.6。普通 QEMU 启动可见 `MenuOS>>`。另一次 GDB 会话使用匹配的 `vmlinux`，命中 `start_kernel`、`rest_init`、`kernel_init`、`kernel_init_freeable` 和 `run_init_process("/init")`。最后的截图出现在调用 `do_execve` 之前。

任务：串起启动路径，并说明断点和终端菜单各自能证明什么。依据 [课程演进记录](../archive/course-evolution.md) 的实验三。
