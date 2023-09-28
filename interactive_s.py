import cmd
from colorama import Fore,init
#Bu bir shell proqramidir l;laskda;lskdakds;askda;dlak;dakd;
class Turtle(cmd.Cmd):

    intro = Fore.GREEN + 'Xos gelmishsiniz!'
    prompt = Fore.YELLOW + 'emr>'

    def do_info(self,arg):
        print(Fore.CYAN + "Bu bir interaktiv shelldir")

    def do_greet(self,arg):

        print(Fore.YELLOW+ "Salam Dunya!")

    def do_exit(self,arg):

        print('exited')
if __name__ == "__main__":
    Turtle().cmdloop()
