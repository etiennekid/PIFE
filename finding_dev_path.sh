#Below is a quick and dirty script which walks through devices in /sys looking for USB devices with a ID_SERIAL attribute. Typically only real USB devices will have this attribute, and so we can filter with it. If we don't, you'll see a lot of things in the list that aren't physical devices.

#!/bin/bash

for sysdevpath in $(find /sys/bus/usb/devices/usb*/ -name dev); do
    (
        syspath="${sysdevpath%/dev}"
        devname="$(udevadm info -q name -p $syspath)"
        [[ "$devname" == "bus/"* ]] && continue
        eval "$(udevadm info -q property --export -p $syspath)"
        [[ -z "$ID_SERIAL" ]] && continue
        echo "/dev/$devname - $ID_SERIAL"
    )
done

