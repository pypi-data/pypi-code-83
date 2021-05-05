class GameObject:

    class Material:
        def __init__(self):
            pass

        def init(self, name : str = "defoult", color : dict = [225, 225, 225]):
            return {"name": name, "color": color}
    
    class Transform:
        def __init__(self):
            self.position = {"x": 0, "y": 0}
            self.rotation = {"x": 0, "y": 0}
            self.scale = {"x": 1, "y": 1}
        
    class Collaider2D:
        def __init__(self):
            self.material = GameObject.Material.init("defoult")
            self.IsTrigger = False
            self.offset = {"x": 0, "y": 0}
            self.size  = {"x": 1, "y": 1}
        
        def __len__(self):
            return 1
    
    class Rigidbody:
        def __init__(self):
            self.Material = GameObject.Material.init(0)
            self.Mass = 1
            self.GravityScale = 1
            self.Constraits = {"x": False, "y": False, "z": False}
    
    def __init__(self):
        self.transform = self.Transform()
        self.collaider = None
        self.rightbody = None
    
    class Examles:
        def __init__(self):
            pass

        def get(name : str):
            if name == "owo":
                owl = GameObject()
                pl = GameObject()
                pl2 = GameObject()
                pl3 = GameObject()
                pl4 = GameObject()
                pl5 = GameObject()
                pl6 = GameObject()
                #Настройка owl
                #collaider
                owl.collaider = GameObject.Collaider2D()
                owl.collaider.offset = {"x": 0.7523813, "y": 0.6345024}
                owl.collaider.size = {"x": 52.87149, "y": 94.15009}
                #rightbody
                owl.rightbody = GameObject.Rigidbody()
                owl.rightbody.Mass = 5
                owl.rightbody.Constraits["z"] = True
                #Настройка pl
                tmp, tmp2, tmp3 = GameObject(), GameObject(), GameObject()
                tmp.collaider, tmp2.collaider, tmp3.collaider = GameObject().Collaider2D(), GameObject().Collaider2D(), GameObject().Collaider2D()
                tmp.collaider.offset = {"x": -7.713602, "y": 1.878332}
                tmp.collaider.size = {"x": 59.9723, "y": 16.06823}
                tmp2.collaider.IsTrigger = True
                tmp2.collaider.offset = {"x": -38.84869, "y": 0.6878853}
                tmp2.collaider.size = {"x": 4.67247, "y": 12.03056}
                tmp3.collaider.IsTrigger = True
                tmp3.collaider.offset = {"x": 24.26949, "y": 0.6878853}
                tmp3.collaider.size = {"x": 3.672638, "y": 12.03056}
                pl.collaider = [tmp, tmp2, tmp3]
                #Настройка pl2
                tmp.collaider.offset = {"x": -14.09399, "y": 4.494222}
                tmp.collaider.size = {"x": 40.21371, "y": 15.94874}
                tmp2.collaider.IsTrigger = True
                tmp2.collaider.offset = {"x": -34.3532, "y": 2.370476}
                tmp2.collaider.size = {"x": 3.49411, "y": 12.18193}
                tmp3.collaider.IsTrigger = True
                tmp3.collaider.offset = {"x": 5.5271, "y": 2.370476}
                tmp3.collaider.size = {"x": 4.283447, "y": 12.18193}
                pl2.collaider = [tmp, tmp2, tmp3]
                #Настройка pl3
                tmp.collaider.offset = {"x": -4.720787, "y": 4.577762}
                tmp.collaider.size = {"x": 59.15073, "y": 15.59875}
                tmp2.collaider.IsTrigger = True
                tmp2.collaider.offset = {"x": -4.935608, "y": 2.765564}
                tmp2.collaider.size = {"x": 64.69803, "y": 12.97211}
                pl3.collaider = [tmp, tmp2]
                #Настройка pl4
                tmp.collaider.offset = {"x": -12.44333, "y": 1.878332}
                tmp.collaider.size = {"x": 30.67053, "y": 16.06823}
                tmp2.collaider.IsTrigger = True
                tmp2.collaider.offset = {"x": -12.83261, "y": 0.3962479}
                tmp2.collaider.size = {"x": 36.26862, "y": 12.97173}
                pl4.collaider = [tmp, tmp2]
                #Настройка pl5
                tmp.collaider.offset = {"x": -3.059146, "y": -4.675931}
                tmp.collaider.size = {"x": 56.36278, "y": 15.49829}
                tmp2.collaider.IsTrigger = True
                tmp2.collaider.offset = {"x": -2.912354, "y": -6.509735}
                tmp2.collaider.size = {"x": 61.97784, "y": 12.03293}
                pl5.collaider = [tmp, tmp2]
                #Настройка pl6
                tmp.collaider.offset = {"x": -21.7598, "y": 4.681614}
                tmp.collaider.size = {"x": 25.05128, "y": 15.68828}
                tmp2.collaider.IsTrigger = True
                tmp2.collaider.offset = {"x": -21.73879, "y": 3.085426}
                tmp2.collaider.size = {"x": 30.04082, "y": 12.4482}
                pl6.collaider = [tmp, tmp2]


                return owl, pl, pl2, pl3, pl4, pl5, pl6
            else:
                print("Incorrect name of Examle")

def help(lan : str = "defoult"):
    if lan.upper() in ["RU", "RUSSIAN"]:
        print("""Привет, разработчик!

Это руководство для тебя
У этого модуля есть пример:
{
import Unity
owl, pl1, pl2, pl3, pl4, pl5, pl6 = Unity.GameObject.Examples.get("owo")
} Вы можете использовать его""")
    else:
        print("""Hi developer!

This is guide for you
It module had a Example:
{
import Unity
owl, pl1, pl2, pl3, pl4, pl5, pl6 = Unity.GameObject.Examles.get("owo")
} You can use it""")