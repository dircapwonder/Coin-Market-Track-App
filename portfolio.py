from tkinter import *
from tkinter import messagebox, Menu
import requests, json
import sqlite3 as sql

pyportfolio = Tk()
pyportfolio.title("Crypto Portfolio")
pyportfolio.iconbitmap("favicon.ico")

con = sql.connect("coin.db")
cursorObj = con.cursor()

cursorObj.execute("CREATE TABLE IF NOT EXISTS crypto(id INTEGER PRIMARY KEY, symbol TEXT, amount INTEGER, price REAL)")
con.commit()

def refresher():
    for cell in pyportfolio.winfo_children():
        cell.destroy()
    
    nav_menu()    
    app_header()
    my_portfolio()
    
def nav_menu():
        
        def clear_all():
            cursorObj.execute("DELETE FROM crypto")
            con.commit()
            
            messagebox.showinfo("Portfolio Notification", "Portfolio Cleared")
            refresher()
        
        def close_app():
            pyportfolio.destroy()
        
        menu = Menu(pyportfolio)
        
        file_item = Menu(menu)
        file_item.add_command(label="Clear All", command=clear_all)
        file_item.add_command(label="Close App", command=close_app)
        menu.add_cascade(label="File", menu=file_item)
        
        pyportfolio.config(menu=menu)
    
def my_portfolio():
    api_request = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=250&convert=USD&CMC_PRO_API_KEY=YOUR_API_KEY_HERE")
    api = json.loads(api_request.content)

    cursorObj.execute("SELECT * FROM crypto")
    coins = cursorObj.fetchall()
    
    def value_track_color(amount):
        if amount > 0:
            return "#1D9233"
        else:
            return "#B61313"
   
#------------------DATABASE FUNCTIONS------------------
    def insert_coin():
        cursorObj.execute("INSERT INTO crypto(symbol, price, amount) VALUES(?, ?, ?)", (symbol_txt.get(), price_txt.get(), amount_txt.get()))
        con.commit()
        
        messagebox.showinfo("Portfolio Notification", "Coin Added to Your Portfolio Successfully")
        refresher()

    def update_coin():
        cursorObj.execute("UPDATE crypto SET symbol=?, price=?, amount=? WHERE id=?", (symbol_update.get(), price_update.get(), amount_update.get(), portid_update.get()))
        con.commit()
        
        messagebox.showinfo("Portfolio Notification", "Coin Updated Successfully")
        refresher()
        
    def delete_coin():
        cursorObj.execute("DELETE FROM crypto WHERE id=?", (portid_deleted.get(),))
        con.commit()
        
        messagebox.showinfo("Portfolio Notification", "Coin Deleted from Your Portfolio Successfully")
        refresher()
        
    total_pl = 0
    coin_row = 1
    total_amount_paid = 0
    cur_val = 0
    
    for i in range(0,250): 
        for coin in coins:  
            if api["data"][i]["symbol"] == coin[1]: 
                total_paid = coin[2] * coin[3]
                current_value = coin[2] * api["data"][i]["quote"]["USD"]["price"]
                pl_percoin = api["data"][i]["quote"]["USD"]["price"] - coin[3]
                total_pl_pcoin = pl_percoin * coin[2]
                
                total_pl += total_pl_pcoin
                total_amount_paid += total_paid
                cur_val += current_value
                
                portfolid = Label(pyportfolio, text=coin[0], bg="#bdaf99", fg="black", font="Lato 12", padx="2", pady="2", borderwidth="2", relief="groove")
                portfolid.grid(row=coin_row, column=0, sticky=N+S+E+W)
                
                name = Label(pyportfolio, text=api["data"][i]["symbol"], bg="#bdaf99", fg="black", font="Lato 12", padx="2", pady="2", borderwidth="2", relief="groove")
                name.grid(row=coin_row, column=1, sticky=N+S+E+W)
        
                price = Label(pyportfolio, text="${0:.2f}".format(api["data"][i]["quote"]["USD"]["price"]), bg="#e6d6bc", fg="black", font="Lato 12", padx="2", pady="2", borderwidth="2", relief="groove")
                price.grid(row=coin_row, column=2, sticky=N+S+E+W)
        
                tot_coins = Label(pyportfolio, text=coin[2], bg="#bdaf99", fg="black", font="Lato 12", padx="2", pady="2", borderwidth="2", relief="groove")
                tot_coins.grid(row=coin_row, column=3, sticky=N+S+E+W)
        
                amount_paid = Label(pyportfolio, text="${0:.2f}".format(total_paid), bg="#e6d6bc", fg="black", font="Lato 12", padx="2", pady="2", borderwidth="2", relief="groove")
                amount_paid.grid(row=coin_row, column=4, sticky=N+S+E+W)
        
                curval = Label(pyportfolio, text="${0:.2f}".format(current_value), bg="#bdaf99", fg="black", font="Lato 12", padx="2", pady="2", borderwidth="2", relief="groove")
                curval.grid(row=coin_row, column=5, sticky=N+S+E+W)
        
                pl_p_coin = Label(pyportfolio, text="${0:.2f}".format(pl_percoin), bg="#e6d6bc", fg=value_track_color(float("{0:.2f}".format(pl_percoin))), font="Lato 12 bold", padx="2", pady="2", borderwidth="2", relief="groove")
                pl_p_coin.grid(row=coin_row, column=6, sticky=N+S+E+W)
            

                pl_totalc = Label(pyportfolio, text="${0:.2f}".format(total_pl_pcoin), bg="#bdaf99", fg=value_track_color(float("{0:.2f}".format(total_pl_pcoin))), font="Lato 12 bold", padx="2", pady="2", borderwidth="2", relief="groove")
                pl_totalc.grid(row=coin_row, column=7, sticky=N+S+E+W)
                    
                coin_row += 1
                
        #---------------------------INSERT DATA---------------------------                
        symbol_txt = Entry(pyportfolio, borderwidth=2, relief="groove")
        symbol_txt.grid(row=coin_row+1, column=1)          
                   
        price_txt = Entry(pyportfolio, borderwidth=2, relief="groove")
        price_txt.grid(row=coin_row+1, column=2)        
        
        amount_txt = Entry(pyportfolio, borderwidth=2, relief="groove")
        amount_txt.grid(row=coin_row+1, column=3)
        
        add_coin = Button(pyportfolio, text="Add Coin", bg="#b3aa94", fg="black", command=insert_coin, font="Lato 12 bold", padx="2", pady="2", borderwidth="2", relief="groove")
        add_coin.grid(row=coin_row+1, column=4, sticky=N+E+W+S)
        
        #---------------------------UPDATE COIN---------------------------
        portid_update = Entry(pyportfolio, borderwidth=2, relief="groove")
        portid_update.grid(row=coin_row+2, column=0)
        
        symbol_update = Entry(pyportfolio, borderwidth=2, relief="groove")
        symbol_update.grid(row=coin_row+2, column=1)            
                           
        price_update = Entry(pyportfolio, borderwidth=2, relief="groove")
        price_update.grid(row=coin_row+2, column=2)        
                
        amount_update = Entry(pyportfolio, borderwidth=2, relief="groove")
        amount_update.grid(row=coin_row+2, column=3)
        
        updated_coin = Button(pyportfolio, text="Update Coin", bg="#b3aa94", fg="black", command=update_coin, font="Lato 12 bold", padx="2", pady="2", borderwidth="2", relief="groove")
        updated_coin.grid(row=coin_row+2, column=4, sticky=N+E+W+S)
        
        #---------------------------DELETE COIN---------------------------
        portid_deleted = Entry(pyportfolio, borderwidth=2, relief="groove")
        portid_deleted.grid(row=coin_row+3, column=0) 
        
        deleted_coin = Button(pyportfolio, text="Delete Coin", bg="#b3aa94", fg="black", command=delete_coin, font="Lato 12 bold", padx="2", pady="2", borderwidth="2", relief="groove")
        deleted_coin.grid(row=coin_row+3, column=4, sticky=N+E+W+S) 
        
        #---------------------------TOTALS---------------------------
        total_amountpaid = Label(pyportfolio, text="${0:.2f}".format(total_amount_paid), bg="#e6d6bc", fg=value_track_color(float("{0:.2f}".format(total_amount_paid))), font="Lato 12 bold", padx="2", pady="2", borderwidth="2", relief="groove")
        total_amountpaid.grid(row=coin_row, column=4, sticky=N+S+E+W)
        
        total_curval = Label(pyportfolio, text="${0:.2f}".format(cur_val), bg="#e6d6bc", fg=value_track_color(float("{0:.2f}".format(cur_val))), font="Lato 12 bold", padx="2", pady="2", borderwidth="2", relief="groove")
        total_curval.grid(row=coin_row, column=5, sticky=N+S+E+W)
        
        total = Label(pyportfolio, text="Total Wallet P/L:", bg="#b3aa94", fg="black", font="Lato 12 bold", padx="2", pady="2", borderwidth="2", relief="groove")
        total.grid(row=coin_row, column=6, sticky=N+S+E+W)
             
        pl_total = Label(pyportfolio, text="${0:.2f}".format(total_pl), bg="#e6d6bc", fg=value_track_color(float("{0:.2f}".format(total_pl))), font="Lato 12 bold", padx="2", pady="2", borderwidth="2", relief="groove")
        pl_total.grid(row=coin_row, column=7, sticky=N+S+E+W)
                                

    api = " "
                 
                 
    refresh = Button(pyportfolio, text="Refresh", bg="#b3aa94", fg="black", command=refresher, font="Lato 12 bold", padx="2", pady="2", borderwidth="2", relief="groove")
    refresh.grid(row=coin_row+1, column=7, sticky=N+E+W+S)


def app_header():
    portfolid = Label(pyportfolio, text="Portfolio ID", bg="#6b4b18", fg="#c2c0be", font="Lato 12 bold", padx="5", pady="5", borderwidth="2", relief="groove")
    portfolid.grid(row=0, column=0, sticky=N+S+E+W)
        
    name = Label(pyportfolio, text="Coin Name", bg="#6b4b18", fg="#c2c0be", font="Lato 12 bold", padx="5", pady="5", borderwidth="2", relief="groove")
    name.grid(row=0, column=1, sticky=N+S+E+W)

    price = Label(pyportfolio, text="Price", bg="#6b4b18", fg="#c2c0be", font="Lato 12 bold", padx="5", pady="5", borderwidth="2", relief="groove")
    price.grid(row=0, column=2, sticky=N+S+E+W)

    tot_coins = Label(pyportfolio, text="Amount Owned", bg="#6b4b18", fg="#c2c0be", font="Lato 12 bold", padx="5", pady="5", borderwidth="2", relief="groove")
    tot_coins.grid(row=0, column=3, sticky=N+S+E+W)

    amount_paid = Label(pyportfolio, text="Amount Paid", bg="#6b4b18", fg="#c2c0be", font="Lato 12 bold", padx="5", pady="5", borderwidth="2", relief="groove")
    amount_paid.grid(row=0, column=4, sticky=N+S+E+W)

    cur_val = Label(pyportfolio, text="Current Value", bg="#6b4b18", fg="#c2c0be", font="Lato 12 bold", padx="5", pady="5", borderwidth="2", relief="groove")
    cur_val.grid(row=0, column=5, sticky=N+S+E+W)

    pl_p_coin = Label(pyportfolio, text="P/L per Coin", bg="#6b4b18", fg="#c2c0be", font="Lato 12 bold", padx="5", pady="5", borderwidth="2", relief="groove")
    pl_p_coin.grid(row=0, column=6, sticky=N+S+E+W)       

    pl_totalc = Label(pyportfolio, text="P/L Total Coin", bg="#6b4b18", fg="#c2c0be", font="Lato 12 bold", padx="5", pady="5", borderwidth="2", relief="groove")
    pl_totalc.grid(row=0, column=7, sticky=N+S+E+W)

nav_menu()
app_header()
my_portfolio()

pyportfolio.mainloop()

cursorObj.close()
con.close()
