# CoLM2024 移植与运行完整指南

## 一、登录与基础操作
```bash
login as: colm099                           # SSH 登录集群
ls                                          # 查看当前目录内容
cd CoLM-CoLM2024-Tutorial                   # 进入模型代码目录
ls -1                                       # 列出目录内容（每行一个）
cd ..                                       # 返回上级目录

cp -r /share/home/dq089/training2026/CoLM-CoLM2024-Tutorial .   # 复制模型代码到当前目录
cp -r /share/home/dq089/training2026/software/ ~/               # 复制软件安装包到用户目录
mkdir -p $HOME/software/installed                              # 创建软件安装目录
cd software/                                                    # 进入软件目录
mv installed/ installed_bk/                                     # 备份已有安装（如有）

./l_HPCKit_p_2021.3.0.3230_offline.sh     # 安装 Intel HPC Kit（Fortran 编译器）
ssh node112                                 # 登录到计算节点（编译需要）
source /share/home/colm150/.bashrc          # 加载已配置好的 Intel 环境
which ifort                                 # 验证 ifort 是否可用
ifort --version                             # 查看版本
