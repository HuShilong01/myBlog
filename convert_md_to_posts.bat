@echo off
chcp 65001 >nul
setlocal enabledelayedexpansion

echo ========================================
echo Markdown 文件转换工具
echo ========================================

:: 检查 Python 是否安装
python --version >nul 2>&1
if errorlevel 1 (
    echo 错误: 未找到 Python，请先安装 Python
    pause
    exit /b 1
)

:: 获取参数
set "source_dir=%~1"
set "date_param=%~2"
set "author_param=%~3"

:: 如果没有提供源目录，提示用户输入
if "%source_dir%"=="" (
    set /p "source_dir=请输入源文件夹路径: "
)

:: 检查源目录是否存在
if not exist "%source_dir%" (
    echo 错误: 源目录 "%source_dir%" 不存在
    pause
    exit /b 1
)

:: 构建命令
set "cmd=python convert_md_to_posts.py "%source_dir%""

:: 添加可选参数
if not "%date_param%"=="" (
    set "cmd=!cmd! --date "%date_param%""
)

if not "%author_param%"=="" (
    set "cmd=!cmd! --author "%author_param%""
)

echo.
echo 执行命令: !cmd!
echo.

:: 执行转换
!cmd!

echo.
echo 转换完成！
pause 