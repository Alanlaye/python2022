class Emploee():
    def __init__(self,f_n,l_n,pay=' '):
        self.f_n = f_n
        self.l_n = l_n
        self.pay = pay
    def give_raise(self,rise=5000):
        self.rise = rise
        print(rise)
    
emploee = Emploee('aa','bb')
emploee.give_raise()
