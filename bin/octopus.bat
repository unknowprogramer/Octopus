@echo off
title OCTOPUS

:main
echo ================================
echo           Pick a number
echo     1. https://feature.com/
echo ================================
echo.

set /p answer=Your choice is = 
if %answer%==exit exit
if %answer% GTR 0 (
    if %answer% LEQ 1 (
        GOTO choice_%answer%
    )
)

echo Invail Input! & echo. & pause
cls & GOTO main

:choice_1
start python "../src/main.py" || echo. && pause
cls & GOTO main