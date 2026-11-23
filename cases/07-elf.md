# 第八周 · ELF 装载与新入口

环境是 Linux 3.18.6 / x86-32 / QEMU。静态样本的 ELF `e_entry=0x8048d0a`，没有 `PT_INTERP`，GDB 的 `start_thread` 给出同值 `new_ip`。动态样本的应用 `e_entry=0x8048350`，`PT_INTERP` 指向 `/lib/ld-linux.so.2`，GDB 的 `new_ip=0xb77d90d0`。两次 GDB 记录可见 `new_sp` 而没有转储新用户栈。成功运行的 MenuOS 测试打印了 `argv[1]=from-MenuOS`。课程记录另有一对对照：装载时链接样本在动态节中含 `libgreet.so` 的 `DT_NEEDED`，用 `dlopen` 的样本没有这条启动依赖。

任务：用静态信息和动态证据解释入口差异，区分两种库装载方式，说明初始栈证据的边界。材料见[课程记录](../archive/course-evolution.md)和[原截图](../archive/elf-evidence/)。
