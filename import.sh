#!/bin/bash
#MUST be run as sudo 
for file in /home/pi/articles/*
	 do php importDump.php $file;
done
