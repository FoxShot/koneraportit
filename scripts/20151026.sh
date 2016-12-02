#!/bin/bash

old="0"
while true; do
	tablet=`cat /sys/devices/platform/hp-wmi/tablet`
	if [[ $old != $tablet ]]
	then
		if test "$tablet" = 1
		then
			xrandr -o inverted
			xsetwacom set "Serial Wacom Tablet stylus" rotate half
		else
			xrandr -o normal
			xsetwacom set "Serial Wacom Tablet stylus" rotate none
		fi
		old=$tablet
	fi
	sleep 1s
done