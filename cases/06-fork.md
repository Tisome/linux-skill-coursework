# 第七周 · fork 创建新进程

归档记录显示 MenuOS 的 `fork` 父分支打印 PID 1 和子 PID 867，子分支返回 0。GDB 归档包含 `sys_clone`、`do_fork`、`copy_process`、`copy_thread`、`wake_up_new_task` 和 `ret_from_fork`。在 `copy_thread` 入口读到 `p->pid=1`、`comm=init`，没有读到 `thread.sp/ip` 赋值后的数值。记录据 3.18.6 源码核对 PID 在其后写入，且子进程寄存器现场的 ax 被置 0。

任务：用用户态现象和断点解释 fork 返回两次，标出字段的观察时点。依据 [课程演进记录](../archive/course-evolution.md) 的实验六。
