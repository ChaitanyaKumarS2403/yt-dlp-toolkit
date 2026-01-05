@echo off
:: Check for administrative privileges
net session >nul 2>&1
if %errorLevel% == 0 (
    echo Administrative permissions confirmed.
) else (
    echo ---------------------------------------------------
    echo This script requires administrative privileges to run.
    echo Please run this script as an Administrator. 
    echo ---------------------------------------------------
    echo.
    echo This file is a simple batch script that installs the required dependencies for the yt-dlp-toolkit.exe file using winget.
    echo.
    echo Here's how to use this file:
    echo.
    echo 1. Run as Admin: Right-click the RunThisFirstAsAdmin.bat file and select Run as Administrator. This is required for winget to modify system files.
    echo.
    echo 2. Wait for Prompts: You may see a prompt asking you to agree to source agreements; just press Y if prompted.
    echo.
    echo 3. Completion: Once the script finishes, you can close the terminal and run the yt-dlp-toolkit.exe file. 
    echo.
    echo ---------------------------------------------------
    echo.
    echo Make sure to uncheck 'Always ask before opening this type of file' if prompted when running the yt-dlp-toolkit.exe file.
    echo ---------------------------------------------------
    echo.
    pause
    exit /b
)

echo ---------------------------------------------------
echo Installing yt-dlp...
echo ---------------------------------------------------
winget install -e --id yt-dlp.yt-dlp
if %errorLevel% == 0 (echo yt-dlp installed successfully.) else (echo yt-dlp install failed or already exists.)

echo.
echo ---------------------------------------------------
echo Installing FFmpeg...
echo ---------------------------------------------------
winget install -e --id Gyan.FFmpeg
if %errorLevel% == 0 (echo FFmpeg installed successfully.) else (echo FFmpeg install failed or already exists.)

echo.
echo ---------------------------------------------------
echo Installation Complete!
echo Since the Publisher Details are Unlicensed, you may be prompted with a Dialogue Box asking you to confirm your trust. Simply uncheck the box that says 'Always ask before opening this type of file.' and hit 'Run'.
echo.
echo PLEASE EXIT THE TERMINAL AND RUN THE yt-dlp-toolkit.exe file. 
echo ---------------------------------------------------
pause