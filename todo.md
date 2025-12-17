# install camelot 

pip install "camelot-py[cv]"


python3 -m http.server 8000 


# install server service in raspi
Ah! You want your Python HTTP server to run as a **systemd service** instead of LXDE autostart. This is actually cleaner and more reliable because the server will start at boot, run in the background, and restart automatically if it crashes.

Here’s how to do it:

---

### 1️⃣ Create a systemd service file

Run:

```bash
sudo nano /etc/systemd/system/solat-timer.service
```

Paste this:

```ini
[Unit]
Description=Solat Timer Python HTTP Server
After=network.target

[Service]
Type=simple
User=aziz
WorkingDirectory=/home/aziz/solat-timer
ExecStart=/usr/bin/python3 -m http.server 8000
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
```

**Explanation:**

* `User=aziz` → runs as your normal user (no `sudo` needed).
* `WorkingDirectory` → where your `time3.html` is located.
* `Restart=always` → if the server crashes, systemd will restart it automatically.
* `WantedBy=multi-user.target` → starts at boot after network is ready.

---

### 2️⃣ Enable and start the service

```bash
sudo systemctl daemon-reload
sudo systemctl enable solat-timer.service
sudo systemctl start solat-timer.service
```

---

### 3️⃣ Check status

```bash
systemctl status solat-timer.service
```

You should see something like:

```
Active: active (running) since ...
```

---

### 4️⃣ Optional: stop or restart

```bash
sudo systemctl stop solat-timer.service
sudo systemctl restart solat-timer.service
```

---

### 5️⃣ Chromium

Once the service is running, you can launch Chromium **separately** in kiosk mode. You can still use LXDE autostart for Chromium only:

```text
@xset s off
@xset -dpms
@xset s noblank
@/usr/bin/chromium-browser --noerrdialogs --kiosk http://localhost:8000/time3.html
```

This way, the **server is managed by systemd**, and **Chromium starts after your desktop is ready**.

---

If you want, I can write a **full solution that automatically waits for the server to be ready before launching Chromium**, using systemd + a tiny shell script. This makes the kiosk fully reliable.

Do you want me to do that?
