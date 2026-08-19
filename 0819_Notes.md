# 实例6：流域单元和侧向流模拟 —— 完整操作步骤

## 一、目录结构总览

/share/home/colm099/
├── CoLM_src/ # 您的源码副本（有完全权限）
│ ├── include/
│ │ └── define.h # 实例6的宏定义
│ ├── run/
│ │ └── *.x # 可执行文件
│ └── Makefile
│
└── working/ # 您的工作目录
├── ex06_catchment/ # 运行目录
│ ├── PearlRiver_Catch_250km2_PC_VG.nml # namelist
│ ├── mksrfdata.x
│ ├── mkinidata.x
│ ├── colm.x
│ ├── lsf.ex06 # 作业脚本
│ ├── log.mksrfdata.ex06
│ ├── log.mkinidata.ex06
│ └── log.colm.ex06
│
└── PearlRiver_Catch_250km2_PC_VG/ # 实例目录（程序自动创建）
├── landdata/
├── restart/
└── history/ # 输出结果

分别弄run包含的三个文件，并写log
mpirun -np 48 ./mksrfdata.x  /share/home/colm099/working/ex06_catchment/PearlRiver_Catch_250km2_PC_VG.nml > /share/home/colm099/working/ex06_catchment/mksrfdata.ex06
mpirun -np 48 ./mkinidata.x  /share/home/colm099/working/ex06_catchment/PearlRiver_Catch_250km2_PC_VG.nml > /share/home/colm099/working/ex06_catchment/log.ex06
mpirun -np 48 ./colm.x  /share/home/colm099/working/ex06_catchment/PearlRiver_Catch_250km2_PC_VG.nml > /share/home/colm099/working/ex06_catchment/log.ex06
