from tkinter import *
import tkinter as tk
from tkinter import ttk
import urllib.request
import xml.dom.minidom
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import datetime

def update_currency_list():
    today_date = datetime.datetime.now()
    today_data = today_date.strftime("%d/%m/%Y")
    url = f"http://www.cbr.ru/scripts/XML_daily.asp?date_req={today_data}"
    response = urllib.request.urlopen(url)
    dom = xml.dom.minidom.parse(response)
    dom.normalize()
    currencies = dom.getElementsByTagName("Valute")
    currency_names = []
    currency_values = {}
    for currency in currencies:
        name = currency.getElementsByTagName("Name")[0].firstChild.nodeValue
        value = float(currency.getElementsByTagName("Value")[0].firstChild.nodeValue.replace(',', '.'))
        nominal = int(currency.getElementsByTagName("Nominal")[0].firstChild.nodeValue)
        currency_values[name] = value / nominal
        currency_names.append(name)
    combo1_1["values"] = currency_names
    combo1_2["values"] = currency_names
    combo2_1["values"] = currency_names
    return currency_values

window = tk.Tk()
window.title("Конвертер Валют")
window.geometry("500x300")

'''КОНВЕРТЕР ВАЛЮТ'''

tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)

tab_control.add(tab1, text="Конвертация валют")
tab_control.add(tab2, text="Динамика курса")
tab_control.pack(expand=1, fill="both")

label_currency1 = tk.Label(tab1, text="Валюта")
label_currency1.grid(column=0, row=0, padx = 5, pady = 10)

combo1_1 = ttk.Combobox(tab1)
combo1_1.grid(column=0, row=1, padx = 5, pady = 10)

combo1_2 = ttk.Combobox(tab1)
combo1_2.grid(column=0, row=2, padx = 5, pady = 10)

amount_entry = tk.Entry(tab1)
amount_entry.grid(column=1, row=1, padx = 5, pady = 10)

def convert():
    from_currency = combo1_1.get()
    to_currency = combo1_2.get()
    amount = float(amount_entry.get())
    currency_values = update_currency_list()
    if from_currency in currency_values and to_currency in currency_values:
        convert_amount = amount * (currency_values[to_currency] / currency_values[from_currency])
        result_label.config(text=f"{convert_amount}")
    else:
        result_label.config(text="Не удалось найти курс валюты")

btn = tk.Button(tab1, text="Конвертировать", command=convert)
btn.grid(column=2, row=1, padx = 5, pady = 10)

result_label = tk.Label(tab1, text="")
result_label.grid(column=1, row=2, padx = 5, pady = 10)

'''ДИНАМИКА КУРСА'''

label_currency2 = tk.Label(tab2, text="Валюта")
label_currency2.grid(column=0, row=0)

combo2_1 = ttk.Combobox(tab2)
combo2_1.grid(column=0, row=1, padx = 5, pady = 10)


scale_var0 = IntVar()
scale_var0.set(4)

radiobutton1 = Radiobutton(tab2, text='неделя', value=1, variable=scale_var0)
radiobutton1.grid(column=1, row=1, padx = 5, pady = 10)
radiobutton2 = Radiobutton(tab2, text='месяц', value=2, variable=scale_var0)
radiobutton2.grid(column=1, row=2, padx = 5, pady = 10)
radiobutton3 = Radiobutton(tab2, text='квартал', value=3, variable=scale_var0)
radiobutton3.grid(column=1, row=3, padx = 5, pady = 10)
radiobutton4 = Radiobutton(tab2, text='год', value=4, variable=scale_var0)
radiobutton4.grid(column=1, row=4, padx = 5, pady = 10)

combo2_2 = ttk.Combobox(tab2)
combo2_2.grid(column=2, row=1, padx = 5, pady = 10)

# обновление дат в зависимости от выбранного периода
def update_combo2_2(*args):
    value = scale_var0.get()
    today = datetime.datetime.now()
    start_date = None
    end_date = None

    if value == 1:  # неделя
        end_date = today
        start_date = end_date - datetime.timedelta(days=7)
    elif value == 2:  # месяц
        end_date = today
        start_date = datetime.datetime(end_date.year, end_date.month, 1)
    elif value == 3:  # квартал
        end_date = today
        start_date = datetime.datetime(end_date.year, (end_date.month - 1) // 3 * 3 + 1, 1)
    elif value == 4:  # год
        end_date = today
        start_date = datetime.datetime(end_date.year, 1, 1)

    # Обновление значений в combo2_2
    if value == 1:
        combo2_2["value"] = [f"{start_date.strftime('%d.%m.%Y')}-{end_date.strftime('%d.%m.%Y')}",
                             f"{start_date - datetime.timedelta(days=7):%d.%m.%Y}-{start_date:%d.%m.%Y}",
                             f"{start_date - datetime.timedelta(days=14):%d.%m.%Y}-{start_date - datetime.timedelta(days=7):%d.%m.%Y}",
                             f"{start_date - datetime.timedelta(days=21):%d.%m.%Y}-{start_date - datetime.timedelta(days=14):%d.%m.%Y}"]
    elif value == 2:
        combo2_2["value"] = [f"{start_date:%m.%Y}",
                             f"{start_date - datetime.timedelta(days=30):%m.%Y}",
                             f"{start_date - datetime.timedelta(days=60):%m.%Y}",
                             f"{start_date - datetime.timedelta(days=90):%m.%Y}"]
    elif value == 3:
        combo2_2["value"] = [f"{start_date:%d.%m.%Y}-{end_date:%d.%m.%Y}",
                             f"{start_date - datetime.timedelta(days=90):%d.%m.%Y}-{start_date - datetime.timedelta(days=60):%d.%m.%Y}",
                             f"{start_date - datetime.timedelta(days=180):%d.%m.%Y}-{start_date - datetime.timedelta(days=120):%d.%m.%Y}",
                             f"{start_date - datetime.timedelta(days=270):%d.%m.%Y}-{start_date - datetime.timedelta(days=210):%d.%m.%Y}"]
    elif value == 4:
        combo2_2["value"] = [f"{start_date:%Y}",
                             f"{start_date - datetime.timedelta(days=365):%Y}",
                             f"{start_date - datetime.timedelta(days=730):%Y}",
                             f"{start_date - datetime.timedelta(days=1095):%Y}"]

    return start_date, end_date

# Обновление дат при изменении периода
scale_var0.trace('w', update_combo2_2)

def fetch_currency_data(currency, start_date, end_date, period):
    current_date = start_date
    currency_data = []

    while current_date <= end_date:
        url = f"http://www.cbr.ru/scripts/XML_daily.asp?date_req={current_date.strftime('%d/%m/%Y')}"
        response = urllib.request.urlopen(url)
        dom = xml.dom.minidom.parse(response)
        dom.normalize()

        # Поиск значения валюты за текущий день
        found = False
        for record in dom.getElementsByTagName("Valute"):
            if record.getElementsByTagName("Name")[0].firstChild.nodeValue == currency:
                value = float(record.getElementsByTagName("Value")[0].firstChild.nodeValue.replace(',', '.'))
                nominal = int(record.getElementsByTagName("Nominal")[0].firstChild.nodeValue)
                currency_data.append((current_date, value / nominal))
                found = True
                break

        if not found:
            currency_data.append((current_date, None))

        # Переход к следующей дате в зависимости от периода
        if period == 1:  # Неделя
            current_date += datetime.timedelta(days=1)
        elif period == 2:  # Месяц
            current_date += datetime.timedelta(days=4)
        elif period == 3:  # Квартал
            current_date += datetime.timedelta(weeks=1)
        elif period == 4:  # Год
            current_date += datetime.timedelta(days=30)  # Примерно месяц

    return currency_data

def on_button_click():
    currency = combo2_1.get()
    period = scale_var0.get()
    start_date, end_date = update_combo2_2()
    data = fetch_currency_data(currency, start_date, end_date, period)
    print(data)

plot1_button = ttk.Button(tab2, text="Получить данные", command = on_button_click)
plot1_button.grid(column=2, row=3, padx=5, pady=10)
# Функция для построения графика
def plot_currency_data(currency_data):
    fig = Figure(figsize=(10, 5))
    ax = fig.add_subplot(111)
    dates = [date for date, value in currency_data]
    values = [value for date, value in currency_data if value is not None]
    ax.plot(dates, values, marker='o', linestyle='-')
    ax.set_title('Курс валюты')
    ax.set_xlabel('Дата')
    ax.set_ylabel('Значение курса')
    ax.grid(True)
    ax.tick_params(axis='x', rotation=45)
    return fig

def show_plot():
    global plot_widget 
    currency = combo2_1.get()
    period = scale_var0.get()
    start_date, end_date = update_combo2_2()
    data = fetch_currency_data(currency, start_date, end_date, period)
    fig = plot_currency_data(data)
    if 'plot_widget' in locals() and plot_widget:
        plot_widget.get_tk_widget().forget()
    plot_widget = FigureCanvasTkAgg(fig, master=tab2)
    plot_widget.draw()
    plot_widget.get_tk_widget().grid(column=0, row=5, columnspan=3, padx=5, pady=10)

plot_button = ttk.Button(tab2, text="Построить график", command=show_plot)
plot_button.grid(column=2, row=4, padx=5, pady=10)

window.after(100, update_currency_list)

window.mainloop()
