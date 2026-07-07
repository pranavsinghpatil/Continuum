@echo off
set PYTHONPATH=%~dp0sdks\python\src
python %~dp0sdks\python\src\engine\cli\ct.py %*
