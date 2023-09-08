from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
import tkinter.messagebox as mb
import webbrowser
from threading import Thread

# MAIN WINDOW PLACEMENT
main_window=Tk()
#ctypes.windll.shcore.SetProcessDpiAwareness(1)
main_window.title("TGZ Tic Tac Toe Game")
main_window.geometry("500x575+430+50")
main_window.resizable(0,0)
icon=ImageTk.PhotoImage(file="Bin/TGZ_icon.ico")
main_window.iconphoto(False,icon)
main_turn=StringVar()
turn=StringVar()
turn.set("Click On Start Button To Start The Game")
main_window.config(bg="black")
player_one_name=StringVar()
player_two_name=StringVar()
player_one_new_name=StringVar()
player_two_new_name=StringVar()
player_one_name.set("X")
player_two_name.set("O")
game_state=StringVar()
show_name=StringVar()
show_name.set("Click to Save")
bg_color=StringVar()
bg_color.set("cyan")
match=IntVar()
match.set(0)
about_us_window=BooleanVar()
game_mode_container=StringVar()
game_mode_container.set("Cpu")


# BUTTONS STATE
button_one_state=BooleanVar()
button_two_state=BooleanVar()
button_three_state=BooleanVar()
button_four_state=BooleanVar()
button_five_state=BooleanVar()
button_six_state=BooleanVar()
button_seven_state=BooleanVar()
button_eight_state=BooleanVar()
button_nine_state=BooleanVar()


# BUTTONS DEFAULT STATE
button_one_state.set(False)
button_two_state.set(False)
button_three_state.set(False)
button_four_state.set(False)
button_five_state.set(False)
button_four_state.set(False)
button_six_state.set(False)
button_seven_state.set(False)
button_eight_state.set(False)
button_nine_state.set(False)


#  PLAYER POSTIONS
pos_one=StringVar()
pos_two=StringVar()
pos_three=StringVar()
pos_four=StringVar()
pos_five=StringVar()
pos_six=StringVar()
pos_seven=StringVar()
pos_eight=StringVar()
pos_nine=StringVar()


#  ALL IMAGES
bg_img=ImageTk.PhotoImage(Image.open("Bin/default_bg_img.png").resize((500, 500), Image.ANTIALIAS))
theme_one_img=ImageTk.PhotoImage(Image.open("Bin/theme_one.png").resize((500, 500), Image.ANTIALIAS))
theme_two_img=ImageTk.PhotoImage(Image.open("Bin/theme_two.png").resize((500, 500), Image.ANTIALIAS))
theme_three_img=ImageTk.PhotoImage(Image.open("Bin/theme_three.png").resize((500, 500), Image.ANTIALIAS))
theme_four_img=ImageTk.PhotoImage(Image.open("Bin/theme_four.png").resize((500, 500), Image.ANTIALIAS))
theme_but_one_img=ImageTk.PhotoImage(Image.open("Bin/theme_but_one.png").resize((20, 20), Image.ANTIALIAS))
theme_but_two_img=ImageTk.PhotoImage(Image.open("Bin/theme_but_two.png").resize((20, 20), Image.ANTIALIAS))
theme_but_three_img=ImageTk.PhotoImage(Image.open("Bin/theme_but_three.png").resize((20, 20), Image.ANTIALIAS))
theme_but_four_img=ImageTk.PhotoImage(Image.open("Bin/theme_but_four.png").resize((20, 20), Image.ANTIALIAS))
theme_but_default_img=ImageTk.PhotoImage(Image.open("Bin/theme_but_default.png").resize((20, 20), Image.ANTIALIAS))
x_img=ImageTk.PhotoImage(Image.open("Bin/x_player.png").resize((140, 140), Image.ANTIALIAS))
zero_img=ImageTk.PhotoImage(Image.open("Bin/zero_img.png").resize((140, 140), Image.ANTIALIAS))
tgz_img=ImageTk.PhotoImage(Image.open("Bin/TGZ_head.png").resize((200, 50), Image.ANTIALIAS))
hg_image=ImageTk.PhotoImage(Image.open("Bin/hg.png").resize((30, 30), Image.ANTIALIAS))


def default_pos():
    pos_one.set("")
    pos_two.set("")
    pos_three.set("")
    pos_four.set("")
    pos_five.set("")
    pos_six.set("")
    pos_seven.set("")
    pos_eight.set("")
    pos_nine.set("")
    label_one.configure(bg="cyan")
    label_two.configure(bg="cyan")
    label_three.configure(bg="cyan")
    label_four.configure(bg="cyan")
    label_five.configure(bg="cyan")
    label_six.configure(bg="cyan")
    label_seven.configure(bg="cyan")
    label_eight.configure(bg="cyan")
    label_nine.configure(bg="cyan")


def stop_game():
    button_one_state.set(False)
    button_two_state.set(False)
    button_three_state.set(False)
    button_four_state.set(False)
    button_five_state.set(False)
    button_six_state.set(False)
    button_seven_state.set(False)
    button_eight_state.set(False)
    button_nine_state.set(False)


def unstop_game():
    button_one_state.set(True)
    button_two_state.set(True)
    button_three_state.set(True)
    button_four_state.set(True)
    button_five_state.set(True)
    button_six_state.set(True)
    button_seven_state.set(True)
    button_eight_state.set(True)
    button_nine_state.set(True)


def start_restart(event):
    if game_state.get()=="" or game_state.get()=="Start":
        match.set(match.get()+1)
        turn.set(player_one_name.get() + "'s Turn")
        unstop_game()
        if player_two_name.get()=="cpu" or player_two_name.get()=="CPU":
            cpu_turn()
        else:
            mode()
        game_state.set("Started")
        start_button.configure(text="RESET")
    else:
        msg = "Are you sure you want to Reset the Game ?"
        if mb.askyesno("Confirmation", msg) == True:
            turn.set("Click On Start Button To Start The Game")
            default_pos()
            main_turn.set("")
            label_one.configure(image="")
            label_two.configure(image="")
            label_three.configure(image="")
            label_four.configure(image="")
            label_five.configure(image="")
            label_six.configure(image="")
            label_seven.configure(image="")
            label_eight.configure(image="")
            label_nine.configure(image="")
            start_button.configure(text="START")
            stop_game()
            game_state.set("Start")
        else:
            pass


def check_positions():
    get_pos_one=pos_one.get()
    get_pos_two=pos_two.get()
    get_pos_three=pos_three.get()
    get_pos_four=pos_four.get()
    get_pos_five=pos_five.get()
    get_pos_six=pos_six.get()
    get_pos_seven=pos_seven.get()
    get_pos_eight=pos_eight.get()
    get_pos_nine=pos_nine.get()
    p_one=player_one_name.get()
    p_two=player_two_name.get()
    if get_pos_one == get_pos_two == get_pos_three == p_one or get_pos_one == get_pos_two == get_pos_three == p_two:
        turn.set("WOW! " + get_pos_one + " is the winner. Reset The Game")
        stop_game()
        label_one.configure(bg="green2")
        label_two.configure(bg="green2")
        label_three.configure(bg="green2")
        bg_color.set("green2")
    elif get_pos_four == get_pos_five == get_pos_six == p_one or get_pos_four == get_pos_five == get_pos_six == p_two:
        turn.set("WOW! " + get_pos_four + " is the Winner. Reset The Game")
        stop_game()
        label_four.configure(bg="green2")
        label_five.configure(bg="green2")
        label_six.configure(bg="green2")
        bg_color.set("green2")
    elif get_pos_seven == get_pos_eight == get_pos_nine == p_one or get_pos_seven == get_pos_eight == get_pos_nine == p_two:
        turn.set("WOW! " + get_pos_seven + " is the winner. Reset The Game")
        stop_game()
        label_seven.configure(bg="green2")
        label_eight.configure(bg="green2")
        label_nine.configure(bg="green2")
        bg_color.set("green2")
    elif get_pos_one == get_pos_four == get_pos_seven == p_one or get_pos_one == get_pos_four == get_pos_seven == p_two:
        turn.set("WOW! " + get_pos_one + " is the winner. Reset The Game")
        stop_game()
        label_one.configure(bg="green2")
        label_four.configure(bg="green2")
        label_seven.configure(bg="green2")
        bg_color.set("green2")
    elif get_pos_two == get_pos_five == get_pos_eight == p_one or get_pos_two == get_pos_five == get_pos_eight == p_two:
        turn.set("WOW! " + get_pos_two + " is the winner. Reset The Game")
        stop_game()
        label_two.configure(bg="green2")
        label_five.configure(bg="green2")
        label_eight.configure(bg="green2")
        bg_color.set("green2")
    elif get_pos_three == get_pos_six == get_pos_nine == p_one or get_pos_three == get_pos_six == get_pos_nine == p_two:
        turn.set("WOW! " + get_pos_three + " is the winner. Reset The Game")
        stop_game()
        label_three.configure(bg="green2")
        label_six.configure(bg="green2")
        label_nine.configure(bg="green2")
        bg_color.set("green2")
    elif get_pos_one == get_pos_five == get_pos_nine == p_one or get_pos_one == get_pos_five == get_pos_nine == p_two:
        turn.set("WOW! " + get_pos_one + " is the winner. Reset The Game")
        stop_game()
        label_one.configure(bg="green2")
        label_five.configure(bg="green2")
        label_nine.configure(bg="green2")
        bg_color.set("green2")
    elif get_pos_three == get_pos_five == get_pos_seven == p_one or get_pos_three == get_pos_five == get_pos_seven == p_two:
        stop_game()
        label_three.configure(bg="green2")
        label_five.configure(bg="green2")
        label_seven.configure(bg="green2")
        bg_color.set("green2")
        turn.set("WOW! " + get_pos_three + " is the winner. Reset The Game")
    elif button_one_state.get() == button_two_state.get() == button_three_state.get() == button_four_state.get() == button_five_state.get() == button_six_state.get() == button_seven_state.get() == button_eight_state.get() == button_nine_state.get() == False:
        turn.set("WOW! Its a tie, Reset the Game ")
        label_one.configure(bg="red")
        label_two.configure(bg="red")
        label_three.configure(bg="red")
        label_four.configure(bg="red")
        label_five.configure(bg="red")
        label_six.configure(bg="red")
        label_seven.configure(bg="red")
        label_eight.configure(bg="red")
        label_nine.configure(bg="red")
        bg_color.set("red")
    else:
        pass


def cpu_turn():
    thread = Thread(target=cpu_turn_now)
    thread.start()


def cpu_turn_now():
    if button_one_state.get() == button_two_state.get() == button_three_state.get() == button_four_state.get() ==\
            button_five_state.get() == button_six_state.get() == button_seven_state.get() == button_eight_state.get() \
            == button_nine_state.get() == False:
        check_positions()
    else:
        get_pos_one = pos_one.get()
        get_pos_two = pos_two.get()
        get_pos_three = pos_three.get()
        get_pos_four = pos_four.get()
        get_pos_five = pos_five.get()
        get_pos_six = pos_six.get()
        get_pos_seven = pos_seven.get()
        get_pos_eight = pos_eight.get()
        get_pos_nine = pos_nine.get()
        cpu_image = zero_img
        cpu_player = player_two_name.get()
        against_player = player_one_name.get()

        def choice(win_pos_one, win_pos_two, win_pos_three, image_one, image_two, image_three, place_one, place_two,
                   place_three, btn_1_s, btn_2_s, btn_3_s):
            if win_pos_one == win_pos_two == against_player and win_pos_three == "":
                if btn_3_s.get() == True:
                    image_three.configure(image=cpu_image)
                    btn_3_s.set(False)
                    place_three.set(cpu_player)
                    turn.set(against_player + "'s Turn")
                    check_positions()
                    cpu_against()
                else:
                    pass
            elif win_pos_two == win_pos_three == against_player and win_pos_one == "":
                if btn_1_s.get() == True:
                    image_one.configure(image=cpu_image)
                    btn_1_s.set(False)
                    place_one.set(cpu_player)
                    turn.set(against_player + "'s Turn")
                    check_positions()
                    cpu_against()
                else:
                    pass
            elif win_pos_one == win_pos_three == against_player and win_pos_two == "":
                if btn_2_s.get() == True:
                    image_two.configure(image=cpu_image)
                    place_two.set(cpu_player)
                    btn_2_s.set(False)
                    turn.set(against_player + "'s Turn")
                    check_positions()
                    cpu_against()
                else:
                    pass
            elif win_pos_one == win_pos_two == win_pos_three == "":
                if btn_1_s.get() == True:
                    image_one.configure(image=cpu_image)
                    place_one.set(cpu_player)
                    turn.set(against_player + "'s Turn")
                    btn_1_s.set(False)
                    check_positions()
                    cpu_against()
                else:
                    pass
            elif win_pos_one == cpu_player and win_pos_two == win_pos_three == "":
                if btn_2_s.get() == True:
                    image_two.configure(image=cpu_image)
                    place_two.set(cpu_player)
                    btn_2_s.set(False)
                    turn.set(against_player + "'s Turn")
                    check_positions()
                    cpu_against()
                else:
                    pass
            elif win_pos_one == win_pos_two == cpu_player and win_pos_three == "":
                if btn_3_s.get() == True:
                    image_three.configure(image=cpu_image)
                    place_three.set(cpu_player)
                    btn_3_s.set(False)
                    turn.set(against_player + "'s Turn")
                    check_positions()
                    cpu_against()
                else:
                    pass
            elif win_pos_two == cpu_player and win_pos_one == win_pos_three == "":
                if btn_1_s.get() == True:
                    image_one.configure(image=cpu_image)
                    place_one.set(cpu_player)
                    btn_1_s.set(False)
                    turn.set(against_player + "'s Turn")
                    check_positions()
                    cpu_against()
                else:
                    pass
            elif win_pos_two == win_pos_one == cpu_player and win_pos_three == "":
                if btn_3_s.get() == True:
                    image_three.configure(image=cpu_image)
                    btn_3_s.set(False)
                    place_three.set(cpu_player)
                    turn.set(against_player + "'s Turn")
                    check_positions()
                    cpu_against()
                else:
                    pass
            elif win_pos_three == cpu_player and win_pos_one == win_pos_two == "":
                if btn_1_s.get() == True:
                    image_one.configure(image=cpu_image)
                    btn_1_s.set(False)
                    place_one.set(cpu_player)
                    turn.set(against_player + "'s Turn")
                    check_positions()
                    cpu_against()
                else:
                    pass
            elif win_pos_one == win_pos_three == cpu_player and win_pos_two == "":
                if btn_2_s.get() == True:
                    image_two.configure(image=cpu_image)
                    btn_2_s.set(False)
                    place_two.set(cpu_player)
                    turn.set(against_player + "'s Turn")
                    check_positions()
                    cpu_against()
                else:
                    pass
            elif win_pos_two == win_pos_three == cpu_player and win_pos_one == "":
                if btn_1_s.get() == True:
                    image_one.configure(image=cpu_image)
                    btn_1_s.set(False)
                    place_one.set(cpu_player)
                    turn.set(against_player + "'s Turn")
                    check_positions()
                    cpu_against()
                else:
                    pass
            else:
                pass

        if get_pos_one == get_pos_two == cpu_player and get_pos_three == "" or get_pos_two == get_pos_three == cpu_player and get_pos_one == "" \
                or get_pos_one == get_pos_three == cpu_player and get_pos_two == "":
            image_one = label_one
            image_two = label_two
            image_three = label_three
            bt_1_s = button_one_state
            bt_2_s = button_two_state
            bt_3_s = button_three_state
            choice(get_pos_one, get_pos_two, get_pos_three, image_one, image_two, image_three, pos_one, pos_two,
                   pos_three,
                   bt_1_s, bt_2_s, bt_3_s)
        elif get_pos_four == get_pos_five == cpu_player and get_pos_six == "" or get_pos_five == get_pos_six == cpu_player and get_pos_four == "" \
                or get_pos_four == get_pos_six == cpu_player and get_pos_five == "":
            image_one = label_four
            image_two = label_five
            image_three = label_six
            bt_1_s = button_four_state
            bt_2_s = button_five_state
            bt_3_s = button_six_state
            choice(get_pos_four, get_pos_five, get_pos_six, image_one, image_two, image_three, pos_four, pos_five,
                   pos_six,
                   bt_1_s, bt_2_s, bt_3_s)
        elif get_pos_seven == get_pos_eight == cpu_player and get_pos_nine == "" or get_pos_eight == get_pos_nine == cpu_player and get_pos_seven == "" \
                or get_pos_seven == get_pos_nine == cpu_player and get_pos_eight == "":
            image_one = label_seven
            image_two = label_eight
            image_three = label_nine
            bt_1_s = button_seven_state
            bt_2_s = button_eight_state
            bt_3_s = button_nine_state
            choice(get_pos_seven, get_pos_eight, get_pos_nine, image_one, image_two, image_three, pos_seven, pos_eight,
                   pos_nine, bt_1_s, bt_2_s, bt_3_s)
        elif get_pos_one == get_pos_four == cpu_player and get_pos_seven == "" or get_pos_four == get_pos_seven == cpu_player and get_pos_one == "" \
                or get_pos_one == get_pos_seven == cpu_player and get_pos_four == "":
            image_one = label_one
            image_two = label_four
            image_three = label_seven
            bt_1_s = button_one_state
            bt_2_s = button_four_state
            bt_3_s = button_seven_state
            choice(get_pos_one, get_pos_four, get_pos_seven, image_one, image_two, image_three, pos_one, pos_four,
                   pos_seven, bt_1_s, bt_2_s, bt_3_s)
        elif get_pos_two == get_pos_five == cpu_player and get_pos_eight == "" or get_pos_five == get_pos_eight == cpu_player and get_pos_two == "" \
                or get_pos_two == get_pos_eight == cpu_player and get_pos_five == "":
            image_one = label_two
            image_two = label_five
            image_three = label_eight
            bt_1_s = button_two_state
            bt_2_s = button_five_state
            bt_3_s = button_eight_state
            choice(get_pos_two, get_pos_five, get_pos_eight, image_one, image_two, image_three, pos_two, pos_five,
                   pos_eight, bt_1_s, bt_2_s, bt_3_s)
        elif get_pos_three == get_pos_six == cpu_player and get_pos_nine == "" or get_pos_six == get_pos_nine == cpu_player and get_pos_three == "" \
                or get_pos_three == get_pos_nine == cpu_player and get_pos_six == "":
            image_one = label_three
            image_two = label_six
            image_three = label_nine
            bt_1_s = button_three_state
            bt_2_s = button_six_state
            bt_3_s = button_nine_state
            choice(get_pos_three, get_pos_six, get_pos_nine, image_one, image_two, image_three, pos_three, pos_six,
                   pos_nine, bt_1_s, bt_2_s, bt_3_s)
        elif get_pos_one == get_pos_five == cpu_player and get_pos_nine == "" or get_pos_five == get_pos_nine == cpu_player and get_pos_one == "" \
                or get_pos_one == get_pos_nine == cpu_player and get_pos_five == "":
            image_one = label_one
            image_two = label_five
            image_three = label_nine
            bt_1_s = button_one_state
            bt_2_s = button_five_state
            bt_3_s = button_nine_state
            choice(get_pos_one, get_pos_five, get_pos_nine, image_one, image_two, image_three, pos_one, pos_five,
                   pos_nine,
                   bt_1_s, bt_2_s, bt_3_s)
        elif get_pos_three == get_pos_five == cpu_player and get_pos_seven == "" or get_pos_five == get_pos_seven == cpu_player and get_pos_three == "" \
                or get_pos_three == get_pos_seven == cpu_player and get_pos_five == "":
            image_one = label_three
            image_two = label_five
            image_three = label_seven
            bt_1_s = button_three_state
            bt_2_s = button_five_state
            bt_3_s = button_seven_state
            choice(get_pos_three, get_pos_five, get_pos_seven, image_one, image_two, image_three, pos_three, pos_five,
                   pos_seven, bt_1_s, bt_2_s, bt_3_s)
        elif get_pos_one == get_pos_two == against_player and get_pos_three == "" or get_pos_two == get_pos_three == against_player and \
                get_pos_one == "" or get_pos_one == get_pos_three == against_player and get_pos_two == "":
            image_one = label_one
            image_two = label_two
            image_three = label_three
            bt_1_s = button_one_state
            bt_2_s = button_two_state
            bt_3_s = button_three_state
            choice(get_pos_one, get_pos_two, get_pos_three, image_one, image_two, image_three, pos_one, pos_two,
                   pos_three, bt_1_s, bt_2_s, bt_3_s)
        elif get_pos_four == get_pos_five == against_player and get_pos_six == "" or get_pos_five == get_pos_six == against_player and get_pos_four == "" \
                or get_pos_four == get_pos_six == against_player and get_pos_five == "":
            image_one = label_four
            image_two = label_five
            image_three = label_six
            bt_1_s = button_four_state
            bt_2_s = button_five_state
            bt_3_s = button_six_state
            choice(get_pos_four, get_pos_five, get_pos_six, image_one, image_two, image_three, pos_four, pos_five,
                   pos_six, bt_1_s, bt_2_s, bt_3_s)
        elif get_pos_seven == get_pos_eight == against_player and get_pos_nine == "" or get_pos_eight == get_pos_nine == against_player and get_pos_seven == "" \
                or get_pos_seven == get_pos_nine == against_player and get_pos_eight == "":
            image_one = label_seven
            image_two = label_eight
            image_three = label_nine
            bt_1_s = button_seven_state
            bt_2_s = button_eight_state
            bt_3_s = button_nine_state
            choice(get_pos_seven, get_pos_eight, get_pos_nine, image_one, image_two, image_three, pos_seven, pos_eight,
                   pos_nine, bt_1_s, bt_2_s, bt_3_s)
        elif get_pos_one == get_pos_four == against_player and get_pos_seven == "" or get_pos_four == get_pos_seven == against_player and get_pos_one == "" \
                or get_pos_one == get_pos_seven == against_player and get_pos_four == "":
            image_one = label_one
            image_two = label_four
            image_three = label_seven
            bt_1_s = button_one_state
            bt_2_s = button_four_state
            bt_3_s = button_seven_state
            choice(get_pos_one, get_pos_four, get_pos_seven, image_one, image_two, image_three, pos_one, pos_four,
                   pos_seven, bt_1_s, bt_2_s, bt_3_s)
        elif get_pos_two == get_pos_five == against_player and get_pos_eight == "" or get_pos_five == get_pos_eight == against_player and get_pos_two == "" \
                or get_pos_two == get_pos_eight == against_player and get_pos_five == "":
            image_one = label_two
            image_two = label_five
            image_three = label_eight
            bt_1_s = button_two_state
            bt_2_s = button_five_state
            bt_3_s = button_eight_state
            choice(get_pos_two, get_pos_five, get_pos_eight, image_one, image_two, image_three, pos_two, pos_five,
                   pos_eight, bt_1_s, bt_2_s, bt_3_s)
        elif get_pos_three == get_pos_six == against_player and get_pos_nine == "" or get_pos_six == get_pos_nine == against_player and get_pos_three == "" \
                or get_pos_three == get_pos_nine == against_player and get_pos_six == "":
            image_one = label_three
            image_two = label_six
            image_three = label_nine
            bt_1_s = button_three_state
            bt_2_s = button_six_state
            bt_3_s = button_nine_state
            choice(get_pos_three, get_pos_six, get_pos_nine, image_one, image_two, image_three, pos_three, pos_six,
                   pos_nine, bt_1_s, bt_2_s, bt_3_s)
        elif get_pos_one == get_pos_five == against_player and get_pos_nine == "" or get_pos_five == get_pos_nine == against_player and get_pos_one == "" \
                or get_pos_one == get_pos_nine == against_player and get_pos_five == "":
            image_one = label_one
            image_two = label_five
            image_three = label_nine
            bt_1_s = button_one_state
            bt_2_s = button_five_state
            bt_3_s = button_nine_state
            choice(get_pos_one, get_pos_five, get_pos_nine, image_one, image_two, image_three, pos_one, pos_five,
                   pos_nine, bt_1_s, bt_2_s, bt_3_s)
        elif get_pos_three == get_pos_five == against_player and get_pos_seven == "" or get_pos_five == get_pos_seven == against_player and get_pos_three == "" \
                or get_pos_three == get_pos_seven == against_player and get_pos_five == "":
            image_one = label_three
            image_two = label_five
            image_three = label_seven
            bt_1_s = button_three_state
            bt_2_s = button_five_state
            bt_3_s = button_seven_state
            choice(get_pos_three, get_pos_five, get_pos_seven, image_one, image_two, image_three, pos_three, pos_five,
                   pos_seven, bt_1_s, bt_2_s, bt_3_s)
        elif get_pos_one == get_pos_two == get_pos_three == "" or get_pos_one == get_pos_two == "" and get_pos_three == cpu_player \
                or get_pos_two == get_pos_three == "" and get_pos_one == cpu_player or get_pos_one == get_pos_three == "" \
                and get_pos_two == cpu_player:
            image_one = label_one
            image_two = label_two
            image_three = label_three
            bt_1_s = button_one_state
            bt_2_s = button_two_state
            bt_3_s = button_three_state
            choice(get_pos_one, get_pos_two, get_pos_three, image_one, image_two, image_three, pos_one, pos_two,
                   pos_three, bt_1_s, bt_2_s, bt_3_s)
        elif get_pos_four == get_pos_five == get_pos_six == "" or get_pos_four == get_pos_five == "" and get_pos_six == cpu_player \
                or get_pos_five == get_pos_six == "" and get_pos_four == cpu_player or get_pos_four == get_pos_six == "" and get_pos_five == cpu_player:
            image_one = label_four
            image_two = label_five
            image_three = label_six
            bt_1_s = button_four_state
            bt_2_s = button_five_state
            bt_3_s = button_six_state
            choice(get_pos_four, get_pos_five, get_pos_six, image_one, image_two, image_three, pos_four, pos_five,
                   pos_six, bt_1_s, bt_2_s, bt_3_s)
        elif get_pos_seven == get_pos_eight == get_pos_nine == "" or get_pos_seven == get_pos_eight == "" and get_pos_nine == cpu_player \
                or get_pos_eight == get_pos_nine == "" and get_pos_seven == cpu_player or get_pos_seven == get_pos_nine == "" and get_pos_eight == cpu_player:
            image_one = label_seven
            image_two = label_eight
            image_three = label_nine
            bt_1_s = button_seven_state
            bt_2_s = button_eight_state
            bt_3_s = button_nine_state
            choice(get_pos_seven, get_pos_eight, get_pos_nine, image_one, image_two, image_three, pos_seven, pos_eight,
                   pos_nine, bt_1_s, bt_2_s, bt_3_s)
        elif get_pos_one == get_pos_four == get_pos_seven == "" or get_pos_one == get_pos_four == "" and get_pos_seven == cpu_player \
                or get_pos_four == get_pos_seven == "" and get_pos_one == cpu_player or get_pos_one == get_pos_seven == "" and get_pos_four == cpu_player:
            image_one = label_one
            image_two = label_four
            image_three = label_seven
            bt_1_s = button_one_state
            bt_2_s = button_four_state
            bt_3_s = button_seven_state
            choice(get_pos_one, get_pos_four, get_pos_seven, image_one, image_two, image_three, pos_one, pos_four,
                   pos_seven, bt_1_s, bt_2_s, bt_3_s)
        elif get_pos_two == get_pos_five == get_pos_eight == "" or get_pos_two == get_pos_five == "" and get_pos_eight == cpu_player \
                or get_pos_five == get_pos_eight == "" and get_pos_two == cpu_player or get_pos_two == get_pos_eight == "" and get_pos_five == cpu_player:
            image_one = label_two
            image_two = label_five
            image_three = label_eight
            bt_1_s = button_two_state
            bt_2_s = button_five_state
            bt_3_s = button_eight_state
            choice(get_pos_two, get_pos_five, get_pos_eight, image_one, image_two, image_three, pos_two, pos_five,
                   pos_eight, bt_1_s, bt_2_s, bt_3_s)
        elif get_pos_three == get_pos_six == get_pos_nine == "" or get_pos_three == get_pos_six == "" and get_pos_nine == cpu_player \
                or get_pos_six == get_pos_nine == "" and get_pos_three == cpu_player or get_pos_three == get_pos_nine == "" and get_pos_six == cpu_player:
            image_one = label_three
            image_two = label_six
            image_three = label_nine
            bt_1_s = button_three_state
            bt_2_s = button_six_state
            bt_3_s = button_nine_state
            choice(get_pos_three, get_pos_six, get_pos_nine, image_one, image_two, image_three, pos_three, pos_six,
                   pos_nine, bt_1_s, bt_2_s, bt_3_s)
        elif get_pos_one == get_pos_five == get_pos_nine == "" or get_pos_one == get_pos_five == "" and get_pos_nine == cpu_player \
                or get_pos_five == get_pos_nine == "" and get_pos_one == cpu_player or get_pos_one == get_pos_nine == "" and get_pos_five == cpu_player:
            image_one = label_one
            image_two = label_five
            image_three = label_nine
            bt_1_s = button_one_state
            bt_2_s = button_five_state
            bt_3_s = button_nine_state
            choice(get_pos_one, get_pos_five, get_pos_nine, image_one, image_two, image_three, pos_one, pos_five,
                   pos_nine, bt_1_s, bt_2_s, bt_3_s)
        elif get_pos_three == get_pos_five == get_pos_seven == "" or get_pos_three == get_pos_five == "" and get_pos_seven == cpu_player \
                or get_pos_five == get_pos_seven == "" and get_pos_three == cpu_player or get_pos_three == get_pos_seven == "" and get_pos_five == cpu_player:
            image_one = label_three
            image_two = label_five
            image_three = label_seven
            bt_1_s = button_three_state
            bt_2_s = button_five_state
            bt_3_s = button_seven_state
            choice(get_pos_three, get_pos_five, get_pos_seven, image_one, image_two, image_three, pos_three, pos_five,
                   pos_seven, bt_1_s, bt_2_s, bt_3_s)
        elif get_pos_one == "":
            if button_one_state.get() == True:
                label_one.configure(image=cpu_image)
                pos_one.set(cpu_player)
                button_one_state.set(False)
                turn.set(against_player + "'s Turn")
                check_positions()
                cpu_turn()
            else:
                pass
        elif get_pos_two == "":
            if button_two_state.get() == True:
                label_two.configure(image=cpu_image)
                pos_two.set(cpu_player)
                button_two_state.set(False)
                turn.set(against_player + "'s Turn")
                check_positions()
                cpu_turn()
            else:
                pass
        elif get_pos_three == "":
            if button_three_state == True:
                label_three.configure(image=cpu_image)
                pos_three.set(cpu_player)
                button_three_state.set(False)
                turn.set(against_player + "'s Turn")
                check_positions()
                cpu_turn()
            else:
                pass
        elif get_pos_four == "":
            if button_four_state.get() == True:
                label_four.configure(image=cpu_image)
                pos_four.set(cpu_player)
                button_four_state.set(False)
                turn.set(against_player + "'s Turn")
                check_positions()
                cpu_turn()
            else:
                pass

        elif get_pos_five == "":
            if button_five_state.get() == True:
                label_five.configure(image=cpu_image)
                pos_five.set(cpu_player)
                button_five_state.set(False)
                turn.set(against_player + "'s Turn")
                check_positions()
                cpu_turn()
            else:
                pass
        elif get_pos_six == "":
            if button_six_state.get() == True:
                label_six.configure(image=cpu_image)
                pos_six.set(cpu_player)
                button_six_state.set(False)
                turn.set(against_player + "'s Turn")
                check_positions()
                cpu_turn()
            else:
                pass
        elif get_pos_seven == "":
            if button_seven_state.get() == True:
                label_seven.configure(image=cpu_image)
                pos_seven.set(cpu_player)
                button_seven_state.set(False)
                turn.set(against_player + "'s Turn")
                check_positions()
                cpu_turn()
            else:
                pass
        elif get_pos_eight == "":
            if button_eight_state.get() == True:
                label_eight.configure(image=cpu_image)
                pos_eight.set(cpu_player)
                button_eight_state.set(False)
                turn.set(against_player + "'s Turn")
                check_positions()
                cpu_turn()
            else:
                pass
        elif get_pos_nine == "":
            if button_nine_state.get() == True:
                label_nine.configure(image=cpu_image)
                pos_nine.set(cpu_player)
                button_nine_state.set(False)
                turn.set(against_player + "'s Turn")
                check_positions()
                cpu_turn()
            else:
                pass
        else:
            check_positions()


def mode():
    def players_turn_one(event):
        if button_one_state.get() == True:
            if main_turn.get() == "" or main_turn.get() == "x_turn":
                label_one.config(image=x_img)
                turn.set(player_two_name.get() + "'s Turn")
                pos_one.set(player_one_name.get())
                main_turn.set("o_turn")
            else:
                label_one.config(image=zero_img)
                turn.set(player_one_name.get() + "'s Turn")
                pos_one.set(player_two_name.get())
                main_turn.set("x_turn")
            button_one_state.set(False)
            check_positions()
        else:
            pass

    def players_turn_two(event):
        if button_two_state.get() == True:
            if main_turn.get() == "" or main_turn.get() == "x_turn":
                label_two.config(image=x_img)
                turn.set(player_two_name.get() + "'s Turn")
                pos_two.set(player_one_name.get())
                main_turn.set("o_turn")
            else:
                label_two.config(image=zero_img)
                turn.set(player_one_name.get() + "'s Turn")
                pos_two.set(player_two_name.get())
                main_turn.set("x_turn")
            button_two_state.set(False)
            check_positions()
        else:
            pass

    def players_turn_three(event):
        if button_three_state.get() == True:
            if main_turn.get() == "" or main_turn.get() == "x_turn":
                label_three.config(image=x_img)
                turn.set(player_two_name.get() + "'s Turn")
                pos_three.set(player_one_name.get())
                main_turn.set("o_turn")
            else:
                label_three.config(image=zero_img)
                turn.set(player_one_name.get() + "'s Turn")
                pos_three.set(player_two_name.get())
                main_turn.set("x_turn")
            button_three_state.set(False)
            check_positions()
        else:
            pass

    def players_turn_four(event):
        if button_four_state.get() == True:
            if main_turn.get() == "" or main_turn.get() == "x_turn":
                label_four.config(image=x_img)
                turn.set(player_two_name.get() + "'s Turn")
                pos_four.set(player_one_name.get())
                main_turn.set("o_turn")
            else:
                label_four.config(image=zero_img)
                turn.set(player_one_name.get() + "'s Turn")
                pos_four.set(player_two_name.get())
                main_turn.set("x_turn")
            button_four_state.set(False)
            check_positions()
        else:
            pass

    def players_turn_five(event):
        if button_five_state.get() == True:
            if main_turn.get() == "" or main_turn.get() == "x_turn":
                label_five.config(image=x_img)
                turn.set(player_two_name.get() + "'s Turn")
                pos_five.set(player_one_name.get())
                main_turn.set("o_turn")
            else:
                label_five.config(image=zero_img)
                turn.set(player_one_name.get() + "'s Turn")
                pos_five.set(player_two_name.get())
                main_turn.set("x_turn")
            button_five_state.set(False)
            check_positions()
        else:
            pass

    def players_turn_six(event):
        if button_six_state.get() == True:
            if main_turn.get() == "" or main_turn.get() == "x_turn":
                label_six.config(image=x_img)
                turn.set(player_two_name.get() + "'s Turn")
                pos_six.set(player_one_name.get())
                main_turn.set("o_turn")
            else:
                label_six.config(image=zero_img)
                turn.set(player_one_name.get() + "'s Turn")
                pos_six.set(player_two_name.get())
                main_turn.set("x_turn")
            button_six_state.set(False)
            check_positions()
        else:
            pass

    def players_turn_seven(event):
        if button_seven_state.get() == True:
            if main_turn.get() == "" or main_turn.get() == "x_turn":
                label_seven.config(image=x_img)
                turn.set(player_two_name.get() + "'s Turn")
                pos_seven.set(player_one_name.get())
                main_turn.set("o_turn")
            else:
                label_seven.config(image=zero_img)
                turn.set(player_one_name.get() + "'s Turn")
                pos_seven.set(player_two_name.get())
                main_turn.set("x_turn")
            button_seven_state.set(False)
            check_positions()
        else:
            pass

    def players_turn_eight(event):
        if button_eight_state.get() == True:
            if main_turn.get() == "" or main_turn.get() == "x_turn":
                label_eight.config(image=x_img)
                turn.set(player_two_name.get() + "'s Turn")
                pos_eight.set(player_one_name.get())
                main_turn.set("o_turn")
            else:
                label_eight.config(image=zero_img)
                turn.set(player_one_name.get() + "'s Turn")
                pos_eight.set(player_two_name.get())
                main_turn.set("x_turn")
            button_eight_state.set(False)
            check_positions()
        else:
            pass

    def players_turn_nine(event):
        if button_nine_state.get() == True:
            if main_turn.get() == "" or main_turn.get() == "x_turn":
                label_nine.config(image=x_img)
                turn.set(player_two_name.get() + "'s Turn")
                pos_nine.set(player_one_name.get())
                main_turn.set("o_turn")
            else:
                label_nine.config(image=zero_img)
                turn.set(player_one_name.get() + "'s Turn")
                pos_nine.set(player_two_name.get())
                main_turn.set("x_turn")
            button_nine_state.set(False)
            check_positions()
        else:
            pass

    label_one.bind("<Button-1>", players_turn_one)
    label_two.bind("<Button-1>", players_turn_two)
    label_three.bind("<Button-1>", players_turn_three)
    label_four.bind("<Button-1>", players_turn_four)
    label_five.bind("<Button-1>", players_turn_five)
    label_six.bind("<Button-1>", players_turn_six)
    label_seven.bind("<Button-1>", players_turn_seven)
    label_eight.bind("<Button-1>", players_turn_eight)
    label_nine.bind("<Button-1>", players_turn_nine)


def cpu_against():
    def players_turn_one(event):
        if button_one_state.get() == True:
            label_one.config(image=x_img)
            pos_one.set(player_one_name.get())
            main_turn.set("o_turn")
            button_one_state.set(False)
            turn.set(player_two_name.get() + "'s Turn")
            check_positions()
            cpu_turn()
        else:
            pass

    def players_turn_two(event):
        if button_two_state.get() == True:
            label_two.config(image=x_img)
            pos_two.set(player_one_name.get())
            main_turn.set("o_turn")
            button_two_state.set(False)
            turn.set(player_two_name.get() + "'s Turn")
            check_positions()
            cpu_turn()
        else:
            pass

    def players_turn_three(event):
        if button_three_state.get() == True:
            label_three.config(image=x_img)
            pos_three.set(player_one_name.get())
            main_turn.set("o_turn")
            button_three_state.set(False)
            turn.set(player_two_name.get() + "'s Turn")
            check_positions()
            cpu_turn()
        else:
            pass

    def players_turn_four(event):
        if button_four_state.get() == True:
            label_four.config(image=x_img)
            pos_four.set(player_one_name.get())
            main_turn.set("o_turn")
            button_four_state.set(False)
            turn.set(player_two_name.get() + "'s Turn")
            check_positions()
            cpu_turn()
        else:
            pass

    def players_turn_five(event):
        if button_five_state.get() == True:
            label_five.config(image=x_img)
            pos_five.set(player_one_name.get())
            main_turn.set("o_turn")
            button_five_state.set(False)
            turn.set(player_two_name.get() + "'s Turn")
            check_positions()
            cpu_turn()
        else:
            pass

    def players_turn_six(event):
        if button_six_state.get() == True:
            label_six.config(image=x_img)
            pos_six.set(player_one_name.get())
            main_turn.set("o_turn")
            button_six_state.set(False)
            turn.set(player_two_name.get() + "'s Turn")
            check_positions()
            cpu_turn()
        else:
            pass

    def players_turn_seven(event):
        if button_seven_state.get() == True:
            label_seven.config(image=x_img)
            pos_seven.set(player_one_name.get())
            main_turn.set("o_turn")
            button_seven_state.set(False)
            turn.set(player_two_name.get() + "'s Turn")
            check_positions()
            cpu_turn()
        else:
            pass

    def players_turn_eight(event):
        if button_eight_state.get() == True:
            label_eight.config(image=x_img)
            pos_eight.set(player_one_name.get())
            main_turn.set("o_turn")
            button_eight_state.set(False)
            turn.set(player_two_name.get() + "'s Turn")
            check_positions()
            cpu_turn()
        else:
            pass

    def players_turn_nine(event):
        if button_nine_state.get() == True:
            label_nine.config(image=x_img)
            pos_nine.set(player_one_name.get())
            main_turn.set("o_turn")
            button_nine_state.set(False)
            turn.set(player_two_name.get() + "'s Turn")
            check_positions()
            cpu_turn()
        else:
            pass

    label_one.bind("<Button-1>", players_turn_one)
    label_two.bind("<Button-1>", players_turn_two)
    label_three.bind("<Button-1>", players_turn_three)
    label_four.bind("<Button-1>", players_turn_four)
    label_five.bind("<Button-1>", players_turn_five)
    label_six.bind("<Button-1>", players_turn_six)
    label_seven.bind("<Button-1>", players_turn_seven)
    label_eight.bind("<Button-1>", players_turn_eight)
    label_nine.bind("<Button-1>", players_turn_nine)


def change_player_two_name(event):
    if game_state.get()=="Started":
        msg="You cant change the Players name while the Match is Started, Please Reset the Match in Order to " \
            "Change Players Names."
        mb.showwarning("Can't Change Names",msg)
    else:
        main = Toplevel()
        main.resizable(0, 0)
        main.geometry("310x155+520+250")
        def change_name(event):
            if len(player_one_new_name.get()) >= 15 or len(player_two_new_name.get()) >= 15:
                msg = "Character Limit Exceeded! Max Characters Allowed are 15 only"
                mb.showerror("Limit Exceeded", msg)
            else:
                if player_one_new_name.get() == "" and player_two_new_name.get() == "":
                    player_two_name_label.configure(text="X" + " Vs " + "O")
                    player_one_name.set("X")
                    player_two_name.set("O")
                elif player_one_new_name.get() == "":
                    player_two_name_label.configure(text="X" + " Vs " + player_two_new_name.get())
                    player_one_name.set("X")
                    player_two_name.set(player_two_new_name.get())
                    info_label.configure(fg="green")
                    show_name.set("Success!")
                elif player_two_new_name.get() == "":
                    player_two_name_label.configure(text=player_one_new_name.get() + " Vs " + "O")
                    player_one_name.set(player_one_new_name.get())
                    player_two_name.set("O")
                    info_label.configure(fg="green")
                    show_name.set("Success!")
                else:
                    player_two_name_label.configure(text=player_one_new_name.get() + " Vs " + player_two_new_name.get())
                    player_one_name.set(player_one_new_name.get())
                    player_two_name.set(player_two_new_name.get())
                    info_label.configure(fg="green")
                    show_name.set("Success!")
        icon = ImageTk.PhotoImage(file="Bin/TGZ_icon.ico")
        main.iconphoto(False, icon)
        main.title("Change Name")
        frame = LabelFrame(main, text="Players Names")
        frame.place(x=5, y=5, relheight=0.92, relwidth=0.97)
        Label(main, text="Enter Player 1 New Name: ").place(x=20, y=20)
        ttk.Entry(main, textvariable=player_one_new_name).place(x=170, y=20)
        Label(main, text="Enter Player 2 New Name: ").place(x=20, y=50)
        ttk.Entry(main, textvariable=player_two_new_name).place(x=170, y=50)
        but_2 = Label(main, text="Save", bg="black", fg="white", cursor="hand2")
        but_2.place(x=265, y=80)
        info_label = Label(main, textvariable=show_name)
        info_label.place(x=180, y=80)
        note_label=Label(main,text="If you Want to Play with CPU then write CPU or cpu\n in Player 2 Name. ",fg="red")
        note_label.place(x=15,y=105)
        but_2.bind("<Button-1>", change_name)


def start_change_bg(event):
    if game_state.get()=="" or game_state.get()=="Start":
        start_button.configure(bg="green2",fg="white")
    else:
        start_button.configure(bg="red", fg="black")


def start_change_bg_2(event):
    if game_state.get() == "" or game_state.get() == "Start":
        start_button.configure(bg="red", fg="black")
    else:
        start_button.configure(bg="green2", fg="white")


def name_change_bg(event):
    player_two_name_label.configure(bg="blue",fg="white")


def name_change_bg_2(event):
    player_two_name_label.configure(bg="white",fg="black")


def about_us(event):
    if about_us_window.get()==0:
        about_us_window.set(1)
        head = Toplevel()
        head.title("About Us")
        head.geometry("220x275+570+210")
        head.config(bg="black")
        head.resizable(0, 0)
        head.iconbitmap("Bin/TGZ_icon.ico")
        logo = PhotoImage(file="Bin/log.gif")
        tgz_logo = Label(head, image=logo, bg="blue", cursor="hand2")
        tgz_logo.pack()
        Label(head, bg="black", fg="white",
              text="Designed And Programmed By\n Harsh Nagar. For Any\n Help Email Us At -\n "
                   "nagar8339@gmail.com Or\n thegamerszone59@gmail.com.\n||Be Happy And "
                   "Programe Your Life||").pack()

        github_logo = ImageTk.PhotoImage(Image.open("Bin/github_image.png").resize((30, 30), Image.ANTIALIAS))
        github_label = Label(head, image=github_logo, text="Follow us on Github", compound=LEFT, cursor="hand2")
        github_label.place(x=20, y=150, width=180)
        instagram_logo = ImageTk.PhotoImage(Image.open("Bin/instagram_image.png").resize((30, 30), Image.ANTIALIAS))
        instagram_label = Label(head, image=instagram_logo, text="Follow us on Instagram", compound=LEFT,
                                cursor="hand2")
        instagram_label.place(x=20, y=190, width=180)
        facebook_logo = ImageTk.PhotoImage(Image.open("Bin/facebook_image.png").resize((50, 40), Image.ANTIALIAS))
        facebook_label = Label(head, image=facebook_logo, text="Follow us on Facebook", compound=LEFT, cursor="hand2")
        facebook_label.place(x=20, y=230, width=180, height=35)

        def open_tgz(event):
            webbrowser.open_new_tab("https://www.facebook.com/thegamerszoneofficial/")

        def open_github(event):
            webbrowser.open_new_tab("https://github.com/harshnagar")

        def open_instagram(event):
            webbrowser.open_new_tab("https://www.instagram.com/harshnagarx/")

        def open_facebook(event):
            webbrowser.open_new_tab("https://www.facebook.com/harshnagarx")

        def fb_bg_change(event):
            facebook_label.configure(bg="blue", fg="white")

        def fb_bg_change_2(event):
            facebook_label.configure(bg="white", fg="black")

        def insta_bg_change(event):
            instagram_label.configure(bg="blue", fg="white")

        def insta_bg_change_2(event):
            instagram_label.configure(bg="white", fg="black")

        def git_bg_change(event):
            github_label.configure(bg="blue", fg="white")

        def git_bg_change_2(event):
            github_label.configure(bg="white", fg="black")

        def tgz_bg_change(event):
            tgz_logo.configure(bg="red")

        def tgz_bg_change_2(event):
            tgz_logo.configure(bg="blue")

        tgz_logo.bind('<Button-1>', open_tgz)
        github_label.bind('<Button-1>', open_github)
        instagram_label.bind('<Button-1>', open_instagram)
        facebook_label.bind('<Button-1>', open_facebook)
        facebook_label.bind('<Enter>', fb_bg_change)
        facebook_label.bind('<Leave>', fb_bg_change_2)
        instagram_label.bind('<Enter>', insta_bg_change)
        instagram_label.bind('<Leave>', insta_bg_change_2)
        github_label.bind('<Enter>', git_bg_change)
        github_label.bind('<Leave>', git_bg_change_2)
        tgz_logo.bind('<Enter>', tgz_bg_change)
        tgz_logo.bind('<Leave>', tgz_bg_change_2)

        def destroy_about_us():
            about_us_window.set(0)
            head.destroy()

        head.protocol("WM_DELETE_WINDOW", destroy_about_us)
        head.mainloop()

    else:
        msg="About us Window is already Opened, Please close it then retry"
        mb.showinfo("Already Opened",msg)


def information(event):
    hg_Label.configure(bg="blue")


def information_2(event):
    hg_Label.configure(bg="white")


def change_theme_one(event):
    label.configure(image=theme_one_img)


def change_theme_two(event):
    label.configure(image=theme_two_img)


def change_theme_three(event):
    label.configure(image=theme_three_img)


def change_theme_four(event):
    label.configure(image=theme_four_img)


def change_theme_default(event):
    label.configure(image=bg_img)


def mode_change_bg(event):
    game_mode.configure(bg="green2")


def mode_change_bg_2(event):
    game_mode.configure(bg="white")


def change_game_mode(event):
    if game_state.get()=="Started":
        msg = "You cant change the Players name while the Match is Started, Please Reset the Match in Order to " \
              "Change Players Names."
        mb.showwarning("Can't Change Names", msg)
    else:
        if game_mode_container.get()=="Cpu":
            msg = "Are you sure you want to change the Game Mode to CPU MODE ?"
            if mb.askyesno("Confirmation", msg) == True:
                game_mode.configure(text="MODE: CPU MODE")
                player_two_name.set("CPU")
                player_two_name_label.configure(text=player_one_name.get() + " Vs " + player_two_name.get())
                game_mode_container.set("Multiplayer")
            else:
                pass
        else:
            msg = "Are you sure you want to change the Game Mode to MULTIPLAYER MODE ?"
            if mb.askyesno("Confirmation", msg) == True:
                game_mode.configure(text="MODE: MULTIPLAYER MODE")
                player_two_name.set("O")
                player_two_name_label.configure(text=player_one_name.get() + " Vs " + player_two_name.get())
                game_mode_container.set("Cpu")
            else:
                pass


# ALL IMAGES CONTAINERS
player_turn_label = Label(main_window,textvariable=turn,bg="yellow",fg="black")
player_turn_label.pack(anchor=CENTER)
start_button = Label(main_window,text="START",fg="black",bg="red",font=100,cursor="hand2")
start_button.pack(anchor=CENTER)
match_label = Label(main_window,text="Match: ",bg="white",fg="black")
match_label.place(x=0,y=5)
match_num_label = Label(main_window,textvariable=match,bg="white",fg="black")
match_num_label.place(x=42,y=5)
player_two_name_label = Label(main_window,text=player_one_name.get()+ " Vs " + player_two_name.get(),bg="white",fg="black",cursor="hand2")
player_two_name_label.place(x=0,y=27)
label = Label(image=bg_img,bg="black")
label.place(y=50)
label_one = Label(bg="cyan",cursor="hand2")
label_one.place(x=20,y=65,height=140,width=140)
label_two = Label(bg="cyan",cursor="hand2")
label_two.place(x=183,y=65,height=140,width=140)
label_three=Label(bg="cyan",cursor="hand2")
label_three.place(x=345,y=65,height=140,width=140)
label_four=Label(bg="cyan",cursor="hand2")
label_four.place(x=20,y=232,height=140,width=140)
label_five=Label(bg="cyan",cursor="hand2")
label_five.place(x=183,y=232,height=140,width=140)
label_six=Label(bg="cyan",cursor="hand2")
label_six.place(x=345,y=232,height=140,width=140)
label_seven=Label(bg="cyan",cursor="hand2")
label_seven.place(x=20,y=394,height=140,width=140)
label_eight=Label(bg="cyan",cursor="hand2")
label_eight.place(x=183,y=394,height=140,width=140)
label_nine=Label(bg="cyan",cursor="hand2")
label_nine.place(x=345,y=395,height=140,width=140)
hg_Label=Label(main_window,image=hg_image,cursor="hand2")
hg_Label.place(x=460, y=15)
theme_one_label=Label(main_window,image=theme_but_one_img,bg="black",cursor="hand2")
theme_one_label.place(x=370,y=25)
theme_two_label=Label(main_window,image=theme_but_two_img,bg="black",cursor="hand2")
theme_two_label.place(x=340,y=25)
theme_three_label=Label(main_window,image=theme_but_three_img,bg="black",cursor="hand2")
theme_three_label.place(x=400,y=25)
theme_four_label=Label(main_window,image=theme_but_four_img,bg="black",cursor="hand2")
theme_four_label.place(x=430,y=25)
theme_default_label=Label(main_window,image=theme_but_default_img,bg="black",cursor="hand2")
theme_default_label.place(x=310,y=25)
game_mode=Label(main_window,text="Mode: MULTIPLAYER",bg="white",fg="black",cursor="hand2")
game_mode.place(x=5,y=555)


# ALL BINDINGS
player_two_name_label.bind("<Button-1>",change_player_two_name)
start_button.bind("<Enter>",start_change_bg)
start_button.bind("<Leave>",start_change_bg_2)
start_button.bind("<Button-1>",start_restart)
player_two_name_label.bind("<Enter>",name_change_bg)
player_two_name_label.bind("<Leave>",name_change_bg_2)
hg_Label.bind('<Button-1>', about_us)
hg_Label.bind('<Enter>', information)
hg_Label.bind('<Leave>', information_2)

def wlcm_msg():
    msg = "Welcome to TGZ Tic Tac Toe Game, Points to keep in mind are- \n" \
          "1) Start the game using START Button at the top.\n" \
          "2) Reset the Game by clicking on RESET button while Match is Over or in between the match.\n" \
          "3) To Change Players name Click on the VS Button.\n" \
          "4) You can't change the names when the game is started.\n" \
          "5) Maximum Characters for adding names are 15 only.\n" \
          "6) If you want to Play with CPU Then write cpu or CPU in player second name.\n" \
          "Thanks And Hope you Enjoy the Game."
    mb.showinfo("Welcome", msg)

theme_one_label.bind("<Button-1>",change_theme_one)
theme_two_label.bind("<Button-1>",change_theme_two)
theme_three_label.bind("<Button-1>",change_theme_three)
theme_four_label.bind("<Button-1>",change_theme_four)
theme_default_label.bind("<Button-1>",change_theme_default)
game_mode.bind("<Button-1>",change_game_mode)
game_mode.bind("<Enter>",mode_change_bg)
game_mode.bind("<Leave>",mode_change_bg_2)
wlcm_msg()

main_window.mainloop()