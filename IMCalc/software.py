import customtkinter
import tkinter.messagebox
import tkinter
from datetime import datetime

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        # Configure Entire Windows
        self.title("IMCalc")
        self.geometry(f"{1000}x{550}")

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

        self.imcFrame.grid_columnconfigure(0, weight=1)

        topText = customtkinter.CTkLabel(self.imcFrame, text="Calculando IMC", font=self.titleFont)
        topText.grid(row=0, column=0, pady=12, padx=10)

        self.nome = customtkinter.CTkEntry(self.imcFrame, placeholder_text="Insira seu nome", width=200, height=30, border_width=2, corner_radius=10, justify=customtkinter.CENTER)
        self.nome.grid(row=1, column=0, pady=12, padx=10)

        self.peso = customtkinter.CTkEntry(self.imcFrame, placeholder_text="Insira seu peso (Kg)", width=200, height=30, border_width=2, corner_radius=10, justify=customtkinter.CENTER)
        self.peso.grid(row=2, column=0, pady=12, padx=10)

        self.altura = customtkinter.CTkEntry(self.imcFrame, placeholder_text="Insira sua altura (m)", width=200, height=30, border_width=2, corner_radius=10, justify=customtkinter.CENTER)
        self.altura.grid(row=3, column=0, pady=12, padx=10)

        self.resultImc = customtkinter.CTkLabel(self.imcFrame, text='Sem resultados ainda')
        self.resultImc.grid(row=6, column=0, padx=10, pady=12)
        
        buttonCalc = customtkinter.CTkButton(self.imcFrame, text="Calcular IMC", command=self.calcula_imc)
        buttonCalc.grid(row=4, column=0, pady=12, padx=10)

        saveCalc = customtkinter.CTkButton(self.imcFrame, text="Salvar Resultado", command=self.save)
        saveCalc.grid(row=5, column=0, pady=12, padx=10)

    def createWidgetsAboutUs(self):
        topText = customtkinter.CTkLabel(self.aboutUsFrame, text="Sobre Nós", font=self.titleFont)
        topText.pack(pady=12, padx=10)

        textDescription = "Projeto da disciplina programação orientada a objetos, ministrada pelo professor Michel da Silva, \natribuído e desenvolvido por Carlos Eduardo, Maria Raquel, Maria Karoliny, Maria Clara Lourenço, \nLucas Nóbrega, Lucas Mateus, na linguagem Python, com o intuito de criar um software \n com uma interface gráfica, que calcule o IMC, conforme os dados cadastrados."

        self.description = customtkinter.CTkLabel(self.aboutUsFrame, text=textDescription, anchor=customtkinter.CENTER, font=self.textFont)
        self.description.pack(pady=80, padx=10)

        self.footer = customtkinter.CTkLabel(self.aboutUsFrame, text="Com muito amor e café S2")
        self.footer.pack(pady=12, padx=10)

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def activeImcFrame(self):
        if self.imcActive == False:
            self.imcFrame.pack(pady=20, padx=50, fill="both", expand=True, anchor=customtkinter.CENTER, side=customtkinter.TOP)
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
    
    def calcula_imc(self):
        self.imc = float(self.peso.get()) / (float(self.altura.get()) ** 2)

        if self.imc < 18.5:
            self.result = f'{round(self.imc)}, Abaixo do peso'
        elif 18.5 <= self.imc < 25:
            self.result = f'{round(self.imc)}, Peso normal'
        elif 25 <= self.imc < 30:
            self.result = f'{round(self.imc)}, Sobrepeso'
        elif 30 <= self.imc < 35:
            self.result = f'{self.imc}, Obesidade grau 1'
        elif 35 <= self.imc < 40:
            self.result = f'{round(self.imc)}, Obesidade grau 2'
        else:
            self.result = f'{round(self.imc)}, Obesidade grau 3'
        
        print('calculei')
        
        self.resultImc.configure(text=self.result)
    
    def save(self):
        name = self.nome.get()
        weight = self.peso.get()
        height = self.altura.get()
        date = datetime.now()
        result = self.result
        
        with open("dados.txt", "a") as file:
            file.write(f"{name},{weight},{height},{date},{result}\n")

if __name__ == "__main__":
    app = App()
    
    try:
        app.iconbitmap("assets/icon/img0.ico")
    except:
        pass
    
    app.mainloop()