@echo off
setlocal enabledelayedexpansion
title Flappy Bird Terminal
mode con cols=50 lines=25
color 0B

:: Variables du jeu
set /a birdY=10
set /a birdX=10
set /a score=0
set /a gameOver=0
set /a pipeX=45
set /a pipeGap=7
set /a pipeY=8
set /a frameCount=0

:: Cacher le curseur
echo [?25l

:menu
cls
echo.
echo     ================================
echo           FLAPPY BIRD TERMINAL
echo     ================================
echo.
echo.
echo       Appuyez sur ENTREE rapidement
echo         pour faire monter l'oiseau
echo.
echo       Relacher pour le laisser tomber
echo.
echo.
echo      Appuyez sur une touche
echo         pour commencer
echo.
pause >nul
goto initGame

:initGame
set /a birdY=10
set /a score=0
set /a gameOver=0
set /a pipeX=45
set /a frameCount=0
if exist input.tmp del input.tmp
goto gameLoop

:gameLoop
:: Creer un fichier temporaire pour la detection
if exist input.tmp (
    :: Si le fichier existe, l'oiseau monte
    set /a birdY-=2
    del input.tmp
) else (
    :: Sinon, l'oiseau descend (gravite)
    set /a birdY+=1
)

:: Limites de l'ecran
if !birdY! LEQ 1 set /a birdY=1
if !birdY! GEQ 19 set /a gameOver=1

:: Deplacer le tuyau
set /a frameCount+=1
if !frameCount! GEQ 2 (
    set /a pipeX-=1
    set /a frameCount=0
)

if !pipeX! LEQ 0 (
    set /a pipeX=45
    set /a pipeY=!random! %% 10 + 3
    set /a score+=1
)

:: Collision avec le tuyau
if !pipeX! GEQ 8 if !pipeX! LEQ 12 (
    if !birdY! LEQ !pipeY! set /a gameOver=1
    set /a pipeBottom=!pipeY!+!pipeGap!
    if !birdY! GEQ !pipeBottom! set /a gameOver=1
)

:: Dessiner le jeu
cls
echo Score: !score!  [Appuyez ENTREE pour voler]
echo.

for /l %%y in (0,1,20) do (
    set "line="
    for /l %%x in (0,1,48) do (
        set "char= "
        
        :: Dessiner l'oiseau
        if %%x==!birdX! if %%y==!birdY! set "char=@"
        
        :: Dessiner le tuyau superieur
        if %%x GEQ !pipeX! if %%x LEQ !pipeX!+2 (
            if %%y LEQ !pipeY! set "char=#"
        )
        
        :: Dessiner le tuyau inferieur
        if %%x GEQ !pipeX! if %%x LEQ !pipeX!+2 (
            set /a pipeBottom=!pipeY!+!pipeGap!
            if %%y GEQ !pipeBottom! set "char=#"
        )
        
        :: Bordures
        if %%y==0 set "char=-"
        if %%y==20 set "char=-"
        if %%x==0 set "char=|"
        if %%x==48 set "char=|"
        
        set "line=!line!!char!"
    )
    echo !line!
)

:: Verifier game over
if !gameOver!==1 goto gameOverScreen

:: Lancer la detection d'input en arriere-plan
start /b cmd /c "set /p dummy= & echo 1 > input.tmp" 2>nul

:: Delai pour controler la vitesse du jeu
timeout /t 1 /nobreak >nul

:: Nettoyer les processus cmd en trop
taskkill /f /fi "WINDOWTITLE eq Administrator:  C:\Windows\system32\cmd.exe" >nul 2>&1

goto gameLoop

:gameOverScreen
cls
echo.
echo     ================================
echo              GAME OVER!
echo     ================================
echo.
echo           Score final: !score!
echo.
echo.
echo      Appuyez sur R pour rejouer
echo      Appuyez sur Q pour quitter
echo.

if exist input.tmp del input.tmp
choice /c RQ /n >nul
if errorlevel 2 goto end
if errorlevel 1 goto initGame

:end
if exist input.tmp del input.tmp
echo [?25h
cls
echo Merci d'avoir joue!
timeout /t 2 >nul
exit