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



if __name__ == "__main__":
    name = input("Введите имя: ")
    octo = Octopus(name)
    print(octo)
    action = input("Выберите действие:\nq - выход, b - бить, h - лечить, f - кормить, x - повысить уровень\n")
    while action:
        if action == 'b':
            hit = int(input("Введите урон: "))
            octo.bit(hit)
            print(octo)
        elif action == "h":
            hp = int(input("Введите здоровье: "))
            octo.heal(hp)
            print(octo)
        elif action == "f":
            food = int(input("Введите еду: "))
            octo.feed(food)
            print(octo)
        elif action == "x":
            level = +1
            octo.rais(level)
            print(octo)
        elif action == "q":
            print("Спасибо за игру!")
            break
        else:
            print("Неверный ввод")
        if not octo.is_alive:
            print(f"\n{octo.name} умер... Игра окончена.")
            break
        action = input("Выберите действие:\nq - выход, b - бить, h - лечить, f - кормить, x - повысить уровень\n")
