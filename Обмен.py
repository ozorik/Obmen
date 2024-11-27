import requests
import json
from tkinter import *
from tkinter import  messagebox as mb
from tkinter import ttk

def update_c_label(event):
    code = combobox.get()
    name = cur[code]
    c_label.config(text=name)


def exchange():
    code = combobox.get()

    if code:
        try:
            otvet = requests.get("https://open.er-api.com/v6/latest/RUB")
            otvet.raise_for_status()
            data = otvet.json()
            if code in data['rates']:
                exchange_rate = data['rates'][code]
                c_name = cur[code]
                mb.showinfo("Курс обмена", f"Курс:{exchange_rate:.2f}{c_name} за 1 доллар")
            else:
                mb.showerror("Ошибка!", f"Валюта {code} не найдена!")
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
    'CAD':'Канадский доллар'}


window = Tk()
window.title("Курсы обмен валют")
window.geometry("360x180")

Label(text="Выберете код валюты").pack(padx=10, pady=10)

combobox = ttk.Combobox(values=list(cur.keys()))
combobox.pack(padx=10, pady=10)
combobox.bind('<<ComboboxSelected>>',update_c_label)

c_label = ttk.Label()
c_label.pack(padx=10, pady=10)

Button(text="Получите курс обмена к доллару", command=exchange).pack(padx=10, pady=10)

window.mainloop()








'''import pprint

result = requests.get("https://open.er-api.com/v6/latest/USD")
data = json.loads(result.text)
p = pprint.PrettyPrinter(indent=4)

p.pprint(data)'''













