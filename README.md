# :robot: Blink: Test the SSH Connection

## 🤓 Overview and learning outcomes 

Throughout the year, we will be writing Python scripts to control external hardware.  This first script will use the equipment in the bag with "Python Demo" written on it. If you closed the SSH connection to the Pi from the earlier section, re-connect it. 🚀

## Set up the circuit:
![The Python Demo Circuit](https://github.com/WHS-Robotics-Test-Org/Robotics_Engineering_Book/blob/master/Images/Python_demo.jpg)

## Prerequisites: 
  1. SSH connection to your Raspberry Pi (Using the Secure Shell App)
  2. Install Git on your Raspberry Pi (Should already be installed)
  3. Personal access token created on your GitHub account for all repos:
    
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

  1. Make a new .md file in this repository named "results".
  2. In your own words, describe what the prototype is doing.
  3. Make a video showing that it works and add it to the results.md file.

## 📚  Resources 

To see what each pin on the Raspberry Pi is named, type `pinout` in the terminal.  There are also many online resources to help with that.

### How to change GPIO pin:
  Change pin number in this line as per your requirements.  
  led = 12 # GPIO pin number is 12 and name is GPIO18
