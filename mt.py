import tkinter as tk
from tkinter import messagebox
import unicodedata
import re

def limpiar_palabra(palabra):
 
    palabra = palabra.lower()  
    palabra = unicodedata.normalize('NFD', palabra).encode('ascii', 'ignore').decode('utf-8')
    palabra = re.sub(r'[^a-z]', '', palabra)
    return palabra

class MaquinaDeTuring:
    def __init__(self, palabra):
        self.cinta = list(limpiar_palabra(palabra))  
        self.cabezal = 0 
        self.estado = 'q0' 
        self.resultado = ""  
        self.transiciones = [] 
    
    def mover_cabezal(self, direccion):
        if direccion == 'R':
            self.cabezal += 1  
        elif direccion == 'L':
            self.cabezal -= 1  
    
    def procesar(self):
       
        while True:
           
            if self.estado == 'q0':
                if self.cabezal < len(self.cinta) // 2:
                    self.transiciones.append(f"Estado: {self.estado}, leyendo: {self.cinta[self.cabezal]}")
                    if self.cinta[self.cabezal] == self.cinta[-(self.cabezal + 1)]:
                        self.estado = 'q1' 
                        self.mover_cabezal('R')
                    else:
                        self.estado = 'q_rechazo'  
                else:
                    self.estado = 'q_aceptacion' 

            elif self.estado == 'q1':
                self.transiciones.append(f"leyendo: {self.cinta[self.cabezal]}")
                if self.cabezal < len(self.cinta) // 2:
                    if self.cinta[self.cabezal] == self.cinta[-(self.cabezal + 1)]:
                        self.mover_cabezal('R')  
                    else:
                        self.estado = 'q_rechazo'
                else:
                    self.estado = 'q_aceptacion' 

            if self.estado == 'q_aceptacion':
                self.resultado = "ES un palíndromo"
                break
            
            if self.estado == 'q_rechazo':
                self.resultado = "NO es un palíndromo"
                break
        
        return self.resultado

def verificar_palindromo():
    palabra = entrada.get() 
    mt = MaquinaDeTuring(palabra)  
    resultado = mt.procesar() 
    resultado_lbl.config(text=f"Resultado: '{palabra}' {resultado}")
    
    transiciones_text.delete(1.0, tk.END)
    for transicion in mt.transiciones:
        transiciones_text.insert(tk.END, transicion + "\n")

ventana = tk.Tk()
ventana.title("Palíndromo")

ventana.geometry("600x400")

titulo = tk.Label(ventana, text="Verificar si una palabra es un palíndromo", font=("Arial", 14))
titulo.pack(pady=10)

entrada = tk.Entry(ventana, width=50)
entrada.pack(pady=10)

boton_verificar = tk.Button(ventana, text="Verificar", command=verificar_palindromo)
boton_verificar.pack(pady=5)

resultado_lbl = tk.Label(ventana, text="", font=("Arial", 12))
resultado_lbl.pack(pady=10)

transiciones_lbl = tk.Label(ventana, text="Transiciones:", font=("Arial", 12))
transiciones_lbl.pack(pady=5)
transiciones_text = tk.Text(ventana, height=10, width=70)
transiciones_text.pack(pady=10)

ventana.mainloop()
