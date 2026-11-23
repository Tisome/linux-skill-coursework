# ELF 入口与初始用户栈

在归档的 32 位样本里，静态程序无 `PT_INTERP`，`e_entry` 与 `start_thread.new_ip` 都是 `0x8048d0a`。动态程序有 `PT_INTERP=/lib/ld-linux.so.2`。它的应用 `e_entry` 是 `0x8048350`，而 GDB 的 `new_ip` 是 `0xb77d90d0`。结合解释器段可判定首次进入动态链接器，再由它将控制权交给应用入口。

装载时链接的程序在动态节列出 `DT_NEEDED=libgreet.so`。用 `dlopen` 的对照程序在运行期显式装载该库，因此没有对它的这条启动依赖。GDB 给了 `new_sp`，课程命令输出则可见应用读取到的 `argv[1]`。初始栈的完整布局仍属机制分析。

## 本次回放批注

[写清互证范围] 静态和动态的文件属性来自 readelf 截图，入口和栈指针来自 GDB。程序能打印参数只证明它读到了该参数，无法替代从 `new_sp` 起逐项转储 `argc/argv/envp/auxv`。
