"""
This file was created for DanaEder
Author:
    Dana Eder
Date:
08/12/19
Purpose:
  weekly
"""
import datetime
import os
import time

import pyautogui

week_dict = {'1': '31', '2': '28', '3': '31', '4': '30', '5': '31', '6': '30', '7': '31', '8': '31', '9': '30',
             '10': '31', '11': '30', '12': '31'}


class Weekly(object):

    def open_outlook(self, user, start, end):
        """

        Args:
            user:
            start:
            end:

        Returns:

        """
        cmd = "start outlook.exe"
        # Open outlook
        args = [" "]
        os.system(cmd)
        # Our Surface is not that fast
        time.sleep(15)

        # Go to Calendar
        pyautogui.hotkey('alt', 'q')
        # Our Surface is not that fast
        time.sleep(5)
        pyautogui.press(list('calendar'))
        time.sleep(2)
        pyautogui.hotkey('enter')
        # Our Surface is not that fast
        time.sleep(10)
        # Export
        pyautogui.hotkey('alt')
        pyautogui.press('f')
        pyautogui.press('o')
        pyautogui.press('i')
        # Our Surface is not that fast
        time.sleep(5)
        pyautogui.hotkey('up')
        pyautogui.hotkey('up')
        pyautogui.hotkey('up')
        # Our Surface is not that fast
        time.sleep(1)
        pyautogui.hotkey('enter')
        time.sleep(1)

        pyautogui.hotkey('enter')
        time.sleep(1)
        pyautogui.hotkey('enter')


        time.sleep(1)
        pyautogui.press(list(user))
        time.sleep(1)
        pyautogui.hotkey('enter')
        time.sleep(1)
        pyautogui.hotkey('enter')



        time.sleep(2)
        pyautogui.press(list(start))
        pyautogui.hotkey('tab')
        pyautogui.press(list(end))
        pyautogui.hotkey('enter')
        time.sleep(10)
        os.system(command=user)

    def get_times(self):
        time_now = datetime.datetime.now()
        ww = int(time_now.date().strftime("%V"))-1
        d=f"{time_now.year}-W{ww}"
        r = datetime.datetime.strptime(d+'-1',"%Y-W%W-%w")
        start_str=None
        if r.day==1:
            if r.month==1:
                start_year=r.year-1
                start_str=f"12/30/{start_year}"
            else:
                start_mon=r.month-1
                start_day=int(week_dict[str(r.month)])-1
                start_str=f"{start_mon}/{start_day}/{r.year}"
        if not start_str:
            start_str=f"{r.month}/{r.day-1}/{r.year}"
        end_str=f"{time_now.month}/{time_now.day}/{time_now.year}"
        return start_str, end_str, ww

    def get_user(self):
        command = "Powershell.exe $env:UserName"
        user = os.popen(command).read()
        user = user.replace('\n', "")

        user=f"C:\\Users\\{user}\\Documents"
        return user


if __name__ == '__main__':
    w = Weekly()
    my_user = w.get_user()
    start,end,ww = w.get_times()
    ww=f"WW{ww}.csv"
    user=os.path.join(my_user,ww)
    if os.path.exists(user):
        user=os.path.join(my_user,f"Copy_{ww}")
    w.open_outlook(user,start,end)
