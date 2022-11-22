from cmath import sqrt

from numpy import double
import Koordinatensystem as ks
import Figuren as f
my_ks=ks.Koordinatensystem(100,100,[])
print("###########Koordinatensystem-Test###########\n")
print("Koordinatensystem Wird erstellt mit den X,Y-Achsen: \nX= %s"%my_ks.x," Y= %s"%my_ks.y)
f0=f.Point(101,101)
f1=f.Dreieck("Dreieck",f.Point(0,0),f.Point(2,2),f.Point(4,0))
f2=f.Vierecke("Viereck",f.Point(0,0),f.Point(2,2),f.Point(5,4),f.Point(1,1))
f3=f.Rechtecke("Rechteck",f.Point(0,0),f.Point(0,4),f.Point(4,4),f.Point(4,0))
f4=f.Kreis("Kreis",f.Point(3,3),4)
f5=f.Polygon("Polygon",[f.Point(300,5),f.Point(4,2),f.Point(5,5),f.Point(7,0),f.Point(1,2),f.Point(0,0)])
f6=f.Line("Line",f.Point(-10,-10),f.Point(20,20))
figuren=[f0,f1,f2,f3,f4,f5]

def flaeche_test():
    for fg in figuren:
        print(fg.get_name()+": "+str(fg.get_flaeche()))
def umfang_test():
    for fg in figuren:
        print(fg.get_name()+": "+str(fg.get_umfang()))

def fügen_test():
    for f in figuren:
        my_ks.fuegen(f)

def ueberlappen_test():
   for x in my_ks.check_all_uberlappungen():
    if not(x is None):
        str1=x[0].get_name()+": "
        str2=x[1].get_name()+": "
        for p in x[0].get_points():
            str1+="("+str(p.x)+","+str(p.y)+"),"
        for p in x[1].get_points():
            str2+="("+str(p.x)+","+str(p.y)+")," 
        print ("Überlappung: "+str1+" Und "+str2)
     
def loeschen_test():
    for fg in figuren:
        if len(fg.get_points())>=4:
            my_ks.loeschen(fg)
    new_figur=f.Kreis("Kreis",(4,4),5)
    my_ks.loeschen(new_figur)

print("\n###########Einfügen-Test###########\n")
fügen_test()
print("\n###########Fläche Berechnen-Test###########\n")
flaeche_test()#alle auf 0??
print("\n###########Umfang Berechnen-Test###########\n")
umfang_test()
print("\n###########Überprüfung-Test###########\n")
ueberlappen_test()
print("\n###########Löschen-Test###########\n")
loeschen_test()
