import customtkinter as ctk
import logging
# set up the level of the logger
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')


class TaxCalculator:
    def __init__(self):
        # initialize the window
        self.window = ctk.CTk()
        self.window.title("Tax Calculator")
        self.window.geometry("480 x 400")
        self.window.resizable(False, False)
        self.padding: dict = {"padx": 20, "pady": 10}
        self.income_label = ctk.CTkLabel(self.window, text="Income (N):")
        self.income_label.grid(row=0, **self.padding)
        self.income_entry = ctk.CTkEntry(self.window)
        self.income_entry.grid(row=0, column=1, **self.padding)
        #     insert tax label
        self.tax_rate_label = ctk.CTkLabel(self.window, text="Percent(%):")
        self.tax_rate_label.grid(row=1, column=0, **self.padding)
        #     insert tax entry
        self.tax_rate_entry = ctk.CTkEntry(self.window)
        self.tax_rate_entry.grid(row=1, column=1, **self.padding)
        #     insert result label and entry
        self.result_label = ctk.CTkLabel(self.window, text="Tax Amount:")
        self.result_label.grid(row=2, column=0, **self.padding)
        #     insert tax result entry
        self.result_entry = ctk.CTkEntry(self.window)
        self.result_entry.insert(0, "0")
        self.result_entry.grid(row=2, column=1, **self.padding)

        # insert income after tax label
        self.income_after_tax_label = ctk.CTkLabel(self.window, text="Income After Tax:")
        self.income_after_tax_label.grid(row=3, column=0, **self.padding)
        # insert income after tax entry
        self.income_after_tax_entry = ctk.CTkEntry(self.window)
        self.income_after_tax_entry.insert(0, "0")
        self.income_after_tax_entry.grid(row=3, column=1)
        #     insert calculate tax button
        self.calculate_button = ctk.CTkButton(self.window, text="Calculate Tax", command=self.calculate_tax)
        self.calculate_button.grid(row=4, column=1, **self.padding)
        # insert a clear button to clear all entries
        self.clear_button = ctk.CTkButton(self.window, text="Clear", command=self.clear_all)
        self.clear_button.grid(row=4, column=0, **self.padding)

        # create a function to clear all fields

    def clear_all(self):
        self.income_entry.delete(0, ctk.END)
        self.income_after_tax_entry.delete(0, ctk.END)
        self.result_entry.delete(0, ctk.END)
        self.tax_rate_entry.delete(0, ctk.END)
        self.income_after_tax_entry.insert(0, "0")
        self.result_entry.insert(0, "0")
        logging.debug('all values cleared successfully')

        #     create a function to calculate tax

    def update_tax_amount(self, text: str):
        self.result_entry.delete(0, ctk.END)
        self.result_entry.insert(0, text)

    def update_after_tax(self, after_tax: str):
        self.income_after_tax_entry.delete(0, ctk.END)
        self.income_after_tax_entry.insert(0, after_tax)

    def calculate_tax(self):
        try:
            income: float = float(self.income_entry.get())
            logging.debug(income)
            tax_rate: float = float(self.tax_rate_entry.get())
            logging.debug(tax_rate)
            self.update_tax_amount(f"N{income * (tax_rate / 100):,.2f}")
            logging.debug(f"N{income * (tax_rate / 100):,.2f}")
            self.update_after_tax(f"N{income - (income * (tax_rate / 100)):,.2f}")
            logging.debug(f"N{income - (income * (tax_rate / 100)):,.2f}")
        except ValueError:
            self.update_tax_amount("Invalid Input")
            logging.debug('tax amount not a float or integer')
            self.update_after_tax("Invalid Input")

    def run(self):
        self.window.mainloop()


if __name__ == '__main__':
    tc = TaxCalculator()
    tc.run()
