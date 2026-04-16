@echo off
REM Audio Optimizer - Build Script para Windows

echo ========================================
echo  Audio Optimizer - Build para Windows
echo ========================================
echo.

REM Check if ffmpeg.exe and ffprobe.exe exist
if not exist "ffmpeg.exe" (
    echo ERROR: ffmpeg.exe no encontrado en el directorio actual
    echo.
    echo Por favor descarga ffmpeg para Windows:
    echo https://ffmpeg.org/download.html
    echo.
    echo Extrae los archivos y coloca ffmpeg.exe y ffprobe.exe en este directorio
    pause
    exit /b 1
)

if not exist "ffprobe.exe" (
    echo ERROR: ffprobe.exe no encontrado en el directorio actual
    echo.
    echo Ambos ffmpeg.exe y ffprobe.exe son requeridos
    pause
    exit /b 1
)

echo [1/4] Limpiando instalaciones previas...
pip install --upgrade pip setuptools wheel
if %ERRORLEVEL% neq 0 (
    echo ERROR: Fallo actualizando pip
    pause
    exit /b 1
)

echo.
echo [2/4] Instalando dependencias...
pip install --no-cache-dir -r requirements.txt
if %ERRORLEVEL% neq 0 (
    echo ERROR: Fallo en la instalacion de dependencias
    echo.
    echo Intenta manualmente:
    echo   pip install --upgrade pip
    echo   pip install pydub
    echo   pip install pyinstaller
    pause
    exit /b 1
)

echo.
echo [3/4] Compilando con PyInstaller...
python -m PyInstaller audio_optimizer.spec --collect-all pydub
if %ERRORLEVEL% neq 0 (
    echo ERROR: Fallo en la compilacion
    pause
    exit /b 1
)

echo.
echo [4/4] Build completado!
echo.
echo El ejecutable se encuentra en: dist\AudioOptimizer.exe
echo.
echo Verifica que exista antes de usar.
echo.
pause
