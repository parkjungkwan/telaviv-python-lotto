import tkinter
from tkinter import ttk
import random
from tkinter import messagebox
check_number_list = []

def gen_number():
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

root = tkinter.Tk()
root.title("로또 번호 생성기")

svar_nums = tkinter.StringVar(root,)
l_nums = ttk.Label(root, textvariable = svar_nums)
b_gen = ttk.Button(root, text = "번호생성", command = gen_number)

for i in range(0, 45):
    x = i % 5
    y = i // 5
    temp_v = tkinter.IntVar(root)
    ttk.Label(root, text = i + 1).grid(row = y, column = x*2)
    check_number_list.append(temp_v)
    ttk.Checkbutton(root, variable = temp_v, onvalue = 1, offvalue = 0).grid(row = y, column = x*2 + 1)

l_nums.grid(row = 9, column = 0, columnspan = 10)
b_gen.grid(row = 10, column = 0, columnspan = 10)

root.mainloop()
        
        


