import requests
import json
from tkinter import *
from tkinter import  messagebox as mb
from tkinter import ttk


def update_v_label(event):
    code = v_combobox.get()
    name = cur[code]
    v_label.config(text=name)


def update_b_label(event):
    code = b_combobox.get()
    name = cur[code]
    b_label.config(text=name)


def update_t_label(event):
    code = t_combobox.get()
    name = cur[code]
    t_label.config(text=name)


def exchange():
    t_code = t_combobox.get()
    b_code = b_combobox.get()
    v_code = v_combobox.get()

    if t_code and b_code:
        try:
            otvet1 = requests.get(f"https://open.er-api.com/v6/latest/{b_code}")
            otvet1.raise_for_status()
            data1 = otvet1.json()
            if t_code in data1['rates']:
                exchange_rate2 = data1['rates'][t_code]
                t_name = cur[t_code]
                b_name = cur[b_code]
                mb.showinfo("Курс обмена", f"Курс:{exchange_rate2:.2f}{t_name} за 1 {b_name}")
            else:
                mb.showerror("Ошибка!", f"Валюта {t_code} не найдена!")

            otvet2 = requests.get(f"https://open.er-api.com/v6/latest/{v_code}")
            otvet2.raise_for_status()
            data2 = otvet2.json()
            if t_code in data2['rates']:
                exchange_rate1 = data2['rates'][t_code]
                t_name = cur[t_code]
                v_name = cur[v_code]
                mb.showinfo("Курс обмена", f"Курс:{exchange_rate1:.2f}{t_name} за 1 {v_name}")
            else:
                mb.showerror("Ошибка!", f"Валюта {t_code} не найдена!")
        except Exception as e:
            mb.showerror("Ошибка", f"Произошла ошибка: {e}.")
    else:
        mb.showwarning("Внимание!", "Введите код валюты!")


cur = {
    'RUB':'Русский рубль',
    'EUR':'Евро',
    'GBP':'Британский фунт',
    'JPY':'Японская йена',
    'CNY':'Юань',
    'KZT':'Тенге',
    'UZS':'Узбекский сум',
    'CHF':'Швейцарский франк',
    'AED':'Дирхач ОАЗ',
    'CAD':'Канадский доллар',
    'USD':'Доллар'}


window = Tk()
window.title("Курсы обмен валют")
window.geometry("360x450")

Label(text="Базовая валют").pack(padx=10, pady=10)
b_combobox = ttk.Combobox(values=list(cur.keys()))
b_combobox.pack(padx=10, pady=10)
b_combobox.bind('<<ComboboxSelected>>', update_b_label)
b_label = ttk.Label()
b_label.pack(padx=10, pady=10)

Label(text="Вторая базовая валюта").pack(padx=10, pady=10)
v_combobox = ttk.Combobox(values=list(cur.keys()))
v_combobox.pack(padx=10, pady=10)
v_combobox.bind('<<ComboboxSelected>>', update_v_label)
v_label = ttk.Label()
v_label.pack(padx=10, pady=10)

Label(text="Целевая валюта").pack(padx=10, pady=10)
t_combobox = ttk.Combobox(values=list(cur.keys()))
t_combobox.pack(padx=10, pady=10)
t_combobox.bind('<<ComboboxSelected>>',update_t_label)
t_label = ttk.Label()
t_label.pack(padx=10, pady=10)

Button(text="Получите курс обмена", command=exchange).pack(padx=10, pady=10)

window.mainloop()








'''import pprint

result = requests.get("https://open.er-api.com/v6/latest/USD")
data = json.loads(result.text)
p = pprint.PrettyPrinter(indent=4)

p.pprint(data)'''













