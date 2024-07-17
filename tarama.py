import tkinter as tk
from tkinter import ttk, messagebox
import socket
import threading
from queue import Queue

class PortScannerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Port Tarayıcı - Rimes Yazılım")
        self.root.geometry("500x400")
        self.queue = Queue()
        self.open_ports = []
        
        # Kullanıcı arayüzü elemanlarını oluştur
        self.create_widgets()

    def create_widgets(self):
        # IP adresi veya domain girişi
        self.target_label = ttk.Label(self.root, text="Hedef IP veya Domain:")
        self.target_label.pack(pady=5)
        self.target_entry = ttk.Entry(self.root, width=50)
        self.target_entry.pack(pady=5)

        # Başlangıç portu girişi
        self.start_port_label = ttk.Label(self.root, text="Başlangıç Portu:")
        self.start_port_label.pack(pady=5)
        self.start_port_entry = ttk.Entry(self.root, width=10)
        self.start_port_entry.pack(pady=5)

        # Bitiş portu girişi
        self.end_port_label = ttk.Label(self.root, text="Bitiş Portu:")
        self.end_port_label.pack(pady=5)
        self.end_port_entry = ttk.Entry(self.root, width=10)
        self.end_port_entry.pack(pady=5)

        # Taramayı başlat butonu
        self.start_button = ttk.Button(self.root, text="Taramayı Başlat", command=self.start_scan)
        self.start_button.pack(pady=20)

        # Sonuçları gösteren liste kutusu
        self.result_listbox = tk.Listbox(self.root, width=50, height=10)
        self.result_listbox.pack(pady=20)

    def start_scan(self):
        target = self.target_entry.get()
        try:
            port_start = int(self.start_port_entry.get())
            port_end = int(self.end_port_entry.get())
        except ValueError:
            messagebox.showerror("Hata", "Geçerli bir port aralığı girin.")
            return
        
        if not target:
            messagebox.showerror("Hata", "Hedef IP veya domain girin.")
            return

        self.result_listbox.delete(0, tk.END)
        self.queue = Queue()
        self.open_ports = []

        for port in range(port_start, port_end + 1):
            self.queue.put(port)

        thread_count = 100
        self.run_scanner(thread_count)

    def scan_port(self, port):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            result = sock.connect_ex((self.target_entry.get(), port))
            if result == 0:
                self.open_ports.append(port)
                self.result_listbox.insert(tk.END, f"Port {port} açık")
            sock.close()
        except socket.error as err:
            print(f"Port {port} taranırken hata oluştu: {err}")

    def worker(self):
        while not self.queue.empty():
            port = self.queue.get()
            self.scan_port(port)
            self.queue.task_done()

    def run_scanner(self, threads):
        for t in range(threads):
            thread = threading.Thread(target=self.worker)
            thread.daemon = True
            thread.start()

        self.queue.join()
        self.result_listbox.insert(tk.END, "Tarama tamamlandı")

if __name__ == "__main__":
    root = tk.Tk()
    app = PortScannerApp(root)
    root.mainloop()
