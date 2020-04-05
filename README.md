# dumb-file-drop
[![Python 3.7](https://upload.wikimedia.org/wikipedia/commons/f/fc/Blue_Python_3.7_Shield_Badge.svg)](https://www.python.org)
[![License: GPL v3](https://upload.wikimedia.org/wikipedia/commons/8/86/GPL_v3_Blue_Badge.svg)](https://www.gnu.org/licenses/gpl-3.0.en.html)

Simple webserver which allows files to be uploaded to it.  Good for quickly sharing files on your local network.

Files will be uploaded to `./uploads`

Run:
```bash
python dumb_file_drop.py
```

Endpoint: [localhost:5000](http://localhost:5000)

⚠️ Do not run this on public/untrusted networks!  There's no built-in authentication, so anybody could upload files to your computer!