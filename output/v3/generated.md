# 从 start_kernel 到 /init

在报告的 Linux 3.18.6 环境，GDB 使用与 QEMU 镜像匹配的 `vmlinux`。已归档断点串起 `start_kernel → rest_init → kernel_init → kernel_init_freeable → run_init_process("/init")`。启动初期，内核先建立基本环境，再完成初始化并准备执行用户态 init。

GDB 在 `do_execve` 前停下，证明走到了准备执行 `/init` 的路径。普通 QEMU 启动另有 MenuOS 提示符。
