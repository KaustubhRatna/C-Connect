"""
This file launches the login page for admins
"""

# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

from tkinter import *
# Explicit imports to satisfy Flake8
import login
from gui import StudentLogin, LoginError,a_dashboard


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def authenticate(window,user,pwd):
    """
    checks with the database for authentication and redirects user accordingly
    """
    auth = login.authentication(user,pwd)
    if(auth == -1):
        LoginError.error(window)
    else:
        a_dashboard.dashboard(window)

def portal(window) :
    user = StringVar()
    pwd = StringVar()

    canvas = Canvas(
        window,
        bg = "#FFFFFF",
        height = 891,
        width = 411,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        205.0,
        373.0,
        image=image_image_1
    )

    canvas.create_text(
        135.0,
        122.0,
        anchor="nw",
        text="Connect",
        fill="#FF6338",
        font=("Spartan Bold", 28 * -1)
    )

    canvas.create_text(
        98.0,
        122.0,
        anchor="nw",
        text="C-",
        fill="#333333",
        font=("Spartan Bold", 28 * -1)
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        205.0,
        451.0,
        image=image_image_2
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("admin_panel.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_1 clicked"),
        relief="flat"
    )
    button_1.place(
        x=48.0,
        y=200.0,
        width=147.0,
        height=68.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("student_panel.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: StudentLogin.portal(window),
        relief="flat"
    )
    button_2.place(
        x=216.0,
        y=200.0,
        width=147.0,
        height=68.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("sign_in.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: authenticate(window,user.get(),pwd.get()),
        relief="flat"
        )
    button_3.place(
        x=105.0,
        y=575.0,
        width=200.0,
        height=60.0
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        197.0,
        454.0,
        image=entry_image_1
    )
    entry_1 = Entry(
        bd=0,
        bg="#FCFCFC",
        textvariable=pwd,
        show="*",
        highlightthickness=0
    )
    entry_1.place(
        x=61.0,
        y=434.0,
        width=272.0,
        height=38.0
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_2 = canvas.create_image(
        197.0,
        377.0,
        image=entry_image_2
    )
    entry_2 = Entry(
        bd=0,
        bg="#FCFCFC",
        textvariable=user,
        highlightthickness=0
    )
    entry_2.place(
        x=61.0,
        y=357.0,
        width=272.0,
        height=38.0
    )

    canvas.create_text(
        68.0,
        371.0,
        anchor="nw",
        text="Registration Number",
        fill="#000000",
        font=("JosefinSansRoman Regular", 18 * -1)
    )

    canvas.create_text(
        68.0,
        449.0,
        anchor="nw",
        text="Password",
        fill="#000000",
        font=("JosefinSansRoman Regular", 18 * -1)
    )

    image_image_3 = PhotoImage(
        file=relative_to_assets("book.png"))
    image_3 = canvas.create_image(
        287.0,
        135.0,
        image=image_image_3
    )

    image_image_4 = PhotoImage(
        file=relative_to_assets("image_5.png"))
    image_4 = canvas.create_image(
        205.505859375,
        277.0,
        image=image_image_4
    )

    image_image_5 = PhotoImage(
        file=relative_to_assets("line.png"))
    image_5 = canvas.create_image(
        198.0,
        400.0,
        image=image_image_5
    )

    image_image_6 = PhotoImage(
        file=relative_to_assets("line.png"))
    image_6 = canvas.create_image(
        198.0,
        477.0,
        image=image_image_6
    )

    image_image_7 = PhotoImage(
        file=relative_to_assets("pencils.png"))
    image_7 = canvas.create_image(
        213.0,
        837.9807739257812,
        image=image_image_7
    )
    window.resizable(False, False)
    window.mainloop()
