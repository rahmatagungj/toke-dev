!["Two Original Key Encryption"](./Documentation/LOGO%20PANJANG%20WITH%20BG.png "Two Original Key Encryption")
<p align="center"> 
    <a href="https://www.python.org/"><img alt="made-with-python" src="http://ForTheBadge.com/images/badges/made-with-python.svg"></a>
</p>

# TOKE DEVELOPMENT 
This is the environment for developing the TOKE system, make sure everything is done according to development procedures and targets.

# INSTALLATION

    pip install -r requirements.txt

# BEFORE BUILD
1. Run unit_text.py and make sure all functions have been checked in ok condition
    
# BUILD

KEY = 'toke10-01-2021'

### METHODE 1
1. Run [auto-py-to-exe](https://github.com/brentvollebregt/auto-py-to-exe)
2. Import [Config.json](https://github.com/rahmatagungj/toke-dev/blob/main/config.json)
3. Start Build
4. Make sure the program can run normally
5. Push into Github [TOKE](https://github.com/rahmatagungj/toke)

### METHODE 2
1. Run CMD in Windows 
2. Execution this command

		pyinstaller --noconfirm --onefile --console --icon "F:/ALGORITHM/toke-dev/Documentation/LOGO.ico" --name "TOKE" --ascii --clean --key "toke10-01-2021"  "F:/ALGORITHM/toke-dev/main.py"

3. Make sure the program can run normally
4. Push into Github [TOKE](https://github.com/rahmatagungj/toke)

Note : Make sure the directory location of the 'main.py' file and the ICON file are set.

## Notes
1. The TOKE application can only run on the windows platform.
