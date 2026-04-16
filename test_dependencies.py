#!/usr/bin/env python3
"""
Test script to verify all dependencies are installed correctly
Run this BEFORE building to ensure everything works
"""

import sys
import os
from pathlib import Path

def test_python_version():
    """Check Python version"""
    if sys.version_info < (3, 8):
        print(f"❌ Python 3.8+ requerido, tienes {sys.version_info.major}.{sys.version_info.minor}")
        return False
    print(f"✓ Python {sys.version_info.major}.{sys.version_info.minor} OK")
    return True

def test_pydub():
    """Test pydub installation"""
    try:
        from pydub import AudioSegment
        print("✓ pydub instalado correctamente")
        return True
    except ImportError as e:
        print(f"❌ Error importando pydub: {e}")
        print("   Instala con: pip install pydub")
        return False

def test_ffmpeg():
    """Check if ffmpeg/ffprobe exist in current directory"""
    ffmpeg_exists = os.path.exists("ffmpeg.exe")
    ffprobe_exists = os.path.exists("ffprobe.exe")

    if ffmpeg_exists and ffprobe_exists:
        print("✓ ffmpeg.exe y ffprobe.exe encontrados")
        return True

    missing = []
    if not ffmpeg_exists:
        missing.append("ffmpeg.exe")
    if not ffprobe_exists:
        missing.append("ffprobe.exe")

    print(f"❌ Archivos faltantes: {', '.join(missing)}")
    print("   Descargalos desde: https://ffmpeg.org/download.html")
    return False

def test_tkinter():
    """Test tkinter (GUI library)"""
    try:
        import tkinter
        print("✓ tkinter disponible (GUI)")
        return True
    except ImportError:
        print("❌ tkinter no instalado")
        print("   En Windows: viene con Python por defecto")
        print("   En Linux: sudo apt install python3-tk")
        return False

def test_pyinstaller():
    """Test PyInstaller installation"""
    try:
        import PyInstaller
        print("✓ PyInstaller instalado")
        return True
    except ImportError:
        print("❌ PyInstaller no instalado")
        print("   Instala con: pip install pyinstaller")
        return False

def test_audio_file():
    """Look for test audio file"""
    possible_paths = [
        "test.mp3",
        "../optimized media/Lacanian_Module_01.mp3",
    ]

    for path in possible_paths:
        if os.path.exists(path):
            print(f"✓ Archivo de prueba encontrado: {path}")
            return True

    print("⚠️  Sin archivo de prueba MP3 (opcional, pero recomendado para testing)")
    return True  # Not critical

def main():
    print("=" * 50)
    print("Audio Optimizer - Test de Dependencias")
    print("=" * 50)
    print()

    tests = [
        ("Python version", test_python_version),
        ("pydub", test_pydub),
        ("tkinter", test_tkinter),
        ("PyInstaller", test_pyinstaller),
        ("ffmpeg binaries", test_ffmpeg),
        ("Test audio file", test_audio_file),
    ]

    results = []
    for name, test_func in tests:
        try:
            result = test_func()
            results.append((name, result))
        except Exception as e:
            print(f"❌ Error en {name}: {e}")
            results.append((name, False))
        print()

    # Summary
    print("=" * 50)
    print("RESUMEN")
    print("=" * 50)

    passed = sum(1 for _, result in results if result)
    total = len(results)

    for name, result in results:
        status = "✓" if result else "❌"
        print(f"{status} {name}")

    print()
    print(f"Total: {passed}/{total} pruebas pasadas")
    print()

    if passed == total:
        print("✅ ¡Todo listo para buildear!")
        print()
        print("Próximo paso: ejecuta build.bat")
        return 0
    else:
        print("❌ Hay problemas que resolver antes de buildear")
        return 1

if __name__ == "__main__":
    sys.exit(main())
