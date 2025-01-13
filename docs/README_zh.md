# O File Processor

使用 PyQt6 创建的多语言文件管理应用程序，可让您轻松管理目录中的文件。

[English](../README.md) | [Türkçe](README_tr.md) | [Azərbaycanca](README_az.md) | [Español](README_es.md) | [Русский](README_ru.md)

## 功能特点

- 按名称筛选文件
- 批量重命名文件
- 复制和重命名文件
- 删除包含特定文本的文件
- 多语言支持（英语、土耳其语、阿塞拜疆语、西班牙语、俄语、中文）

## 安装

1. 克隆此仓库：

```bash
git clone https://github.com/hamer1818/file-processor.git
```

2. 安装所需依赖：

```bash
pip install -r requirements.txt
```


## 使用方法

1. 启动应用程序：

```bash
python main.py
```

2. 选择目录
3. 可用功能：
   - 筛选文件：在筛选框中输入文本，然后点击 "Apply Filter"
   - 重命名文件：输入 "旧名称 新名称" 然后点击 "Rename Files"
   - 复制并重命名文件：输入 "旧名称 新名称" 然后点击 "Copy and Rename Files"
   - 删除文件：输入匹配文本，然后点击 "Delete Files"

## 截图

[在此添加截图]

## 系统要求

- Python 3.6+
- PyQt6

## 许可证

本项目采用 MIT 许可证 - 详情请参阅 [LICENSE](LICENSE) 文件。