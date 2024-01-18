# :robot: Blink: Test the SSH Connection

## 🤓 Overview and learning outcomes 

Throughout the year, we will be writing Python scripts to control external hardware.  In order to do this we will need to create a Secure Shell (SSH) connection from the Chromebook to your Raspberry Pi.  Some improtant things to remember when using SSH:
1. The Chromebook and the Raspberry Pi should be on the same wifi network.  By default, the Pi will join the Mechlab network.  All you need to do is join the same.  If you go home and try to SSH in to the Pi you will need to change the settings on the Pi.  There are a number of ways to do this:
    - If you have a monitor, keyboard and mouse, that is pretty easy.  Go in to the pi and change it with the desktop GUI or go into the terminal and type `sudo raspi-config` and work through the menu there.
    - If you do not, go to the section of [this article](https://www.tomshardware.com/reviews/raspberry-pi-headless-setup-how-to,6028.html) called "Editing Wi-Fi on a Prewritten Card" and follow those steps.
2. You will need an app installed on your Chromebook called [Secure Shell](https://chromewebstore.google.com/detail/secure-shell/iodihamcpbpeioajjeobimgagajmlibd?pli=1).  We will work through how to use this in class.
3. Remember that you will only be using the command line prompt with this app.  While we will not set up a GUI for the SSH process in class, you can find ways to do it.  [This article from HowtoGeek](https://www.howtogeek.com/141157/how-to-configure-your-raspberry-pi-for-remote-shell-desktop-and-file-transfer/) is pretty helpful.

This first script will use the equipment in the bag with "Python Demo" written on it. If you closed the SSH connection to the Pi from the earlier section, re-connect it. 🚀

## Set up the circuit:
![The Python Demo Circuit](https://github.com/WHS-Robotics-Test-Org/Robotics_Engineering_Book/blob/master/Images/Python_demo.jpg)

## Prerequisites: 
  1. SSH connection to your Raspberry Pi (Using the Secure Shell App)
  2. Install Git on your Raspberry Pi (Should already be installed)
  3. Personal access token created on your GitHub account for all repos.  To do this, follow the steps found [here](https://docs.github.com/en/github/authenticating-to-github/keeping-your-account-and-data-secure/creating-a-personal-access-token).
    
## How to execute code (from the terminal window in the SSH application):

Type the commands below into your terminal window.  Replace [username] with your username on GitHub:

    git clone https://github.com/WHS-Robotics-Engineering-2021-22/blink-led-python-[username]
    
Change the working directory to the now one that you just cloned. Replace [username] with your username on GitHub.

    cd blink-led-python-[username]

When prompted for them, enter your github username and personal access token created in step 3 above.

Run the Python script using root access (sudo).

    sudo python main.py

## 📝 Next steps

If you have a blinking LED, everything works fine. If not, go back through the steps to make sure you set everything up correctly.

  1. Make a new .md file in this repository named "results.md".
  2. In your own words, describe what the prototype is doing.
  3. Make a video showing that it works and add it to the results.md file.

## 📚  Resources 

To see what each pin on the Raspberry Pi is named, type `pinout` in the terminal.  There are also many online resources to help with that.

### How to change GPIO pin:
  Change pin number in this line as per your requirements.  
  led = 12 # GPIO pin number is 12 and name is GPIO18
