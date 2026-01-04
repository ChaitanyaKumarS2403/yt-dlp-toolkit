@echo off
:: Check for administrative privileges
net session >nul 2>&1
if %errorLevel% == 0 (
    echo Administrative permissions confirmed.
) else (
    echo ---------------------------------------------------
    echo ERROR: PLEASE RUN THIS AS ADMINISTRATOR 
    echo ---------------------------------------------------
    echo.
    echo Here's how to use it:
    echo.
    echo 1. Run as Admin: Right-click the install_tools.bat file and select Run as Administrator. This is required for winget to modify system files.
    echo.
    echo 2. Wait for Prompts: You may see a prompt asking you to agree to source agreements; just press Y if prompted.
    echo.
    echo 3. Restart PowerShell/CMD: Once the script finishes, you must close and reopen your PowerShell window for the new "Path" variables to take effect.
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
echo PLEASE RESTART YOUR TERMINAL TO USE THE COMMANDS.
echo ---------------------------------------------------
pause