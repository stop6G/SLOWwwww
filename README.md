
# 🐌 SLOWwwww

**S**ystematic **L**ag **O**ver **W**orld-wide-web... *wait... wait...*

A lightweight Python wrapper for the Linux Traffic Control (`tc`) subsystem. This tool allows people to turn their fast connection into a **Sanctuary of Lag** 🧘.

Instead of rushing through the web, simulate **Starlink** jitters, **2G** dropouts, or **Satellite** latency. We even included a theoretical  fucking **6G** preset for the speed addicts, though honestly, where is the fun in that? (fuck it!) 
Take a deep breath and **enjoy the slowness**.

## 🖕 Fuck Efficiency

We are obsessed with "Hi-Tech.". 
We love "Performance." 
We measure milliseconds and worship efficiency.
The real world is a 3G signal in a basement.
It's a crowded coffee shop Wi-Fi.
It is messy, chaotic, and **slow**.
In a world of instant gratification, we have forgotten the art of waiting
With 600ms latency, every interaction becomes intentional.
Watch a progress bar fill up pixel by pixel. Feel the anticipation.
Reclaim your coffee break. Select the *Dial-up* preset, hit enter, and go brew a fresh pot while your dependencies install
Sometimes
to
go
fast,
you
have
to
go
SLOWwwww


## 🚀 Features

* **Pre-configured Presets:** Simulate real-world scenarios like GPRS, 4G, Starlink, or Dial-up.
* **Chaos Engineering:** Automatically injects realistic **Jitter** and **Packet Loss** based on the chosen technology.
* **Custom Mode:** Manually define your own bandwidth, delay, and loss parameters.
* **Safe Reset:** Automatically restores full internet speed when the script exits (CTRL+C).
* **Technology Groups:** Organized by Cellular, Satellite, Wired, and Theoretical (6G) standards.

## 📋 Prerequisites

This tool requires **Linux** :). It relies on the kernel's `netem` (Network Emulator) module.

1.  **Python 3.6+**
2.  **Root Privileges** (Required to modify network interface settings)
3.  **iproute2** (Usually installed by default on Ubuntu/Debian/Fedora)

To check if you have the required tools:
```bash
tc -V
python3 --version

```

If `tc` is missing, install it:

```bash
# Ubuntu / Debian / Kali
sudo apt install iproute2

# Fedora / CentOS
sudo dnf install iproute-tc

# Arch Linux
sudo pacman -S iproute2

```

## 🛠️ Installation

1. Clone this repository:
```bash
git clone [https://github.com/stop6G/SLOWwwww.git](https://github.com/STOP6G/SLOWwwww.git)
cd SLOWwwww

```


2. Make sure the script is executable (optional):
```bash
chmod +x SLOWwwww.py

```



## 💻 Usage

⚠️ **Note:** You must run this script with `sudo` because it modifies network driver settings.

1. **Start the tool:**
```bash
sudo python3 SLOWwwww.py

```


2. **Select a Preset:**
Type the key corresponding to the network you want to simulate (e.g., `s` for Starlink, `w` for Public Wi-Fi).
3. **Confirm Settings:**
The script will suggest realistic default Jitter/Loss values. Press **ENTER** to accept them, or type `edit` to customize them.
4. **Stop:**
Press `CTRL+C` to stop the simulation and restore your original internet speed.

## 📊 Presets Guide

| Key | Preset Name | Speed | Latency | Jitter | Packet Loss | Description |
| --- | --- | --- | --- | --- | --- | --- |
| **1** | GPRS (1 Bar) | 50 kbit | 700ms | 200ms | 5% | Extremely unstable rural connection. |
| **2** | 2G (EDGE) | 250 kbit | 400ms | 50ms | 1% | Stable but very slow mobile data. |
| **3** | 3G (HSPA) | 3 mbit | 150ms | 20ms | 0.1% | Basic mobile broadband. |
| **4** | 4G (LTE) | 20 mbit | 50ms | 10ms | 0% | Standard modern mobile speed. |
| **5** | 5G (Low Latency) | 100 mbit | 10ms | 1ms | 0% | Near perfect mobile connection. |
| **s** | Starlink (LEO) | 150 mbit | 40ms | 15ms | 0.5% | Fast but "jittery" due to satellite handovers. |
| **l** | Legacy Sat (GEO) | 15 mbit | 600ms | 60ms | 0.5% | High latency space internet (e.g., Viasat). |
| **w** | Public Wi-Fi | 2 mbit | 100ms | 80ms | 2% | Congested coffee shop / hotel Wi-Fi. |
| **d** | Dial-up | 56 kbit | 200ms | 30ms | 0% | Retro phone line connection. |
| **6** | 6G (Theoretical) | 1 Tbit | 0.1ms | 0ms | 0% | Removes all limits (Benchmark mode). |

## ⚠️ Disclaimer

This tool modifies your network interface queuing discipline (`qdisc`).

* **Do not run this on a production server** unless you know what you are doing; it will slow down connections for everyone accessing that server.
* If the script crashes or is killed forcefully (e.g., `kill -9`), your internet might remain slow. To fix this, simply run:
```bash
sudo tc qdisc del dev <your_interface> root

```



## 📄 License

This project is open source and available under the [MIT License](https://opensource.org/licenses/MIT).

```

```
