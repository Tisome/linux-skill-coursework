# 第五周 · 同一个系统调用的两种方式

归档记录显示 x86_64 实验主机上用 `-m32` 生成 i386 ELF。一个调用经过 libc 的 `write@plt`，另一个用 i386 的 `int $0x80`。反汇编展示了 eax＝4 与在 ebx、ecx、edx 装载参数，两条路径都写出预期文本。该实验未运行 strace。

任务：对照 libc 接口和内联汇编，说明实际证据和 ABI 范围。依据 [课程演进记录](../archive/course-evolution.md) 的实验四。
