import tkinter
from tkinter import ttk
import random
from tkinter import messagebox

class Lotto():
    def gen_number(check_number_list):
        # check_number_list = []
        except_nums = []
        for i in range(0,45):
            if check_number_list[i].get() == 1:
                except_nums.append(i+1)
            if len(except_nums) > 39:
                messagebox.showinfo(title = "--;;",message = "최소 6개의 숫자는 남겨주세요")
                return
            numbers = []
            while(len(numbers)<6):
                num = random.randint(1, 45)
                if num in except_nums or num in numbers:
                    continue
                numbers.append(num)
            numbers.sort()
            svar_nums.set(numbers)

