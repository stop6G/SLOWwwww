
# 🐌 SLOoOoW

**S**ystematic **L**ag **O**ver... **o**h... **O**h... **o**h... **W**ait.

**A lightweight cross-platform Python wrapper for Linux (`tc`) and macOS (`dnctl`).** This tool allows people to turn their fast connection into a **Sanctuary of Lag** 🧘.
<picture>
<source media="(prefers-color-scheme: dark)" srcset="dark-mode-image.png">
  <source media="(prefers-color-scheme: light)" srcset="light-mode-image.png">
  <img alt="Fallback image description" src="default-image.png">
</picture>

Instead of rushing through the web, simulate **Starlink** jitters, **2G** dropouts, or **Satellite** latency. We even included a theoretical  fucking **6G** preset for the speed addicts, though honestly, where is the fun in that? (fuck it!) 
Take a deep breath and **enjoy the slowness**.

## 🖕 Fuck Efficiency

We are obsessed with "Hi-Tech.".   
We love "Performance."   
We measure milliseconds and worship efficiency.  
The real world is a 3G signal in a basement.  
It's a crowded coffee shop Wi-Fi.  
It is messy, chaotic, and **slow**.  
In a world of instant gratification, we have forgotten the art of waiting.  
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
SLOoOoW


## 🚀 Features

* **Cross-Platform:** Works on **Linux** (via `tc` + `netem`) and **macOS** (via `dnctl` + `pfctl`).
* **Pre-configured Presets:** Simulate real-world scenarios like GPRS, 4G, Starlink, or Dial-up.
* **Chaos Engineering:** Automatically injects realistic **Jitter** and **Packet Loss** based on the chosen technology.
* **Custom Mode:** Manually define your own bandwidth, delay, and loss parameters 
* **Safe Reset:** Automatically restores full internet speed when the script exits (CTRL+C).
* **Technology Groups:** Organized by Cellular, Satellite, Wired, and Theoretical (6G) standards.



## 🛠️ Installation

1. Clone this repository:
```bash
git clone https://github.com/STOP6G/SLOWwwww.git  
cd SLOWwwww

```


## 🛠️ Usage

### 🐧 For Linux Users
*Requires `iproute2` installed.*

1.  Run the Linux script:
    ```bash
    sudo python3 SLOoOoW.py
    ```
2.  Follow the on-screen menu:


### 🍏 For Mac Users
*No installation required. Uses native macOS tools.*

1.  Run the Mac script:
    ```bash
    sudo python3 SLOoOoW_OSX.py
    ```
2.  Follow the on-screen menu:

## 📊 Presets Guide

| Key | Preset Name | Speed | Latency | Jitter/Loss | Description |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **1** | GPRS (1 Bar) | 50 kbit | 700ms | High | Extremely unstable rural connection. |
| **2** | 2G (EDGE) | 250 kbit | 400ms | Med | Stable but very slow mobile data. |
| **3** | 3G (HSPA) | 3 mbit | 150ms | Low | Basic mobile broadband. |
| **4** | 4G (LTE) | 20 mbit | 50ms | None | Standard modern mobile speed. |
| **5** | 5G (Low Latency)| 100 mbit| 10ms | None | Near perfect mobile connection. |
| **s** | Starlink (LEO) | 150 mbit | 40ms | Med | Fast but "jittery" due to satellite handovers. |
| **l** | Legacy Sat (GEO) | 15 mbit | 600ms | High | High latency space internet (e.g., Viasat). |
| **w** | Public Wi-Fi | 2 mbit | 100ms | Med | Congested coffee shop / hotel Wi-Fi. |
| **d** | Dial-up | 56 kbit | 200ms | None | Retro phone line connection. |
| **6** | 6G (Theoretical) | 1 Tbit | 0.1ms | None | Removes all limits (Benchmark mode). |

## ⚠️ Disclaimer

This tool modifies your network interface settings.
* **Do not run this on a production server** unless you know what you are doing.
* If the script crashes or is killed forcefully, your internet might remain slow.
    * **Linux Fix:** `sudo tc qdisc del dev <interface> root`
    * **Mac Fix:** `sudo dnctl -q flush && sudo pfctl -F all`

## 📄 License

This project is open source and available under the [MIT License](https://opensource.org/licenses/MIT).
