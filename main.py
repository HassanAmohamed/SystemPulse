"""
COMPREHENSIVE SYSTEM DIAGNOSTICS TOOL
-------------------------------------
Collects hardware/software metrics including:
- Basic system info
- CPU/GPU details
- Memory/Disk usage
- Network interfaces
- Temperature sensors
- Optional GUI output
"""
import os
import platform
import cpuinfo
import psutil
import shutil
import socket
import subprocess
from tabulate import tabulate

try:
    import tkinter as tk
    GUI_ENABLED = True
except ImportError:
    GUI_ENABLED = False


def get_system_info():
    """Fetch basic OS and hardware information"""
    info = platform.uname()
    return {
        "OS": f"{info.system} {info.release}",
        "Hostname": info.node,
        "Architecture": f"{info.machine} ({platform.architecture()[0]})",
        "Python Version": platform.python_version()
    }


def get_cpu_info():
    """Fetch detailed CPU metrics"""
    info = cpuinfo.get_cpu_info()
    return {
        "Processor": info['brand_raw'],
        "Cores (Physical/Logical)": f"{psutil.cpu_count(logical=False)}/{psutil.cpu_count()}",
        "Frequency": info['hz_actual_friendly'],
        "Usage (%)": psutil.cpu_percent(interval=1)
    }


def get_gpu_info():
    """Fetch GPU information using cross-platform methods"""
    try:
        gpus = []
        if platform.system() == "Windows":
            # Windows GPU detection
            try:
                result = subprocess.check_output(
                    ['wmic', 'path', 'win32_VideoController', 'get', 'name'],
                    text=True,
                    stderr=subprocess.DEVNULL
                )
                for i, line in enumerate(result.strip().split('\n')[1:]):
                    if line.strip():
                        gpus.append({
                            "ID": i,
                            "Name": line.strip(),
                            "Load (%)": "N/A",
                            "VRAM (GB)": "N/A",
                            "Temperature (°C)": "N/A"
                        })
            except (subprocess.CalledProcessError, FileNotFoundError):
                pass
        else:
            # Linux/macOS GPU detection
            try:
                result = subprocess.check_output(
                    ['lspci', '-vnnn'],
                    text=True,
                    stderr=subprocess.DEVNULL
                )
                gpu_lines = [line for line in result.split('\n') if 'VGA' in line or '3D' in line]
                for i, line in enumerate(gpu_lines):
                    gpus.append({
                        "ID": i,
                        "Name": line.split(':')[-1].strip(),
                        "Load (%)": "N/A",
                        "VRAM (GB)": "N/A",
                        "Temperature (°C)": "N/A"
                    })
            except (subprocess.CalledProcessError, FileNotFoundError):
                pass

        return gpus if gpus else {"Error": "No GPU detected"}
    except Exception as e:
        return {"Error": f"GPU detection failed: {str(e)}"}


def get_memory_info():
    """Fetch RAM statistics"""
    mem = psutil.virtual_memory()
    return {
        "Total (GB)": f"{mem.total / (1024 ** 3):.2f}",
        "Available (GB)": f"{mem.available / (1024 ** 3):.2f}",
        "Used (%)": mem.percent
    }


def get_disk_info():
    """Fetch storage devices information"""
    disks = []
    for part in psutil.disk_partitions():
        try:
            usage = psutil.disk_usage(part.mountpoint)
            disks.append({
                "Device": part.device,
                "Mountpoint": part.mountpoint,
                "Total (GB)": f"{usage.total / (1024 ** 3):.2f}",
                "Used (%)": usage.percent
            })
        except PermissionError:
            continue
    return disks


def get_network_info():
    """Fetch network interface data"""
    interfaces = []
    for name, addrs in psutil.net_if_addrs().items():
        for addr in addrs:
            if addr.family == socket.AF_INET:
                interfaces.append({
                    "Interface": name,
                    "IP Address": addr.address,
                    "Netmask": addr.netmask
                })
    return interfaces


def get_temperatures():
    """Fetch hardware temperatures"""
    temps = {}
    try:
        if hasattr(psutil, "sensors_temperatures"):
            for name, entries in psutil.sensors_temperatures().items():
                if entries:  # Check if entries list is not empty
                    temps[name] = f"{entries[0].current}°C"
        return temps if temps else {"Info": "No temperature sensors found"}
    except AttributeError:
        return {"Error": "Temperature data not available"}


def display_text_report():
    """Generate console-based report"""
    print("\n" + "=" * 50)
    print("SYSTEM DIAGNOSTICS REPORT".center(50))
    print("=" * 50)

    sections = [
        ("System Info", get_system_info()),
        ("CPU Info", get_cpu_info()),
        ("GPU Info", get_gpu_info()),
        ("Memory Info", get_memory_info()),
        ("Disk Info", get_disk_info()),
        ("Network Info", get_network_info()),
        ("Temperatures", get_temperatures())
    ]

    for title, data in sections:
        print(f"\n{title.upper()}:")
        if isinstance(data, list):
            print(tabulate(data, headers="keys", tablefmt="grid"))
        elif isinstance(data, dict):
            print(tabulate([data], headers="keys", tablefmt="grid"))
        else:
            print(data)


def display_gui_report():
    """Generate graphical report (if tkinter available)"""
    root = tk.Tk()
    root.title("System Diagnostics")

    text = tk.Text(root, wrap=tk.WORD)
    text.pack(expand=True, fill=tk.BOTH)

    # Build report string
    report = []
    for title, func in [
        ("SYSTEM INFO", get_system_info),
        ("CPU INFO", get_cpu_info),
        ("GPU INFO", get_gpu_info),
        ("MEMORY INFO", get_memory_info),
        ("DISK INFO", get_disk_info),
        ("NETWORK INFO", get_network_info),
        ("TEMPERATURES", get_temperatures)
    ]:
        report.append(f"\n{title}\n{'=' * 30}")
        data = func()
        if isinstance(data, list):
            report.append(tabulate(data, headers="keys", tablefmt="plain"))
        elif isinstance(data, dict):
            report.append(tabulate([data], headers="keys", tablefmt="plain"))
        else:
            report.append(str(data))

    text.insert(tk.END, "\n".join(report))
    root.mainloop()



if __name__ == "__main__":
    # Check for admin privileges (recommended for temperature readings)
    if not psutil.WINDOWS and os.geteuid() != 0:
        print("Warning: Some metrics require root privileges")

    display_text_report()

    if GUI_ENABLED:
        user_input = input("\nShow graphical report? (y/n): ")
        if user_input.lower() == 'y':
            display_gui_report()