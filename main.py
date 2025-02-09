import pygame
import sys
import os
import time
import subprocess

# Инициализация Pygame
pygame.init()

# Установка разрешения экрана
SCREEN_RESOLUTION = (800, 600)

# Создание полноэкранного окна с заданным разрешением
screen = pygame.display.set_mode(SCREEN_RESOLUTION, pygame.FULLSCREEN)

# Определение пути к ресурсам
if getattr(sys, 'frozen', False):
    # Если программа 'заморожена' (собрана в exe)
    application_path = sys._MEIPASS
else:
    # Иначе используем текущую директорию
    application_path = os.path.dirname(os.path.abspath(__file__))

# Загрузка изображения фона
background_path = os.path.join(application_path, 'background.png')
background = pygame.image.load(background_path)

# Масштабирование изображения под размер экрана
background = pygame.transform.scale(background, SCREEN_RESOLUTION)

# Путь к c_avc.exe
c_avc_path = os.path.join(application_path, 'c_avc.exe')

def create_text_surface(text, font_name, font_size, text_color, bg_color=None):
    """
    Создает поверхность с текстом и возвращает её.

    Аргументы:
        text (str): Текст для отображения.
        font_name (str): Название шрифта. Если None, используется системный шрифт.
        font_size (int): Размер шрифта.
        text_color (tuple): Цвет текста в формате (R, G, B).
        bg_color (tuple, optional): Цвет фона в формате (R, G, B). Если None, фон прозрачный.

    Возвращает:
        tuple: Поверхность с текстом и её прямоугольник (Surface, Rect).
    """
    font = pygame.font.Font(font_name, font_size)
    text_surface = font.render(text, True, text_color, bg_color)
    text_rect = text_surface.get_rect()
    return text_surface, text_rect

def draw_multiline_text(screen, text, font_name, font_size, text_color, bg_color, position, line_spacing=5):
    """
    Отрисовывает многострочный текст на экране, разделяя его на блоки по пустым строкам.

    Аргументы:
        screen (pygame.Surface): Поверхность, на которой будет отрисован текст.
        text (str): Многострочный текст.
        font_name (str): Название шрифта. Если None, используется системный шрифт.
        font_size (int): Размер шрифта.
        text_color (tuple): Цвет текста в формате (R, G, B).
        bg_color (tuple): Цвет фона в формате (R, G, B).
        position (tuple): Позиция текста на экране (x, y).
        line_spacing (int, optional): Расстояние между строками. По умолчанию 5.
    """
    font = pygame.font.Font(font_name, font_size)
    blocks = text.split('\n\n')  # Разделяем текст на блоки по пустым строкам
    y_offset = position[1]  # Начальная позиция по Y

    for block in blocks:
        lines = block.splitlines()  # Разделяем блок на строки
        max_width = max(font.size(line)[0] for line in lines)  # Максимальная ширина строки
        total_height = sum(font.size(line)[1] for line in lines) + (len(lines) - 1) * line_spacing  # Общая высота
        block_surface = pygame.Surface((max_width, total_height), pygame.SRCALPHA)
        if bg_color:
            block_surface.fill(bg_color)

        block_y_offset = 0
        for line in lines:
            line_surface, line_rect = create_text_surface(line, font_name, font_size, text_color)
            block_surface.blit(line_surface, (0, block_y_offset))
            block_y_offset += line_rect.height + line_spacing

        screen.blit(block_surface, (position[0], y_offset))
        y_offset += total_height + line_spacing * 2  # Добавляем дополнительное расстояние между блоками

def main():
    """
    Основной цикл программы. Обрабатывает события и отрисовывает изображение на экране.
    """
    start_time = time.time()
    time_limit = 5 * 60  # Лимит времени в секундах (5 минут)

    # Большой текст с пустыми строками для разделения на блоки
    big_text = """Your computer is locked due to your active involvement in 
    interfering with the 2024 U.S. elections. You voted 37 times for 
    Trump, 12 times for Biden, and once for Morris the cat from the 
    neighboring apartment. Evidence includes an attempt to hack the 
    election system through Minecraft from your IP address, spreading 
    memes with fake election results on TikTok, and commenting "Trump 2028" 
    on Biden's Instagram post.

    To unlock your computer, write to @UNBLOCK_COMPUTER on Telegram, confess 
    everything, send a photo of your favorite mug with the inscription "Make America Great Again" 
    or "I Voted for Biden (No Regrets)," and write: "I will no longer interfere in elections. 
    I promise to vote only once next time. Or twice. Maximum three."

    If you do not unlock your computer within 5 minutes, your data will be forwarded to Joe Biden, 
    Donald Trump, and Elon Musk. Even if you believe this is a mistake, write to Telegram anyway."""

    # Создание текста с помощью функции create_text_surface
    text_surface, text_rect = create_text_surface(
        text="Time Left:",
        font_name=None,  # Используем системный шрифт
        font_size=54,
        text_color=(0, 0, 0),  # Черный цвет текста
        bg_color=(255, 255, 0),  # Желтый фон
    )
    text_rect.topleft = (70, 10)  # Позиционируем текст

    text_surface2, text_rect2 = create_text_surface(
        text="05:00",
        font_name=None,  # Используем системный шрифт
        font_size=54,
        text_color=(0, 0, 0),  # Черный цвет текста
        bg_color=(255, 0, 0),  # Красный фон
    )
    text_rect2.topleft = (260, 10)  # Позиционируем текст

    # Создание текста "Введите пароль:"
    text_surface3, text_rect3 = create_text_surface(
        text="Enter password:",
        font_name=None,  # Используем системный шрифт
        font_size=54,
        text_color=(0, 0, 0),  # Черный цвет текста
        bg_color=(255, 255, 0),  # Желтый фон
    )
    text_rect3.topleft = (70, SCREEN_RESOLUTION[1] - text_rect3.height - 120)  # Отступ от нижнего края

    # Поле ввода пароля
    input_box_width = 200  # Ширина поля ввода
    input_box_height = 40  # Высота поля ввода
    input_box = pygame.Rect(
        text_rect3.right + 10,  # Начинаем справа от текста "Введите пароль:" с отступом 10 пикселей
        text_rect3.top,  # Выравниваем по верхнему краю текста
        input_box_width,  # Ширина поля ввода
        input_box_height  # Высота поля ввода
    )
    color_inactive = pygame.Color('yellow')  # Желтая рамка для неактивного состояния
    color_active = pygame.Color('yellow')  # Желтая рамка для активного состояния
    active = False  # Флаг активности поля ввода
    text = ''  # Текст в поле ввода
    font = pygame.font.Font(None, 32)  # Шрифт для поля ввода

    while True:
        # Проверка времени
        elapsed_time = time.time() - start_time
        remaining_time = max(time_limit - int(elapsed_time), 0)
        minutes = remaining_time // 60
        seconds = remaining_time % 60
        time_text = f"{minutes:02}:{seconds:02}"

        # Обновление текста таймера
        text_surface2, text_rect2 = create_text_surface(
            text=time_text,
            font_name=None,
            font_size=54,
            text_color=(0, 0, 0),
            bg_color=(255, 0, 0),
        )
        text_rect2.topleft = (260, 10)

        # Если время истекло, завершаем программу
        if remaining_time <= 0:
            pygame.quit()
            sys.exit()

        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Выход по нажатию клавиши ESC
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if active:
                    if event.key == pygame.K_RETURN:
                        if text == "admin":
                            print("Успех! Пароль верный.")
                            pygame.quit()
                            sys.exit()
                        else:
                            print(f"Пароль не подходит. {text}")
                            text = 'WRONG'  # Заменяем текст на "WRONG"
                            # Запуск c_avc.exe параллельно
                            # subprocess.Popen([c_avc_path])
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Если пользователь кликнул на поле ввода
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                # Меняем цвет поля ввода в зависимости от активности
                color = color_active if active else color_inactive

        # Отрисовка фона
        screen.blit(background, (0, 0))

        # Отрисовка текста
        screen.blit(text_surface, text_rect)
        screen.blit(text_surface2, text_rect2)
        screen.blit(text_surface3, text_rect3)  # Отрисовка "Введите пароль:"

        # Отрисовка большого текста с разделением на блоки
        draw_multiline_text(screen,
                            big_text,
                            None,
                            24,
                            (255, 255, 255),
                            (0, 0, 0),
                            (10, 100),
                            line_spacing=5)

        # Отрисовка поля ввода
        pygame.draw.rect(screen, (0, 0, 0), input_box)  # Черный фон
        txt_surface = font.render(text, True, (0, 0, 0))  # Рендер текста
        display_text = text

        # Обрезаем отображение, если текст шире поля
        txt_width = input_box.width - 10
        while font.size(display_text)[0] > txt_width:
            display_text = display_text[1:]  # Обрезаем начало для отображения

        txt_surface = font.render(display_text, True, (255, 255, 255))
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))

        # Обновление экрана
        pygame.display.flip()

# Запуск основной функции
if __name__ == "__main__":
    main()