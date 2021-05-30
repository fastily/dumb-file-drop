# dumb-file-drop
[![Python 3.9+](https://upload.wikimedia.org/wikipedia/commons/4/4f/Blue_Python_3.9%2B_Shield_Badge.svg)](https://www.python.org)
[![License: GPL v3](https://upload.wikimedia.org/wikipedia/commons/8/86/GPL_v3_Blue_Badge.svg)](https://www.gnu.org/licenses/gpl-3.0.en.html)

Simple webserver which allows files to be uploaded to it.  Good for quickly sharing files on your local network.

Files will be uploaded to `./uploads`

## Install
```bash
pip install dumb-file-drop
```

## Run
```bash
# invoked directly from source
python -m dumb_file_drop

# if installed as a package
dfd
```

Endpoint: [localhost:5000](http://localhost:5000)

⚠️ Do not use this on public/untrusted networks!  There's no built-in authentication, so anybody could upload files to your computer!