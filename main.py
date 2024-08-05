import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
checkmark = "✔"
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global timer, checkmark, reps
    window.after_cancel(timer)
    canvas.itemconfig(text_timer, text=f"00:00")
    label2.config(text=f"Timer")
    checkmark = "✔"
    check_mark.config(text="")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps, checkmark
    tick = checkmark
    work_sec = WORK_MIN * 60
    # work_sec = 10
    short_break_sec = SHORT_BREAK_MIN * 60
    # short_break_sec = 7
    long_break_sec = LONG_BREAK_MIN * 60
    # long_break_sec = 20
    if reps == 1 or reps == 3 or reps == 5 or reps == 7:
        countdown(work_sec)
        label2.config(text="Work", fg=RED)
    elif reps == 8:
        countdown(long_break_sec)
        label2.config(text="Long Break", fg=GREEN)
        check_mark.config(text=tick)
        checkmark += "✔"
    elif reps == 2 or reps == 4 or reps == 6:
        countdown(short_break_sec)
        label2.config(text="Short Break", fg=YELLOW)
        check_mark.config(text=tick)
        checkmark += "✔"
    elif reps == 0:
        countdown(5)
    reps += 1

    # ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def countdown(seconds):
    min_timer = math.floor(seconds / 60)
    sec_timer = (seconds % 60)
    if 0 <= sec_timer < 10:
        sec_timer = f"0{sec_timer}"
    if seconds >= 0:
        canvas.itemconfig(text_timer, text=f"{min_timer}:{sec_timer}")
        global timer
        timer = window.after(1000, countdown, seconds - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=PINK)

label1 = Label(text="", font=FONT_NAME)
label1.grid(row=0, column=0)
label1.config(bg=PINK)

label2 = Label(text="Timer", font=(FONT_NAME, 34, "bold"), fg=GREEN, bg=PINK)
label2.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=PINK, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
text_timer = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

starting_button = Button(text="Start", command=start_timer)
starting_button.grid(row=2, column=0)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(row=2, column=2)

check_mark = Label(text="", fg=GREEN, bg=PINK, font=(FONT_NAME, 35, "normal"))
check_mark.grid(row=3, column=1)

window.mainloop()
