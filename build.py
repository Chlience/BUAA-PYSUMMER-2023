from PyInstaller.__main__ import run

# 获取需要打包的主程序文件路径
main_script = "ui.py"  # 替换为你的主程序文件名

# 打包参数
params = [
    '--name=航味————吃在北航！',         # 替换为你的应用名称
    '--onefile',                  # 生成单个可执行文件
    '--noconsole',                # 不显示终端窗口
    f'--add-data=resources/food.json;.',   # 添加 food_data.json 文件
    f'--add-data=resources/data.json;.',        # 添加 data.json 文件

    f'--icon=resources/tupian.ico',
]

# 运行 PyInstaller
run([main_script] + params)
