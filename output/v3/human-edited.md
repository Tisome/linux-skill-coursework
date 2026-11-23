# 从 start_kernel 到 /init

在报告的 Linux 3.18.6 环境，GDB 使用与 QEMU 镜像匹配的 `vmlinux`。已归档断点串起 `start_kernel → rest_init → kernel_init → kernel_init_freeable → run_init_process("/init")`。启动初期，内核先建立基本环境，再完成初始化并准备执行用户态 init。

GDB 在 `do_execve` 前停下，证明走到了准备执行 `/init` 的路径。普通 QEMU 启动另有 MenuOS 提示符。

## 本次回放批注

[拆开两次记录] 普通启动的提示符支持“系统另一次启动到用户态菜单”。要在同一次 GDB 会话证明从断点到菜单的完整轨迹，须继续执行并保留该会话终端证据。
