import customtkinter as ctk
import tkinter
import re

default_theme = "dark-blue"
default_appearance = "system"
custom_font = ('Roboto', 20)

def Create_Window(title):
    window = ctk.CTk()
    window.geometry("1400x800")
    window.resizable(width=False, height=False)
    Center_Window(window)
    frame = Create_Frame(window)
    window.wm_title(title)
    return window, frame 

def Center_Window(window):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    window_width = 1400
    window_height = 800
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    window.geometry(f"{window_width}x{window_height}+{x}+{y}")

def Create_Frame(window):
    frame = ctk.CTkFrame(master=window, width=750, height=600)
    frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    return frame

def Load_Page(window, page_type):
    window.destroy()
    if page_type == "admin":
        Admin_Registration_Page()
    elif page_type == "employee":
        Employee_Registration_Page()
    elif page_type == "settings":
        Settings_Page()
    elif page_type == "admin_main_page":
        Admin_Main_Page()
    elif page_type == "employee_main_page":
        Employee_Main_Page()
    elif page_type == "invalid_details_page":
        Invalid_Details_Page()
    else:
        Login_Page()

def Login_Page():
    LogPg_window, LogPg_frame = Create_Window("Login Page")

    LogPg_admin_txt = ctk.CTkLabel(master=LogPg_frame, text="Login as Admin:", font=('Roboto', 25))
    LogPg_admin_txt.place(x=85, y=50)

    LogPg_employee_txt = ctk.CTkLabel(master=LogPg_frame, text="Login as Employee:", font=('Roboto', 25))
    LogPg_employee_txt.place(x=450, y=50)

    LogPg_register_txt_1 = ctk.CTkLabel(master=LogPg_frame, font=('Roboto', 19), text="Don't have an account?   Register here as an")
    LogPg_register_txt_1.place(x=15, y=565)
    
    LogPg_register_txt_1 = ctk.CTkLabel(master=LogPg_frame, text="Or an", font=('Roboto', 18))
    LogPg_register_txt_1.place(x=535, y=565)

    LogPg_admin_underline = ctk.CTkButton(master=LogPg_frame, width=190, height=3, corner_radius=0, text="")
    LogPg_admin_underline.place(x=78, y=80)
 
    LogPg_employee_underline = ctk.CTkButton(master=LogPg_frame, width=230, height=3, corner_radius=0, text="")
    LogPg_employee_underline.place(x=442, y=80)

    LogPG_companyname_entry = ctk.CTkEntry(master=LogPg_frame, width=260, justify="center", font=('Roboto', 15), placeholder_text='Enter Company Name...')
    LogPG_companyname_entry.place(x=43, y=140)

    LogPG_admin_password_entry = ctk.CTkEntry(master=LogPg_frame, width=260, show="*", justify="center", font=('Roboto', 15), placeholder_text='Enter Password...')
    LogPG_admin_password_entry.place(x=43, y=260)

    LogPg_employee_username_entry = ctk.CTkEntry(master=LogPg_frame, width=260, justify="center", font=('Roboto', 15), placeholder_text='Enter Username...')
    LogPg_employee_username_entry.place(x=428, y=140)

    LogPg_employee_password_entry = ctk.CTkEntry(master=LogPg_frame, width=260, show="*", justify="center", font=('Roboto', 15), placeholder_text='Enter Password...')
    LogPg_employee_password_entry.place(x=428, y=260)
    
    LogPg_admin_login_button = ctk.CTkButton(master=LogPg_frame, width=200, text="Login", font=('Roboto', 15), corner_radius=20)
    LogPg_admin_login_button.configure(command=lambda:Load_Page(LogPg_window, "admin_main_page"))
    LogPg_admin_login_button.place(x=75, y=350)

    LogPg_employee_login_button = ctk.CTkButton(master=LogPg_frame, width=200, text="Login", font=('Roboto', 15), corner_radius=20)
    LogPg_employee_login_button.configure(command=lambda:Load_Page(LogPg_window, "employee_main_page"))
    LogPg_employee_login_button.place(x=460, y=350)

    LogPg_settings_button = ctk.CTkButton(master=LogPg_frame, width=100, corner_radius=20, text="Settings", font=('Roboto', 15))
    LogPg_settings_button.configure(command=lambda:Load_Page(LogPg_window, "settings"))
    LogPg_settings_button.place(x=645, y=5)
    
    LogPg_refresh_button = ctk.CTkButton(master=LogPg_frame, width=100, corner_radius=20, text="Refresh Page", font=('Roboto', 15))
    LogPg_refresh_button.configure(command=lambda: Load_Page(LogPg_window, "login"))
    LogPg_refresh_button.place(x=5, y=5)
    
    LogPg_employee_register_button = ctk.CTkButton(master=LogPg_frame, width=115, text="Employee", corner_radius=20, font=('Roboto', 15))
    LogPg_employee_register_button.configure(command=lambda: Load_Page(LogPg_window, "employee"))
    LogPg_employee_register_button.place(x=610, y=565)
    
    LogPg_admin_register_button = ctk.CTkButton(master=LogPg_frame, width=115, text="Admin", corner_radius=20, font=('Roboto', 15))
    LogPg_admin_register_button.configure(command=lambda: Load_Page(LogPg_window, "admin"))
    LogPg_admin_register_button.place(x=400, y=565)

    LogPg_window.mainloop()

def Admin_Registration_Page():
    AdPg_window, AdPg_frame = Create_Window("Admin Registration")

    AdPg_txt = ctk.CTkLabel(master=AdPg_frame, text="Admin Registration:", font=('Roboto', 25))
    AdPg_txt.place(x=260, y=50)

    AdPg_underline = ctk.CTkButton(master=AdPg_frame, width=230, height=3, corner_radius=0, text="")
    AdPg_underline.place(x=250, y=80)

    AdPg_firstname_entry = ctk.CTkEntry(master=AdPg_frame, width=260, justify="center", font=('Roboto', 15), placeholder_text='Enter First Name...')
    AdPg_firstname_entry.place(x=73, y=150)

    AdPg_lastname_entry = ctk.CTkEntry(master=AdPg_frame, width=260, justify="center", font=('Roboto', 15), placeholder_text='Enter Last Name...')
    AdPg_lastname_entry.place(x=408, y=150)

    AdPg_password_entry = ctk.CTkEntry(master=AdPg_frame, width=260, show="*", justify="center", font=('Roboto', 15), placeholder_text='Enter Password...')
    AdPg_password_entry.place(x=73, y=315)

    AdPg_confirmpassword_entry = ctk.CTkEntry(master=AdPg_frame, width=260, show="*", justify="center", font=('Roboto', 15), placeholder_text='Confirm Password...')
    AdPg_confirmpassword_entry.place(x=408, y=315)

    AdPg_companyname_entry = ctk.CTkEntry(master=AdPg_frame, width=260, justify="center", font=('Roboto', 15), placeholder_text='Enter Company Name...')
    AdPg_companyname_entry.place(x=238, y=430)

    AdPg_register_button = ctk.CTkButton(master=AdPg_frame, width=200, text="Register for an account", font=('Roboto', 18), corner_radius=20)
    AdPg_register_button.configure(command=lambda:Get_Admin_Details(AdPg_firstname_entry, AdPg_lastname_entry, AdPg_password_entry, AdPg_confirmpassword_entry, AdPg_companyname_entry))
    AdPg_register_button.place(x=260, y=525)
    
    AdPg_refresh_button = ctk.CTkButton(master=AdPg_frame, width=100, text="Refresh Page", font=('Roboto', 15), corner_radius=20)
    AdPg_refresh_button.configure(command=lambda: Load_Page(AdPg_window, "admin"))
    AdPg_refresh_button.place(x=5, y=5)
    
    AdPg_return_button = ctk.CTkButton(master=AdPg_frame, width=100, corner_radius=20, text="Return", font=('Roboto', 15))
    AdPg_return_button.configure(command=lambda: Load_Page(AdPg_window, "login"))
    AdPg_return_button.place(x=645, y=5)
    
    AdPg_window.mainloop()

def Employee_Registration_Page():
    EmpPg_window, EmpPg_frame = Create_Window("Employee Registration")

    EmpPg_txt = ctk.CTkLabel(master=EmpPg_frame, text="Employee Registration:", font=('Roboto', 25))
    EmpPg_txt.place(x=260, y=50)

    EmpPg_underline = ctk.CTkButton(master=EmpPg_frame, width=270, height=3, corner_radius=0, text="")
    EmpPg_underline.place(x=253, y=80)

    EmpPg_firstname_entry = ctk.CTkEntry(master=EmpPg_frame, width=260, justify="center", font=('Roboto', 15), placeholder_text='Enter First Name...')
    EmpPg_firstname_entry.place(x=73, y=150)

    EmpPg_lastname_entry = ctk.CTkEntry(master=EmpPg_frame, width=260, justify="center", font=('Roboto', 15), placeholder_text='Enter Last Name...')
    EmpPg_lastname_entry.place(x=408, y=150)

    EmpPg_password_entry = ctk.CTkEntry(master=EmpPg_frame, width=260, show="*", justify="center", font=('Roboto', 15), placeholder_text='Enter Password...')
    EmpPg_password_entry.place(x=73, y=295)

    EmpPg_confirmpassword_entry = ctk.CTkEntry(master=EmpPg_frame, width=260, show="*", justify="center", font=('Roboto', 15), placeholder_text='Confirm Password...')
    EmpPg_confirmpassword_entry.place(x=408, y=295)

    EmpPg_companyname_entry = ctk.CTkEntry(master=EmpPg_frame, width=260, justify="center", font=('Roboto', 15), placeholder_text='Enter Company Name...')
    EmpPg_companyname_entry.place(x=73, y=430)

    EmpPg_companyid_entry = ctk.CTkEntry(master=EmpPg_frame, width=260, justify="center", font=('Roboto', 15), placeholder_text='Enter Company ID...')
    EmpPg_companyid_entry.place(x=408, y=430)

    EmpPg_registration_button = ctk.CTkButton(master=EmpPg_frame, width=200, text="Register for an account", font=('Roboto', 18), corner_radius=20)
    EmpPg_registration_button.configure(command=lambda: Get_Employee_Details(EmpPg_firstname_entry, EmpPg_lastname_entry, EmpPg_password_entry, EmpPg_confirmpassword_entry, EmpPg_companyname_entry))
    EmpPg_registration_button.place(x=260, y=525) 

    EmpPg_refresh_button = ctk.CTkButton(master=EmpPg_frame, width=100, text="Refresh Page", font=('Roboto', 15), corner_radius=20)
    EmpPg_refresh_button.configure(command=lambda: Load_Page(EmpPg_window, "employee"))
    EmpPg_refresh_button.place(x=5, y=5)
    
    EmpPg_return_button = ctk.CTkButton(master=EmpPg_frame, width=100, corner_radius=20, text="Return", font=('Roboto', 15))
    EmpPg_return_button.configure(command=lambda: Load_Page(EmpPg_window, "login"))
    EmpPg_return_button.place(x=645, y=5)
    
    EmpPg_window.mainloop()

def Settings_Page():
    SetPg_window, SetPg_frame = Create_Window("Settings")

    SetPg_txt = ctk.CTkLabel(master=SetPg_frame, text="Change colour scheme:", font=('Roboto', 30))
    SetPg_txt.place(x=220, y=75)

    SetPg_underline = ctk.CTkButton(master=SetPg_frame, width=330, height=3, corner_radius=0, text="")
    SetPg_underline.place(x=213, y=110)

    SetPg_theme_dropdownmenu = ctk.CTkComboBox(master=SetPg_frame,justify="center", values=["green", "dark-blue", "blue"], width=250, font=('Roboto', 20))
    SetPg_theme_dropdownmenu.set("Set Theme...")
    SetPg_theme_dropdownmenu.place(x=75, y=250)

    SetPg_appearance_dropdownmenu = ctk.CTkComboBox(master=SetPg_frame,justify="center", values=["light", "dark", "system"], width=250, font=('Roboto', 20))
    SetPg_appearance_dropdownmenu.set("Set Appearance Mode...")
    SetPg_appearance_dropdownmenu.place(x=425, y=250)

    SetPg_confirm_button = ctk.CTkButton(master=SetPg_frame, width=250, corner_radius=20, text="Confirm changes", font=('Roboto', 20))
    SetPg_confirm_button.configure(command=lambda: Confirm_Colour(SetPg_theme_dropdownmenu, SetPg_appearance_dropdownmenu,SetPg_window))
    SetPg_confirm_button.place(x=260, y=390)

    SetPg_return_button = ctk.CTkButton(master=SetPg_frame, width=100, corner_radius=20, text="Return", font=('Roboto', 15))
    SetPg_return_button.configure(command=lambda: Load_Page(SetPg_window, "login"))
    SetPg_return_button.place(x=645, y=5)

    SetPg_exit_button = ctk.CTkButton(master=SetPg_frame, width=250, corner_radius=20, text="Exit System", font=('Roboto', 20))
    SetPg_exit_button.configure(command=lambda: SetPg_window.destroy())
    SetPg_exit_button.place(x=260, y=505)

    SetPg_window.mainloop()

def Confirm_Colour(SetPg_theme_dropdownmenu, SetPg_appearance_dropdownmenu, SetPg_window):
    selected_theme = SetPg_theme_dropdownmenu.get()
    selected_appearance = SetPg_appearance_dropdownmenu.get()

    if selected_theme != "Set Theme..." and selected_appearance != "Set Appearance Mode...":
        ctk.set_default_color_theme(selected_theme)
        ctk.set_appearance_mode(selected_appearance)
    else:
        ctk.set_default_color_theme(default_theme)
        ctk.set_appearance_mode(default_appearance)

    Load_Page(SetPg_window, "settings")

def Admin_Main_Page():
    AdMainPg_window, AdMainPg_frame = Create_Window("Admin Main Page")

    AdMainPg_tabview = ctk.CTkTabview(AdMainPg_frame, width=850, height=615, corner_radius=15)
    AdMainPg_tabview.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    AdMainPg_tab_names = ["Overview", "View Employee", "Settings", "Exit"]
    for tab_name in AdMainPg_tab_names:
        AdMainPg_tabview.add(tab_name)
        
    AdMainPg_tabview._segmented_button.configure(font=custom_font,height=40)

    AdMainPg_return_button = ctk.CTkButton(AdMainPg_tabview.tab("Exit"), width=250, corner_radius=20, text="Return To Login Page", font=('Roboto', 22))
    AdMainPg_return_button.configure(command=lambda: Load_Page(AdMainPg_window, "login"))
    AdMainPg_return_button.place(x=100, y=225)

    AdMainPg_exit_button = ctk.CTkButton(AdMainPg_tabview.tab("Exit"), width=250, corner_radius=20, text="Exit System", font=('Roboto', 22))
    AdMainPg_exit_button.configure(command=lambda: AdMainPg_window.destroy())
    AdMainPg_exit_button.place(x=475, y=225)

    AdMainPg_window.mainloop()

def Employee_Main_Page():
    EmpMainPg_window, EmpMainPg_frame = Create_Window("Employee Main Page")

    EmpMainPg_tabview = ctk.CTkTabview(EmpMainPg_frame, width=850, height=615, corner_radius=15)
    EmpMainPg_tabview.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    EmpMainPg_tab_names = ["Overview", "Live Feed", "Settings", "Exit"]
    for tab_name in EmpMainPg_tab_names:
        EmpMainPg_tabview.add(tab_name)

    EmpMainPg_tabview._segmented_button.configure(font=custom_font, height=40)

    EmpMainPg_return_button = ctk.CTkButton(EmpMainPg_tabview.tab("Exit"), width=250, corner_radius=20, text="Return To Login Page", font=('Roboto', 22))
    EmpMainPg_return_button.configure(command=lambda: Load_Page(EmpMainPg_window, "login"))
    EmpMainPg_return_button.place(x=100, y=225)

    EmpMainPg_exit_button = ctk.CTkButton(EmpMainPg_tabview.tab("Exit"), width=250, corner_radius=20, text="Exit System", font=('Roboto', 22))
    EmpMainPg_exit_button.configure(command=lambda: EmpMainPg_window.destroy())
    EmpMainPg_exit_button.place(x=475, y=225)

    EmpMainPg_window.mainloop()

def Invalid_Details_Page():
    InvDePg_window, InvDePg_frame = Create_Window("Invalid Details")

    InvDePg_txt1 = ctk.CTkLabel(master=InvDePg_frame, text="Errenous Detials:", font=('Roboto', 30))
    InvDePg_txt1.place(x=250, y=75)

    InvDePg_underline = ctk.CTkButton(master=InvDePg_frame, width=225, height=3, corner_radius=0, text="")
    InvDePg_underline.place(x=250, y=110)

    InvDePg_txt2 = ctk.CTkLabel(master=InvDePg_frame, text="The details entered were invalid, please try again!", font=('Roboto', 20))
    InvDePg_txt2.place(x=150, y=250)

    InvDePg_return_button = ctk.CTkButton(master=InvDePg_frame, width=100, corner_radius=20, text="Return", font=('Roboto', 30))
    InvDePg_return_button.configure(command=lambda: InvDePg_window.destroy())
    InvDePg_return_button.place(x=300, y=400)

    InvDePg_window.mainloop()

def Get_Admin_Details(AdPg_firstname_entry, AdPg_lastname_entry, AdPg_password_entry, AdPg_confirmpassword_entry, AdPg_companyname_entry):
    GetAd_firstname = AdPg_firstname_entry.get()
    GetAd_lastname = AdPg_lastname_entry.get()
    GetAd_password = AdPg_password_entry.get()
    GetAd_confirmpassword = AdPg_confirmpassword_entry.get()
    GetAd_companyname = AdPg_companyname_entry.get()

    if Verify_Admin_Details(GetAd_firstname, GetAd_lastname, GetAd_password, GetAd_confirmpassword, GetAd_companyname):
        Write_Admin_Details_To_File(GetAd_firstname, GetAd_lastname, GetAd_password, GetAd_confirmpassword, GetAd_companyname)
    else:
        Invalid_Details_Page()

def Verify_Admin_Details(GetAd_firstname, GetAd_lastname, GetAd_password, GetAd_confirmpassword, GetAd_companyname):
    if len(GetAd_firstname) < 1:
        return False
    if len(GetAd_lastname) < 1:
        return False
    if len(GetAd_password) < 1:
        return False
    if len(GetAd_confirmpassword) < 1:
        return False
    if len(GetAd_companyname) < 1:
        return False

    for entry in [GetAd_firstname, GetAd_lastname, GetAd_password, GetAd_confirmpassword, GetAd_companyname]:
        if not entry.isalnum():
            return False 

    return True

def Write_Admin_Details_To_File(GetAd_firstname, GetAd_lastname, GetAd_password, GetAd_confirmpassword, GetAd_companyname):
    with open('user_details.py', 'w') as file:
        file.write(f"Admin_First_Name = '{GetAd_firstname}'\n")
        file.write(f"Admin_Last_Name = '{GetAd_lastname}'\n")
        file.write(f"Admin_Password = '{GetAd_password}'\n")
        file.write(f"Admin_Confirm_Password = '{GetAd_confirmpassword}'\n")
        file.write(f"Admin_Company_Name = '{GetAd_companyname}'\n")

def Get_Employee_Details(EmpPg_firstname_entry, EmpPg_lastname_entry, EmpPg_password_entry, EmpPg_confirmpassword_entry, EmpPg_companyname_entry):
    GetEmp_firstname = EmpPg_firstname_entry.get()
    GetEmp_lastname = EmpPg_lastname_entry.get()
    GetEmp_password = EmpPg_password_entry.get()
    GetEmp_confirmpassword = EmpPg_confirmpassword_entry.get()
    GetEmp_companyname = EmpPg_companyname_entry.get()

    if Verify_Employee_Details(GetEmp_firstname, GetEmp_lastname, GetEmp_password, GetEmp_confirmpassword, GetEmp_companyname):
        Write_Employee_Details_To_File(GetEmp_firstname, GetEmp_lastname, GetEmp_password, GetEmp_confirmpassword, GetEmp_companyname)
    else:
        Invalid_Details_Page()

def Verify_Employee_Details(GetEmp_firstname, GetEmp_lastname, GetEmp_password, GetEmp_confirmpassword, GetEmp_companyname):
    if len(GetEmp_firstname) < 1:
        return False
    if len(GetEmp_lastname) < 1:
        return False
    if len(GetEmp_password) < 1:
        return False
    if len(GetEmp_confirmpassword) < 1:
        return False
    if len(GetEmp_companyname) < 1:
        return False

    for entry in [GetEmp_firstname, GetEmp_lastname, GetEmp_password, GetEmp_confirmpassword, GetEmp_companyname]:
        if not entry.isalnum():
            return False 

    return True

def Write_Employee_Details_To_File(GetEmp_firstname, GetEmp_lastname, GetEmp_password, GetEmp_confirmpassword, GetEmp_companyname):
    with open('user_details.py', 'w') as file:
        file.write(f"Employee_First_Name = '{GetEmp_firstname}'\n")
        file.write(f"Employee_Last_Name = '{GetEmp_lastname}'\n")
        file.write(f"Employee_Password = '{GetEmp_password}'\n")
        file.write(f"Employee_Confirm_Password = '{GetEmp_confirmpassword}'\n")
        file.write(f"Employee_Company_Name = '{GetEmp_companyname}'\n")

if __name__ == "__main__":
    Login_Page()
