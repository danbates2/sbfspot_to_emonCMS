# SBFspot_to_emonCMS
Python script to interface SBFspot and emonCMS, by reading the sbfspot database and then make a HTTP request to emonCMS.

. Works only by sending the most recent datapoint.

. To get this working with SBFspot installed, this script placed in /home/pi/scripts make it exacutable $ sudo chown 755 sbfspot_to_emonCMS.py and $ crontab -e newline added:

__*/5 * * * * python /home/pi/scripts/sbfspot_to_emonCMS.py > /dev/null__

. The */5 is the interval in minutes, matching the SBFspotUploadDaemon default recommendation.

. User must modify the script to include the emonCMS API Write key.

. With emonCMS already installed on a rPi, SBFspot will run fine. Tested using the default SQLite.

. With emonCMS Oct2017.img, the default SBFspot folder locations need changing during install from /home/pi/smadata to /home/pi/data/smadata, for write permissions to not throw errors. This will need changing in both SBFspot conf, and SBFspotUploadDaemon conf.

. Included in the script folder is an example database and my python learning steps to complete this.


Possible Improvement : Another one-time script could be made to upload the whole database to emonCMS using the bulk-upload API.

Big thanks to these guys: https://community.openenergymonitor.org/t/sbfspot/8245
