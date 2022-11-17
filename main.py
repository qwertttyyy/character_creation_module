from random import randint

from graphic_arts.start_game_banner import run_screensaver


def attack(char_name: str, char_class: str) -> str:
    """Атака по противнику.
    Герой, в зависимости от класса, наносит разный урон.
    Возвращает сообщение с кол-вом нанесённого урона.
    """
    damage: int = 5
    if char_class == 'warrior':
        damage += randint(3, 5)
        return f'{char_name} нанёс урон противнику равный {damage}'
    if char_class == 'mage':
        damage += randint(5, 10)
        return f'{char_name} нанёс урон противнику равный {damage}'
    if char_class == 'healer':
        damage += randint(-3, -1)
        return f'{char_name} нанёс урон противнику равный {damage}'
    return f'{char_name} не нанёс урон'


def defence(char_name: str, char_class: str) -> str:
    """Блокируется урона противника.
    Герой блокирует урон от противника по разному в зависимости от класса.
    Возвращает сообщение о блокированом уроне.
    """
    blocked_damage: int = 10
    if char_class == 'warrior':
        blocked_damage += randint(5, 10)
        return f'{char_name} блокировал {blocked_damage} урона'
    if char_class == 'mage':
        blocked_damage += randint(-2, 2)
        return f'{char_name} блокировал {blocked_damage} урона'
    if char_class == 'healer':
        blocked_damage += randint(2, 5)
        return f'{char_name} блокировал {blocked_damage} урона'
    return f'{char_name} не блокировал урон'


def special(char_name: str, char_class: str) -> str:
    """Использование спеуиального умения.
    Применение различных умений разных классов.
    Возвращает сообщение о применении спецприёма.
    """
    skill: int = 0
    if char_class == 'warrior':
        skill = 80 + 25
        return (f'{char_name} применил специальное умение '
                f'«Выносливость {skill}»')
    if char_class == 'mage':
        skill = 5 + 40
        return f'{char_name} применил специальное умение «Атака {skill}»'
    if char_class == 'healer':
        skill = 10 + 30
        return f'{char_name} применил специальное умение «Защита {skill}»'
    return f'{char_name} не применил специальное умение'


def start_training(char_name: str, char_class: str) -> str:
    """Тренеровка для игрока.
    Предлагает использовать разные навыки.
    Выводит результаты работы функций attack, defence и special.
    """
    if char_class == 'warrior':
        print(f'{char_name}, ты Воитель — отличный боец ближнего боя.')
    if char_class == 'mage':
        print(f'{char_name}, ты Маг — превосходный укротитель стихий.')
    if char_class == 'healer':
        print(f'{char_name}, ты Лекарь — чародей, способный исцелять раны.')
    print('Потренируйся управлять своими навыками.')
    print(
        'Введи одну из команд: '
        'attack — чтобы атаковать противника, '
        'defence — чтобы блокировать атаку противника или '
        'special — чтобы использовать свою суперсилу. ')
    print('Если не хочешь тренироваться, введи команду skip.')
    cmd: str = ''
    while cmd != 'skip':
        cmd = input('Введи команду: ')
        if cmd == 'attack':
            print(attack(char_name, char_class))
        if cmd == 'defence':
            print(defence(char_name, char_class))
        if cmd == 'special':
            print(special(char_name, char_class))
    return 'Тренировка окончена.'


def choice_char_class() -> str:
    """Выбор героя.
    Предлагает выбрать героия из списка: Воитель, Маг, Лекарь.
    """
    approve_choice: str = ''
    char_class: str = ''
    while approve_choice != 'y':
        char_class = input(
            'Введи название персонажа, за которого хочешь играть:'
            'Воитель — warrior, Маг — mage, Лекарь — healer: ')
        if char_class == 'warrior':
            print('Воитель — дерзкий воин ближнего боя. '
                  'Сильный, выносливый и отважный.')
        if char_class == 'mage':
            print('Маг — находчивый воин дальнего боя. '
                  'Обладает высоким интеллектом.')
        if char_class == 'healer':
            print('Лекарь — могущественный заклинатель. '
                  'Черпает силы из природы, веры и духов.')
        approve_choice = input(
            'Нажми (Y), чтобы подтвердить выбор, '
            'или любую другую кнопку,'
            'чтобы выбрать другого персонажа ').lower()
    return char_class


if __name__ == '__main__':
    run_screensaver()
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name: str = input('...назови себя: ')
    print(f'Здравствуй, {char_name}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    char_class: str = choice_char_class()
    print(start_training(char_name, char_class))
