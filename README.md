# python-speedtest
perform speedtest in certain intervals using python


1. Install python 3.x in windows  - https://www.python.org/downloads/
2. Run `python` to check if the installed version is 3.x and can be run from cmd
3. Go to the installation directory `cd python-speedtest`
4. Run `python -m pip install -r requirements.txt`
5. Run the script `python python-speedtest.py`

The script will run speedtest every 5 mins, you can increase this time by increasing the sleep duration in script.
It will save log data in log.txt

Saving data to csv is implemented. Data can be found in `data.csv` file and creating graph is not implemented yet.
