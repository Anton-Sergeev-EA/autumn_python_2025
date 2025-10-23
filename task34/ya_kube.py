import random
import uuid
import datetime
import json

from code.db import DICT_DEFENITION_WORD


class GameState:
    def __init__(self):
        self.game_key = None
        self.current_word = None
        self.display_word = []
        self.guessed_letters = set()
        self.score = 0
        self.players = []
        self.current_player = None
        self.timestamp = datetime.datetime.now().isoformat()

    def save(self):
        with open(f"save_{self.game_key}.json", "w") as f:
            json.dump(self.__dict__, f)

    def load(self, game_key):
        with open(f"save_{game_key}.json", "r") as f:
            data = json.load(f)
            self.__dict__.update(data)


class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.prizes = []

    def add_points(self, points):
        self.score += points

    def add_prize(self, prize):
        self.prizes.append(prize)

    def __str__(self):
        return f"Игрок: {self.name}, Очки: {self.score}"


class Game:
    def __init__(self):
        self.state = GameState()
        self.game_active = False

    def start_game(self):
        self.game_active = True
        self.state.game_key = self._generate_key()
        self.state.current_word = random.choice(list(DICT_DEFENITION_WORD.keys()))
        self.state.display_word = ['_'] * len(self.state.current_word)
        player_name = input("Введите имя игрока: ")
        self.state.players = [Player(player_name)]
        self.state.current_player = self.state.players[0]
        print(f"\nЗагаданное слово: {' '.join(self.state.display_word)}")
        print(f"Определение: {DICT_DEFENITION_WORD[self.state.current_word]}")
        self.game_loop()
    
    def game_loop(self):
        while self.game_active:
            letter = input(
                f"\nХод игрока {self.state.current_player.name}. Введите букву: ").strip().upper()
            
            if len(letter) != 1 or not letter.isalpha():
                print("Пожалуйста, введите одну букву!")
                continue
            
            if letter in self.state.guessed_letters:
                print("Эта буква уже была названа!")
                continue
            
            self.state.guessed_letters.add(letter)
            
            if letter in self.state.current_word:
                for i, char in enumerate(self.state.current_word):
                    if char == letter:
                        self.state.display_word[i] = letter
                self.state.current_player.add_points(10)
                print(f"Правильно! {' '.join(self.state.display_word)}")
            else:
                print(f"Такой буквы нет! {' '.join(self.state.display_word)}")
            
            if ''.join(self.state.display_word) == self.state.current_word:
                print(
                    f"\nПоздравляем! Вы угадали слово: {self.state.current_word}")
                print(f"Ваш счет: {self.state.current_player.score} очков")
                self.game_active = False
                self.end_game()
    
    def save_game(self):
        self.state.save()
        print("Игра сохранена!")
    
    def load_game(self):
        try:
            game_key = input("Введите ключ сохранения: ")
            self.state.load(game_key)
            print("\nИгра успешно загружена!")
            print(f"Текущее слово: {' '.join(self.state.display_word)}")
            print(f"Текущий счет: {self.state.current_player.score} очков")
            print(
                f"Уже названные буквы: {', '.join(self.state.guessed_letters)}")
            print(
                f"Определение: {DICT_DEFENITION_WORD[self.state.current_word]}")
            
            self.game_active = True
            self.game_loop()
        
        except FileNotFoundError:
            print("Файл сохранения не найден. Попробуйте снова.")
            self.load_game()
        
        except Exception as e:
            print(f"Ошибка при загрузке игры: {str(e)}")
            self.print_menu()
    
    def end_game(self):
        self.game_active = False
        print("Игра завершена.")
        self.state = GameState()
    
    def _generate_key(self) -> str:
        return str(uuid.uuid4())[:8]
    
    def print_menu(self):
        print("\nДобро пожаловать в игру 'Поле чудес'!")
        print("1. Начать новую игру")
        print("2. Загрузить сохраненную игру")
        print("3. Выйти из игры")
        choice = input("Выберите пункт меню: ")
        
        if choice == '1':
            self.start_game()
        elif choice == '2':
            self.load_game()
        elif choice == '3':
            print("До свидания!")
        else:
            print("Неверный выбор. Попробуйте снова.")
            self.print_menu()


class GameController:
    def __init__(self):
        self.game = Game()
    
    def run(self):
        try:
            self.game.print_menu()
        except KeyboardInterrupt:
            print("\nИгра прервана пользователем. До свидания!")


if __name__ == "__main__":
    controller = GameController()
    controller.run()
