@echo off
set PYTHONPATH=%~dp0engines\python\src
python %~dp0engines\python\src\engine\cli\ct.py %*
