# 🔍 SystemScan - Comprehensive System Diagnostics Tool

![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Dependencies](https://img.shields.io/badge/dependencies-3-success)

A powerful Python utility that provides detailed insights into your system's hardware and software configuration. SystemScan delivers enterprise-grade diagnostics in an easy-to-use package.

## 🌟 Features

### Hardware Intelligence
- **Processor Analysis**: Model, architecture, core count, and real-time frequency/usage
- **Memory Metrics**: Total/available RAM, swap space, and utilization percentages
- **Storage Overview**: Partition details, capacity, and usage statistics

### System Profiling
- **OS Identification**: Platform, version, and hostname detection
- **Network Configuration**: Active interfaces and IP addresses
- **Temperature Monitoring** (where supported): Critical component temperatures

### Presentation
- **Interactive CLI**: Clean tabular output with `tabulate`
- **GUI Mode**: Optional Tkinter interface for visual learners
- **Export Ready**: Structured data perfect for logging or analysis

## 📦 Installation

```bash
# Install from PyPI (recommended)
pip install systemscan

# Or install directly
git clone https://github.com/yourusername/SystemScan.git
cd SystemScan
pip install -r requirements.txt
🚀 Usage
Basic CLI Mode
bash

python systemscan.py
Advanced Options
bash

# GUI Mode
python systemscan.py --gui

# Specific component focus
python systemscan.py --components cpu,memory

# Save to file
python systemscan.py --output system_report.txt
📊 Sample Output
text

==============================================
          SYSTEM DIAGNOSTICS REPORT          
==============================================

SYSTEM INFO:
+------------------+---------------------------+
| OS               | Windows 10 10.0.19045     |
| Hostname         | WORKSTATION-42           |
| Architecture     | AMD64 (64bit)            |
| Python Version   | 3.9.7                    |
+------------------+---------------------------+

CPU INFO:
+---------------------+-----------------------+
| Processor           | Intel Core i7-11800H  |
| Cores (P/L)         | 8/16                  |
| Frequency           | 2.90 GHz (4.60 Boost) |
| Current Usage       | 34.7%                 |
+---------------------+-----------------------+

MEMORY INFO:
+----------------+----------------+
| Total          | 31.7 GB        |
| Available      | 12.3 GB        |
| Used           | 61.2%          |
+----------------+----------------+
🛠️ Requirements
Package	Version	Purpose
psutil	≥5.8.0	System monitoring
py-cpuinfo	≥8.0.0	CPU identification
tabulate	≥0.8.9	Beautiful console output
Install with:


bash

pip install -r requirements.txt