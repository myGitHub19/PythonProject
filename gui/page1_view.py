import tkinter as tk
from popup_view import PopupView
from tkinter import messagebox
class Page1View(tk.Frame):
    """ Page 1 """

    def __init__(self, parent):
        """ Initialize Page 1 """
        print('page 1')
        tk.Frame.__init__(self, parent, width=800, height=800)

        self._parent = parent

        self._create_widgets()

    def _create_widgets(self):
        """ Creates the widgets for Page 1 """
        #self._entry_name = tk.Entry(self)
        self._list = tk.Listbox(self)
        self._list.grid(row=0,column=1)

        DeleteBtn = tk.Button(self,text='Delete',command=self._delete_callback)
        UpdateBtn = tk.Button(self,text='Update',command=self._update_callback)
        CreateBtn = tk.Button(self,text='Create',command=self._create_callback)

        DeleteBtn.grid(row=1,column=1)
        UpdateBtn.grid(row=2,column=1)
        CreateBtn.grid(row=3,column=1)
        #self._entry_name.grid(row=1,column=1)

    def _delete_callback(self):
        selection = self._list.get(self._list.curselection())
        if messagebox.askyesno('Verify', 'Really delete?'):
            # this is where delete api is
            pass

    def _update_callback(self):
        selection = self._list.get(self._list.curselection())
        # get selection stuff from api call and pass into popup
        popup_win = tk.Toplevel()
        popup = PopupView(popup_win,)

    def _create_callback(self):
        popup_win = tk.Toplevel()
        popup = PopupView(popup_win)
        #popup.tkraise(self._parent)
