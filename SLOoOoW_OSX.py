import subprocess
import sys
import time
import signal
import re

# 🐌 SLOoOoW - macOS Edition
# Systematic Lag Over... oh... Oh... oh... Wait.

def print_banner():
    print(r"""
   _____ _      ____        ____      _       __
  / ___/| |    / / __ \____/ __ \____| |     / /
  \__ \ | |   / / / / / __ \/ / / __ \ | /| / / 
 ___/ / | |___/ / /_/ / /_/ / /_/ / /_/ |/ |/ /  
/____/  |_____/\____/\____/\____/\____/|__/|__/   
                                                  
    [ macOS Edition ]
    """)
    print("Systematic Lag Over... oh... Oh... oh... Wait.\n")

# --- Configuration & Presets ---
PRESETS = {
    "1": {"name": "GPRS (1 Bar)",     "bw": "50Kbit",  "delay": 700, "loss": 5},
    "2": {"name": "2G (EDGE)",        "bw": "250Kbit", "delay": 400, "loss": 1},
    "3": {"name": "3G (HSPA)",        "bw": "3Mbit",   "delay": 150, "loss": 0.1},
    "4": {"name": "4G (LTE)",         "bw": "20Mbit",  "delay": 50,  "loss": 0},
    "5": {"name": "5G (Low Latency)", "bw": "100Mbit", "delay": 10,  "loss": 0},
    "s": {"name": "Starlink (LEO)",   "bw": "150Mbit", "delay": 40,  "loss": 0.5},
    "l": {"name": "Legacy Sat (GEO)", "bw": "15Mbit",  "delay": 600, "loss": 0.5},
    "w": {"name": "Public Wi-Fi",     "bw": "2Mbit",   "delay": 100, "loss": 2},
    "d": {"name": "Dial-up",          "bw": "56Kbit",  "delay": 200, "loss": 0},
    "6": {"name": "6G (Theoretical)", "bw": "1Gbit",   "delay": 1,   "loss": 0},
}

def run_command(cmd):
    """Runs a shell command and hides output unless there is an error."""
    try:
        subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        print(f"[-] Error running command: {cmd}")
        print(e.output.decode())
        sys.exit(1)

def reset_network():
    """Flushes dnctl pipes and pfctl rules to restore speed."""
    print("\n[+] Restoring network speed... (Back to the rat race)")
    
    # 1. Flush dummynet pipes
    run_command("sudo dnctl -q flush")
    
    # 2. Reset Packet Filter (pf)
    # Note: This clears custom anchors. If you use a complex firewall setup, 
    # you might want to be more specific, but for dev machines, this is standard.
    run_command("sudo pfctl -F all 2>/dev/null") 
    
    print("[+] Done. You are fast (and stressed) again.")

def signal_handler(sig, frame):
    reset_network()
    sys.exit(0)

def apply_slowness(bw, delay, loss):
    """
    Applies the rules using dnctl and pfctl.
    macOS Logic:
    1. Create a pipe in dnctl with bandwidth/delay/loss.
    2. Use pfctl to route traffic into that pipe.
    """
    print(f"\n[+] Injecting Chaos: {bw}, {delay}ms delay, {loss}% loss...")

    # Convert percentage to ratio (0.0 - 1.0) for dnctl
    loss_ratio = float(loss) / 100.0

    # Step 1: Configure the pipe (Pipe #1)
    # plr = Packet Loss Rate
    dnctl_cmd = f"sudo dnctl pipe 1 config bw {bw} delay {delay} plr {loss_ratio}"
    run_command(dnctl_cmd)

    # Step 2: Enable Packet Filter
    # We use 'token' to ensure we don't error if it's already enabled
    try:
        run_command("sudo pfctl -E 2>/dev/null") 
    except:
        pass # It might already be enabled

    # Step 3: Route traffic into the pipe
    # "dummynet on any" means apply to all interfaces
    pf_rule = "dummynet in quick proto tcp from any to any pipe 1"
    
    # We echo the rule into pfctl
    run_command(f"echo '{pf_rule}' | sudo pfctl -f -")

    print("[!] Network is SLOoOoW. Press CTRL+C to stop.")
    
    # Keep script running
    while True:
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            reset_network()
            sys.exit(0)

def main():
    # Catch CTRL+C
    signal.signal(signal.SIGINT, signal_handler)

    if subprocess.call("whoami | grep root", shell=True, stdout=subprocess.DEVNULL) != 0:
        print("[-] You must run this script as root (sudo).")
        print("    Try: sudo python3 slow_mac.py")
        sys.exit(1)

    print_banner()
    print("Choose your suffering:")
    for key, val in PRESETS.items():
        print(f" [{key}] {val['name']:<18} ({val['bw']}, {val['delay']}ms, {val['loss']}%)")

    choice = input("\nSelect preset > ").lower().strip()

    if choice in PRESETS:
        p = PRESETS[choice]
        
        # Allow custom tweaks
        confirm = input(f"Selected {p['name']}. Edit chaos? (y/N) > ").lower()
        
        bw = p['bw']
        delay = p['delay']
        loss = p['loss']

        if confirm == 'y':
            print("\n--- Customizing (Press Enter to keep default) ---")
            new_bw = input(f"Bandwidth ({bw}): ")
            new_delay = input(f"Delay ms ({delay}): ")
            new_loss = input(f"Packet Loss % ({loss}): ")

            if new_bw: bw = new_bw
            if new_delay: delay = int(new_delay)
            if new_loss: loss = float(new_loss)

        apply_slowness(bw, delay, loss)
    else:
        print("[-] Invalid selection.")

if __name__ == "__main__":
    main()