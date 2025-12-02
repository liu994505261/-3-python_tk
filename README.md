# 今日运势应用

一个简单的 Python Tkinter 应用，用于显示今日运势。专为树莓派 32 位系统优化，无需额外依赖。

## 功能特点

- 🎲 随机生成今日运势（大吉、中吉、小吉等）
- 💡 提供运势建议
- 🍀 显示幸运数字、颜色和方位
- 🎨 简洁美观的界面
- 📦 轻量级，无额外依赖

## 快速开始

### 直接运行（开发/测试）

```bash
python3 fortune_app.py
```

### 打包部署

#### Linux/树莓派系统

```bash
# 给打包脚本添加执行权限
chmod +x build.sh

# 运行打包脚本
./build.sh
```

这将生成 `fortune_app_raspi32.tar.gz` 压缩包。

#### Windows 系统

```cmd
build.bat
```

这将创建 `fortune_app_package` 文件夹，可以压缩后传输到树莓派。

## 在树莓派上安装

### 1. 安装依赖

```bash
sudo apt-get update
sudo apt-get install python3 python3-tk
```

### 2. 解压应用

```bash
# 如果使用 build.sh 打包
tar -xzf fortune_app_raspi32.tar.gz
cd fortune_app_package

# 如果使用 build.bat 打包
unzip fortune_app_package.zip
cd fortune_app_package
```

### 3. 运行应用

```bash
chmod +x run.sh
./run.sh
```

或直接运行：

```bash
python3 fortune_app.py
```

### 4. 创建桌面快捷方式（可选）

```bash
# 复制到桌面
chmod +x fortune_app.desktop
cp fortune_app.desktop ~/Desktop/

# 或添加到应用程序菜单
mkdir -p ~/.local/share/applications
cp fortune_app.desktop ~/.local/share/applications/
```

### 5. 设置开机自启动（可选）

```bash
mkdir -p ~/.config/autostart
cp fortune_app.desktop ~/.config/autostart/
```

## 文件说明

- `fortune_app.py` - 主应用程序
- `build.sh` - Linux/树莓派打包脚本
- `build.bat` - Windows 打包脚本
- `requirements.txt` - 依赖说明（Tkinter 是标准库，无需安装）
- `README.md` - 本说明文件

## 系统要求

- 树莓派（32 位或 64 位系统）
- Python 3.x
- Tkinter（通常随 Python 一起安装）
- 最小内存：256MB
- 最小存储：10MB

## 运势等级

- 大吉 🔴
- 中吉 🟠
- 小吉 🟡
- 吉 🟢
- 半吉 🔵
- 末吉 🟣
- 末小吉 🟤
- 凶 ⚫
- 小凶 ⚪
- 半凶 🔘

## 许可证

MIT License

## 贡献

欢迎提交问题和改进建议！
