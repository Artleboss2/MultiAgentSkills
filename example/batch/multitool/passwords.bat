@echo off
chcp 65001 >nul
title Inscription Utilisateur
color 0B

:MENU
cls
echo.
echo ╔════════════════════════════════════════╗
echo ║    INSCRIPTION UTILISATEUR             ║
echo ╔════════════════════════════════════════╗
echo.
echo.

set /p username="  👤 Nom d'utilisateur : "
echo.
set /p email="  📧 Email : "
echo.
set /p password="  🔒 Mot de passe : "
echo.
set /p birthdate="  🎂 Date de naissance (AAAA-MM-JJ) : "
echo.
echo.

if "%username%"=="" (
    echo ❌ Le nom d'utilisateur ne peut pas être vide.
    timeout /t 3 >nul
    goto MENU
)

if "%email%"=="" (
    echo ❌ L'email ne peut pas être vide.
    timeout /t 3 >nul
    goto MENU
)

if "%password%"=="" (
    echo ❌ Le mot de passe ne peut pas être vide.
    timeout /t 3 >nul
    goto MENU
)

if "%birthdate%"=="" (
    echo ❌ La date de naissance ne peut pas être vide.
    timeout /t 3 >nul
    goto MENU
)

echo ⏳ Enregistrement en cours...
echo.

REM Exécuter directement le code PHP en ligne
"C:\xampp\php\php.exe" -r "$conn = new mysqli('localhost', 'root', '', 'personas'); if ($conn->connect_error) { echo 'ERREUR: ' . $conn->connect_error; exit(1); } $username = '%username%'; $email = '%email%'; $password = '%password%'; $birthdate = '%birthdate%'; $stmt = $conn->prepare('INSERT INTO users (username, email, password, birthdate) VALUES (?, ?, ?, ?)'); $stmt->bind_param('ssss', $username, $email, $password, $birthdate); if ($stmt->execute()) { echo 'SUCCESS'; } else { echo 'ERREUR: ' . $conn->error; } $stmt->close(); $conn->close();" 2>&1 | findstr /C:"SUCCESS" >nul

if %errorlevel% equ 0 (
    echo ✅ Utilisateur enregistré avec succès!
) else (
    "C:\xampp\php\php.exe" -r "$conn = new mysqli('localhost', 'root', '', 'personas'); if ($conn->connect_error) { echo 'ERREUR: ' . $conn->connect_error; exit(1); } $username = '%username%'; $email = '%email%'; $password = '%password%'; $birthdate = '%birthdate%'; $stmt = $conn->prepare('INSERT INTO users (username, email, password, birthdate) VALUES (?, ?, ?, ?)'); $stmt->bind_param('ssss', $username, $email, $password, $birthdate); if ($stmt->execute()) { echo 'SUCCESS'; } else { echo 'ERREUR: ' . $conn->error; } $stmt->close(); $conn->close();"
)

echo.
echo.
set /p continue="Voulez-vous enregistrer un autre utilisateur? (O/N) : "
if /i "%continue%"=="O" goto MENU
if /i "%continue%"=="OUI" goto MENU

cls
echo.
echo ╔════════════════════════════════════════╗
echo ║         Merci et à bientôt!            ║
echo ╚════════════════════════════════════════╝
echo.
timeout /t 3 >nul
exit