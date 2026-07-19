@echo off
chcp 65001 > nul

echo Привет.
echo Эта командная строка позволит вам настроить бота, и приготовить его к исполнению.
echo.
set /p TOKEN="your token: "
mkdir data
(
echo({
echo(    "token": "%TOKEN%"
echo(}
) > data/config.json