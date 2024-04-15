# sinotrack-gpx
Get gpx from sinotrack files

## Development
Developed in Python 3.10.9

* Dependencies installed

### Create virtual environment
```bash
python -m venv gpx_venv
Source gpx_venv/Scripts/activate
pip install -r requirements.txt
```

*In powershell Source is not mandarory. use .\gpx_venv\Scripts\Activate*

### Run
```bash
py sinotrack-csv-gpx.py
```

### Create executable

```bash
pyinstaller --onefile --windowed --icon=icon.ico sinotrack-csv-gpx.py
```

Get gpx from sinotrack from position report and download it from the web interface.


