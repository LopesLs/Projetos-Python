import customtkinter

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        # Configure Entire Windows
        self.title("IMCalc")
        self.geometry(f"{800}x{500}")

        # Configuring Layout
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Create sidebar frame with widgets
        self.sidebarFrame = customtkinter.CTkFrame(self, width=100, corner_radius=0)
        self.sidebarFrame.grid(row=0, column=0, sticky="nsew")
        self.sidebarFrame.grid_rowconfigure(3, weight=1)
        
        self.logoLabel = customtkinter.CTkLabel(self.sidebarFrame, text="IMCalc", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logoLabel.grid(row=0, column=0, padx=20, pady=(20, 10))

        # Creating All Frames
        self.contentFrame = customtkinter.CTkFrame(self, width=200)
        self.contentFrame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
        self.imcFrame = customtkinter.CTkFrame(self.contentFrame)
        self.imcActive = False
        self.aboutUsFrame = customtkinter.CTkFrame(self.contentFrame)
        self.aboutActive = False
        self.style()

        # Creating Widgets
        self.createWidgetsImc()
        self.createWidgetsAboutUs()

        self.sidebarButtonImc = customtkinter.CTkButton(self.sidebarFrame, text="Calcular IMC", command=self.activeImcFrame)
        self.sidebarButtonImc.grid(row=1, column=0, padx=20, pady=10)
        
        self.sidebarButtonAboutUs = customtkinter.CTkButton(self.sidebarFrame, text="Sobre nós", command=self.activeAboutUsFrame)
        self.sidebarButtonAboutUs.grid(row=2, column=0, padx=20, pady=10)
    
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebarFrame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebarFrame, values=["Light", "Dark"], command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))

    def createWidgetsImc(self):
        topText = customtkinter.CTkLabel(self.imcFrame, text="Calculando IMC", font=self.titleFont)
        topText.pack(pady=12, padx=10)
    
    def createWidgetsAboutUs(self):
        topText = customtkinter.CTkLabel(self.aboutUsFrame, text="Sobre Nós", font=self.titleFont)
        topText.pack(pady=12, padx=10)

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def activeImcFrame(self):
        if self.imcActive == False:
            self.imcFrame.pack(pady=20, padx=50, fill="both", expand=True)
            self.imcActive = True
        else:
            self.imcFrame.pack_forget()
            self.imcActive = False

    def activeAboutUsFrame(self):
        if self.aboutActive == False:
            self.aboutUsFrame.pack(pady=20, padx=50, fill="both", expand=True)
            self.aboutActive = True
        else:
            self.aboutUsFrame.pack_forget()
            self.aboutActive = False

    def style(self):
        self.titleFont = customtkinter.CTkFont(family="Miriam",size=24, weight="bold")
        self.textFont = customtkinter.CTkFont(family="Miriam Fixed", size=13)

if __name__ == "__main__":
    app = App()
    
    try:
        app.iconbitmap("assets/icon/img0.ico")
    except:
        pass
    
    app.mainloop()