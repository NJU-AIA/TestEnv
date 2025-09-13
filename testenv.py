import importlib
import sys

# 需要检测的库
libraries = [
    "struct",
    "os",
    "urllib.request",
    "zipfile",
    "numpy",
    "matplotlib"
]

print("===== 环境检测开始 =====\n")

print("=== 安装检测 ===")
for lib in libraries:
    try:
        importlib.import_module(lib.split('.')[0])  
        print(f"[OK] {lib} 已安装")
    except ImportError:
        print(f"[X] {lib} 未安装，请先运行: pip install {lib.split('.')[0]}")

print("\n=== 测试 numpy ===")
try:
    import numpy as np
    a = np.array([1, 2, 3])
    print("\nNumpy 测试成功:", a, "平方:", a**2)
except Exception as e:
    print("[X] numpy 测试失败:", e)

print("\n=== 测试 matplotlib ===")
try:
    import matplotlib.pyplot as plt
    plt.plot([0,1,2],[0,1,4])
    plt.title("Matplotlib 测试")
    plt.savefig("matplotlib_test.png")
    print("\nMatplotlib 测试成功，已保存 matplotlib_test.png")
except Exception as e:
    print("[X] matplotlib 测试失败:", e)

print("\n===== 环境检测结束 =====")
