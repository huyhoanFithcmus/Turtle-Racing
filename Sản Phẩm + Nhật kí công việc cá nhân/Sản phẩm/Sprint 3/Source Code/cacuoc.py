def cacuoc():
        # key down function
        def click():    #submit BUTTON
            global bank
            global choice
            global wager
            char_text = int(char_textentry.get())
            money_text = int(money_textentry.get()) 
            if char_text <= 6 and char_text > 0 and money_text <= bank:
                choice = char_text # collect character (nhan vat)
                wager = money_text # collect text (tien cuoc)
                Label(window, text = "submitted !!!         .       ", bg= "white", fg = "black", font = "none 12 bold"). grid(row = 7, column = 0, sticky = W)
                draw_smallbutton(vitri_x + 110, vitri_y, "red", "white", choice)
                draw_smallbutton(vitri_x + 190, vitri_y, "yellow", "black", wager)
                window.destroy()
                exit()
            else:
                if char_text > 6 or char_text <= 0:
                    Label(window, text = "invalid choice !", bg= "white", fg = "black", font = "none 12 bold"). grid(row = 7, column = 0, sticky = W)
                    Label(window, text = "enter choice again !", bg= "white", fg = "black", font = "none 12 bold"). grid(row = 8, column = 0, sticky = W)
                else:
                    Label(window, text = "not enough money !!!", bg= "white", fg = "black", font = "none 12 bold"). grid(row = 7, column = 0, sticky = W)
                    Label(window, text = "enter wager again !!!", bg= "white", fg = "black", font = "none 12 bold"). grid(row = 8, column = 0, sticky = W)              
        ## main