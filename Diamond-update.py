import os
import sys
import time
import random
import shutil

# ====== COLORS ======
R = '\033[1;31m'; G = '\033[1;32m'; Y = '\033[1;33m'
B = '\033[1;34m'; C = '\033[1;36m'; M = '\033[1;35m'
W = '\033[1;37m'; K = '\033[90m'; RESET = '\033[0m'

def clear():
    os.system('clear' if os.name != 'nt' else 'cls')

def typewrite(text, delay=0.007):
    for ch in text:
        sys.stdout.write(ch); sys.stdout.flush(); time.sleep(delay)
    print()

def spinner(title, secs=2.0):
    frames = ['|','/','-','\\']
    sys.stdout.write(Y + title + " ")
    t0 = time.time(); i = 0
    while time.time() - t0 < secs:
        sys.stdout.write(frames[i % 4]); sys.stdout.flush()
        time.sleep(0.10); sys.stdout.write('\b'); i += 1
    print(G + "✓" + RESET)

def progress_bar(title, width=36, duration=1.6):
    sys.stdout.write(C + title + "\n")
    steps = max(1, int(duration / 0.04))
    for i in range(steps + 1):
        filled = int(i / steps * width)
        bar = "█" * filled + "░" * (width - filled)
        pct = int(i / steps * 100)
        sys.stdout.write(M + f"[{bar}] {pct:3d}%\r" + RESET)
        sys.stdout.flush()
        time.sleep(0.04)
    print()

def neon_banner():
    clear()
    neon = [
        f"{M}██████╗ ███████╗███████╗     ██╗██╗ ███████╗ ██████╗",
        f"{C}██╔══██╗██╔════╝██╔════╝     ██║██║ ██╔════╝██╔════╝",
        f"{B}██████╔╝█████╗  █████╗       ██║██║ █████╗  ██║     ",
        f"{G}██╔═══╝ ██╔══╝  ██╔══╝  ██   ██║██║ ██╔══╝  ██║     ",
        f"{Y}██║     ███████╗███████╗ ╚█████╔╝██║ ███████╗╚██████╗",
        f"{R}╚═╝     ╚══════╝╚══════╝  ╚════╝ ╚═╝ ╚══════╝ ╚═════╝{RESET}"
    ]
    for ln in neon:
        print(ln); time.sleep(0.02)
    print(W + "                 H A C K I N G   W O R L D™" + RESET)
    print(K + "         Free Fire Diamond  • ROOT-ONLY (WORK)" + RESET)
    print(W + "────────────────────────────────────────────────────────\n")

def require_root():
    # Check effective UID (Unix)
    has_geteuid = hasattr(os, "geteuid")
    euid_ok = (os.geteuid() == 0) if has_geteuid else False
    # Fallback: presence of su/tsu binary
    su_path = shutil.which("su") or shutil.which("tsu")
    if not euid_ok and not su_path:
        print(R + "\n[✘] Root Access Not Found!" + RESET)
        print(Y + "[!] This tool requires ROOT. Open a root shell (e.g., 'tsu') and run again." + RESET)
        input(W + "\nPress Enter to exit…" + RESET)
        sys.exit(1)
    if has_geteuid and os.geteuid() != 0:
        print(R + "\n[✘] Not running as root (effective UID != 0)." + RESET)
        print(C + "Tip: In Termux run: " + W + "tsu" + C + " then: " + W + "python ff_diamond_root_v2.py" + RESET)
        input(W + "\nPress Enter to exit…" + RESET)
        sys.exit(1)
    # passed
    print(G + "[✓] Root privileges verified." + RESET)
    time.sleep(0.6)

def fake_edge_logs(uid, pkg):
    clusters = ["sg-core-1","in-mum-2","eu-fr-1","us-va-3","id-core-2","bd-edge-1"]
    events = [
        "Negotiating TLS … OK",
        "Fingerprint Sync … OK",
        "UID Validation … OK",
        "Queue Ticket … GRANTED",
        "Anti-Abuse Window … 83%",
        "Token … {tok}",
        "Preparing Wallet Bridge … READY"
    ]
    for ev in events:
        evf = ev.replace("{tok}", hex(random.getrandbits(44)))
        tag = random.choice(clusters)
        typewrite(C + f"[{tag}] {evf}  (uid:{uid})  pkg:{pkg}" + RESET, 0.006)
        time.sleep(0.07)

def confetti(lines=3, width=64):
    syms = ['✦','✧','✪','✺','✹','✱','✲']
    cols = [R,G,Y,B,C,M,W]
    for _ in range(lines):
        print("".join(random.choice(cols)+random.choice(syms)+RESET for _ in range(width)))
        time.sleep(0.02)

def save_log(uid, amount):
    try:
        os.makedirs("logs", exist_ok=True)
        path = f"logs/ff_work{int(time.time())}.log"
        with open(path, "w", encoding="utf-8") as f:
            f.write("HACKING WORLD — Free Fire Diamond  (WORK / ROOT)\n")
            f.write(f"uid={uid}\namount={amount}\n")
            f.write(f"time={time.ctime()}\n")
        return path
    except Exception:
        return None

def simulate_inject(uid, amount):
    progress_bar("[#] Preparing secure shard channels", 40, 1.8)
    print()
    total = 0
    goal = amount
    bar_len = 42
    print(M + f"[*] Streaming diamonds to UID {uid} (visual) …" + RESET)
    while total < goal:
        step = random.randint(max(10, goal//30), max(22, goal//12))
        total = min(goal, total + step)
        filled = int(total/goal*bar_len)
        bar = G + "█"*filled + RESET + "░"*(bar_len-filled)
        pct = int(total/goal*100)
        sys.stdout.write(C + f"Injected: {W}{total:>6}/{goal:<6}  {bar}  {pct:3d}%\r" + RESET)
        sys.stdout.flush()
        time.sleep(random.uniform(0.04, 0.09))
        if random.random() < 0.07:
            sys.stdout.write("\n" + Y + "[!] Minor rate-limit encountered — smoothing traffic\n" + RESET)
            time.sleep(0.45)
    print("\n")
    progress_bar("[#] Verifying delivery receipts", 30, 1.4)
    spinner("[✓] Clearing temporary artifacts", 1.6)

def finale(uid, amount):
    clear(); neon_banner(); confetti(4, 68)
    print(G + "✅ PROCESS COMPLETED (SIMULATION)" + RESET)
    print(W + f"Approximate Diamonds queued for UID {C}{uid}{W}: {G}{amount}{RESET}")
    print(K + "\nNOTE (বাংলা): এটি একটি  হ্যাকিং / সিমুলেশন মাত্র — বাস্তবে  ডায়মন্ড যোগ হয় ।" + RESET)
    path = save_log(uid, amount)
    if path:
        print(C + f"\n[log saved] → {W}{path}{RESET}")
    input(W + "\nPress Enter to exit…" + RESET)

def main():
    neon_banner()
    require_root()   # enforce root-only

    # cookie (fake) first
    print(W + "[+] Login Method: Cookie Session (WORK) " + RESET)
    cookie = input(Y + "[?] Paste Cookie (any text, WORK only): " + W).strip()
    if not cookie:
        print(R + "Cookie required for demo. Exiting." + RESET); time.sleep(1); return
    spinner("[✓] Validating cookie (visual)", 2.0)

    # uid
    uid = input(Y + "[+] Enter Free Fire UID: " + W).strip()
    if not uid:
        print(R + "UID required. Exiting." + RESET); time.sleep(1); return
    print(G + f"[✓] UID Verified: {uid}" + RESET)
    time.sleep(0.6)

    # choose package
    print(W + "\nSelect Diamond Package:" + RESET)
    packs = [("Starter", 1000), ("Pro", 5000), ("Elite", 10000), ("Ultra", 20000)]
    for i, (n, v) in enumerate(packs, 1):
        print(C + f"[{i}] {n:<7} → ~{v} Diamonds" + RESET)
    choice = input(Y + "Choose (1-4): " + W).strip()
    try:
        idx = max(1, min(4, int(choice)))
    except:
        idx = 2
    amount = packs[idx-1][1]
    print(G + f"\n[✓] Selected: {packs[idx-1][0]} (~{amount} Diamonds)" + RESET)
    time.sleep(0.6)

    # security checks (visual)
    fake_edge_logs(uid, amount)
    simulate_inject(uid, amount)
    finale(uid, amount)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(RESET + "\n\nInterrupted by user.\n")