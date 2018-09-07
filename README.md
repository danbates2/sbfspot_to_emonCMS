# SBFspot to emonCMS
Python script to interface SBFspot and emonCMS, by reading the most recent sbfspot database entry and then making a HTTP request to emonCMS.

https://github.com/SBFspot/SBFspot/

https://emoncms.org/

. Works only by sending the most recent datapoint.

. To get this working with SBFspot installed, this script placed in /home/pi/scripts make it exacutable $ sudo chown 755 sbfspot_to_emonCMS.py and $ crontab -e newline added:

__*/5 * * * * python /home/pi/scripts/sbfspot_to_emonCMS.py > /dev/null__

. The */5 is the interval in minutes, matching the SBFspotUploadDaemon default recommendation.

. User must modify the script to include their emonCMS API Write key.

. With emonCMS already installed on a rPi, SBFspot will run fine. Tested using the default SQLite.

. With emonCMS Oct2017.img, the default SBFspot folder locations need changing during install from /home/pi/smadata to /home/pi/data/smadata, for write permissions to not throw errors. This will need changing in both SBFspot conf, and SBFspotUploadDaemon conf.

. Included in the script folder is an example database and my python learning steps to complete this.


Possible Improvement : Another one-time script could be made to upload the whole database to emonCMS using the bulk-upload API.
Possible Improvement (minor) : To use the timestamp information to more accurately place the datapoints in time.

Big thanks to these guys: https://community.openenergymonitor.org/t/sbfspot/8245

Thank you developer(s) of SBFspot, and to their Raspberry Pi install guide, which have given me greater understanding of how my rPi worked under the hood.

*SBFspot is a tool for accessing the data stored in SMA solar inverters via bluetooth or ethernet.
