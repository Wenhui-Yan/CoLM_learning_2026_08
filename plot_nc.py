import netCDF4 as nc
import matplotlib.pyplot as plt
import numpy as np

# ========== 修改这里的文件路径 ==========
file_path = '/share/home/colm099/point_case/IT-Isp/history/IT-Isp_hist_2014.nc'
# =====================================

# 读取文件
ds = nc.Dataset(file_path)

# 查看所有变量
print("=== 文件中的变量 ===")
for var in ds.variables:
    print(f"  {var}")

# 查看变量列表
print("\n=== 变量的维度信息 ===")
for var in ds.variables:
    if len(ds.variables[var].dimensions) > 0:
        print(f"  {var}: {ds.variables[var].dimensions}")

# 选择一个变量画图（以地表温度 t_grnd 为例）
if 't_grnd' in ds.variables:
    data = ds.variables['t_grnd'][:]
    plt.figure(figsize=(10, 4))
    plt.plot(data)
    plt.xlabel('Time step')
    plt.ylabel('t_grnd (K)')
    plt.title('Surface Temperature (IT-Isp)')
    plt.grid()
    plt.show()

# 如果有 LAI，画 LAI
if 'lai' in ds.variables:
    data = ds.variables['lai'][:]
    plt.figure(figsize=(10, 4))
    plt.plot(data)
    plt.xlabel('Time step')
    plt.ylabel('LAI')
    plt.title('Leaf Area Index (IT-Isp)')
    plt.grid()
    plt.show()