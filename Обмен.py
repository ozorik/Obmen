import requests
import json
from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk


def update_b_label(event):
    code = base_combobox.get()
    name = cur[code]
    b_label.config(text=name)


def update_t_label(event):
    code = target_combobox.get()
    name = cur[code]
    t_label.config(text=name)


def exchange():
    target_code = target_combobox.get().lower()
    base_code = base_combobox.get().lower()


    if target_code and base_code:
        try:
            #url = f'https://www.coingecko.com/api/btc'
            response = requests.get(f'https://api.coingecko.com/api/{base_code}')
            response.raise_for_status()
            data = response.json()

            if target_code in data['rates']:
                exchange_rate = data['rates'][target_code]
                base = cur[base_code]
                target = cur[target_code]
                mb.showinfo("Курс обмена", f"Курс {exchange_rate:.1f} {target} за 1 {base}")
            else:
                mb.showerror("Ошибка", f"Валюта {target_code} не найдена")
        except Exception as e:
            mb.showerror("Ошибка", f"Ошибка: {e}")
    else:
        mb.showwarning("Внимание", "Выберите коды валют")


cur = {
'etc': 'Российский рубль',
'btc': 'Евро',
'usd': 'Американский доллар'
}


window = Tk()
window.title("Курсы обмена валют")
window.geometry("360x420")

Label(text="Базовая валюта").pack(padx=10, pady=10)
base_combobox = ttk.Combobox(values=list(cur.keys()))
base_combobox.pack(padx=10, pady=10)
base_combobox.bind("<<ComboboxSelected>>", update_b_label)
b_label = ttk.Label()
b_label.pack(padx=10, pady=10)



Label(text="Целевая валюта").pack(padx=10, pady=10)
target_combobox = ttk.Combobox(values=list(cur.keys()))
target_combobox.pack(padx=10, pady=10)
target_combobox.bind("<<ComboboxSelected>>", update_t_label)
t_label = ttk.Label()
t_label.pack(padx=10, pady=10)

Button(text="Получить курс обмена", command=exchange).pack(padx=10, pady=10)

window.mainloop()


















