import tkinter as tk
from tkinter import messagebox

# Tu clase Stack original, un mini ajuste para la GUI (ya lo hicimos antes).
class Stack:
  def __init__(self):
    self.stack = []

  def agregar(self, element):
    self.stack.append(element)

  def eliminar(self):
    if self.existencia():
      return None
    return self.stack.pop()

  def ver(self):
    if self.existencia():
      return None
    return self.stack[-1]

  def existencia(self):
    return len(self.stack) == 0

  def tamano(self):
    return len(self.stack)

# --- AHORA SÍ, LA MAGIA CON TKINTER Y EL DISEÑO ---

class StackApp:
    """
    Esta clase se encarga de toda la ventana y su lógica, con el nuevo diseño.
    """
    def __init__(self, root):
        self.stack = Stack()
        
        self.root = root
        self.root.title("Visualizador de Stack LIFO 🔵")
        self.root.geometry("450x650") # Ajustamos el tamaño para que quepa bien
        self.root.resizable(False, False) # Para que no cambien el tamaño de la ventana
        self.root.config(bg="#2C3E50") # Fondo principal azul oscuro (Midnight Blue)

        # Paleta de colores para el diseño
        self.bg_dark = "#2C3E50"  # Fondo oscuro
        self.bg_medium = "#34495E" # Fondo medio para frames
        self.text_light = "#ECF0F1" # Texto claro
        self.accent_blue = "#3498DB" # Azul de acento (para botones y bordes)
        self.accent_hover = "#2980B9" # Azul más oscuro para hover
        self.error_red = "#E74C3C"  # Rojo para errores
        self.success_green = "#2ECC71" # Verde para éxito

        # Frame principal
        main_frame = tk.Frame(root, bg=self.bg_dark)
        main_frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

        # Título
        tk.Label(main_frame, text="Stack Visual (LIFO)", font=('Segoe UI', 18, 'bold'), 
                 fg=self.accent_blue, bg=self.bg_dark).pack(pady=(0, 15))

        # --- Sección de Controles ---
        control_frame = tk.Frame(main_frame, bg=self.bg_medium, bd=2, relief="groove")
        control_frame.pack(pady=10, fill=tk.X, ipadx=10, ipady=10)

        tk.Label(control_frame, text="Nuevo Elemento:", font=('Segoe UI', 10), 
                 fg=self.text_light, bg=self.bg_medium).pack(side=tk.LEFT, padx=(5, 10))
        
        self.entry_element = tk.Entry(control_frame, width=20, font=('Segoe UI', 10), 
                                     bg="#ECF0F1", fg="#2C3E50", insertbackground=self.bg_dark)
        self.entry_element.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=5)
        self.entry_element.bind("<Return>", self.agregar_elemento)

        btn_agregar = tk.Button(control_frame, text="➕ Agregar", command=self.agregar_elemento,
                                font=('Segoe UI', 10, 'bold'), bg=self.accent_blue, fg=self.text_light,
                                activebackground=self.accent_hover, relief="raised", bd=2)
        btn_agregar.pack(side=tk.LEFT, padx=(10, 5))
        
        # --- Sección de Operaciones ---
        op_frame = tk.Frame(main_frame, bg=self.bg_medium, bd=2, relief="groove")
        op_frame.pack(pady=10, fill=tk.X, ipadx=10, ipady=5)

        btn_eliminar = tk.Button(op_frame, text="➖ Eliminar (Pop)", command=self.eliminar_elemento,
                                 font=('Segoe UI', 10, 'bold'), bg=self.error_red, fg=self.text_light,
                                 activebackground="#C0392B", relief="raised", bd=2)
        btn_eliminar.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=5)

        btn_ver = tk.Button(op_frame, text="👁️ Ver (Peek)", command=self.ver_elemento,
                            font=('Segoe UI', 10, 'bold'), bg=self.accent_blue, fg=self.text_light,
                            activebackground=self.accent_hover, relief="raised", bd=2)
        btn_ver.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=5)

        # --- Sección de Visualización del Stack (Canvas) ---
        tk.Label(main_frame, text="--- Representación Visual del Stack ---", font=('Segoe UI', 12, 'italic'), 
                 fg=self.text_light, bg=self.bg_dark).pack(pady=(10, 5))
        
        self.canvas_width = 300
        self.canvas_height = 300
        self.canvas = tk.Canvas(main_frame, width=self.canvas_width, height=self.canvas_height,
                                bg="#516D8A", bd=0, highlightthickness=0, relief="flat") # Fondo del canvas un azul un poco más claro
        self.canvas.pack(pady=5, expand=True)

        # Parámetros para dibujar los discos
        self.disk_height = 30
        self.disk_width_base = 200 # Ancho máximo del disco base
        self.disk_spacing = 5    # Espacio entre discos
        self.max_disks_on_screen = int((self.canvas_height - 10) / (self.disk_height + self.disk_spacing))

        # --- Sección de Mensajes/Resultados ---
        self.label_info = tk.Label(main_frame, text="Info: ¡Esperando tu acción!", font=('Segoe UI', 10), 
                                     fg=self.text_light, bg=self.bg_dark, wraplength=400)
        self.label_info.pack(pady=(10, 0))

        # Actualizar display inicial
        self.actualizar_display()

    def actualizar_display(self):
        """Limpia el canvas y redibuja los discos que representan el stack."""
        self.canvas.delete("all") # Borra todo lo que haya en el canvas

        stack_size = self.stack.tamano()
        
        # Para que los discos se vean "apilados" desde abajo hacia arriba
        # Calculamos la posición inicial y los dibujamos
        
        # El centro horizontal del canvas
        center_x = self.canvas_width / 2

        # Altura inicial para el primer disco (abajo)
        # Dejamos un pequeño margen en la base
        y_bottom = self.canvas_height - (self.disk_height / 2) - 10 

        # Si el stack es muy grande, solo mostramos los últimos `max_disks_on_screen` elementos
        elements_to_draw = self.stack.stack[-self.max_disks_on_screen:] if stack_size > self.max_disks_on_screen else self.stack.stack

        # Dibujamos cada disco
        for i, item in enumerate(elements_to_draw):
            # Calculamos la posición vertical. Los de abajo tienen un índice menor.
            # `i` es el índice del elemento en la parte visible del stack
            # Si el stack real tiene 10 elementos y solo mostramos 5, el primer `i` (0)
            # corresponderá al sexto elemento en el stack real.
            current_y = y_bottom - i * (self.disk_height + self.disk_spacing)

            # Calculamos un ancho variable para el disco (el de abajo más ancho, el de arriba más estrecho)
            # Esto es un efecto visual, no significa que el dato sea más grande.
            # Cuantos más elementos, más variará el tamaño para los de abajo.
            width_variation_factor = 0.8 # Factor para variar el tamaño
            
            # Ajustamos el ancho del disco
            # Si hay muchos elementos, los discos de abajo serán más anchos, los de arriba más estrechos.
            # Ojo: esto es solo para el look and feel, no afecta la lógica.
            current_disk_width = self.disk_width_base - (len(elements_to_draw) - 1 - i) * width_variation_factor * 10
            
            # Asegurarse de que el ancho mínimo sea razonable
            if current_disk_width < 100:
                current_disk_width = 100

            half_disk_width = current_disk_width / 2

            x1 = center_x - half_disk_width
            y1 = current_y - (self.disk_height / 2)
            x2 = center_x + half_disk_width
            y2 = current_y + (self.disk_height / 2)

            # Color del disco: el de hasta arriba (tope) tiene un color de acento
            fill_color = self.accent_blue if i == len(elements_to_draw) - 1 else "#6A8BA8" # Azul más claro para los demás
            text_color = self.text_light if i == len(elements_to_draw) - 1 else self.text_light

            # Dibujar el óvalo (disco)
            self.canvas.create_oval(x1, y1, x2, y2, fill=fill_color, outline=self.text_light, width=1)
            # Dibujar el texto del elemento en el centro del disco
            self.canvas.create_text(center_x, current_y, text=str(item), fill=text_color, 
                                     font=('Segoe UI', 9, 'bold'))
        
        # Si el stack excede el número máximo de discos visibles, indicarlo
        if stack_size > self.max_disks_on_screen:
            # Dibujar puntos suspensivos o un indicador
            self.canvas.create_text(center_x, 20, text=f"... {stack_size - self.max_disks_on_screen} más abajo ...", 
                                    fill=self.text_light, font=('Segoe UI', 9, 'italic'))

    def agregar_elemento(self, event=None):
        """Toma el elemento del Entry, lo agrega al stack y actualiza la GUI."""
        elemento = self.entry_element.get().strip() # .strip() para quitar espacios extras
        if elemento:
            self.stack.agregar(elemento)
            self.actualizar_display()
            self.entry_element.delete(0, tk.END)
            self.label_info.config(text=f"✅ '{elemento}' se agregó. Tamaño: {self.stack.tamano()}", fg=self.success_green)
        else:
            messagebox.showwarning("Input Vacío", "¡Escribe algo para agregar al stack!")
            self.label_info.config(text="⚠️ Error: Campo vacío.", fg=self.error_red)

    def eliminar_elemento(self):
        """Saca un elemento del stack y muestra cuál fue."""
        elemento_eliminado = self.stack.eliminar()
        if elemento_eliminado is not None:
            self.actualizar_display()
            self.label_info.config(text=f"🗑️ '{elemento_eliminado}' fue eliminado. Tamaño: {self.stack.tamano()}", fg=self.success_green)
            messagebox.showinfo("Elemento Eliminado (Pop)", f"¡Sacaste el elemento: '{elemento_eliminado}'!")
        else:
            messagebox.showerror("Error", "El stack está vacío. ¡No hay nada que eliminar!")
            self.label_info.config(text="🚫 Error: El stack está vacío.", fg=self.error_red)

    def ver_elemento(self):
        """Muestra el elemento del tope sin sacarlo."""
        elemento_tope = self.stack.ver()
        if elemento_tope is not None:
            messagebox.showinfo("Elemento en el Tope (Peek)", f"El elemento de hasta arriba es: '{elemento_tope}'")
            self.label_info.config(text=f"🔍 El tope es '{elemento_tope}'.", fg=self.accent_blue)
        else:
            messagebox.showerror("Error", "El stack está vacío. ¡No hay nada que ver!")
            self.label_info.config(text="🚫 Error: El stack está vacío.", fg=self.error_red)

# --- Punto de Entrada de la Aplicación ---
if __name__ == "__main__":
    ventana_principal = tk.Tk()
    app = StackApp(ventana_principal)
    ventana_principal.mainloop()