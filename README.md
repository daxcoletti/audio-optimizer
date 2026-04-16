# Audio Optimizer — Ejecutable Windows

Herramienta para comprimir archivos de audio MP3 sin perder calidad perceptible.

## Características

✅ **Interfaz simple** — Selecciona, optimiza, listo  
✅ **Compresión automática** — 64kbps + mono + 22050Hz  
✅ **Sin instalaciones** — Todo incluido en el .exe  
✅ **Reducción ~50%** — 79 MB → 40 MB en audio de voz  

## Cómo usar (Usuario Final)

1. Descarga `AudioOptimizer.exe`
2. Doble-click para abrir
3. Selecciona un archivo MP3
4. Click en "Optimizar"
5. Archivo guardado como `nombre_optimized.mp3` en la misma carpeta

## Cómo buildear (Desarrollador)

### Requisitos
- Windows 10/11
- Python 3.8+

### Pasos

1. **Descargar ffmpeg para Windows:**
   - Ve a https://ffmpeg.org/download.html
   - Descarga la versión Windows completa
   - Extrae los archivos

2. **Copiar binarios ffmpeg:**
   ```
   Copia ffmpeg.exe y ffprobe.exe desde la carpeta de ffmpeg
   al mismo directorio que este archivo README.md
   ```

3. **Ejecutar el build:**
   ```
   Doble-click en build.bat
   ```

4. **Resultado:**
   ```
   dist/AudioOptimizer.exe  ← Tu ejecutable listo para usar
   ```

## Estructura del proyecto

```
audio-optimizer/
├── audio_optimizer.py       # Código principal (GUI + lógica)
├── audio_optimizer.spec     # Configuración de PyInstaller
├── requirements.txt         # Dependencias Python
├── build.bat               # Script de build para Windows
├── README.md               # Este archivo
├── ffmpeg.exe              # (descargar) Binario ffmpeg
└── ffprobe.exe             # (descargar) Binario ffprobe
```

## Parámetros de compresión

| Parámetro | Valor | Razón |
|-----------|-------|-------|
| Bitrate | 64 kbps | Óptimo para voz, reduce ~50% |
| Canales | Mono | Voz no necesita estéreo |
| Sample rate | 22050 Hz | Suficiente para frecuencias de voz |
| Codec | MP3 | Compatibilidad universal |

## Limitaciones

- **Solo MP3** — Input y output en MP3 (fácil de extender)
- **Un archivo a la vez** — Sin procesamiento batch
- **Confía en ffmpeg** — Requiere ffmpeg.exe funcional

## Troubleshooting

**"ffmpeg.exe no encontrado"**
→ Descarga ffmpeg desde https://ffmpeg.org/download.html y copia los .exe a este directorio

**"No se pudo procesar el archivo"**
→ Asegúrate de que el MP3 es válido y que ffmpeg está correctamente instalado

**El .exe tarda mucho en abrirse**
→ Normal en primer uso (extrae binarios). Luego será más rápido.

## Desarrollo

Para testear el script sin compilar:

```bash
pip install -r requirements.txt
python audio_optimizer.py
```

(En Linux/macOS funciona pero sin GUI visual en ambiente headless)

---

**Versión:** 1.0  
**Licencia:** MIT
