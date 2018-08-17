# sbfspot_to_emonCMS
python script to interface sbfspot and emonCMS, by reading sbfspot database and then make GET request to emonCMS

. With emonCMS already installed on a rPi, SBFspot will run fine. Tested using the default SBFspot SQLite.

. The default SBFspot folder locations will need changing during install from /home/pi/smadata to /home/pi/data/smadata, for write permissions to not throw errors. This will need changing in both SBFspot conf, and SBFspotUploadDaemon conf.
