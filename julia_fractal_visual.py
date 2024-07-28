import tkinter as tk

# CANVAS
root = tk.Tk()
root.title("JULIA SET!")

canvas_width = 800
canvas_height = 800
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg='black')
canvas.pack()

# PLANE BOUNDARIES (complex)
xmin, xmax, ymin, ymax = -2, 2, -2, 2
def map_complex(x,y):
    real = xmin + (xmax - xmin) * x / canvas_width
    imag = ymin + (ymax - ymin) * y / canvas_height
    return complex(real,imag)


def get_color(iterations, max_iterations):
    # New color if theres more iterations needed to get to that point
    # gets closer to blue the closer the iterations are from max
    # (deeper that part goes aka the points that are very much not part of the set)
    if iterations == max_iterations:
        return "#000000" # black for points that are stable (part of the set)
    else:
        t = iterations / max_iterations
        r = int(9 * (1-t) * t * t * t * 255)
        g = int(15 * (1-t) * (1-t) * t * t * 255)
        b = int(8.5 * (1-t) * (1-t) * (1-t) * t * 255)
        return f'#{r:02X}{g:02X}{b:02X}'


def mandelbrot_set(z,c, max_iterations):
    for iterations in range(max_iterations):
        if abs(z) >2:
            return iterations
        z = z ** 2 + c
    return max_iterations


def draw_mandelbrot(c):
    # for mandelbrot, pick c=0
    max_iterations = 150
    for x in range(canvas_width):
        for y in range(canvas_height):
            z = map_complex(x,y)
            iterations = mandelbrot_set(z,c, max_iterations)
            color = get_color(iterations, max_iterations)
            canvas.create_rectangle(x, y, x+1, y+1, fill = color, outline='')

draw_mandelbrot(0.355 + 0.355j)

root.mainloop()