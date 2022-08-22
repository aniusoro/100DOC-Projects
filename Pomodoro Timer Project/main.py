from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    checkmark.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=RED)
    if reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    """ math.floor returns the largest whole number <= x"""
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        """ executes a command after a delay, measured in milliseconds
                after x milliseconds call the function, call the count_down function
            """
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✅"
        checkmark.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)


def say_something(thing):
    print(thing)



"""canvas is used to create an image"""
canvas = Canvas(width=200, height=230, bg=YELLOW, highlightthickness=0)
"""a way to read through a file and get hold of an image at a file location"""
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 115, image=tomato)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold", "italic"))
canvas.grid(column=1, row=1)


"""this is the timer label"""
timer_label = Label(text="Timer", bg=YELLOW,  fg=GREEN, font=(FONT_NAME, 50, "bold"))
timer_label.grid(column=1, row=0)

"""here I create the start and stop buttons"""
start_button = Button(text="Start", font=(FONT_NAME, 20), highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", font=(FONT_NAME, 20), highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

checkmark = Label(text="✅", fg=GREEN, bg=YELLOW)
checkmark.grid(column=1, row=3)


""" Dynamic Typing: changing a variables data type by changing its content """

window.mainloop()
