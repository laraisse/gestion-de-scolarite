from PIL import Image, ImageTk
from reportlab.pdfgen import canvas
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from reportlab.lib.utils import ImageReader
import tkinter as tk
from tkinter import messagebox, filedialog
import shutil
import os
import sqlite3
from tkcalendar import DateEntry

root = tk.Tk()
root.geometry('600x700')
root.title('ECC : gestion de scolarité')

bg_image = Image.open(r"C:\Users\pc\PycharmProjects\exam poo\image\eccim1.jpg")
bg_photo = ImageTk.PhotoImage(bg_image)

# Create a label to display the background image
bg_label = tk.Label(root, image=bg_photo)
bg_label.place(relwidth=1, relheight=1)

bg_color = 'green'

#image

school_icon = tk.PhotoImage(file='image/logo-ecc.png')
login_student_icon = tk.PhotoImage(file='image/student icon.png')
login_admin_icon = tk.PhotoImage(file='image/admin icon.png')
login_teacher_icon = tk.PhotoImage(file='image/prof icon.png')
add_student_icon = tk.PhotoImage(file='image/student icon.png')
hidden_mdp_icon = tk.PhotoImage(file='image/hiddenmdp.png')
open_mdp_icon = tk.PhotoImage(file='image/openmdp.png')
left_arow = tk.PhotoImage(file='image/left arow.png')
human = tk.PhotoImage(file='image/human.png')
ajouter = tk.PhotoImage(file='image/ajouter.png')
search = tk.PhotoImage(file='image/search.png')
sup = tk.PhotoImage(file='image/trash.png')
modif = tk.PhotoImage(file='image/modify.png')


# noinspection PyTypeChecker
class WelcomWindow():
    def welcom_page(self):
        def student_login_direction():
            Welcom_page.destroy()
            self.student_login_page()

        def admin_login_direction():
            Welcom_page.destroy()
            self.fadmin_login_page()

        def prof_login_direction():
            Welcom_page.destroy()
            self.prof_login_page()

        #premiere page

        Welcom_page = tk.Frame(root, highlightbackground=bg_color, highlightthickness=3)

        heading_lb = tk.Label(Welcom_page, text="Bienvenue  ", bg=bg_color, fg='white', font=('Bold', 19))
        heading_lb.place(x=50, y=0, width=400)

        school_icon_btn = tk.Button(Welcom_page, image=school_icon, bd=0)
        school_icon_btn.place(x=0, y=0)

        student_login_btn = tk.Button(Welcom_page, text='étudiant login', bg=bg_color, fg='white', font=('Bold', 15),
                                      command=student_login_direction)
        student_login_btn.place(x=120, y=125, width=200)

        student_login_img = tk.Button(Welcom_page, image=login_student_icon, bd=0)
        student_login_img.place(x=60, y=115)

        admin_login_btn = tk.Button(Welcom_page, text='Admin login', bg=bg_color, fg='white', font=('Bold', 15),
                                    command=admin_login_direction)
        admin_login_btn.place(x=120, y=225, width=200)

        admin_login_img = tk.Button(Welcom_page, image=login_admin_icon, bd=0)
        admin_login_img.place(x=60, y=215)

        prof_login_btn = tk.Button(Welcom_page, text='Enseignant login', bg=bg_color, fg='white', font=('Bold', 15),
                                   command=prof_login_direction)
        prof_login_btn.place(x=120, y=325, width=200)

        prof_login_img = tk.Button(Welcom_page, image=login_teacher_icon, bd=0)
        prof_login_img.place(x=60, y=315)

        Welcom_page.pack(pady=30)
        Welcom_page.pack_propagate(False)
        Welcom_page.configure(width=400, height=420)

    def student_login_page(self): #page d'authentification de l'eleve
        def show_hide_button():
            if mdp_entry['show'] == '*':
                mdp_entry.configure(show='')
                lock_img.configure(image=open_mdp_icon)
            else:
                mdp_entry.configure(show='*')
                lock_img.configure(image=hidden_mdp_icon)

        def go_back():
            student_login_page.destroy()
            self.welcom_page()

        def eleveExiste(): #check l'existance lors de l'authentification
            with open("etudiant.txt", "r") as f:
                for ligne in f:
                    txt = ligne.split('\t')
                    if txt[1] == email_entry.get() and txt[2] == mdp_entry.get():
                        f.close()
                        student_login_page.destroy()
                        student_afterlogin(txt[0])
                        return True
            f.close()
            messagebox.showerror('Erreur', "il y'a une erreur dans le mot de passe ou votre email")

        student_login_page = tk.Frame(root, highlightbackground=bg_color, highlightthickness=3)

        heading_lb = tk.Label(student_login_page, text="Bienvenue", bg=bg_color, fg='white', font=('Bold', 19))
        heading_lb.place(x=50, y=0, width=400)

        larow_img = tk.Button(student_login_page, image=left_arow, bd=0, command=go_back)
        larow_img.place(x=30, y=80)

        lock_img = tk.Button(student_login_page, image=hidden_mdp_icon, bd=0, command=show_hide_button)
        lock_img.place(x=355, y=270)

        school_icon_btn = tk.Button(student_login_page, image=school_icon, bd=0)
        school_icon_btn.place(x=0, y=0)

        student_login_img = tk.Button(student_login_page, image=login_student_icon, bd=0)
        student_login_img.place(x=200, y=70)

        login_btn = tk.Button(student_login_page, text='Login', bg=bg_color, fg='white', font=('Bold', 15),
                              command=eleveExiste)
        login_btn.place(x=100, y=350, width=200)

        email = tk.Label(student_login_page, text='Email', fg='green', font=('Bold', 15))
        email.place(x=20, y=125, width=200)

        email_entry = tk.Entry(student_login_page, font=('Bold', 10), justify=tk.CENTER)
        email_entry.place(x=100, y=175, width=250)

        mdp = tk.Label(student_login_page, text='Mot de passe', fg='green', font=('Bold', 15))
        mdp.place(x=60, y=225, width=200)

        mdp_entry = tk.Entry(student_login_page, font=('Bold', 10), justify=tk.CENTER, show='*')
        mdp_entry.place(x=100, y=275, width=250)

        student_login_page.pack(pady=30)
        student_login_page.pack_propagate(False)
        student_login_page.configure(width=400, height=420)

    def fadmin_login_page(self): #page de conection de l'admin
        def show_hide_button():
            if mdp_entry['show'] == '*':
                mdp_entry.configure(show='')
                lock_img.configure(image=open_mdp_icon)
            else:
                mdp_entry.configure(show='*')
                lock_img.configure(image=hidden_mdp_icon)

        def go_back():
            admin_login_page.destroy()
            self.welcom_page()

        def adminExiste():
            with open("admin.txt", "r") as f:
                for ligne in f:
                    txt = ligne.split()
                    if txt[0] == email_entry.get() and txt[1] == mdp_entry.get():
                        f.close()
                        admin_login_page.destroy()
                        admin.after_admin_stu(self, txt[2])
                        return True
            f.close()
            messagebox.showerror('Erreur', "il y'a une erreur dans le mot de passe ou votre email")

        admin_login_page = tk.Frame(root, highlightbackground=bg_color, highlightthickness=3)

        heading_lb = tk.Label(admin_login_page, text="Bienvenue", bg=bg_color, fg='white', font=('Bold', 19))
        heading_lb.place(x=50, y=0, width=400)

        larow_img = tk.Button(admin_login_page, image=left_arow, bd=0, command=go_back)
        larow_img.place(x=30, y=80)

        lock_img = tk.Button(admin_login_page, image=hidden_mdp_icon, bd=0, command=show_hide_button)
        lock_img.place(x=355, y=270)

        school_icon_btn = tk.Button(admin_login_page, image=school_icon, bd=0)
        school_icon_btn.place(x=0, y=0)

        admin_login_img = tk.Button(admin_login_page, image=login_admin_icon, bd=0)
        admin_login_img.place(x=200, y=70)

        email = tk.Label(admin_login_page, text='Email', fg='green', font=('Bold', 15))
        email.place(x=20, y=125, width=200)

        email_entry = tk.Entry(admin_login_page, font=('Bold', 10), justify=tk.CENTER)
        email_entry.place(x=100, y=175, width=250)

        mdp = tk.Label(admin_login_page, text='Mot de passe', fg='green', font=('Bold', 15))
        mdp.place(x=60, y=225, width=200)

        mdp_entry = tk.Entry(admin_login_page, font=('Bold', 10), justify=tk.CENTER, show='*')
        mdp_entry.place(x=100, y=275, width=250)

        login_btn = tk.Button(admin_login_page, text='Login', bg=bg_color, fg='white', font=('Bold', 15),
                              command=adminExiste)
        login_btn.place(x=100, y=350, width=200)

        admin_login_page.pack(pady=30)
        admin_login_page.pack_propagate(False)
        admin_login_page.configure(width=400, height=420)

    def prof_login_page(self):
        def show_hide_button():
            if mdp_entry['show'] == '*':
                mdp_entry.configure(show='')
                lock_img.configure(image=open_mdp_icon)
            else:
                mdp_entry.configure(show='*')
                lock_img.configure(image=hidden_mdp_icon)

        def go_back():
            prof_login_page.destroy()
            self.welcom_page()

        def profExiste():
            with open("prof.txt", "r") as f:
                for ligne in f:
                    txt = ligne.split()
                    if txt[1] == email_entry.get() and txt[2] == mdp_entry.get():
                        f.close()
                        prof_login_page.destroy()
                        prof_afterlogin(txt[4])
                        return True
            f.close()
            messagebox.showerror('Erreur', "il y'a une erreur dans le mot de passe ou votre email")

        prof_login_page = tk.Frame(root, highlightbackground=bg_color, highlightthickness=3)

        heading_lb = tk.Label(prof_login_page, text="Bienvenue", bg=bg_color, fg='white', font=('Bold', 19))
        heading_lb.place(x=50, y=0, width=400)

        school_icon_btn = tk.Button(prof_login_page, image=school_icon, bd=0)
        school_icon_btn.place(x=0, y=0)

        lock_img = tk.Button(prof_login_page, image=hidden_mdp_icon, bd=0, command=show_hide_button)
        lock_img.place(x=355, y=270)

        larow_img = tk.Button(prof_login_page, image=left_arow, bd=0, command=go_back)
        larow_img.place(x=30, y=80)

        prof_login_img = tk.Button(prof_login_page, image=login_teacher_icon, bd=0)
        prof_login_img.place(x=200, y=70)

        login_btn = tk.Button(prof_login_page, text='Login', bg=bg_color, fg='white', font=('Bold', 15),
                              command=profExiste)
        login_btn.place(x=100, y=350, width=200)

        email = tk.Label(prof_login_page, text='Email', fg='green', font=('Bold', 15))
        email.place(x=20, y=125, width=200)

        email_entry = tk.Entry(prof_login_page, font=('Bold', 10), justify=tk.CENTER)
        email_entry.place(x=100, y=175, width=250)

        mdp = tk.Label(prof_login_page, text='Mot de passe', fg='green', font=('Bold', 15))
        mdp.place(x=60, y=225, width=200)

        mdp_entry = tk.Entry(prof_login_page, font=('Bold', 10), justify=tk.CENTER, show='*')
        mdp_entry.place(x=100, y=275, width=250)

        prof_login_page.pack(pady=30)
        prof_login_page.pack_propagate(False)
        prof_login_page.configure(width=400, height=420)


class CoursPages(tk.Frame): #page de la lecture des cours pour les eleve
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, bg='#F8F9FA')
        self.parent = parent

        label = tk.Label(self, text="Page des cours", font=('Arial', 16, 'bold'), fg='#2E3B4E',bg='#F8F9FA')
        label.pack(pady=10)

        self.open_button = tk.Button(self, text="Ouvrir un PDF", command=self.show_pdf_list, font=('Arial', 12),
                                     bg='#3498db', fg='#ffffff')
        self.open_button.pack(pady=10)

    def show_pdf_list(self):
        pdf_directory = r'C:\Users\pc\PycharmProjects\exam poo\pdf'
        pdf_files = [f for f in os.listdir(pdf_directory) if f.endswith('.pdf')]

        # Créer une nouvelle fenêtre pour afficher la liste des fichiers PDF
        pdf_list_window = tk.Toplevel(self)
        pdf_list_window.title("Liste des PDF")

        # Créer une boîte de liste pour afficher les noms des fichiers PDF
        listbox = tk.Listbox(pdf_list_window, selectmode=tk.SINGLE, font=('Arial', 12), bg='#ffffff', fg='#000000',
                             height=5)
        listbox.pack(pady=10)

        # Remplir la boîte de liste avec les noms des fichiers PDF
        for pdf_file in pdf_files:
            listbox.insert(tk.END, pdf_file)

        # Ajouter un bouton pour ouvrir le fichier PDF sélectionné
        open_selected_button = tk.Button(pdf_list_window, text="Ouvrir",
                                         command=lambda: self.open_selected_pdf(pdf_directory, listbox.get(tk.ACTIVE)),
                                         font=('Arial', 12), bg='#3498db', fg='#ffffff')
        open_selected_button.pack(pady=10)

    def open_selected_pdf(self, pdf_directory, pdf_name):
        try:
            pdf_path = os.path.join(pdf_directory, pdf_name)
            os.startfile(pdf_path)  # Ouverture du fichier PDF
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur lors de l'ouverture du fichier : {e}")


class Notes(tk.Frame):#affichage des note pour les eleve
    def __init__(self, parent, Nom):
        tk.Frame.__init__(self, parent, bg='#F8F9FA')
        self.parent = parent

        self.Nom = Nom

        label = tk.Label(self, text="Page des notes", font=('Arial', 16, 'bold'), fg='#2E3B4E',bg='#F8F9FA')
        label.pack(pady=10)

        self.show_grades_button = tk.Button(self, text="Voir mes notes", command=self.show_grades, font=('Arial', 12),
                                            bg='#3498db', fg='#ffffff')
        self.show_grades_button.pack(pady=10)

    def fetch_student_grades(self):#chercher les note dans la base de donne sql
        try:
            conn = database()
            cursor = conn.cursor()
            cursor.execute("SELECT cours_id, Note FROM note WHERE Nom= ?", (self.Nom,))
            grades = cursor.fetchall()
            conn.close()
            return grades
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur lors de la récupération des notes : {e}")

    def show_grades(self):
        student_grades = self.fetch_student_grades()

        # Clear any previous content except for the label widget
        for widget in self.winfo_children():
            if widget.winfo_class() != 'Label':
                widget.destroy()

        label = tk.Label(self, text="Vos notes :", font=('Arial', 14, 'bold'), bg='#F8F9FA')
        label.pack(pady=10)

        if student_grades:
            for course_id, grade in student_grades:
                grade_label = tk.Label(self, text=f"Cours {course_id}: {grade}", font=('Arial', 12), bg='#F8F9FA')
                grade_label.pack(pady=5)
        else:
            no_grades_label = tk.Label(self, text="Aucune note disponible.", font=('Arial', 12), bg='#F8F9FA')
            no_grades_label.pack(pady=10)


class Absences(tk.Frame):#l'afichage des absence pour les eleve
    def __init__(self, parent, Nom):
        tk.Frame.__init__(self, parent, bg='#F8F9FA')
        self.parent = parent
        self.Nom = Nom  # Assuming Nom is the student's name

        label = tk.Label(self, text="Page des absences", font=('Arial', 16, 'bold'), fg='#2E3B4E',bg='#F8F9FA')
        label.pack(pady=10)

        self.show_absences_button = tk.Button(self, text="Voir mes absences", command=self.show_absences,
                                              font=('Arial', 12),
                                              bg='#3498db', fg='#ffffff')
        self.show_absences_button.pack(pady=10)

    def fetch_student_absences(self):
        try:
            conn = database()
            cursor = conn.cursor()
            cursor.execute("SELECT cours_id, date FROM abscences WHERE Nom= ?", (self.Nom,))
            absences = cursor.fetchall()
            conn.close()
            return absences
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur lors de la récupération des absences : {e}")

    def show_absences(self):
        student_absences = self.fetch_student_absences()

        # Clear any previous content except for the label widget
        for widget in self.winfo_children():
            if widget.winfo_class() != 'Label':
                widget.destroy()

        label = tk.Label(self, text="Vos absences :", font=('Arial', 14, 'bold'), bg='#F8F9FA')
        label.pack(pady=10)

        if student_absences:
            for date, motif in student_absences:
                absence_label = tk.Label(self, text=f"Date {date}: {motif}", font=('Arial', 12), bg='#F8F9FA')
                absence_label.pack(pady=5)
        else:
            no_absences_label = tk.Label(self, text="Aucune absence enregistrée.", font=('Arial', 12), bg='#F8F9FA')
            no_absences_label.pack(pady=10)


def student_afterlogin(id): #page d'acceuil de l'eleve
    def deconnct():
        confirm = messagebox.askquestion(message="Voulez-vous vous déconnecter\n de votre compte ?")
        if confirm=='yes':
            dashboard_fm.destroy()
            b.welcom_page()
            root.update()

    def switch(indicator, page):
        first_btn_indice.config(bg='grey')
        seconde_btn_indice.config(bg='grey')
        third_btn_indice.config(bg='grey')
        fourth_btn_indice.config(bg='grey')

        indicator.config(bg='green')
        for i in pages_fm.winfo_children():
            i.destroy()
            root.update()
        page()

    dashboard_fm = tk.Frame(root, highlightbackground='green', highlightthickness=3)
    options_fm = tk.Frame(dashboard_fm, highlightbackground='green', highlightthickness=2)

    first_btn = tk.Button(options_fm, text="Page\nd'acceuil", font=('Bold', 15), fg='black', bd=0,
                          command=lambda: switch(indicator=first_btn_indice, page=acceuil_page))
    first_btn.place(x=10, y=20)
    first_btn_indice = tk.Label(options_fm, bg='green')
    first_btn_indice.place(x=5, y=28, width=3, height=40)

    seconde_btn = tk.Button(options_fm, text="Relevé\nde note", font=('Bold', 15), fg='black', bd=0, justify=tk.LEFT,
                            command=lambda: switch(indicator=seconde_btn_indice, page=seconde_page))
    seconde_btn.place(x=10, y=85)
    seconde_btn_indice = tk.Label(options_fm, bg='grey')
    seconde_btn_indice.place(x=5, y=93, width=3, height=40)

    third_btn = tk.Button(options_fm, text="Cours", font=('Bold', 15), fg='black', bd=0,
                          command=lambda: switch(indicator=third_btn_indice, page=third_page))
    third_btn.place(x=10, y=155)
    third_btn_indice = tk.Label(options_fm, bg='grey')
    third_btn_indice.place(x=5, y=155, width=3, height=40)

    fourth_btn = tk.Button(options_fm, text="Absence", font=('Bold', 15), fg='black', bd=0,
                           command=lambda: switch(indicator=fourth_btn_indice, page=fourth_page))
    fourth_btn.place(x=10, y=220)
    fourth_btn_indice = tk.Label(options_fm, bg='grey')
    fourth_btn_indice.place(x=5, y=220, width=3, height=40)

    fifth_btn = tk.Button(options_fm, text="Logout", font=('Bold', 15), fg='black', bd=0, bg='red', command=deconnct)
    fifth_btn.place(x=5, y=500)

    options_fm.place(x=0, y=0, width=120, height=575)

    def acceuil_page():

        acceuil_page_fm = tk.Frame(pages_fm)
        acceuil_page_lb = tk.Label(acceuil_page_fm, text="Espace étudiant", font=('bold', 15))
        acceuil_page_lb.place(x=100, y=200)
        acceuil_page_lb2 = tk.Label(acceuil_page_fm, text="Ecole centrale casablanca", font=('bold', 12))
        acceuil_page_lb2.place(x=80, y=530)
        acceuil_page_fm.pack(fill=tk.BOTH, expand=True)

    def seconde_page():
        student_name = id
        note = Notes(pages_fm, student_name)
        note.pack(fill=tk.BOTH, expand=True)

    def third_page():
        cours_page = CoursPages(pages_fm)
        cours_page.pack(fill=tk.BOTH, expand=True)

    def fourth_page():
        student_name = id  # Replace with actual student's name
        absence = Absences(pages_fm, Nom=student_name)
        absence.pack(fill=tk.BOTH, expand=True)

    pages_fm = tk.Frame(dashboard_fm)
    pages_fm.place(x=122, y=5, width=350, height=550)
    acceuil_page()
    dashboard_fm.pack(pady=5)
    dashboard_fm.pack_propagate(False)
    dashboard_fm.configure(width=480, height=580)


def database():#conection à la base de donne sql
    return sqlite3.connect(r'C:\Users\pc\PycharmProjects\exam poo\professeur.db')


class Absence(tk.Frame):
    def __init__(self, parent,matier):
        tk.Frame.__init__(self, parent, bg='#F8F9FA')
        self.parent = parent
        self.matier=matier

        label = tk.Label(self, text="Page des absences", font=('Arial', 16, 'bold'), fg='#2E3B4E', bg='#F8F9FA')
        label.pack(pady=10)

        ajout_modif_button = tk.Button(self, text="Ajouter une absence", command=self.ajouter_abs, font=('Arial', 12), bg='#4CAF50', fg='#ffffff')
        ajout_modif_button.pack(pady=10)
        ajout_modif_button.place(x=100,y=110,width=200,height=40)

        im=tk.Button(self,image=ajouter,bg='#F8F9FA',bd=0)
        im.place(x=20,y=100)

        delete_button = tk.Button(self, text="Supprimer une absence", command=self.supprimer_abs,font=('Arial', 12), bg='#4CAF50', fg='#ffffff')
        delete_button.pack(pady=10)
        delete_button.place(x=100, y=210, width=200, height=40)

        im3 = tk.Button(self, image=sup, bg='#F8F9FA', bd=0)
        im3.place(x=20, y=200)
    def ajouter_abs(self):#ajouter les absence
        el = []
        with open("etudiant.txt", "r") as f:
            for ligne in f:
                txt = ligne.split('\t')
                el.append(txt[0])
            f.close()

        absence_window = tk.Toplevel(self)
        absence_window.title("Ajouter une absence")

        tk.Label(absence_window, text="Nom de l'étudiant:").pack()
        student_id_entry = ttk.Combobox(absence_window, values=el)
        student_id_entry.pack()

        tk.Label(absence_window, text='Date d\'absence:').pack()
        date_entry = DateEntry(absence_window, selectmode='day', date_pattern='dd/MM/yyyy')
        date_entry.pack()

        def enregistrer_abs():
            Nom = student_id_entry.get()
            cours_id = self.matier
            absence_date = date_entry.get_date()

            conn = database()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO abscences (Nom, cours_id, date) VALUES (?, ?, ?)",
                           (Nom, cours_id, absence_date))
            conn.commit()
            conn.close()
            messagebox.showinfo("Succès", "Absence ajoutée avec succès.")
            absence_window.destroy()

        tk.Button(absence_window, text="Enregistrer l'absence", command=enregistrer_abs).pack()

    def supprimer_abs(self):#suprimer les absence

        def delete_abs(Nom, cours_id, absence_id):
            try:
                conn = database()
                cursor = conn.cursor()
                cursor.execute("DELETE FROM abscences WHERE id = ?", (absence_id,))
                conn.commit()
                conn.close()

                messagebox.showinfo("Succès", "Abscence supprimée avec succès.")
                absences_frame.destroy()
                edit_absence_window.destroy()
                self.supprimer_abs()
            except Exception as e:
                messagebox.showerror("Erreur", f"Une erreur s'est produite lors de la suppression de l'abscence: {e}")

        edit_absence_window = tk.Toplevel(self)
        edit_absence_window.title("Supprimer une abscence")

        tk.Label(edit_absence_window, text="Sélectionner un étudiant:").pack()
        listbox_students = tk.Listbox(edit_absence_window)
        listbox_students.pack()

        conn = database()
        cursor = conn.cursor()
        cursor.execute("SELECT DISTINCT Nom FROM abscences")
        students = cursor.fetchall()

        for student in students:
            listbox_students.insert(tk.END, student[0])

        conn.close()

        def on_student_select(event):
            for widget in absences_frame.winfo_children():
                widget.destroy()

            selected_index = listbox_students.curselection()
            selected_student_id = listbox_students.get(selected_index)

            conn = database()
            cursor = conn.cursor()
            cursor.execute("SELECT id, cours_id, date FROM abscences WHERE Nom = ?", (selected_student_id,))
            absences = cursor.fetchall()

            for absence in absences:
                absence_id, cours_id, date = absence
                tk.Label(absences_frame, text=f"Cours : {cours_id}, Date: {date}").grid(row=absences.index(absence),
                                                                                        column=0)
                tk.Button(absences_frame, text="Supprimer",command=lambda a_id=absence_id: delete_abs(selected_student_id, cours_id, a_id,)).grid(row=absences.index(absence), column=2)
            conn.close()

        listbox_students.bind('<<ListboxSelect>>', on_student_select)

        absences_frame = tk.Frame(edit_absence_window)
        absences_frame.pack(fill='x')



class Note(tk.Frame):

    def __init__(self, parent,matier):
        tk.Frame.__init__(self, parent, bg='#F8F9FA')
        self.parent = parent
        self.matier=matier

        label = tk.Label(self, text="Page des notes", font=('Arial', 16, 'bold'), fg='#2E3B4E', bg='#F8F9FA')
        label.pack(pady=10)

        # Remove the button creation code from here
        ajout_modif_button = tk.Button(self, text="Ajouter une note", command=self.add_or_edit_grade,
                                            font=('Arial', 12),
                                            bg='#4CAF50', fg='#ffffff')
        ajout_modif_button.place(x=90,y=110,width=150)

        im = tk.Button(self, image=ajouter, bg='#F8F9FA', bd=0)
        im.place(x=20, y=100)

        delete_button = tk.Button(self, text="Supprimer une note", command=self.delete_grade, font=('Arial', 12),
                                       bg='#4CAF50', fg='#ffffff')
        delete_button.place(x=90,y=220)

        im2 = tk.Button(self, image=sup, bg='#F8F9FA', bd=0)
        im2.place(x=20, y=200)

    def add_or_edit_grade(self):#ajouter ou modifier note
        el = []
        with open("etudiant.txt", "r") as f:
            for ligne in f:
                txt = ligne.split('\t')
                el.append(txt[0])
            f.close()
        grade_window = tk.Toplevel(self)
        grade_window.title("Ajouter/Modifier une note")

        tk.Label(grade_window, text="Nom et prénom de l'étudiant:").pack()
        student_id_entry = ttk.Combobox(grade_window, values=el)
        student_id_entry.pack()

        tk.Label(grade_window, text="Note:").pack()
        grade_entry = tk.Entry(grade_window)
        grade_entry.pack()

        def save_grade():
            Nom = student_id_entry.get()
            cours_id = self.matier
            Note = grade_entry.get()

            conn = database()
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM note WHERE Nom = ? AND cours_id = ?", (Nom, cours_id))
            if cursor.fetchone():
                cursor.execute("UPDATE note SET note = ? WHERE Nom = ? AND cours_id = ?",
                               (Note, Nom, cours_id))
            else:
                cursor.execute("INSERT INTO note (Nom, cours_id, Note) VALUES (?, ?, ?)",
                               (Nom, cours_id, Note))

            conn.commit()
            conn.close()
            messagebox.showinfo("Succès", "Note enregistrée avec succès.")
            grade_window.destroy()

        tk.Button(grade_window, text="Enregistrer la note", command=save_grade).pack()

    def delete_grade(self):#suprimer note
        delete_grade_window = tk.Toplevel(self)
        delete_grade_window.title("Supprimer une note")
        el = []
        with open("etudiant.txt", "r") as f:
            for ligne in f:
                txt = ligne.split('\t')
                el.append(txt[0])
            f.close()

        tk.Label(delete_grade_window, text="Nom et prénom de l'étudiant:").pack()
        student_id_entry = ttk.Combobox(delete_grade_window, values=el)
        student_id_entry.pack()

        def save_delete():
            Nom = student_id_entry.get()
            cours_id = self.matier

            conn = database()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM note WHERE Nom = ? AND cours_id = ?", (Nom, cours_id))
            conn.commit()
            conn.close()

            messagebox.showinfo("Succès", "Note supprimée avec succès.")
            delete_grade_window.destroy()

        tk.Button(delete_grade_window, text="Supprimer la note", command=save_delete).pack()


class CoursPage(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, bg='#F8F9FA')
        self.parent = parent
        self.conn = sqlite3.connect(r'C:\Users\pc\PycharmProjects\exam poo\professeur.db')
        self.cursor = self.conn.cursor()

        label = tk.Label(self, text="Page des cours", font=(
            'Arial', 16, 'bold'), fg='#2E3B4E', bg='#F8F9FA')
        label.pack(pady=10)

        self.import_button = tk.Button(self, text="Importer un PDF", command=self.import_pdf, font=('Arial', 12),
                                       bg='#4CAF50', fg='#ffffff')
        self.import_button.pack(pady=20)

        self.delete_button = tk.Button(self, text="Supprimer un PDF", command=self.delete_pdf, font=('Arial', 12),
                                       bg='#FF5733', fg='#ffffff')
        self.delete_button.pack(pady=10)

        self.open_button = tk.Button(self, text="Ouvrir un PDF", command=self.show_pdf_list, font=('Arial', 12),
                                     bg='#3498db', fg='#ffffff')
        self.open_button.pack(pady=10)

    def import_pdf(self):#importer un cours
        file_path = filedialog.askopenfilename(
            initialdir='/', title="Sélectionner un fichier PDF", filetypes=[("Fichiers PDF", "*.pdf")])
        if file_path:
            # Chemin général pour les documents
            destination_path = r'C:\Users\pc\PycharmProjects\exam poo\pdf'
            file_name = os.path.basename(file_path)
            destination_file_path = os.path.join(destination_path, file_name)

            try:
                shutil.copyfile(file_path, destination_file_path)
                print(
                    f"Fichier copié avec succès vers : {destination_file_path}")

                # Enregistrement du chemin et du nom du cours dans la base de données
                # Nom du cours basé sur le nom du fichier
                cours_nom = file_name.split('.')[0]
                self.cursor.execute(
                    "INSERT INTO cours (cours_nom, pdf_path) VALUES (?, ?)", (cours_nom, destination_file_path))
                self.conn.commit()

            except Exception as e:
                messagebox.showerror(
                    "Erreur", f"Erreur lors de la copie du fichier : {e}")

    def delete_pdf(self):#suprimer un cours
        file_path = filedialog.askopenfilename(
            initialdir=r'C:\Users\pc\PycharmProjects\exam poo\pdf', title="Choisir un fichier PDF",
            filetypes=[("Fichiers PDF", "*.pdf")])
        if file_path:
            try:
                # Conversion du chemin de fichier pour assurer la cohérence
                file_path = file_path.replace("/", "\\")

                # Imprimez le chemin de fichier pour le débogage
                print("Chemin de fichier sélectionné :", file_path)

                # Vérifier si le fichier est dans la base de données
                self.cursor.execute(
                    "SELECT id FROM cours WHERE pdf_path=?", (file_path,))
                data = self.cursor.fetchone()

                if data:
                    # Suppression de l'enregistrement dans la base de données
                    self.cursor.execute(
                        "DELETE FROM cours WHERE pdf_path=?", (file_path,))
                    self.conn.commit()

                    # Suppression du fichier du système de fichiers
                    os.remove(file_path)
                    print(f"Fichier supprimé avec succès : {file_path}")
                    messagebox.showinfo(
                        "Succès", "Fichier supprimé avec succès de la base de données et du système de fichiers.")
                else:
                    messagebox.showinfo(
                        "Information", "Le fichier n'existe pas dans la base de données.")

            except Exception as e:
                messagebox.showerror(
                    "Erreur", f"Erreur lors de la suppression du fichier : {e}")

    def show_pdf_list(self):#afficher les cours
        pdf_directory = r'C:\Users\pc\PycharmProjects\exam poo\pdf'
        pdf_files = [f for f in os.listdir(
            pdf_directory) if f.endswith('.pdf')]

        # Créer une nouvelle fenêtre pour afficher la liste des fichiers PDF
        pdf_list_window = tk.Toplevel(self)
        pdf_list_window.title("Liste des PDF")

        # Créer une boîte de liste pour afficher les noms des fichiers PDF
        listbox = tk.Listbox(pdf_list_window, selectmode=tk.SINGLE, font=(
            'Arial', 12), bg='#ffffff', fg='#000000', height=5)
        listbox.pack(pady=10)

        # Remplir la boîte de liste avec les noms des fichiers PDF
        for pdf_file in pdf_files:
            listbox.insert(tk.END, pdf_file)

        # Ajouter un bouton pour ouvrir le fichier PDF sélectionné
        open_selected_button = tk.Button(pdf_list_window, text="Ouvrir",
                                         command=lambda: self.open_selected_pdf(pdf_directory, listbox.get(tk.ACTIVE)),
                                         font=('Arial', 12), bg='#3498db', fg='#ffffff')
        open_selected_button.pack(pady=10)

    def open_selected_pdf(self, pdf_directory, pdf_name):
        try:
            pdf_path = os.path.join(pdf_directory, pdf_name)
            os.startfile(pdf_path)  # Ouverture du fichier PDF
        except Exception as e:
            messagebox.showerror(
                "Erreur", f"Erreur lors de l'ouverture du fichier : {e}")


def prof_afterlogin(matiere):#page d'acceuil du prof
    def switch(indicator, page):
        first_btn_indice.config(bg='grey')
        seconde_btn_indice.config(bg='grey')
        third_btn_indice.config(bg='grey')
        fourth_btn_indice.config(bg='grey')

        indicator.config(bg='green')
        for i in pages_fm.winfo_children():
            i.destroy()
            root.update()
        page()

    def acceuil_page():
        acceuil_page_fm = tk.Frame(pages_fm)
        acceuil_page_lb = tk.Label(acceuil_page_fm, text="Espace enseignant", font=('bold', 15))
        acceuil_page_lb.place(x=100, y=200)
        acceuil_page_lb2 = tk.Label(acceuil_page_fm, text="Ecole centrale casablanca", font=('bold', 12))
        acceuil_page_lb2.place(x=80, y=530)
        acceuil_page_fm.pack(fill=tk.BOTH, expand=True)

    def seconde_page():
        seconde_page_fm = Note(pages_fm,matier=matiere)
        seconde_page_fm.pack(fill=tk.BOTH, expand=True)

    def third_page():
        cours_page = CoursPage(pages_fm)
        cours_page.pack(fill=tk.BOTH, expand=True)

    def fourth_page():
        fourth_page_fm = Absence(pages_fm, matier= matiere)
        fourth_page_fm.pack(fill=tk.BOTH, expand=True)

    def logout():
        confirm = messagebox.askquestion(message="Voulez-vous vous déconnecter\n de votre compte ?")
        print(confirm)
        if confirm == 'yes':
            dashboard_fm.destroy()
            b.welcom_page()
            root.update()

    dashboard_fm = tk.Frame(root, highlightbackground='green', highlightthickness=3)
    options_fm = tk.Frame(dashboard_fm, highlightbackground='green', highlightthickness=2)

    first_btn = tk.Button(options_fm, text="Page\nd'acceuil", font=('Bold', 15), fg='black', bd=0,
                          command=lambda: switch(indicator=first_btn_indice, page=acceuil_page))
    first_btn.place(x=10, y=20)
    first_btn_indice = tk.Label(options_fm, bg='green')
    first_btn_indice.place(x=5, y=28, width=3, height=40)

    seconde_btn = tk.Button(options_fm, text="Relevé\nde note", font=('Bold', 15), fg='black', bd=0, justify=tk.LEFT,
                            command=lambda: switch(indicator=seconde_btn_indice, page=seconde_page))
    seconde_btn.place(x=10, y=85)
    seconde_btn_indice = tk.Label(options_fm, bg='grey')
    seconde_btn_indice.place(x=5, y=93, width=3, height=40)

    third_btn = tk.Button(options_fm, text="Cours", font=('Bold', 15), fg='black', bd=0,
                          command=lambda: switch(indicator=third_btn_indice, page=third_page))
    third_btn.place(x=10, y=155)
    third_btn_indice = tk.Label(options_fm, bg='grey')
    third_btn_indice.place(x=5, y=160, width=3, height=40)  # Adjusted y coordinate

    fourth_btn = tk.Button(options_fm, text="Absence", font=('Bold', 15), fg='black', bd=0,
                           command=lambda: switch(indicator=fourth_btn_indice, page=fourth_page))
    fourth_btn.place(x=10, y=220)
    fourth_btn_indice = tk.Label(options_fm, bg='grey')
    fourth_btn_indice.place(x=5, y=220, width=3, height=40)

    fifth_btn = tk.Button(options_fm, text="Logout", font=('Bold', 15), fg='black', bd=0, bg='red', command=logout)
    fifth_btn.place(x=5, y=500)

    options_fm.place(x=0, y=0, width=120, height=575)

    pages_fm = tk.Frame(dashboard_fm, bg='grey')
    pages_fm.place(x=122, y=5, width=350, height=550)
    acceuil_page()
    dashboard_fm.pack(pady=5)
    dashboard_fm.pack_propagate(False)
    dashboard_fm.configure(width=480, height=580)

    root.mainloop()


class admin:
    def create_profile(self, nomaffi):#cree un profile
        pic_path = tk.StringVar()
        pic_path.set('')

        def go_back():
            create_profile_page.destroy()
            self.after_admin_stu(nomaffi)

        def new_image():
            path = askopenfilename()
            if path:
                img = ImageTk.PhotoImage(Image.open(path).resize((100, 100)))
                pic_path.set(path)
                profile_img.configure(image=img)
                profile_img.image = img

        def generate_pdf():#pour generer un pdf
            # Gather personal information from your Tkinter fields
            nometprenom = username_entry.get()
            mail = email_entry.get()
            motdepass = mdp_entry.get()
            datedenaiss = ddn_entry.get()
            classeleve = stu_class_entry.get()
            genre = gender_entry.get()
            num = phone_entry.get()
            nationalit = natio_entry.get()
            img = ImageReader('image/bigecc-logo.png')
            img2 = ImageReader(pic_path.get())

            with open("etudiant.txt", "a") as f:
                f.write(
                    nometprenom + "\t" + mail + "\t" + motdepass + "\t" + datedenaiss + "\t" + classeleve + "\t" + genre + "\t" + num + "\t" + nationalit + "\n")
            f.close()

            # Collect other information similarly

            # Create a PDF document
            pdf_filename = f"{nometprenom}.pdf"
            pdf = canvas.Canvas(pdf_filename)

            # Write the information onto the PDF
            pdf.drawBoundary(0, 50, 300, 500, 500)
            pdf.drawString(150, 700, f"Nom et prenom        : {nometprenom}")
            pdf.drawString(150, 650, f"Email                        : {mail}")
            pdf.drawString(150, 600, f"Mot de passe           : {motdepass}")
            pdf.drawString(150, 550, f"date de naissance    : {datedenaiss}")
            pdf.drawString(150, 500, f"classe de l'eleve       : {classeleve}")
            pdf.drawString(150, 450, f"sexe                          : {genre}")
            pdf.drawString(150, 400, f"numero de telephone: {num}")
            pdf.drawString(150, 350, f"nationalité                  : {nationalit}")
            pdf.drawImage(img, 100, 750, mask='auto', width=100, height=100)
            pdf.drawImage(img2, 449, 679, mask='auto', width=100, height=120)
            pdf.drawBoundary(0, 50, 90, 500, 200)
            pdf.drawString(100, 250, f"Pôle scolarité")
            pdf.drawString(100, 220, f"Fondation Ecole Centrale Casablanca")
            pdf.drawString(100, 190, f"Ville Verte Côté Latéral Est - Bouskoura – Maroc")
            pdf.drawString(100, 160, f"T +212 (0) 5 22 49 35 00 | F +212 (0) 5 22 49 35 20")
            pdf.save()
            create_profile_page.destroy()
            a.after_admin_stu(nomaffi)

        create_profile_page = tk.Frame(root, highlightbackground='green', highlightthickness=3)

        heading_lb = tk.Label(create_profile_page, text="crée un profile", bg='green', fg='white', font=('Bold', 19))
        heading_lb.place(x=100, y=0, width=400)

        username = tk.Label(create_profile_page, text='nom et prenom', fg='green', font=('Bold', 15))
        username.place(x=10, y=80)

        username_entry = tk.Entry(create_profile_page, font=('Bold', 10), justify=tk.CENTER)
        username_entry.place(x=10, y=130, width=250)

        email = tk.Label(create_profile_page, text='email', fg='green', font=('Bold', 15))
        email.place(x=10, y=180)

        email_entry = tk.Entry(create_profile_page, font=('Bold', 10), justify=tk.CENTER)
        email_entry.place(x=10, y=230, width=250)

        mdp = tk.Label(create_profile_page, text='Mot de passe', fg='green', font=('Bold', 15))
        mdp.place(x=10, y=280)

        mdp_entry = tk.Entry(create_profile_page, font=('Bold', 10), justify=tk.CENTER)
        mdp_entry.place(x=10, y=330, width=250)

        ddn = tk.Label(create_profile_page, text='Date de naissance', fg='green', font=('Bold', 15))
        ddn.place(x=10, y=380)

        ddn_entry = DateEntry(create_profile_page, selectmode='day', date_pattern='dd/MM/yyyy')
        ddn_entry.grid(row=1, column=1, padx=15)
        ddn_entry.place(x=10, y=430, width=250)

        valider_btn = tk.Button(create_profile_page, text='Valider', fg='white', bg='green', font=('Bold', 15),
                                command=generate_pdf)
        valider_btn.place(x=350, y=520)

        phone = tk.Label(create_profile_page, text='numero de telephone', fg='green', font=('Bold', 15))
        phone.place(x=300, y=380)

        phone_entry = tk.Entry(create_profile_page, font=('Bold', 10), justify=tk.CENTER)
        phone_entry.place(x=300, y=430, width=250)

        stu_class = tk.Label(create_profile_page, text="classe de l'éleve", fg='green', font=('Bold', 15))
        stu_class.place(x=300, y=180)

        AN = ['1A', '2A', '3A']
        stu_class_entry = ttk.Combobox(create_profile_page, values=AN)
        stu_class_entry.place(x=300, y=230, width=250)

        natio = tk.Label(create_profile_page, text="nationalité", fg='green', font=('Bold', 15))
        natio.place(x=10, y=470)

        ctr = ['Aruba', 'Afghanistan', 'Angola', 'Anguilla', 'Åland Islands', 'Albania', 'Andorra',
               'United Arab Emirates',
               'Argentina', 'Armenia', 'American Samoa', 'Antarctica', 'French Southern Territories',
               'Antigua and Barbuda',
               'Australia', 'Austria', 'Azerbaijan', 'Burundi', 'Belgium', 'Benin', 'Bonaire, Sint Eustatius and Saba',
               'Burkina Faso', 'Bangladesh', 'Bulgaria', 'Bahrain', 'Bahamas', 'Bosnia and Herzegovina',
               'Saint Barthélemy',
               'Belarus', 'Belize', 'Bermuda', 'Bolivia, Plurinational State of', 'Brazil', 'Barbados',
               'Brunei Darussalam',
               'Bhutan', 'Bouvet Island', 'Botswana', 'Central African Republic', 'Canada', 'Cocos (Keeling) Islands',
               'Switzerland', 'Chile', 'China', "Côte d'Ivoire", 'Cameroon', 'Congo, The Democratic Republic of the',
               'Congo', 'Cook Islands', 'Colombia', 'Comoros', 'Cabo Verde', 'Costa Rica', 'Cuba', 'Curaçao',
               'Christmas Island', 'Cayman Islands', 'Cyprus', 'Czechia', 'Germany', 'Djibouti', 'Dominica', 'Denmark',
               'Dominican Republic', 'Algeria', 'Ecuador', 'Egypt', 'Eritrea', 'Western Sahara', 'Spain', 'Estonia',
               'Ethiopia', 'Finland', 'Fiji', 'Falkland Islands (Malvinas)', 'France', 'Faroe Islands',
               'Micronesia, Federated States of', 'Gabon', 'United Kingdom', 'Georgia', 'Guernsey', 'Ghana',
               'Gibraltar',
               'Guinea', 'Guadeloupe', 'Gambia', 'Guinea-Bissau', 'Equatorial Guinea', 'Greece', 'Grenada', 'Greenland',
               'Guatemala', 'French Guiana', 'Guam', 'Guyana', 'Hong Kong', 'Heard Island and McDonald Islands',
               'Honduras',
               'Croatia', 'Haiti', 'Hungary', 'Indonesia', 'Isle of Man', 'India', 'British Indian Ocean Territory',
               'Ireland', 'Iran, Islamic Republic of', 'Iraq', 'Iceland', 'Italy', 'Jamaica', 'Jersey', 'Jordan',
               'Japan', 'Kazakhstan', 'Kenya', 'Kyrgyzstan', 'Cambodia', 'Kiribati', 'Saint Kitts and Nevis',
               'Korea, Republic of', 'Kuwait', "Lao People's Democratic Republic", 'Lebanon', 'Liberia', 'Libya',
               'Saint Lucia', 'Liechtenstein', 'Sri Lanka', 'Lesotho', 'Lithuania', 'Luxembourg', 'Latvia', 'Macao',
               'Saint Martin (French part)', 'Morocco', 'Monaco', 'Moldova, Republic of', 'Madagascar', 'Maldives',
               'Mexico', 'Marshall Islands', 'North Macedonia', 'Mali', 'Malta', 'Myanmar', 'Montenegro', 'Mongolia',
               'Northern Mariana Islands', 'Mozambique', 'Mauritania', 'Montserrat', 'Martinique', 'Mauritius',
               'Malawi',
               'Malaysia', 'Mayotte', 'Namibia', 'New Caledonia', 'Niger', 'Norfolk Island', 'Nigeria', 'Nicaragua',
               'Niue',
               'Netherlands', 'Norway', 'Nepal', 'Nauru', 'New Zealand', 'Oman', 'Pakistan', 'Panama', 'Pitcairn',
               'Peru',
               'Philippines', 'Palau', 'Papua New Guinea', 'Poland', 'Puerto Rico',
               "Korea, Democratic People's Republic of", 'Portugal', 'Paraguay', 'Palestine, State of',
               'French Polynesia',
               'Qatar', 'Réunion', 'Romania', 'Russian Federation', 'Rwanda', 'Saudi Arabia', 'Sudan', 'Senegal',
               'Singapore', 'South Georgia and the South Sandwich Islands',
               'Saint Helena, Ascension and Tristan da Cunha',
               'Svalbard and Jan Mayen', 'Solomon Islands', 'Sierra Leone', 'El Salvador', 'San Marino', 'Somalia',
               'Saint Pierre and Miquelon', 'Serbia', 'South Sudan', 'Sao Tome and Principe', 'Suriname', 'Slovakia',
               'Slovenia', 'Sweden', 'Eswatini', 'Sint Maarten (Dutch part)', 'Seychelles', 'Syrian Arab Republic',
               'Turks and Caicos Islands', 'Chad', 'Togo', 'Thailand', 'Tajikistan', 'Tokelau', 'Turkmenistan',
               'Timor-Leste', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Türkiye', 'Tuvalu',
               'Taiwan, Province of China',
               'Tanzania, United Republic of', 'Uganda', 'Ukraine', 'United States Minor Outlying Islands', 'Uruguay',
               'United States', 'Uzbekistan', 'Holy See (Vatican City State)', 'Saint Vincent and the Grenadines',
               'Venezuela, Bolivarian Republic of', 'Virgin Islands, British', 'Virgin Islands, U.S.', 'Viet Nam',
               'Vanuatu', 'Wallis and Futuna', 'Samoa', 'Yemen', 'South Africa', 'Zambia', 'Zimbabwe']
        natio_entry = ttk.Combobox(create_profile_page, values=ctr)
        natio_entry.place(x=10, y=520, width=250)

        gender = tk.Label(create_profile_page, text="Homme ou Femme ?", fg='green', font=('Bold', 15))
        gender.place(x=300, y=280)

        profile_img = tk.Button(create_profile_page, image=human, bd=0, command=new_image)
        profile_img.place(x=300, y=80)

        AN = ['Homme', 'Femme']
        gender_entry = ttk.Combobox(create_profile_page, values=AN)
        gender_entry.place(x=300, y=330)

        larow_img = tk.Button(create_profile_page, image=left_arow, bd=0, command=go_back)
        larow_img.place(x=30, y=30)

        create_profile_page.pack(pady=30)
        create_profile_page.pack_propagate(False)
        create_profile_page.configure(width=600, height=600)

    def after_admin_stu(self, username):#page d'acceuil de l admin
        def go_back():
            confirm = messagebox.askquestion(message="Voulez-vous vous déconnecter\n de votre compte ?")
            if confirm=='yes':
                admin_stu.destroy()
                b.welcom_page()
                root.update()

        def p_ou_e():
            if e_p_entry.get() == 'élève':
                admin_stu.destroy()
                a.create_profile(username)
            elif e_p_entry.get() == 'enseignant':
                admin_stu.destroy()
                a.create_profile_prof(username)
            else:
                messagebox.showerror('Erreur', 'vous avez oublié de choisir entre enseignant et élève')

        def existance() : #existance
            if e_p_entry.get() == 'élève':
                with open("etudiant.txt", "r") as f:
                    for ligne in f:
                        txt = ligne.split('\t')
                        if txt[0] == chercher_entry_en.get():
                            messagebox.showinfo('chercher', 'élève trouver')
                            return 1
                    messagebox.showinfo('chercher', 'élève non trouver')
                    return 0
            elif e_p_entry.get() == 'enseignant':
                with open("prof.txt", "r") as f:
                    for ligne in f:
                        txt = ligne.split('\t')
                        if txt[0] == chercher_entry_en.get():
                            messagebox.showinfo('chercher', 'enseignant trouver')
                            return 1
                    messagebox.showinfo('chercher', 'enseignant non trouver')
                    return 0
            else:
                messagebox.showerror('Erreur', 'vous avez oublié de choisir entre enseignant et élève')

        def miniexiste():
            if e_p_entry.get() == 'élève':
                with open("etudiant.txt", "r") as f:
                    for ligne in f:
                        txt = ligne.split('\t')
                        if txt[0] == sup_btn.get():
                            return True
                    return False
            elif e_p_entry.get() == 'enseignant':
                with open("prof.txt", "r") as f:
                    for ligne in f:
                        txt = ligne.split('\t')
                        if txt[0] == sup_btn.get():
                            return True
                    return False
            else:
                return False

        def miniexiste2():
            if e_p_entry.get() == 'élève':
                with open("etudiant.txt", "r") as f:
                    for ligne in f:
                        txt = ligne.split('\t')
                        if txt[0] == mod_ent.get():
                            return True
                    return False
            elif e_p_entry.get() == 'enseignant':
                with open("prof.txt", "r") as f:
                    for ligne in f:
                        txt = ligne.split('\t')
                        if txt[0] == mod_ent.get():
                            return True
                    return False
            else:
                return False

        def supprimer():#suprimer compte
            if e_p_entry.get() == 'élève':
                if miniexiste():
                    lignes = []
                    with open("etudiant.txt", "r") as f:
                        for ligne in f:
                            txt = ligne.split("\t")
                            if txt[0] != sup_btn.get():
                                lignes.append(ligne)
                        f.close()
                        with open("etudiant.txt", "w") as f:
                            for l in lignes:
                                f.write(l)
                    f.close()
                    messagebox.showinfo('Resultat', "Etudiant supprimé avec succés")
                else:
                    messagebox.showinfo('Resultat', "Etudiant " + sup_btn.get() + " n'existe pas")
            elif e_p_entry.get() == 'enseignant':
                if miniexiste():
                    lignes = []
                    with open("prof.txt", "r") as f:
                        for ligne in f:
                            txt = ligne.split("\t")
                            if txt[0] != sup_btn.get():
                                lignes.append(ligne)
                    f.close()
                    with open("prof.txt", "w") as f:
                        for l in lignes:
                            f.write(l)
                    f.close()
                    messagebox.showinfo('Resultat', "Enseignant supprimé avec succés")
                else:
                    messagebox.showinfo('Resultat', "Enseignant " + sup_btn.get() + " n'existe pas")
            else:
                messagebox.showerror('Erreur', 'vous avez oublié de choisir entre enseignant et élève')

        def modifier_profile():#modifier profile
            id = mod_ent.get()
            if e_p_entry.get() == 'enseignant':
                if miniexiste2():
                    pic_path = tk.StringVar()
                    pic_path.set('')

                    def go_back():
                        mod_profile_page.destroy()
                        self.after_admin_stu(username)

                    def new_image():
                        path = askopenfilename()
                        if path:
                            img = ImageTk.PhotoImage(Image.open(path).resize((100, 100)))
                            pic_path.set(path)
                            profile_img.configure(image=img)
                            profile_img.image = img

                    def generate_pdf():
                        # Gather personal information from your Tkinter fields
                        nometprenom = username_entry.get()
                        mail = email_entry.get()
                        motdepass = mdp_entry.get()
                        datedenaiss = ddn_entry.get()
                        module = prof_module_entry.get()
                        genre = gender_entry.get()
                        num = phone_entry.get()
                        nationalit = natio_entry.get()
                        img = ImageReader('image/bigecc-logo.png')
                        img2 = ImageReader(pic_path.get())

                        with open("prof.txt", "a") as f:
                            f.write(
                                nometprenom + "\t" + mail + "\t" + motdepass + "\t" + datedenaiss + "\t" + module + "\t" + genre + "\t" + num + "\t" + nationalit + "\n")
                            f.close()

                            # Collect other information similarly

                            # Create a PDF document
                        pdf_filename = f"{nometprenom}.pdf"
                        pdf = canvas.Canvas(pdf_filename)

                        # Write the information onto the PDF
                        pdf.drawBoundary(0, 50, 300, 500, 500)
                        pdf.drawString(150, 700, f"Nom et prenom           : {nometprenom}")
                        pdf.drawString(150, 650, f"Email                           : {mail}")
                        pdf.drawString(150, 600, f"Mot de passe              : {motdepass}")
                        pdf.drawString(150, 550, f"date de naissance       : {datedenaiss}")
                        pdf.drawString(150, 500, f"module de l'enseignant: {module}")
                        pdf.drawString(150, 450, f"sexe                             : {genre}")
                        pdf.drawString(150, 400, f"numero de telephone   : {num}")
                        pdf.drawString(150, 350, f"nationalité                     : {nationalit}")
                        pdf.drawImage(img, 100, 750, mask='auto', width=100, height=100)
                        pdf.drawImage(img2, 449, 679, mask='auto', width=100, height=120)
                        pdf.drawBoundary(0, 50, 90, 500, 200)
                        pdf.drawString(100, 250, f"Pôle scolarité")
                        pdf.drawString(100, 220, f"Fondation Ecole Centrale Casablanca")
                        pdf.drawString(100, 190, f"Ville Verte Côté Latéral Est - Bouskoura – Maroc")
                        pdf.drawString(100, 160, f"T +212 (0) 5 22 49 35 00 | F +212 (0) 5 22 49 35 20")
                        pdf.save()
                        mod_profile_page.destroy()
                        self.after_admin_stu(username)

                    with open("prof.txt", "r") as f:
                        for ligne in f:
                            txt = ligne.split('\t')
                            if txt[0] == id:
                                admin_stu.destroy()
                                mod_profile_page = tk.Frame(root, highlightbackground='green', highlightthickness=3)

                                heading_lb = tk.Label(mod_profile_page, text="crée un profile", bg='green', fg='white',
                                                      font=('Bold', 19))
                                heading_lb.place(x=100, y=0, width=400)

                                nometprenom = tk.Label(mod_profile_page, text='nom et prenom', fg='green',
                                                       font=('Bold', 15))
                                nometprenom.place(x=10, y=80)

                                username_entry = tk.Entry(mod_profile_page, font=('Bold', 10), justify=tk.CENTER)
                                username_entry.place(x=10, y=130, width=250)
                                username_entry.insert(0, txt[0])

                                email = tk.Label(mod_profile_page, text='email', fg='green', font=('Bold', 15))
                                email.place(x=10, y=180)

                                email_entry = tk.Entry(mod_profile_page, font=('Bold', 10), justify=tk.CENTER)
                                email_entry.place(x=10, y=230, width=250)
                                email_entry.insert(0, txt[1])

                                mdp = tk.Label(mod_profile_page, text='Mot de passe', fg='green', font=('Bold', 15))
                                mdp.place(x=10, y=280)

                                mdp_entry = tk.Entry(mod_profile_page, font=('Bold', 10), justify=tk.CENTER)
                                mdp_entry.place(x=10, y=330, width=250)
                                mdp_entry.insert(0, txt[2])

                                ddn = tk.Label(mod_profile_page, text='Date de naissance', fg='green',
                                               font=('Bold', 15))
                                ddn.place(x=10, y=380)

                                ddn_entry = DateEntry(mod_profile_page, selectmode='day', date_pattern='dd/MM/yyyy', )
                                ddn_entry.grid(row=1, column=1, padx=15)
                                ddn_entry.place(x=10, y=430, width=250)
                                ddn_entry.set_date(txt[3])

                                valider_btn = tk.Button(mod_profile_page, text='Valider', fg='white', bg='green',
                                                        font=('Bold', 15), command=generate_pdf)
                                valider_btn.place(x=350, y=520)

                                phone = tk.Label(mod_profile_page, text='numero de telephone', fg='green',
                                                 font=('Bold', 15))
                                phone.place(x=300, y=380)

                                phone_entry = tk.Entry(mod_profile_page, font=('Bold', 10), justify=tk.CENTER)
                                phone_entry.place(x=300, y=430, width=250)
                                phone_entry.insert(0, txt[6])

                                prof_module = tk.Label(mod_profile_page, text="module ", fg='green', font=('Bold', 15))
                                prof_module.place(x=300, y=180)

                                AN = ['analyse', 'proba', 'mecanique', 'PMOO',
                                      'analyse des valeur',
                                      'sociologie',
                                      'phylosophie', 'traitement du signale', 'mecanique quantique',
                                      'mecanique des fluide',
                                      'statistique', 'economie']
                                prof_module_entry = ttk.Combobox(mod_profile_page, values=AN)
                                prof_module_entry.place(x=300, y=230, width=250)
                                prof_module_entry.insert(0, txt[4])

                                natio = tk.Label(mod_profile_page, text="nationalité", fg='green', font=('Bold', 15))
                                natio.place(x=10, y=470)

                                ctr = ['Aruba', 'Afghanistan', 'Angola', 'Anguilla', 'Åland Islands', 'Albania',
                                       'Andorra',
                                       'United Arab Emirates',
                                       'Argentina', 'Armenia', 'American Samoa', 'Antarctica',
                                       'French Southern Territories',
                                       'Antigua and Barbuda',
                                       'Australia', 'Austria', 'Azerbaijan', 'Burundi', 'Belgium', 'Benin',
                                       'Bonaire, Sint Eustatius and Saba',
                                       'Burkina Faso', 'Bangladesh', 'Bulgaria', 'Bahrain', 'Bahamas',
                                       'Bosnia and Herzegovina',
                                       'Saint Barthélemy',
                                       'Belarus', 'Belize', 'Bermuda', 'Bolivia, Plurinational State of', 'Brazil',
                                       'Barbados',
                                       'Brunei Darussalam',
                                       'Bhutan', 'Bouvet Island', 'Botswana', 'Central African Republic', 'Canada',
                                       'Cocos (Keeling) Islands',
                                       'Switzerland', 'Chile', 'China', "Côte d'Ivoire", 'Cameroon',
                                       'Congo, The Democratic Republic of the',
                                       'Congo', 'Cook Islands', 'Colombia', 'Comoros', 'Cabo Verde', 'Costa Rica',
                                       'Cuba',
                                       'Curaçao',
                                       'Christmas Island', 'Cayman Islands', 'Cyprus', 'Czechia', 'Germany', 'Djibouti',
                                       'Dominica', 'Denmark',
                                       'Dominican Republic', 'Algeria', 'Ecuador', 'Egypt', 'Eritrea', 'Western Sahara',
                                       'Spain', 'Estonia',
                                       'Ethiopia', 'Finland', 'Fiji', 'Falkland Islands (Malvinas)', 'France',
                                       'Faroe Islands',
                                       'Micronesia, Federated States of', 'Gabon', 'United Kingdom', 'Georgia',
                                       'Guernsey',
                                       'Ghana', 'Gibraltar',
                                       'Guinea', 'Guadeloupe', 'Gambia', 'Guinea-Bissau', 'Equatorial Guinea', 'Greece',
                                       'Grenada', 'Greenland',
                                       'Guatemala', 'French Guiana', 'Guam', 'Guyana', 'Hong Kong',
                                       'Heard Island and McDonald Islands', 'Honduras',
                                       'Croatia', 'Haiti', 'Hungary', 'Indonesia', 'Isle of Man', 'India',
                                       'British Indian Ocean Territory',
                                       'Ireland', 'Iran, Islamic Republic of', 'Iraq', 'Iceland', 'Italy',
                                       'Jamaica',
                                       'Jersey', 'Jordan',
                                       'Japan', 'Kazakhstan', 'Kenya', 'Kyrgyzstan', 'Cambodia', 'Kiribati',
                                       'Saint Kitts and Nevis',
                                       'Korea, Republic of', 'Kuwait', "Lao People's Democratic Republic", 'Lebanon',
                                       'Liberia',
                                       'Libya',
                                       'Saint Lucia', 'Liechtenstein', 'Sri Lanka', 'Lesotho', 'Lithuania',
                                       'Luxembourg',
                                       'Latvia', 'Macao',
                                       'Saint Martin (French part)', 'Morocco', 'Monaco', 'Moldova, Republic of',
                                       'Madagascar',
                                       'Maldives',
                                       'Mexico', 'Marshall Islands', 'North Macedonia', 'Mali', 'Malta', 'Myanmar',
                                       'Montenegro', 'Mongolia',
                                       'Northern Mariana Islands', 'Mozambique', 'Mauritania', 'Montserrat',
                                       'Martinique',
                                       'Mauritius', 'Malawi',
                                       'Malaysia', 'Mayotte', 'Namibia', 'New Caledonia', 'Niger', 'Norfolk Island',
                                       'Nigeria',
                                       'Nicaragua', 'Niue',
                                       'Netherlands', 'Norway', 'Nepal', 'Nauru', 'New Zealand', 'Oman', 'Pakistan',
                                       'Panama',
                                       'Pitcairn', 'Peru',
                                       'Philippines', 'Palau', 'Papua New Guinea', 'Poland', 'Puerto Rico',
                                       "Korea, Democratic People's Republic of", 'Portugal', 'Paraguay',
                                       'Palestine, State of',
                                       'French Polynesia',
                                       'Qatar', 'Réunion', 'Romania', 'Russian Federation', 'Rwanda', 'Saudi Arabia',
                                       'Sudan',
                                       'Senegal',
                                       'Singapore', 'South Georgia and the South Sandwich Islands',
                                       'Saint Helena, Ascension and Tristan da Cunha',
                                       'Svalbard and Jan Mayen', 'Solomon Islands', 'Sierra Leone', 'El Salvador',
                                       'San Marino',
                                       'Somalia',
                                       'Saint Pierre and Miquelon', 'Serbia', 'South Sudan', 'Sao Tome and Principe',
                                       'Suriname', 'Slovakia',
                                       'Slovenia', 'Sweden', 'Eswatini', 'Sint Maarten (Dutch part)', 'Seychelles',
                                       'Syrian Arab Republic',
                                       'Turks and Caicos Islands', 'Chad', 'Togo', 'Thailand', 'Tajikistan', 'Tokelau',
                                       'Turkmenistan',
                                       'Timor-Leste', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Türkiye', 'Tuvalu',
                                       'Taiwan, Province of China',
                                       'Tanzania, United Republic of', 'Uganda', 'Ukraine',
                                       'United States Minor Outlying Islands', 'Uruguay',
                                       'United States', 'Uzbekistan', 'Holy See (Vatican City State)',
                                       'Saint Vincent and the Grenadines',
                                       'Venezuela, Bolivarian Republic of', 'Virgin Islands, British',
                                       'Virgin Islands, U.S.',
                                       'Viet Nam',
                                       'Vanuatu', 'Wallis and Futuna', 'Samoa', 'Yemen', 'South Africa', 'Zambia',
                                       'Zimbabwe']
                                natio_entry = ttk.Combobox(mod_profile_page, values=ctr)
                                natio_entry.place(x=10, y=520, width=250)
                                natio_entry.insert(0, txt[7])

                                gender = tk.Label(mod_profile_page, text="Homme ou Femme ?", fg='green',
                                                  font=('Bold', 15))
                                gender.place(x=300, y=280)

                                profile_img = tk.Button(mod_profile_page, image=human, bd=0, command=new_image)
                                profile_img.place(x=300, y=80)

                                AN = ['Homme', 'Femme']
                                gender_entry = ttk.Combobox(mod_profile_page, values=AN)
                                gender_entry.place(x=300, y=330)
                                gender_entry.insert(0, txt[5])

                                larow_img = tk.Button(mod_profile_page, image=left_arow, bd=0, command=go_back)
                                larow_img.place(x=30, y=30)

                                mod_profile_page.pack(pady=30)
                                mod_profile_page.pack_propagate(False)
                                mod_profile_page.configure(width=600, height=600)

                                lignes = []
                                with open("prof.txt", "r") as f:
                                    for ligne in f:
                                        txt = ligne.split("\t")
                                        if txt[0] != id:
                                            lignes.append(ligne)
                                f.close()
                                with open("prof.txt", "w") as f:
                                    for l in lignes:
                                        f.write(l)
                                f.close()
                else:
                    messagebox.showerror('Erreur', "n'est pas trouver")
            elif e_p_entry.get() == 'élève':
                if miniexiste2():
                    pic_path = tk.StringVar()
                    pic_path.set('')

                    def go_back():
                        mod_profile_page.destroy()
                        self.after_admin_stu(username)

                    def new_image():
                        path = askopenfilename()
                        if path:
                            img = ImageTk.PhotoImage(Image.open(path).resize((100, 100)))
                            pic_path.set(path)
                            profile_img.configure(image=img)
                            profile_img.image = img

                    def generate_pdf():
                        # Gather personal information from your Tkinter fields
                        nometprenom = username_entry.get()
                        mail = email_entry.get()
                        motdepass = mdp_entry.get()
                        datedenaiss = ddn_entry.get()
                        classeleve = stu_class_entry.get()
                        genre = gender_entry.get()
                        num = phone_entry.get()
                        nationalit = natio_entry.get()
                        img = ImageReader('image/bigecc-logo.png')
                        img2 = ImageReader(pic_path.get())

                        with open("etudiant.txt", "a") as f:
                            f.write(
                                nometprenom + "\t" + mail + "\t" + motdepass + "\t" + datedenaiss + "\t" + classeleve + "\t" + genre + "\t" + num + "\t" + nationalit + "\n")
                            f.close()

                            # Collect other information similarly

                            # Create a PDF document
                        pdf_filename = f"{nometprenom}.pdf"
                        pdf = canvas.Canvas(pdf_filename)

                        # Write the information onto the PDF
                        pdf.drawBoundary(0, 50, 300, 500, 500)
                        pdf.drawString(150, 700, f"Nom et prenom        : {nometprenom}")
                        pdf.drawString(150, 650, f"Email                        : {mail}")
                        pdf.drawString(150, 600, f"Mot de passe           : {motdepass}")
                        pdf.drawString(150, 550, f"date de naissance    : {datedenaiss}")
                        pdf.drawString(150, 500, f"classe de l'eleve       : {classeleve}")
                        pdf.drawString(150, 450, f"sexe                          : {genre}")
                        pdf.drawString(150, 400, f"numero de telephone: {num}")
                        pdf.drawString(150, 350, f"nationalité                  : {nationalit}")
                        pdf.drawImage(img, 100, 750, mask='auto', width=100, height=100)
                        pdf.drawImage(img2, 449, 679, mask='auto', width=100, height=120)
                        pdf.drawBoundary(0, 50, 90, 500, 200)
                        pdf.drawString(100, 250, f"Pôle scolarité")
                        pdf.drawString(100, 220, f"Fondation Ecole Centrale Casablanca")
                        pdf.drawString(100, 190, f"Ville Verte Côté Latéral Est - Bouskoura – Maroc")
                        pdf.drawString(100, 160, f"T +212 (0) 5 22 49 35 00 | F +212 (0) 5 22 49 35 20")
                        pdf.save()
                        mod_profile_page.destroy()
                        self.after_admin_stu(username)

                    with open("etudiant.txt", "r") as f:
                        for ligne in f:
                            txt = ligne.split('\t')

                            if txt[0] == id:
                                admin_stu.destroy()
                                mod_profile_page = tk.Frame(root, highlightbackground='green', highlightthickness=3)

                                heading_lb = tk.Label(mod_profile_page, text="crée un profile", bg='green', fg='white',
                                                      font=('Bold', 19))
                                heading_lb.place(x=100, y=0, width=400)

                                nometprenom = tk.Label(mod_profile_page, text='nom et prenom', fg='green',
                                                       font=('Bold', 15))
                                nometprenom.place(x=10, y=80)

                                username_entry = tk.Entry(mod_profile_page, font=('Bold', 10), justify=tk.CENTER)
                                username_entry.place(x=10, y=130, width=250)
                                username_entry.insert(0, txt[0])

                                email = tk.Label(mod_profile_page, text='email', fg='green', font=('Bold', 15))
                                email.place(x=10, y=180)

                                email_entry = tk.Entry(mod_profile_page, font=('Bold', 10), justify=tk.CENTER)
                                email_entry.place(x=10, y=230, width=250)
                                email_entry.insert(0, txt[1])

                                mdp = tk.Label(mod_profile_page, text='Mot de passe', fg='green', font=('Bold', 15))
                                mdp.place(x=10, y=280)

                                mdp_entry = tk.Entry(mod_profile_page, font=('Bold', 10), justify=tk.CENTER)
                                mdp_entry.place(x=10, y=330, width=250)
                                mdp_entry.insert(0, txt[2])

                                ddn = tk.Label(mod_profile_page, text='Date de naissance', fg='green',
                                               font=('Bold', 15))
                                ddn.place(x=10, y=380)

                                ddn_entry = DateEntry(mod_profile_page, selectmode='day', date_pattern='dd/MM/yyyy')
                                ddn_entry.grid(row=1, column=1, padx=15)
                                ddn_entry.place(x=10, y=430, width=250)
                                ddn_entry.set_date(txt[3])

                                valider_btn = tk.Button(mod_profile_page, text='Valider', fg='white', bg='green',
                                                        font=('Bold', 15), command=generate_pdf)
                                valider_btn.place(x=350, y=520)

                                phone = tk.Label(mod_profile_page, text='numero de telephone', fg='green',
                                                 font=('Bold', 15))
                                phone.place(x=300, y=380)

                                phone_entry = tk.Entry(mod_profile_page, font=('Bold', 10), justify=tk.CENTER)
                                phone_entry.place(x=300, y=430, width=250)
                                phone_entry.insert(0, txt[6])

                                stu_class = tk.Label(mod_profile_page, text="classe de l'éleve", fg='green',
                                                     font=('Bold', 15))
                                stu_class.place(x=300, y=180)

                                AN = ['1A', '2A', '3A']
                                stu_class_entry = ttk.Combobox(mod_profile_page, values=AN)
                                stu_class_entry.place(x=300, y=230, width=250)
                                stu_class_entry.insert(0, txt[4])

                                natio = tk.Label(mod_profile_page, text="nationalité", fg='green', font=('Bold', 15))
                                natio.place(x=10, y=470)

                                ctr = ['Aruba', 'Afghanistan', 'Angola', 'Anguilla', 'Åland Islands', 'Albania',
                                       'Andorra',
                                       'United Arab Emirates',
                                       'Argentina', 'Armenia', 'American Samoa', 'Antarctica',
                                       'French Southern Territories',
                                       'Antigua and Barbuda',
                                       'Australia', 'Austria', 'Azerbaijan', 'Burundi', 'Belgium', 'Benin',
                                       'Bonaire, Sint Eustatius and Saba',
                                       'Burkina Faso', 'Bangladesh', 'Bulgaria', 'Bahrain', 'Bahamas',
                                       'Bosnia and Herzegovina',
                                       'Saint Barthélemy',
                                       'Belarus', 'Belize', 'Bermuda', 'Bolivia, Plurinational State of', 'Brazil',
                                       'Barbados',
                                       'Brunei Darussalam',
                                       'Bhutan', 'Bouvet Island', 'Botswana', 'Central African Republic', 'Canada',
                                       'Cocos (Keeling) Islands',
                                       'Switzerland', 'Chile', 'China', "Côte d'Ivoire", 'Cameroon',
                                       'Congo, The Democratic Republic of the',
                                       'Congo', 'Cook Islands', 'Colombia', 'Comoros', 'Cabo Verde', 'Costa Rica',
                                       'Cuba',
                                       'Curaçao',
                                       'Christmas Island', 'Cayman Islands', 'Cyprus', 'Czechia', 'Germany', 'Djibouti',
                                       'Dominica', 'Denmark',
                                       'Dominican Republic', 'Algeria', 'Ecuador', 'Egypt', 'Eritrea', 'Western Sahara',
                                       'Spain', 'Estonia',
                                       'Ethiopia', 'Finland', 'Fiji', 'Falkland Islands (Malvinas)', 'France',
                                       'Faroe Islands',
                                       'Micronesia, Federated States of', 'Gabon', 'United Kingdom', 'Georgia',
                                       'Guernsey',
                                       'Ghana', 'Gibraltar',
                                       'Guinea', 'Guadeloupe', 'Gambia', 'Guinea-Bissau', 'Equatorial Guinea', 'Greece',
                                       'Grenada', 'Greenland',
                                       'Guatemala', 'French Guiana', 'Guam', 'Guyana', 'Hong Kong',
                                       'Heard Island and McDonald Islands', 'Honduras',
                                       'Croatia', 'Haiti', 'Hungary', 'Indonesia', 'Isle of Man', 'India',
                                       'British Indian Ocean Territory',
                                       'Ireland', 'Iran, Islamic Republic of', 'Iraq', 'Iceland', 'Israel', 'Italy',
                                       'Jamaica',
                                       'Jersey', 'Jordan',
                                       'Japan', 'Kazakhstan', 'Kenya', 'Kyrgyzstan', 'Cambodia', 'Kiribati',
                                       'Saint Kitts and Nevis',
                                       'Korea, Republic of', 'Kuwait', "Lao People's Democratic Republic", 'Lebanon',
                                       'Liberia',
                                       'Libya',
                                       'Saint Lucia', 'Liechtenstein', 'Sri Lanka', 'Lesotho', 'Lithuania',
                                       'Luxembourg',
                                       'Latvia', 'Macao',
                                       'Saint Martin (French part)', 'Morocco', 'Monaco', 'Moldova, Republic of',
                                       'Madagascar',
                                       'Maldives',
                                       'Mexico', 'Marshall Islands', 'North Macedonia', 'Mali', 'Malta', 'Myanmar',
                                       'Montenegro', 'Mongolia',
                                       'Northern Mariana Islands', 'Mozambique', 'Mauritania', 'Montserrat',
                                       'Martinique',
                                       'Mauritius', 'Malawi',
                                       'Malaysia', 'Mayotte', 'Namibia', 'New Caledonia', 'Niger', 'Norfolk Island',
                                       'Nigeria',
                                       'Nicaragua', 'Niue',
                                       'Netherlands', 'Norway', 'Nepal', 'Nauru', 'New Zealand', 'Oman', 'Pakistan',
                                       'Panama',
                                       'Pitcairn', 'Peru',
                                       'Philippines', 'Palau', 'Papua New Guinea', 'Poland', 'Puerto Rico',
                                       "Korea, Democratic People's Republic of", 'Portugal', 'Paraguay',
                                       'Palestine, State of',
                                       'French Polynesia',
                                       'Qatar', 'Réunion', 'Romania', 'Russian Federation', 'Rwanda', 'Saudi Arabia',
                                       'Sudan',
                                       'Senegal',
                                       'Singapore', 'South Georgia and the South Sandwich Islands',
                                       'Saint Helena, Ascension and Tristan da Cunha',
                                       'Svalbard and Jan Mayen', 'Solomon Islands', 'Sierra Leone', 'El Salvador',
                                       'San Marino',
                                       'Somalia',
                                       'Saint Pierre and Miquelon', 'Serbia', 'South Sudan', 'Sao Tome and Principe',
                                       'Suriname', 'Slovakia',
                                       'Slovenia', 'Sweden', 'Eswatini', 'Sint Maarten (Dutch part)', 'Seychelles',
                                       'Syrian Arab Republic',
                                       'Turks and Caicos Islands', 'Chad', 'Togo', 'Thailand', 'Tajikistan', 'Tokelau',
                                       'Turkmenistan',
                                       'Timor-Leste', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Türkiye', 'Tuvalu',
                                       'Taiwan, Province of China',
                                       'Tanzania, United Republic of', 'Uganda', 'Ukraine',
                                       'United States Minor Outlying Islands', 'Uruguay',
                                       'United States', 'Uzbekistan', 'Holy See (Vatican City State)',
                                       'Saint Vincent and the Grenadines',
                                       'Venezuela, Bolivarian Republic of', 'Virgin Islands, British',
                                       'Virgin Islands, U.S.',
                                       'Viet Nam',
                                       'Vanuatu', 'Wallis and Futuna', 'Samoa', 'Yemen', 'South Africa', 'Zambia',
                                       'Zimbabwe']
                                natio_entry = ttk.Combobox(mod_profile_page, values=ctr)
                                natio_entry.place(x=10, y=520, width=250)
                                natio_entry.insert(0, txt[7])

                                gender = tk.Label(mod_profile_page, text="Homme ou Femme ?", fg='green',
                                                  font=('Bold', 15))
                                gender.place(x=300, y=280)

                                profile_img = tk.Button(mod_profile_page, image=human, bd=0, command=new_image)
                                profile_img.place(x=300, y=80)

                                AN = ['Homme', 'Femme']
                                gender_entry = ttk.Combobox(mod_profile_page, values=AN)
                                gender_entry.place(x=300, y=330)
                                gender_entry.insert(0, txt[5])

                                larow_img = tk.Button(mod_profile_page, image=left_arow, bd=0, command=go_back)
                                larow_img.place(x=30, y=30)

                                mod_profile_page.pack(pady=30)
                                mod_profile_page.pack_propagate(False)
                                mod_profile_page.configure(width=600, height=600)

                                lignes = []
                                with open("etudiant.txt", "r") as f:
                                    for ligne in f:
                                        txt = ligne.split("\t")
                                        if txt[0] != id:
                                            lignes.append(ligne)
                                    f.close()
                                    with open("etudiant.txt", "w") as f:
                                        for l in lignes:
                                            f.write(l)
                                    f.close()
                else:
                    messagebox.showerror('Erreur', "n'est pas trouver")
            else:
                messagebox.showerror('Erreur', 'vous avez oublié de choisir entre enseignant et élève')

        admin_stu = tk.Frame(root, highlightbackground=bg_color, highlightthickness=3)

        heading_lb = tk.Label(admin_stu, text=f"Bienvenue {username}  ", bg=bg_color, fg='white', font=('Bold', 19))
        heading_lb.place(x=100, y=0, width=400)

        e_p = tk.Label(admin_stu, text="enseignant ou élève ?", fg='green', font=('Bold', 15))
        e_p.place(x=170, y=100)

        AN = ['élève', 'enseignant']
        e_p_entry = ttk.Combobox(admin_stu, values=AN)
        e_p_entry.place(x=170, y=125, width=200)

        chercher_entry = tk.Button(admin_stu, text='Chercher', fg='white', font=('Bold', 13), bg=bg_color,
                                   command=existance)
        chercher_entry.place(x=90, y=200, width=150)

        chercher_entry_en = tk.Entry(admin_stu, font=('calibri', 10))
        chercher_entry_en.place(x=90, y=230, width=150)

        chercher_img = tk.Button(admin_stu, image=search, bd=0)
        chercher_img.place(x=30, y=200)

        ajouter_btn = tk.Button(admin_stu, text="ajouter quelqu'un", bg=bg_color, fg='white', font=('calibri', 11),
                                command=p_ou_e)
        ajouter_btn.place(x=90, y=310, width=150)

        ajouter_img = tk.Button(admin_stu, image=ajouter, bd=0)
        ajouter_img.place(x=30, y=300)

        sup_lb = tk.Button(admin_stu, text='supprimer', fg='white', font=('Bold', 13), bg=bg_color, command=supprimer)
        sup_lb.place(x=380, y=200, width=150)

        sup_btn = tk.Entry(admin_stu, font=('calibri', 10))
        sup_btn.place(x=380, y=230, width=150)

        sup_img = tk.Button(admin_stu, image=sup, bd=0)
        sup_img.place(x=320, y=200)

        mod_lb = tk.Button(admin_stu, text='Modifier', fg='white', font=('Bold', 13), bg=bg_color,
                           command=modifier_profile)
        mod_lb.place(x=380, y=300, width=150)

        mod_ent = tk.Entry(admin_stu, font=('calibri', 10))
        mod_ent.place(x=380, y=330, width=150)

        mod_but = tk.Button(admin_stu, image=modif, bd=0)
        mod_but.place(x=320, y=300)

        larow_img = tk.Button(admin_stu, text='logout', bd=0, command=go_back, background='red')
        larow_img.place(x=30, y=440, width=100, height=30)

        admin_stu.pack(pady=30)
        admin_stu.pack_propagate(False)
        admin_stu.configure(width=550, height=500)

    def create_profile_prof(self, nomaffi):
        pic_path = tk.StringVar()
        pic_path.set('')

        def go_back():
            create_profile_page.destroy()
            self.after_admin_stu(nomaffi)

        def new_image():
            path = askopenfilename()
            if path:
                img = ImageTk.PhotoImage(Image.open(path).resize((100, 100)))
                pic_path.set(path)
                profile_img.configure(image=img)
                profile_img.image = img

        def generate_pdf():
            # Gather personal information from your Tkinter fields
            nometprenom = username_entry.get()
            mail = email_entry.get()
            motdepass = mdp_entry.get()
            datedenaiss = ddn_entry.get()
            module = prof_module_entry.get()
            genre = gender_entry.get()
            num = phone_entry.get()
            nationalit = natio_entry.get()
            img = ImageReader('image/bigecc-logo.png')
            img2 = ImageReader(pic_path.get())

            with open("prof.txt", "a") as f:
                f.write(
                    nometprenom + "\t" + mail + "\t" + motdepass + "\t" + datedenaiss + "\t" + module + "\t" + genre + "\t" + num + "\t" + nationalit + "\n")
            f.close()

            # Collect other information similarly

            # Create a PDF document
            pdf_filename = f"{nometprenom}.pdf"
            pdf = canvas.Canvas(pdf_filename)

            # Write the information onto the PDF
            pdf.drawBoundary(0, 50, 300, 500, 500)
            pdf.drawString(150, 700, f"Nom et prenom           : {nometprenom}")
            pdf.drawString(150, 650, f"Email                           : {mail}")
            pdf.drawString(150, 600, f"Mot de passe              : {motdepass}")
            pdf.drawString(150, 550, f"date de naissance       : {datedenaiss}")
            pdf.drawString(150, 500, f"module de l'enseignant: {module}")
            pdf.drawString(150, 450, f"sexe                             : {genre}")
            pdf.drawString(150, 400, f"numero de telephone   : {num}")
            pdf.drawString(150, 350, f"nationalité                     : {nationalit}")
            pdf.drawImage(img, 100, 750, mask='auto', width=100, height=100)
            pdf.drawImage(img2, 449, 679, mask='auto', width=100, height=120)
            pdf.drawBoundary(0, 50, 90, 500, 200)
            pdf.drawString(100, 250, f"Pôle scolarité")
            pdf.drawString(100, 220, f"Fondation Ecole Centrale Casablanca")
            pdf.drawString(100, 190, f"Ville Verte Côté Latéral Est - Bouskoura – Maroc")
            pdf.drawString(100, 160, f"T +212 (0) 5 22 49 35 00 | F +212 (0) 5 22 49 35 20")
            pdf.save()
            create_profile_page.destroy()
            a.after_admin_stu(nomaffi)

        create_profile_page = tk.Frame(root, highlightbackground='green', highlightthickness=3)

        heading_lb = tk.Label(create_profile_page, text="crée un profile", bg='green', fg='white', font=('Bold', 19))
        heading_lb.place(x=100, y=0, width=400)

        username = tk.Label(create_profile_page, text='nom et prenom', fg='green', font=('Bold', 15))
        username.place(x=10, y=80)

        username_entry = tk.Entry(create_profile_page, font=('Bold', 10), justify=tk.CENTER)
        username_entry.place(x=10, y=130, width=250)

        email = tk.Label(create_profile_page, text='email', fg='green', font=('Bold', 15))
        email.place(x=10, y=180)

        email_entry = tk.Entry(create_profile_page, font=('Bold', 10), justify=tk.CENTER)
        email_entry.place(x=10, y=230, width=250)

        mdp = tk.Label(create_profile_page, text='Mot de passe', fg='green', font=('Bold', 15))
        mdp.place(x=10, y=280)

        mdp_entry = tk.Entry(create_profile_page, font=('Bold', 10), justify=tk.CENTER)
        mdp_entry.place(x=10, y=330, width=250)

        ddn = tk.Label(create_profile_page, text='Date de naissance', fg='green', font=('Bold', 15))
        ddn.place(x=10, y=380)

        ddn_entry = DateEntry(create_profile_page, selectmode='day', date_pattern='dd/MM/yyyy')
        ddn_entry.grid(row=1, column=1, padx=15)
        ddn_entry.place(x=10, y=430, width=250)

        valider_btn = tk.Button(create_profile_page, text='Valider', fg='white', bg='green', font=('Bold', 15),
                                command=generate_pdf)
        valider_btn.place(x=350, y=520)

        phone = tk.Label(create_profile_page, text='numero de telephone', fg='green', font=('Bold', 15))
        phone.place(x=300, y=380)

        phone_entry = tk.Entry(create_profile_page, font=('Bold', 10), justify=tk.CENTER)
        phone_entry.place(x=300, y=430, width=250)

        prof_module = tk.Label(create_profile_page, text="module ", fg='green', font=('Bold', 15))
        prof_module.place(x=300, y=180)

        AN = ['analyse', 'proba', 'mecanique', 'PMOO', 'analyse des valeur', 'sociologie',
              'phylosophie', 'traitement du signale', 'mecanique quantique', 'mecanique des fluide',
              'statistique', 'economie']
        prof_module_entry = ttk.Combobox(create_profile_page, values=AN)
        prof_module_entry.place(x=300, y=230, width=250)

        natio = tk.Label(create_profile_page, text="nationalité", fg='green', font=('Bold', 15))
        natio.place(x=10, y=470)

        ctr = ['Aruba', 'Afghanistan', 'Angola', 'Anguilla', 'Åland Islands', 'Albania', 'Andorra',
               'United Arab Emirates',
               'Argentina', 'Armenia', 'American Samoa', 'Antarctica', 'French Southern Territories',
               'Antigua and Barbuda',
               'Australia', 'Austria', 'Azerbaijan', 'Burundi', 'Belgium', 'Benin', 'Bonaire, Sint Eustatius and Saba',
               'Burkina Faso', 'Bangladesh', 'Bulgaria', 'Bahrain', 'Bahamas', 'Bosnia and Herzegovina',
               'Saint Barthélemy',
               'Belarus', 'Belize', 'Bermuda', 'Bolivia, Plurinational State of', 'Brazil', 'Barbados',
               'Brunei Darussalam',
               'Bhutan', 'Bouvet Island', 'Botswana', 'Central African Republic', 'Canada', 'Cocos (Keeling) Islands',
               'Switzerland', 'Chile', 'China', "Côte d'Ivoire", 'Cameroon', 'Congo, The Democratic Republic of the',
               'Congo', 'Cook Islands', 'Colombia', 'Comoros', 'Cabo Verde', 'Costa Rica', 'Cuba', 'Curaçao',
               'Christmas Island', 'Cayman Islands', 'Cyprus', 'Czechia', 'Germany', 'Djibouti', 'Dominica', 'Denmark',
               'Dominican Republic', 'Algeria', 'Ecuador', 'Egypt', 'Eritrea', 'Western Sahara', 'Spain', 'Estonia',
               'Ethiopia', 'Finland', 'Fiji', 'Falkland Islands (Malvinas)', 'France', 'Faroe Islands',
               'Micronesia, Federated States of', 'Gabon', 'United Kingdom', 'Georgia', 'Guernsey', 'Ghana',
               'Gibraltar',
               'Guinea', 'Guadeloupe', 'Gambia', 'Guinea-Bissau', 'Equatorial Guinea', 'Greece', 'Grenada', 'Greenland',
               'Guatemala', 'French Guiana', 'Guam', 'Guyana', 'Hong Kong', 'Heard Island and McDonald Islands',
               'Honduras',
               'Croatia', 'Haiti', 'Hungary', 'Indonesia', 'Isle of Man', 'India', 'British Indian Ocean Territory',
               'Ireland', 'Iran, Islamic Republic of', 'Iraq', 'Iceland', 'Israel', 'Italy', 'Jamaica', 'Jersey',
               'Jordan',
               'Japan', 'Kazakhstan', 'Kenya', 'Kyrgyzstan', 'Cambodia', 'Kiribati', 'Saint Kitts and Nevis',
               'Korea, Republic of', 'Kuwait', "Lao People's Democratic Republic", 'Lebanon', 'Liberia', 'Libya',
               'Saint Lucia', 'Liechtenstein', 'Sri Lanka', 'Lesotho', 'Lithuania', 'Luxembourg', 'Latvia', 'Macao',
               'Saint Martin (French part)', 'Morocco', 'Monaco', 'Moldova, Republic of', 'Madagascar', 'Maldives',
               'Mexico', 'Marshall Islands', 'North Macedonia', 'Mali', 'Malta', 'Myanmar', 'Montenegro', 'Mongolia',
               'Northern Mariana Islands', 'Mozambique', 'Mauritania', 'Montserrat', 'Martinique', 'Mauritius',
               'Malawi',
               'Malaysia', 'Mayotte', 'Namibia', 'New Caledonia', 'Niger', 'Norfolk Island', 'Nigeria', 'Nicaragua',
               'Niue',
               'Netherlands', 'Norway', 'Nepal', 'Nauru', 'New Zealand', 'Oman', 'Pakistan', 'Panama', 'Pitcairn',
               'Peru',
               'Philippines', 'Palau', 'Papua New Guinea', 'Poland', 'Puerto Rico',
               "Korea, Democratic People's Republic of", 'Portugal', 'Paraguay', 'Palestine, State of',
               'French Polynesia',
               'Qatar', 'Réunion', 'Romania', 'Russian Federation', 'Rwanda', 'Saudi Arabia', 'Sudan', 'Senegal',
               'Singapore', 'South Georgia and the South Sandwich Islands',
               'Saint Helena, Ascension and Tristan da Cunha',
               'Svalbard and Jan Mayen', 'Solomon Islands', 'Sierra Leone', 'El Salvador', 'San Marino', 'Somalia',
               'Saint Pierre and Miquelon', 'Serbia', 'South Sudan', 'Sao Tome and Principe', 'Suriname', 'Slovakia',
               'Slovenia', 'Sweden', 'Eswatini', 'Sint Maarten (Dutch part)', 'Seychelles', 'Syrian Arab Republic',
               'Turks and Caicos Islands', 'Chad', 'Togo', 'Thailand', 'Tajikistan', 'Tokelau', 'Turkmenistan',
               'Timor-Leste', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Türkiye', 'Tuvalu',
               'Taiwan, Province of China',
               'Tanzania, United Republic of', 'Uganda', 'Ukraine', 'United States Minor Outlying Islands', 'Uruguay',
               'United States', 'Uzbekistan', 'Holy See (Vatican City State)', 'Saint Vincent and the Grenadines',
               'Venezuela, Bolivarian Republic of', 'Virgin Islands, British', 'Virgin Islands, U.S.', 'Viet Nam',
               'Vanuatu', 'Wallis and Futuna', 'Samoa', 'Yemen', 'South Africa', 'Zambia', 'Zimbabwe']
        natio_entry = ttk.Combobox(create_profile_page, values=ctr)
        natio_entry.place(x=10, y=520, width=250)

        gender = tk.Label(create_profile_page, text="Homme ou Femme ?", fg='green', font=('Bold', 15))
        gender.place(x=300, y=280)

        profile_img = tk.Button(create_profile_page, image=human, bd=0, command=new_image)
        profile_img.place(x=300, y=80)

        AN = ['Homme', 'Femme']
        gender_entry = ttk.Combobox(create_profile_page, values=AN)
        gender_entry.place(x=300, y=330)

        larow_img = tk.Button(create_profile_page, image=left_arow, bd=0, command=go_back)
        larow_img.place(x=30, y=30)

        create_profile_page.pack(pady=30)
        create_profile_page.pack_propagate(False)
        create_profile_page.configure(width=600, height=600)


b = WelcomWindow()
a = admin()
b.welcom_page()

root.mainloop()
