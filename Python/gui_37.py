""" Created by danaeder at 29/10/2020 """
import os
import tkinter as tk
import tkinter.ttk


class KissGui():

    def __init__(self, window=None, data=None):
        self.main_color = 'MistyRose2'
        self.button_color = 'snow2'
        self.window = tk.Tk()
        self.var = tk.StringVar()
        self.var.set("one")
        self.data = self.get_all_tests()
        self.selected = []
        self.box_value = tk.StringVar()
        self.lable_value = tk.StringVar()
        self.lable_value_results = tk.StringVar()

        right = tk.Frame(self.window, bg=self.main_color)
        left = tk.Frame(self.window, bg=self.main_color)
        right.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH, ipadx=10)
        left.pack(side=tk.BOTTOM, expand=True, fill=tk.BOTH, ipadx=10)

        # Add Text info
        self.lable = tk.Label(self.window, textvariable=self.lable_value, bg=self.main_color, foreground='black')
        self.lable_value.set("Thank you for using KISS, Please select your tests")
        self.lable.pack(in_=left, pady=15, ipadx=15)

        # Add Dropdown
        self.cb = tk.ttk.Combobox(self.window, textvariable=self.box_value, values=self.data)
        self.cb.pack(in_=left, pady=5)

        # Add a button for adding a test
        self.b = tk.Button(self.window, text="Add Test", command=self.add_test, bg=self.button_color)
        self.b.pack(in_=left, pady=5)

        # Add a list block for the tests
        self.lb = tk.Listbox(self.window, height=10)
        self.lb.pack(in_=left, pady=5)

        # Add a button for removing a test
        self.b = tk.Button(self.window, text="Remove", command=self.remove_test, bg=self.button_color)
        self.b.pack(in_=left, side=tk.TOP, pady=5)

        # Add a button for running a test
        self.b = tk.Button(self.window, text=" Run ", command=None, bg=self.button_color)
        self.b.pack(in_=right, side=tk.TOP, pady=10)

        # Add text for the test result
        self.txtlb = tk.Label(self.window, textvariable=self.lable_value_results, bg=self.main_color,
                              foreground='black',
                              relief=tk.RAISED, pady=200)
        # change pady after run
        self.lable_value_results.set("Test Results will be placed here")
        self.txtlb.pack(in_=right, pady=15, ipadx=15)

        # Add Chackbox
        self.C1, self.C2 = self.add_checkbox()
        self.C1.pack(in_=left, side=tk.LEFT, pady=5, padx=5)
        self.C2.pack(in_=left, side=tk.LEFT, pady=5, padx=5)

        # Starting Window
        self.window.title('KISS GUI')
        self.window.geometry("600x400+20+20")
        self.window.attributes('-alpha', 0.97)
        self.window.mainloop()

    def add_radiobutton(self):
        v0 = tk.IntVar()
        v0.set(1)
        r1 = tk.Radiobutton(self.window, text="male", variable=v0, value=1)
        r2 = tk.Radiobutton(self.window, text="female", variable=v0, value=2)
        r1.place(x=100, y=50)
        r2.place(x=180, y=50)

    def add_checkbox(self):
        v1 = tk.IntVar()
        v2 = tk.IntVar()
        C1 = tk.Checkbutton(self.window, text="Cambria", variable=v1, bg=self.main_color)
        C2 = tk.Checkbutton(self.window, text="Admiral", variable=v2, bg=self.main_color)
        return C1, C2

    def get_all_tests(self):
        test_path = os.getcwd() + r'\Testing'
        onlytests = []
        if os.path.exists(test_path):
            for (dirpath, dirnames, filenames) in os.walk(test_path):
                onlytests.extend([test for test in filenames if test.__contains__("test_")])
        else:
            onlytests = ["fake_test.py", "fake2_test.py", "fake3_test.py", "fake4_test.py", "fake5_test.py",
                         "fake6_test.py", ]
        return onlytests

    def add_test(self):
        test = self.box_value.get()
        self.selected.append(test)
        self.lb.insert(tk.END, test)

    def remove_test(self):
        test = self.lb.get(tk.ACTIVE)
        self.selected.remove(test)
        idx = self.lb.get(0, tk.END).index(test)
        self.lb.delete(idx)


if __name__ == '__main__':
    gui_test = KissGui()
