import tkinter as tk
from tkinter import ttk

class VentanaPrincipal:
    def __init__(self, root):
        self.root = root
        self.root.title("Programa de Credenciales de la Facultad de Derecho y Estudios Políticos")
        self.root.geometry("700x300")
        self.root.configure(bg="white")

        tk.Label(self.root, text="Calculadora de puntos por experiencia docente", font=("Arial", 16, "bold"), bg="#FFFFFF").pack(pady=15)

        self.radio_frame = tk.Frame(self.root, bg="white") 
        self.radio_frame.pack(pady=5)

        self.option_var = tk.StringVar(value="intensidad_horaria")
        ttk.Radiobutton(self.radio_frame, text="Calcular por Intensidad Horaria Semanal", variable=self.option_var, value="intensidad_horaria").pack(pady=5)
        ttk.Radiobutton(self.radio_frame, text="Calcular por Número de Horas Dictadas", variable=self.option_var, value="horas_dictadas").pack(pady=5)

        self.input_frame = tk.Frame(self.root, bg="#FFFFFF")
        self.input_frame.pack(pady=10)

        self.intensidad_frame = tk.Frame(self.input_frame, bg="#FFFFFF")
        tk.Label(self.intensidad_frame, text="Horas por semana:", bg="#FFFFFF").pack(side=tk.LEFT, padx=5)
        self.intensidad_entry = tk.Entry(self.intensidad_frame, bd=2, highlightbackground="black")
        self.intensidad_entry.pack(side=tk.LEFT, padx=5)
        self.intensidad_frame.pack()

        self.horas_dictadas_frame = tk.Frame(self.input_frame, bg="#FFFFFF")
        tk.Label(self.horas_dictadas_frame, text="Horas por semana:", bg="#FFFFFF").pack(side=tk.LEFT, padx=5)
        self.horas_semanales_entry = tk.Entry(self.horas_dictadas_frame, bd=2, highlightbackground="black")
        self.horas_semanales_entry.pack(side=tk.LEFT, padx=5)
        tk.Label(self.horas_dictadas_frame, text="Semanas:", bg="#FFFFFF").pack(side=tk.LEFT, padx=5)
        self.semanas_entry = tk.Entry(self.horas_dictadas_frame, bd=2, highlightbackground="black")
        self.semanas_entry.pack(side=tk.LEFT, padx=5)
        self.horas_dictadas_frame.pack()

        self.update_frames()

        self.result_frame = tk.Frame(self.root, bg="#FFFFFF")
        self.result_frame.pack(pady=15)

        self.result_label = tk.Label(self.result_frame, text="", font=("Arial", 12), bg="#FFFFFF")
        self.result_label.pack(side=tk.LEFT)

        self.calculate_button = tk.Button(self.root, text="Calcular puntos", command=self.calculate_points, bg="red", fg="white", font=("Arial", 12, "bold"))
        self.calculate_button.pack(pady=20)

        self.option_var.trace("w", lambda *args: self.update_frames())

    def update_frames(self):
        if self.option_var.get() == "intensidad_horaria":
            self.intensidad_frame.pack()
            self.horas_dictadas_frame.pack_forget()
        else:
            self.intensidad_frame.pack_forget()
            self.horas_dictadas_frame.pack()

    def calculate_points(self):
        try:
            if self.option_var.get() == "intensidad_horaria":
                # Cálculo basado en intensidad horaria semanal
                horas_semana = float(self.intensidad_entry.get())
                puntos = horas_semana * 0.167  
                self.result_label.config(text=f"Puntos calculados: {puntos:.3f}")
            else:
                # Cálculo basado en horas dictadas
                horas_semana = float(self.horas_semanales_entry.get())
                semanas = int(self.semanas_entry.get())
                total_horas = horas_semana * semanas
                puntos = total_horas * 0.01042  
                self.result_label.config(text=f"Puntos calculados: {puntos:.3f}")
        except ValueError:
            self.result_label.config(text="Por favor, ingrese valores numéricos válidos.")

if __name__ == "__main__":
    root = tk.Tk()
    app = VentanaPrincipal(root)
    root.mainloop()
