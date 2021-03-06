# python -m pip install speedtest-cli
import speedtest
import logging
import time
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

# Handler - 1
file = logging.FileHandler('log.txt')
fileformat = logging.Formatter(fmt='<br> %(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
file.setLevel(logging.DEBUG)
file.setFormatter(fileformat)

# Handler - 2
stream = logging.StreamHandler()
streamformat = logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
stream.setLevel(logging.INFO)
stream.setFormatter(streamformat)

# Adding all handlers to the logs
log.addHandler(file)
log.addHandler(stream)

from datetime import datetime

import csv
# fields = ['Time', 'Download', 'Upload', 'Ping']
filename = "log.csv"

s = speedtest.Speedtest()
with open(filename, 'a', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    # csvwriter.writerow(fields)
    while 1:
        log.info('Testing..')
        # s.get_servers()
        # s.get_best_server()
        s.download()
        s.upload()
        res = s.results.dict()
        log.debug(res)
        download = round(res["download"]/(1024*1024),2)
        upload = round(res["upload"]/(1024*1024),2)
        ping = round(res["ping"])
        client = res["client"]["isp"]
        country = res["client"]["country"]
        log.info("[+] Download Speed: %s Mbps", download)
        log.info("[+] Upload Speed: %s Mbps", upload)
        log.info("[+] Ping: %s", ping)
        log.info("[+] ISP: %s, %s", client,country)
        currentTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        data = [str(currentTime), str(download), str(upload), str(ping)]
        log.info(data)
        csvwriter.writerow(data)
        
        time.sleep(300)
