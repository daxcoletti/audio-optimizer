# Instalación y Build del Audio Optimizer

## ⚡ Quick Start (Usuario Final)

Si ya tienes el `AudioOptimizer.exe`:
1. Descárgalo y guárdalo donde quieras
2. Doble-click para ejecutar
3. ¡Listo! No necesita instalación

---

## 🛠️ Build desde código (Desarrollador)

### Prerequisitos

- **Windows 10/11** (PyInstaller está optimizado para Windows)
- **Python 3.8+** instalado (verificar con `python --version`)

### Paso 1: Descargar ffmpeg

1. Ir a https://ffmpeg.org/download.html
2. Buscar **Windows builds** → descargar versión completa (ej: "Full build")
3. Extraer el ZIP descargado
4. Copiar estos dos archivos:
   - `ffmpeg.exe`
   - `ffprobe.exe`

### Paso 2: Preparar el directorio

Coloca los archivos en la carpeta `audio-optimizer/`:

```
audio-optimizer/
├── audio_optimizer.py
├── audio_optimizer.spec
├── requirements.txt
├── build.bat
├── README.md
├── INSTALL.md (este archivo)
├── ffmpeg.exe        ← Copiar aquí
└── ffprobe.exe       ← Copiar aquí
```

### Paso 3: Ejecutar el build

1. Abre **Command Prompt** o **PowerShell**
2. Navega a la carpeta:
   ```cmd
   cd C:\ruta\al\audio-optimizer
   ```
3. Ejecuta el script:
   ```cmd
   build.bat
   ```

### Paso 4: Esperar

El script automáticamente:
- ✓ Instala dependencias Python
- ✓ Compila con PyInstaller
- ✓ Genera `dist/AudioOptimizer.exe`

El proceso tarda **3-5 minutos** en la primera ejecución.

---

## 📦 Resultado

Cuando termina, encontrarás:

```
dist/
└── AudioOptimizer.exe    ← ¡Tu ejecutable!
```

**Este .exe es portátil** — puedes moverlo, compartirlo, ejecutarlo en cualquier Windows sin requerimientos adicionales.

---

## 🔍 Troubleshooting

### "Python no es reconocido"
**Solución:** Python no está en el PATH
1. Desinstala Python
2. Reinstala con ✓ "Add Python to PATH"
3. Abre una nueva ventana de cmd

### "ffmpeg.exe no encontrado"
**Solución:** Los binarios no están en la carpeta
1. Verifica que `ffmpeg.exe` y `ffprobe.exe` estén en el mismo directorio
2. Ejecuta `build.bat` nuevamente

### "pip: comando no encontrado"
**Solución:** Python no está instalado correctamente
1. Descarga Python desde https://www.python.org
2. Asegúrate de marcar "Add Python to PATH"
3. Reinicia cmd y vuelve a intentar

### El .exe tarda en abrir
**Es normal** — la primera ejecución extrae y carga los binarios. Luego es más rápido.

### El .exe se cierra al hacer click
1. Abre una terminal en el directorio y ejecuta:
   ```cmd
   dist\AudioOptimizer.exe
   ```
2. Verifica si hay mensajes de error en la terminal

---

## 📖 Desarrollo

Para modificar el código y testear antes de buildear:

```cmd
pip install -r requirements.txt
python audio_optimizer.py
```

Se abrirá la interfaz gráfica en Windows.

---

## 📋 Especificaciones técnicas

**Parámetros de compresión:**
- Bitrate: 64 kbps (óptimo para voz)
- Canales: Mono (más compacto)
- Sample rate: 22050 Hz (suficiente para voz)
- Resultado: ~80% menos tamaño

**Archivos necesarios:**
- Python 3.8+ (para build)
- ffmpeg + ffprobe (incluidos en el .exe)
- pydub (descargado automáticamente)

---

## ❓ Preguntas frecuentes

**¿Necesito instalar ffmpeg después de tener el .exe?**
No, está embebido en el ejecutable.

**¿Puedo usar el .exe en macOS o Linux?**
No, solo Windows. Para otras plataformas, ejecuta el script Python directamente.

**¿Qué formatos soporta?**
Actualmente: MP3 entrada → MP3 salida. Fácil de extender a WAV, OGG, etc.

**¿Se puede procesar múltiples archivos a la vez?**
Actualmente: uno a la vez. Se puede extender para batch processing.

---

Versión 1.0 — Última actualización: 2026-04-16
