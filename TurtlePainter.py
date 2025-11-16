import turtle as t
import tkinter as tk
import tkinter.messagebox as messagebox
from tkinter import filedialog
from PIL import ImageGrab
import os

root = tk.Tk()
root.title("ToolBar")
root.attributes("-topmost", True)
root.update_idletasks()

stat = tk.Toplevel()
stat.title("Status")
stat.attributes("-topmost", True)
penstat = tk.Label(stat, text="Pen is Up")
sizestat = tk.Label(stat, text="")
colorstat = tk.Label(stat, text="Color: black")
turtlestat = tk.Label(stat, text="Turtle is Visible")
penstat.pack()
colorstat.pack()
turtlestat.pack()
sizestat.pack()

t.title("Turtle Draw")
t.color("black")
t.shape("classic")

def update_window():
    root.update_idletasks()
    root.minsize(190, root.winfo_height())
    stat.update_idletasks()
    stat.minsize(190, root.winfo_height())

def forward():
    t.forward(10)

def backward():
    t.backward(10)

def left():
    t.left(30)

def right():
    t.right(30)

def pen_up():
    t.penup()
    penstat.config(text="Pen is Up")

def pen_down():
    t.pendown()
    penstat.config(text="Pen is Down")

def undo():
    t.undo()

def clear():
    t.clear()

def show_turtle():
    t.showturtle()
    turtlestat.config(text="Turtle is Visible")

def hide_turtle():
    t.hideturtle()
    turtlestat.config(text="Turtle is Invisible")

def change_color():
    colorwin = tk.Toplevel(root)
    colorwin.title("Color")

    colorlabel = tk.Label(colorwin, text="Enter a color name")
    colorentry = tk.Entry(colorwin)

    def set_color():
        try:
            t.color(colorentry.get())
            colorstat.config(text=f"Color: {colorentry.get()}")
            update_window()
        except tk.TclError:  # 잘못된 색 입력 대비
            pass
        colorwin.destroy()  # 창 닫기

    colorbutton = tk.Button(colorwin, text="Set Color", command=set_color)
    colorlabel.pack(pady=5)
    colorentry.pack(pady=5)
    colorbutton.pack(pady=5)

def pensize():
    sizewin = tk.Toplevel(root)
    sizewin.title("Pen Size")

    sizelabel = tk.Label(sizewin, text="Enter pen size (1-10)")
    sizeentry = tk.Entry(sizewin)
    sizebutton = tk.Button(sizewin, text="Set Size")

    def set_size():
        try:
            size = int(sizeentry.get())
            t.pensize(size)
            sizestat.config(text=f"Pen size: {size}")
            update_window()

        except ValueError:
             pass
        
        sizewin.destroy()
    sizebutton = tk.Button(sizewin, text="Set Size", command=set_size)
    sizelabel.pack(pady=5)
    sizeentry.pack(pady=5)
    sizebutton.pack(pady=5)


def draw_circle():
    circlewin = tk.Toplevel(root)
    circlewin.title("Circle")
    circlelabel = tk.Label(circlewin, text="Enter radius")
    circleentry = tk.Entry(circlewin)
    circlebutton = tk.Button(circlewin, text="Draw Circle")
    circlefillcheckbox = tk.Checkbutton(circlewin, text="Fill Circle")
    def set_circle():
        try:
            radius = int(circleentry.get())
            if circlefillcheckbox.var.get():
                t.begin_fill()
                t.circle(radius)
                t.end_fill()
            else:
                t.circle(radius)
        except ValueError:
            pass
        circlewin.destroy()
    circlebutton = tk.Button(circlewin, text="Draw Circle", command=set_circle)
    circlelabel.pack(pady=5)
    circleentry.pack(pady=5)
    circlebutton.pack(pady=5)
    circlefillcheckbox.var = tk.IntVar()
    circlefillcheckbox.config(variable=circlefillcheckbox.var)
    circlefillcheckbox.pack(pady=5)

def draw_square():
    squarewin = tk.Toplevel(root)
    squarewin.title("Square")
    squarelabel = tk.Label(squarewin, text="Enter side length")
    squareentry = tk.Entry(squarewin)
    squarebutton = tk.Button(squarewin, text="Draw Square")
    squarefillcheckbox = tk.Checkbutton(squarewin, text="Fill Square")
    def set_square():
        try:
            side = int(squareentry.get())
            if squarefillcheckbox.var.get():
                t.begin_fill()
                for temp in range(4):
                    t.forward(side)
                    t.right(90)
                t.end_fill()
            else:
                for temp in range(4):
                    t.forward(side)
                    t.right(90)
        except ValueError:
            pass
        squarewin.destroy()
    squarebutton = tk.Button(squarewin, text="Draw Square", command=set_square)
    squarelabel.pack(pady=5)
    squareentry.pack(pady=5)
    squarebutton.pack(pady=5)
    squarefillcheckbox.var = tk.IntVar()
    squarefillcheckbox.config(variable=squarefillcheckbox.var)
    squarefillcheckbox.pack(pady=5)

def draw_triangle():
    trianglewin = tk.Toplevel(root)
    trianglewin.title("Triangle")
    trianglelabel = tk.Label(trianglewin, text="Enter side length")
    triangleentry = tk.Entry(trianglewin)
    trianglebutton = tk.Button(trianglewin, text="Draw Triangle")
    trianglefillcheckbox = tk.Checkbutton(trianglewin, text="Fill Triangle")
    def set_triangle():
        try:
            side = int(triangleentry.get())
            if trianglefillcheckbox.var.get():
                t.begin_fill()
                for temp in range(3):
                    t.forward(side)
                    t.right(120)
                t.end_fill()
            else:
                for temp in range(3):
                    t.forward(side)
                    t.right(120)
        except ValueError:
            pass
        trianglewin.destroy()
    trianglebutton = tk.Button(trianglewin, text="Draw Triangle", command=set_triangle)
    trianglelabel.pack(pady=5)
    triangleentry.pack(pady=5)
    trianglebutton.pack(pady=5)
    trianglefillcheckbox.var = tk.IntVar()
    trianglefillcheckbox.config(variable=trianglefillcheckbox.var)
    trianglefillcheckbox.pack(pady=5)

def draw_star():
    starwin = tk.Toplevel(root)
    starwin.title("Star")
    starlabel = tk.Label(starwin, text="Enter side length")
    starentry = tk.Entry(starwin)
    starbutton = tk.Button(starwin, text="Draw Star")
    def set_star():
        try:
            side = int(starentry.get())
            for temp in range(5):
                t.forward(side)
                t.right(144)
        except ValueError:
            pass
        starwin.destroy()
    starbutton = tk.Button(starwin, text="Draw Star", command=set_star)
    starlabel.pack(pady=5)
    starentry.pack(pady=5)
    starbutton.pack(pady=5)

def save_png():
    if os.environ.get("XDG_SESSION_TYPE") == "wayland":
        messagebox.showerror(
        title="Error",
        message="Saving is not supported on Wayland. Only X11 is supported.",
        parent=stat
        )
        return
    root.update()

    canvas = t.getcanvas()
    x = root.winfo_rootx() + canvas.winfo_x()
    y = root.winfo_rooty() + canvas.winfo_y()
    w = x + canvas.winfo_width()
    h = y + canvas.winfo_height()

    img = ImageGrab.grab(bbox=(x, y, w, h))

    save_path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG files", "*.png")],
        title="Save your drawing"
    )
    if save_path:
        img.save(save_path)
        print(f"Saved to {save_path}")

color = tk.Button(root, text="Color", command=change_color)
penup_button = tk.Button(root, text="Pen Up", command=pen_up)
pendown_button = tk.Button(root, text="Pen Down", command=pen_down)
pensize_button = tk.Button(root, text="Pen Size", command=pensize)
undo_button = tk.Button(root, text="Undo", command=undo)
clear_button = tk.Button(root, text="Clear", command=clear)
show_turtle_button = tk.Button(root, text="Show Turtle", command=show_turtle)
hide_turtle_button = tk.Button(root, text="Hide Turtle", command=hide_turtle)
draw_circle_button = tk.Button(root, text="Circle", command=draw_circle)
draw_square_button = tk.Button(root, text="Square", command=draw_square)
draw_triangle_button = tk.Button(root, text="Triangle", command=draw_triangle)
draw_star_button = tk.Button(root, text="Star", command=draw_star)
save_button = tk.Button(root, text="Save", command=save_png)

color.pack(fill="x", pady=5)
penup_button.pack(fill="x", pady=5)
pendown_button.pack(fill="x", pady=5)
pensize_button.pack(fill="x", pady=5)
undo_button.pack(fill="x", pady=5)
clear_button.pack(fill="x", pady=5)
show_turtle_button.pack(fill="x", pady=5)
hide_turtle_button.pack(fill="x", pady=5)
draw_circle_button.pack(fill="x", pady=5)
draw_square_button.pack(fill="x", pady=5)
draw_triangle_button.pack(fill="x", pady=5)
draw_star_button.pack(fill="x", pady=5)
save_button.pack(fill="x", pady=5)

root.update_idletasks()
root.minsize(190, root.winfo_height())
stat.update_idletasks()
stat.minsize(190, root.winfo_height())

t.onscreenclick(t.goto)
t.onkey(forward, "Up")
t.onkey(backward, "Down")
t.onkey(left, "Left")
t.onkey(right, "Right")
t.listen()

t.mainloop()