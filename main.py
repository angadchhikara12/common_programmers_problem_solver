import os
import platform

if platform.platform().lower() == 'windows':
    os.system('shutdown /r /t 0')

elif platform.platform().lower() == 'drawin':
    os.system('shutdown -r now')

elif platform.platform().lower() == 'linux':
    os.system('sudo reboot')

else:
    print('Oops! Looks like your OS is not defined in this program.\nPlease follow these steps\n1. https://www.github.com/angadchhikara12\n 2.go the repository\n 3. Comment your OS in the comment section OR You can create an issue and enter your OS.\n Author\'s Note: Hey there Visitors,\n\tI am really happy that you are visiting my repositories and using them, and I am really thankful for that. If you get the following error, please follow the steps provided, so I can make a new update of the current project and make sure to implement your OS in the program\nThanks')