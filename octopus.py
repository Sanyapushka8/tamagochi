from tamagochi import Tamagochi

class Octopus(Tamagochi):
    def __init__(self, name: str):
        super().__init__(name)
        self.view = f"""          
          ,---.
         ( @ @ )
          ).-.(
         '/|||\`
           '|`   
       """
class Dog(Tamagochi):
    def __init__(self, name):
        super().__init__(name)
        self.view = f""" 
                            __
     ,                    ," e`--o
    ((                   (  | __,'
     \.\~----------------' \_;/
      (                      /
     /) ._______________.  )
    (( (               (( (
     ``-'               ``-'"""

    def rais(self, level):
            self._lv += level
            if self._lv == 2:
                self.view = f"""   
          ____
         / |   |\.
  _____/ @ |   | \.
 |> . .    |   |  \.
  \  .     |||||     \________________________
   |||||||\                                    )
            \                                 |
             \                                |
               \                             /
                |   ____________------\     |
                |  | |                ||    /
                |  | |                ||  |
                |  | |                ||  |
                |  | |                ||  |  
               (__/_/                ((__/"""
            elif self._lv >= 3:
                self.view = f"""
       __,-----._                       ,-. 
     ,'   ,-.    \`---.          ,-----<._/ 
    (,.-. o:.`    )),"\.\-._    ,'         `. 
   ('"-` .\       \`:_ )\  `-;'-._          \. 
  ,,-.    \` ;  :  \( `-'     ) -._     :   `: 
 (    \ `._\.\ ` ;             ;    `    :    ) 
  \`.  `-.    __   ,         /  \        ;, ( 
   `.`-.___--'  `-          /    ;     | :   | 
     `-' `-.`--._          '           ;     | 
           (`--._`.                ;   /\    | 
            \     '                \  ,  )   : 
            |  `--::----            \.   ;  ;| 
            \    .__,-      (        )   :  :| 
             \    : `------; \      |    |   ; 
              \   :       / , )     |    |  ( 
               \   \      `-^-|     |   / , ,\ .
                )  )          | -^- ;   `-^-^' 
             _,' _ ;          |    | 
            / , , ,'         /---. : 
            `-^-^'          (  :  :,' 
                             `-^--' """

if __name__ == "__main__":
    pet_type = input("Выберите питомца (1 - Осьминог, 2 - Собака): ")
    name = input("Введите имя: ")

    if pet_type == "1":
        pet = Octopus(name)
    elif pet_type == "2":
        pet = Dog(name)
    else:
        print("Неверный выбор. Создан осьминог по умолчанию.")
        pet = Octopus(name)
    print(pet)
    action = input("Выберите действие:\nq - выход, b - бить, h - лечить, f - кормить, x - повысить уровень\n")
    while True:
        if action == 'b':
            hit = int(input("Введите урон: "))
            pet.bit(hit)
            print(pet)
        elif action == "h":
            hp = int(input("Введите здоровье: "))
            pet.heal(hp)
            print(pet)
        elif action == "f":
            food = int(input("Введите еду: "))
            pet.feed(food)
            print(pet)
        elif action == "x":
            level = +1
            pet.rais(level)
            print(pet)
        elif action == "q":
            print("Спасибо за игру!")
            break
        else:
            print("Неверный ввод")
        if not pet.is_alive:
            print(f"\n{pet.name} умер... Игра окончена.")
            break
        action = input("Выберите действие:\nq - выход, b - бить, h - лечить, f - кормить, x - повысить уровень\n")
