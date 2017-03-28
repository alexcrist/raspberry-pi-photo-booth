# photo-booth
This is a project to make a home "photo booth" using a Raspberry Pi. Anytime somebody on the Pi's network goes to a website, the Pi snaps a photo and displays it on the website.

## How does it work?
The Pi uses Flask to run a simple Python web-server on the local network. Anytime another device on the network makes a GET request to the Pi's interanl IP address with the correct port, the Pi snaps a photo and serves it as a response. Additionally, the Pi saves all of the photos it takes.

## Set up

1. Download and install (Raspbian Jessie with Pixel)[https://www.raspberrypi.org/downloads/raspbian/] to your Pi
1. Connect your Pi to your network with an Ethernet cable and power it up
1. Find out your Pi's internal IP address (I like using Fing mobile app)
  * (Fing for Android)[https://play.google.com/store/apps/details?id=com.overlook.android.fing&hl=en]
  * (Fing for iOS)[https://itunes.apple.com/us/app/fing-network-scanner/id430921107?mt=8]
1. (Optional) SSH into your Pi from another computer on the network for the following steps
1. Log into your pi. If you are booted to the GUI, open up Terminal
1. Configure your pi, `sudo raspi-config`. You may have to dig around for some of the options below
  * Boot to CLI by default
  * Enable camera
  * Expand file system
  * Change password
1. Restart your pi, `sudo reboot`
1. Install Flask, `sudo pip install Flask`
1. Get the code, `git clone https://github.com/alexcrist/photo-booth.git`
1. Enter the code's folder, `cd photo-booth`
1. Make a folder to store the photos, `mkdir photos` (Note: exact name is important)
1. Edit `app.py` to use your Pi's internal IP address
  1. `nano app.py`
  1. Change `host='10.0.0.22'` on line 18 to be `host='YOUR PI'S INTERNAL IP ADDRESS'`
  1. Save the file, `Ctrl-X` -> `y`
1. Give `app.py` permissions, `sudo chmod app.py 755` (Note: I'm actually not sure if you need to do this)
1. Run `app.py`, `python app.py`
1. Your photo booth is now running! Try going to `http://PI_IP_ADDRESS:2222` from another device on the network

## To do

* Verify set up steps actually work
* Add some photos
* Add instructions on how to run `app.py` on boot using crontabs
* Modify `app.py` to automatically get the pi's internal IP address
