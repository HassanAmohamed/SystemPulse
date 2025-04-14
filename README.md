# System Information Script

This Python script retrieves and displays system information, including CPU details, memory usage, and more. It uses the `psutil` and `py-cpuinfo` libraries to gather the data and presents it in a clear format using `tabulate`.

## Features

- Retrieve and display CPU information (model, cores, frequency).
- Get memory usage statistics (total, available, used).
- Present information in a user-friendly table format.

## Requirements

Make sure you have Python installed on your system. This script requires the following libraries:

- `psutil`
- `py-cpuinfo`
- `tabulate`

You can install the required packages using:

```bash
pip install psutil py-cpuinfo tabulate
Usage
Clone the repository or download the script.
Navigate to the script directory in your terminal.
Run the script using Python:


bash

python system_info.py


Example Output


+----------------+---------------------+
|     Parameter   |        Value        |
+----------------+---------------------+
| CPU Model      | Intel Core i7-9700 |
| Cores          | 8                   |
| Frequency      | 3.0 GHz             |
| Total Memory   | 16 GB               |
| Used Memory    | 8 GB                |
| Available Memory| 8 GB               |
+----------------+---------------------+
License
This project is licensed under the MIT License. See the LICENSE file for more details.

Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.
