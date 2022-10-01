#!/bin/bash
# 1. Set wallpaper path
# Set wallpaperPath = %1

# 2. Get a link of a random wallpaper
downloadLink=$(python Parser.py)

# 3. Download from link to the path
wget --no-check-certificate -O wallpaper.jpg $downloadLink

#4. Set new wallpaper
feh --bg-scale wallpaper.jpg
