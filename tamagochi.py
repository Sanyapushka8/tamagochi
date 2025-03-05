from xml.etree.ElementPath import xpath_tokenizer


class Tamagochi:
    def __init__(self, name:str):
        self.name = name
        self._hp = 100
        self._hunger = 100
        self._lv = 1
        self.view = ""
        self.is_alive = True

    def bit(self, hit):
        self._hp = max(0, self._hp - hit)
        self._hunger -= 5
        if self._hp <= 0 or self._hunger >= 101:
            self.is_alive = False

    def heal(self, points):
        self._hp = min(100, self._hp + points)
        print(f"{self.name} полечился!")
        if self._hp <= 0 or self._hunger >= 101:
            self.is_alive = False

    def feed(self, food):
        self._hunger = max(0, self._hunger + food)
        print(f"{self.name} покормлен!")
        if self._hp <= 0 or self._hunger >= 101:
            self.is_alive = False

    def rais(self, level):
        self._lv += level
        if self._lv == 2:
            self.view = f"""
          ,'""`.
         / _  _ \.
         |(@)(@)|
         )  __  (
        /,'))((`.\.
       (( ((  )) ))     
        `\ `)(' /'"""
        elif self._lv >= 3:
            self.view = f"""             
                        _,--._
                      ,'      `.
              |\     / ,-.  ,-. \     /|
              )o),/ ( ( o )( o ) ) \.(o(
             /o/// /|  `-'  `-'  |\ \.\.\.
            / / |\ \(   .    ,   )/ /| \ \.
            | | \o`-/    `\/'    \-'o/ | |
            \ \  `,'              `.'  / /
         \.  \ `-'  ,'|   /\   |`.  `-' /  ,/
          \`. `.__,' /   /  \   \ `.__,' ,'/
           \o\     ,'  ,'    `.  `.     /o/
            \o`---'  ,'        `.  `---'o/
             `.____,'            `.____,'"""



    def __str__(self):
        return self.view + "\n" +  f"Имя {self.name}, HP: {self._hp}, Голод: {self._hunger}, Уровень: {self._lv}"