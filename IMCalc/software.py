import customtkinter 

class Software(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")

        self.title("IMCalc")
        self.geometry("500x300")
        self.resizable(False, False)

        self.style()
        self.loginFrame()
    
    def loginFrame(self):

        self.loginWindow = customtkinter.CTkFrame(self)
        self.loginWindow.pack(pady=20, padx=60, fill="both", expand=True)

        self.topText = customtkinter.CTkLabel(master=self.loginWindow, text="Seja bem-vindo(a)!", font=self.titleFont)
        self.topText.pack(pady=12, padx=10)

        self.inputName = customtkinter.CTkEntry(master=self.loginWindow, placeholder_text="Insira seu nome")
        self.inputName.configure(font=self.textFont, justify=customtkinter.CENTER)
        self.inputName.pack(pady=12, padx=10)

        self.buttonNext = customtkinter.CTkButton(master=self.loginWindow, corner_radius=15, text="Entrar", command=self.imcFrame, font=self.textFont)
        self.buttonNext.pack(pady=12, padx=10)

        self.check = customtkinter.CTkCheckBox(master=self.loginWindow, text="Manter-se logado", font=self.textFont)
        self.check.pack(pady=12, padx=10)

    def imcFrame(self):
        
        print(self.inputName.get())
        print(self.check.get())
        
        self.loginWindow.pack_forget()
        
        self.mainMenu = customtkinter.CTkFrame(self)
        self.mainMenu.pack(pady=20, padx=60, fill="both", expand=True)

        self.topText = customtkinter.CTkLabel(master=self.mainMenu, text="CalculandoIMC", font=self.titleFont)
        self.topText.pack(pady=12, padx=10)

    def style(self):
        self.titleFont = customtkinter.CTkFont(family="Miriam",size=24, weight="bold")
        self.textFont = customtkinter.CTkFont(family="Miriam Fixed", size=13)

if __name__ == "__main__":
    app = Software()
    
    # If the computer don't support to icons, then ingore it.
    try:
        app.iconbitmap("assets/icon/img0.ico")
    except:
        pass
    
    app.mainloop()
