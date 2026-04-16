import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import threading
import os
import sys
import subprocess
from pathlib import Path

class AudioOptimizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Audio Optimizer")
        self.root.geometry("450x300")
        self.root.resizable(False, False)

        self.selected_file = None
        self.is_processing = False

        # Build UI
        self.create_widgets()

    def create_widgets(self):
        """Create GUI components"""
        # Title
        title_label = tk.Label(
            self.root,
            text="Audio Optimizer",
            font=("Arial", 16, "bold"),
            pady=10
        )
        title_label.pack()

        # File selection frame
        file_frame = tk.Frame(self.root)
        file_frame.pack(padx=20, pady=10, fill=tk.X)

        tk.Label(file_frame, text="Archivo:", font=("Arial", 10)).pack(side=tk.LEFT)

        self.file_label = tk.Label(
            file_frame,
            text="Ninguno seleccionado",
            font=("Arial", 9),
            fg="gray",
            wraplength=300,
            justify=tk.LEFT
        )
        self.file_label.pack(side=tk.LEFT, padx=10, fill=tk.X, expand=True)

        # Select file button
        select_btn = tk.Button(
            self.root,
            text="Seleccionar archivo MP3...",
            command=self.select_file,
            width=40,
            bg="#007ACC",
            fg="white",
            font=("Arial", 10),
            cursor="hand2"
        )
        select_btn.pack(pady=10)

        # Progress bar
        self.progress = ttk.Progressbar(
            self.root,
            mode='indeterminate',
            length=400
        )
        self.progress.pack(pady=10)

        # Optimize button
        self.optimize_btn = tk.Button(
            self.root,
            text="Optimizar",
            command=self.optimize_file,
            width=40,
            bg="#28A745",
            fg="white",
            font=("Arial", 11, "bold"),
            cursor="hand2"
        )
        self.optimize_btn.pack(pady=10)

        # Status label
        self.status_label = tk.Label(
            self.root,
            text="",
            font=("Arial", 9),
            wraplength=400
        )
        self.status_label.pack(pady=10)

    def select_file(self):
        """Open file dialog to select MP3"""
        file_path = filedialog.askopenfilename(
            title="Seleccionar archivo de audio",
            filetypes=[("MP3 files", "*.mp3"), ("All files", "*.*")],
            initialdir=str(Path.home())
        )

        if file_path:
            self.selected_file = file_path
            filename = os.path.basename(file_path)
            self.file_label.config(text=filename, fg="black")
            self.status_label.config(text="", fg="black")

    def optimize_file(self):
        """Optimize selected audio file"""
        if not self.selected_file:
            messagebox.showwarning("Advertencia", "Por favor selecciona un archivo primero")
            return

        if not os.path.exists(self.selected_file):
            messagebox.showerror("Error", "El archivo no existe")
            self.selected_file = None
            self.file_label.config(text="Ninguno seleccionado", fg="gray")
            return

        if self.is_processing:
            messagebox.showinfo("Información", "Ya hay un archivo siendo procesado")
            return

        # Disable button and show progress
        self.is_processing = True
        self.optimize_btn.config(state=tk.DISABLED, bg="#999999")
        self.progress.start()
        self.status_label.config(text="Procesando...", fg="blue")

        # Process in separate thread to avoid freezing UI
        thread = threading.Thread(target=self._process_audio, daemon=True)
        thread.start()

    def get_ffmpeg_path(self):
        """Get ffmpeg path - handles both PyInstaller bundles and system PATH"""
        if getattr(sys, 'frozen', False):
            # Running as PyInstaller executable
            ffmpeg_path = os.path.join(sys._MEIPASS, 'ffmpeg.exe')
            if os.path.exists(ffmpeg_path):
                return ffmpeg_path

        # Try system PATH
        try:
            result = subprocess.run(['ffmpeg', '-version'], capture_output=True)
            if result.returncode == 0:
                return 'ffmpeg'
        except:
            pass

        return None

    def _process_audio(self):
        """Background thread: process audio with ffmpeg"""
        try:
            ffmpeg_path = self.get_ffmpeg_path()
            if not ffmpeg_path:
                raise Exception("ffmpeg no encontrado. Asegúrate de que ffmpeg.exe esté en la carpeta del programa.")

            # Get file info
            input_path = self.selected_file
            file_size_before = os.path.getsize(input_path) / (1024 * 1024)  # MB

            # Generate output path
            base, ext = os.path.splitext(input_path)
            output_path = f"{base}_optimized{ext}"

            # ffmpeg command: convert to mono, 22050Hz, 64kbps
            cmd = [
                ffmpeg_path,
                '-i', input_path,
                '-ac', '1',           # mono
                '-ar', '22050',        # 22050 Hz sample rate
                '-b:a', '64k',         # 64 kbps bitrate
                '-q:a', '9',           # quality
                output_path,
                '-y'                   # overwrite without asking
            ]

            # Run ffmpeg
            result = subprocess.run(cmd, capture_output=True, text=True)

            if result.returncode != 0:
                raise Exception(f"ffmpeg error: {result.stderr}")

            # Get file sizes
            file_size_after = os.path.getsize(output_path) / (1024 * 1024)  # MB
            reduction_percent = ((file_size_before - file_size_after) / file_size_before) * 100

            # Update UI with success
            self.root.after(0, self._on_success, file_size_before, file_size_after, reduction_percent, output_path)

        except Exception as e:
            self.root.after(0, self._on_error, str(e))

    def _on_success(self, size_before, size_after, reduction, output_path):
        """Called when optimization succeeds"""
        self.progress.stop()
        self.is_processing = False
        self.optimize_btn.config(state=tk.NORMAL, bg="#28A745")

        message = f"✓ {size_before:.1f} MB → {size_after:.1f} MB (-{reduction:.0f}%)"
        self.status_label.config(text=message, fg="green")

        messagebox.showinfo(
            "¡Éxito!",
            f"Archivo optimizado correctamente\n\n{message}\n\nGuardado en:\n{output_path}"
        )

    def _on_error(self, error_msg):
        """Called when optimization fails"""
        self.progress.stop()
        self.is_processing = False
        self.optimize_btn.config(state=tk.NORMAL, bg="#28A745")

        self.status_label.config(text=f"Error: {error_msg}", fg="red")
        messagebox.showerror("Error", f"No se pudo procesar el archivo:\n\n{error_msg}")


if __name__ == "__main__":
    root = tk.Tk()
    app = AudioOptimizer(root)
    root.mainloop()
