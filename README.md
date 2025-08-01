

## 🧠 Why Use This?

Some VPS hosts claim "unmetered bandwidth" but silently throttle or suspend users with high download and low upload.  
This tool helps you **simulate heavy upload traffic** to:
- Avoid automatic throttling/suspension.
- Test bandwidth performance.
- Keep your traffic ratio healthy.

---

## ⚙️ Features

- 🔍 Auto-detects the fastest public upload test server
- ⚡ Custom upload size (MB) and interval (seconds)
- 🔁 Infinite loop (fake upload every X seconds)
- 🧪 Optional manual host override
- 📊 Shows real upload speed during host testing

---

## 📦 Requirements

- Python 3.x  
- No external libraries required

---

## 📂 Usage and download
```bash
bash <(curl -Ls https://raw.githubusercontent.com/hoseinlolready/Fake-Upload/refs/heads/main/Install.sh )
```

```bash
python3 fake_uploader.py [--host <host>] [--port <port>] [--size <MB>] [--interval <seconds>]
```

---

### 🔹 Example: Auto-select best host

```bash
python3 fake_uploader.py --size 100 --interval 1
```

Sends **100 MB** of random data every **1 second** to the best upload host it finds.

---

### 🔹 Example: Manual target

```bash
python3 fake_uploader.py --host speedtest.serverius.net --port 80 --size 50 --interval 3
```

---

## 🔧 Arguments

| Argument      | Description                                   | Default |
|---------------|-----------------------------------------------|---------|
| `--host`      | Target upload host (optional, auto-selects)  | auto    |
| `--port`      | TCP port to connect to                        | 80      |
| `--size`      | Upload size per request (in MB)               | 50      |
| `--interval`  | Seconds to wait between uploads               | 2       |

---

## 🌐 Public Upload-Friendly Targets (if needed)

- `speed.hetzner.de`
- `speedtest.serverius.net`
- `speedtest-sgp1.digitalocean.com`
- `speedtest.ftp.otenet.gr`

---

## ⚠️ Disclaimer

This tool is for **educational and diagnostic purposes only**.  
Do **not** use it to violate your hosting provider's **Terms of Service**.  
Use responsibly and ethically on servers you own or have permission to test.

---

## 🪪 License

MIT License © hoseinlol
