from math import pi, sqrt
class Point():
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def get_points(self):
        return [Point(self.x,self.y)]
    def get_name(self):
        return "Point("+str(self.x)+","+str(self.y)+")"
    def get_flaeche(self):
        return 0
    def get_umfang(self):
        return 0

class Figur():
    def __init__(self,name):
        self.name=name
    def get_name(self):
        return self.name
class Line(Figur):
    def __init__(self,name,p1,p2):
        super().__init__(name)
        self.p1=p1
        self.p2=p2
    def get_length(self):
        return sqrt((self.p2.x-self.p1.x)**2+(self.p2.y-self.p2.y)**2)
    def  get_umfang(self):
        return self.get_length()
    def get_flaeche(self):
        return 0
    def get_points(self):
        return [self.p1,self.p2]

class Dreieck(Figur):#um die vierecke zu vereifachen
    #p1->p2->p3->p1
    def __init__(self, name,p1,p2,p3):
        super().__init__(name)
        self.p1=p1
        self.p2=p2
        self.p3=p3
    
    def get_points(self):
        return [self.p1,self.p2,self.p3]

    def get_umfang(self):
        l1=Line("l1",self.p1,self.p2)
        l2=Line("l2",self.p2,self.p3)
        l3=Line("l3",self.p3,self.p1)
        return l1.get_length()+l2.get_length()+l3.get_length()

    def get_flaeche(self):
        #mit Herons Formel
        s=self.get_umfang()/2
        l1=Line("l1",self.p1,self.p2).get_length()
        l2=Line("l2",self.p2,self.p3).get_length()
        l3=Line("l3",self.p3,self.p1).get_length()
        return sqrt(s*(s-l1)*(s-l2)*(s-l3))


class Vierecke(Figur):
    #darunter sind Rechtecke,Quadrate,Parallelogramme,etc
    #p1->p2->p3->p4-->p1
    def __init__(self, name,p1,p2,p3,p4):
        super().__init__(name)
        self.p1=p1
        self.p2=p2
        self.p3=p3
        self.p4=p4
    def get_points(self):
        return [self.p1,self.p2,self.p3,self.p4]
        #Das Viereck in 2 Dreiecke teilen:
        #p1->p2->p3-->p1 & p3->p4-p1-->p3
    def get_flaeche(self):
        d1=Dreieck("Dreieck",self.p1,self.p2,self.p3)
        d2=Dreieck("Dreieck",self.p3,self.p4,self.p1)
        return d1.get_flaeche()+d2.get_flaeche()

    def get_umfang(self):
        d1=Dreieck("Dreieck",self.p1,self.p2,self.p3)
        d2=Dreieck("Dreieck",self.p3,self.p4,self.p1)
        return d1.get_umfang()+d2.get_umfang()

class Rechtecke(Vierecke):
    #p1->p2->p3->p4-->p1
    def __init__(self, name, p1, p2, p3, p4):
        super().__init__(name, p1, p2, p3, p4)

    def point_in_Rechteck(self,p):
        min_x=min(self.p1.x,self.p2.x,self.p3.x,self.p4.x)
        max_x=max(self.p1.x,self.p2.x,self.p3.x,self.p4.x)
        min_y=min(self.p1.y,self.p2.y,self.p3.y,self.p4.y)
        max_y=min(self.p1.y,self.p2.y,self.p3.y,self.p4.y)
        if p.x>= min_x and  p.x<=max_x:
            return p.y<=max_y and p.y>=min_y
        return False

    def get_flaeche(self):
        l1=Line("l1",self.p1,self.p2)
        l2=Line("l2",self.p2,self.p3)
        return (l1.get_length())*(l2.get_length())
    
    def get_umfang(self):
        l1=Line("l1",self.p1,self.p2)
        l2=Line("l2",self.p2,self.p3)
        return (2*l1.get_length())+(2*l2.get_length())

class Kreis(Figur):
    #p1:=Mittelpunk,r=Radius
    def __init__(self, name,p1,r):
        super().__init__(name)
        self.p1=p1
        self.r=r
    def get_radius(self):
        return self.r
    def get_mittelpunkt(self):
        return self.p1
    
    def get_points(self):
        return [self.p1]

    def get_flaeche(self):
        return pi*self.r**2
    
    def get_umfang(self):
        return 2*pi*self.r
    def point_in_Kreis(self,p):
        l=Line("Line",self.p1,p)
        return l.get_length()<=self.r

#nicht vollständig!
class Polygon(Figur):
    #[p1->p2->...->pn],n>=5
    def __init__(self, name,points_list):
        super().__init__(name)
        self.points_list=points_list
    
    def get_points(self):
        return self.points_list

    def get_umfang(self):
        l0=Line("l0",self.points_list[0],self.points_list[-1])
        umfang=l0.get_length()
        for i in range(len(self.points_list)-1):
            l=Line("l",self.points_list[i],self.points_list[i+1])
            umfang +=l.get_length()
        return umfang

    def get_flaeche(self):
        #gaußschen Trapezformel für einfache Polygons
        n=len(self.points_list)
        a=0
        for i in range(n-1):
            a+=abs((self.points_list[i].y+self.points_list[(i+1)%n].y)*(self.points_list[i].x+self.points_list[(i+1)%n].x))/2
#https://www.geeksforgeeks.org/convex-hull-set-2-graham-scan/ == für die Konvex Hülle um die überlappung später zu finden
#die Überprüfung auf überlappung wird hier ignoriert.
#es gibt übrigens auch eine fertige Bibliothek: "from shapely.geometry import Point, Polygon"

        


    
    


    

    




    
