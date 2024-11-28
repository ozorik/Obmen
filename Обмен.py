import requests
from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk


def update_b_label(event):
    code = base_combobox.get()
    name = cur1[code]
    b_label.config(text=name)


def update_t_label(event):
    code = target_combobox.get()
    name = cur2[code]
    t_label.config(text=name)


def exchange():
    target_code = target_combobox.get().lower()
    base_code = base_combobox.get().lower()


    if target_code and base_code:
        try:
            #создаем путь откуда берем информацию
            response = requests.get(
                f"https://api.coingecko.com/api/v3/simple/price?ids={base_code}&vs_currencies={target_code}")
            response.raise_for_status()
            data = response.json()
            #код программы
            if target_code in data[base_code]:
                exchange_rate = data[base_code][target_code]
                base = cur1[base_code]
                target = cur2[target_code]
                mb.showinfo("Курс обмена", f"Курс {exchange_rate:.1f} {target} за 1 {base}")
            else: #проверка на неправельное написание
                mb.showerror("Ошибка", f"Валюта {target_code} не найдена")
        except Exception as e: # проверка на ошибки
            mb.showerror("Ошибка", f"Ошибка: {e}")
    else: #проверка на ввод данных
        mb.showwarning("Внимание", "Выберите коды валют")


#словарь криптовалют
cur1 = {
    "bitcoin": "Bitcoin",
    "ethereum": "Ethereum",
    "ripple": "Ripple",
    "litecoin": "Litecoin",
    "cardano": "Cardano"
}


#словарь валют
cur2 = {
    'rub': 'Российский рубль',
    "eur": "Евро",
    'usd': 'Американский доллар'
}


#Создаем основное окно
window = Tk()
window.title("Курсы обмена валют")
window.geometry("360x420")

#Строка для ввода начальной валюты(криптовалюты)
Label(text="Базовая криптовалюта").pack(padx=10, pady=10)
base_combobox = ttk.Combobox(values=list(cur1.keys()))
base_combobox.pack(padx=10, pady=10)
base_combobox.bind("<<ComboboxSelected>>", update_b_label)
b_label = ttk.Label()
b_label.pack(padx=10, pady=10)

#Строка для ввода конечной валюты
Label(text="Целевая валюта").pack(padx=10, pady=10)
target_combobox = ttk.Combobox(values=list(cur2.keys()))
target_combobox.pack(padx=10, pady=10)
target_combobox.bind("<<ComboboxSelected>>", update_t_label)
t_label = ttk.Label()
t_label.pack(padx=10, pady=10)

#кнопка магии
Button(text="Получить курс обмена", command=exchange).pack(padx=10, pady=10)

window.mainloop()


















