# fork 的父子分支和字段观察时点

MenuOS 归档显示父分支获得子 PID 867，子分支看到自己的 `fork` 返回 0。GDB 追踪到 `sys_clone → do_fork → copy_process`，后续还有 `wake_up_new_task` 与 `ret_from_fork`。对应版本中 `copy_thread` 准备子进程的寄存器现场，将子返回寄存器 ax 设为 0。

在 `copy_thread` 入口看到 `p->pid=1` 和 `comm=init`。依据归档的源码核对，PID 后续才写入，入口观察不能当作子进程最终 PID。

## 审阅批注

[补足栈字段的观察范围] `thread.sp/ip` 的赋值后数值没有动态读取。需要在实际赋值之后观察字段，再与本次断点的入口值比较。
