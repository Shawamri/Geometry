from Figuren import Figur,Line,Point
class Koordinatensystem():
    def __init__(self,x,y,figurliste):
        self.x=abs(x)
        self.y=abs(y)
        self.figurliste=figurliste
    
    def get_all_figuren(self):
        return self.figurliste
    

    def fuegen(self,figur):
        if self.check_figur(figur):
            print("Die Figur "+figur.get_name()+":"+str([(p.x,p.y) for p in figur.get_points()])+" wurde erfolgreich ins Koordinatensystem eingefügt")
            self.figurliste.append(figur)
            return True
        else:
            print("Die Figur "+figur.get_name()+":"+str(figur.get_points()[0].x)+" passt nicht ins Koordinatensystem!")
            return False

    def loeschen(self,figur):
        if figur in self.figurliste[:]:
            self.figurliste.remove(figur)
            print("Die Figur "+figur.get_name()+":"+str([(p.x,p.y) for p in figur.get_points()])+" wurde erfolgreich gelöscht")
            return True
        else:
            try:
              print("Die Figur "+figur.get_name()+":"+str([(p.x,p.y) for p in figur.get_points()])+"  wurde nicht gefunden!!!")
              return False
            except:
                print("Die Figur "+figur.get_name()+":"+str([(p) for p in figur.get_points()])+"  wurde nicht gefunden!!!")
                return False

    def check_figur(self,figur):
        for point in figur.get_points():
            if not(point.x <=self.x) or not(point.x >=-1*(self.x)):
                return False
            if not(point.y <=self.y) or not (point.y >=-1*(self.y)):
                return False
            else:
                continue    
        return True

    #Wird nur über Kreise und Rechtecke überprüft und ohne Oberfläche zu berechnen
    def ueberlappen(self,figur1,figur2):
        #2 Rechtecke
        if figur1.get_name()=="Rechteck" and figur2.get_name()=="Rechteck":
            if figur1.get_umfang()>=figur2.get_umfang():
                for p in figur2.get_points():
                    if figur1.point_in_Rechteck(p):
                        #print(figur1.get_name()," and ",figur2.get_name()," überlappen sich")
                        return(figur1,figur2)
                        #return True
            else:
                for p in figur1.get_points():
                    if figur1.point_in_Rechteck(p):
                        #print(figur1.get_name()," and ",figur2.get_name()," überlappen sich")
                        return(figur1,figur2)
         #2Kreise
        elif figur1.get_name()=="Kreis" and figur2.get_name()=="Kreis":
            l=Line(figur1.get_mittelpunkt(),figur2.get_mittelpunkt())
            if l.get_length()>figur1.get_radius()+figur2.get_radius():
                return (figur1,figur2)
        #kreis und Rechteck
        elif figur1.get_name()=="Rechteck" and figur2.get_name()=="Kreis":
            x1=figur2.get_mittelpunkt().x
            y1=figur2.get_mittelpunkt().y
            points=figur1.get_points()
            nearest_x=points[0].x
            nearest_y=points[0].y
            for p in points:
                if abs(p.x-x1)<(nearest_x-x1):
                    nearest_x=p.x
                if abs(p.y-y1)<(nearest_y-y1):
                    nearest_y=p.y
            nearest_point=Point(nearest_x,nearest_y)
            if figur2.point_in_Kreis(nearest_point):
                #figur1.get_name()," and ",figur2.get_name()," überlappen sich"
                return (figur1,figur2)    
        #Rechteck und Kreis
        elif figur1.get_name()=="Kreis" and figur2.get_name()=="Rechteck":
            x1=figur1.get_mittelpunkt().x
            y1=figur1.get_mittelpunkt().y
            points=figur2.get_points()
            nearest_x=points[0].x
            nearest_y=points[0].y
            for p in points:
                if abs(p.x-x1)<(nearest_x-x1):
                    nearest_x=p.x
                if abs(p.y-y1)<(nearest_y-y1):
                    nearest_y=p.y
            nearest_point=Point(nearest_x,nearest_y)
            if figur1.point_in_Kreis(nearest_point):
                #figur1.get_name()," and ",figur2.get_name()," überlappen sich"
                return (figur1,figur2)
    #Andere Figuren
        else:
            return
    def check_all_uberlappungen(self):
        schachtel=[]
        for figur1 in self.figurliste:
            for figur2 in self.figurliste:
                if figur1 is figur2:
                    continue
                else:
                    schachtel.append(self.ueberlappen(figur1,figur2))
        return schachtel


