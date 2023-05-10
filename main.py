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
REPS = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)
    title_label.config(text="Timer")
    label_mark.config(text="")
    canvas.itemconfig(image_timer, text="00:00")
    global REPS
    REPS = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def statr_timer():
    global REPS
    REPS += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if REPS == 1 or REPS == 3 or REPS == 5 or REPS == 7:
        title_label.config(text="Work")
        count_down(work_sec)
    elif REPS == 8:
        title_label.config(text="Break", fg=RED)
        count_down(long_break_sec)
    elif REPS == 2 or REPS == 4 or REPS == 6:
        title_label.config(text="Break", fg=PINK)
        count_down(short_break_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(image_timer, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    elif count == 0:
        statr_timer()
        marks = ""
        work_sessions = math.floor(REPS / 2)
        for _ in range(work_sessions):
            marks += "&"
        label_mark.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("pomodoro")
window.config(padx=100, pady=100, bg=YELLOW)

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40))
title_label.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
image_timer = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

label_mark = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15, "bold"))
label_mark.grid(row=3, column=1)

start = Button(text="start", highlightthickness=0, command=statr_timer)
start.grid(row=2, column=0)

reset = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset.grid(row=2, column=2)

window.mainloop()
