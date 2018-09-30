import os

print('Добро пожаловать в программу создания web-проекта.')
print('Эта программа сгенерит базовую структуру проекта: папку с именем проекта, index.html файл, подпапки со скриптами css и js.')

path = os.getcwd()
print("Текущая рабочая директория %s" % path)

while 1:
    try:
        key = int(input("Введите 1 чтобы продолжить в этой директории, введите 2, чтобы задать другой адрес или 3 чтобы выйти из программы: \n"))
        if key != 1 and key != 2 and key !=3:
            key = int(input("Неверное значение. Введите заново:"))

        if key == 1:

            while 1:
                try:
                    path = input('Введите имя проекта: ')
                    os.mkdir(path)
                except OSError:
                    print("Создать директорию %s не удалось, такое имя уже существует." % path)

                else:
                    print("Успешно создана директория %s " % path)
                    now_path = os.getcwd()
                    final_path = now_path + "\\" + path + "\\" #создаем строку с адресом для перехода
                    os.chdir(final_path)
                    head_path = os.getcwd()                         # запоминаем путь к папке проекта
                    print("Текущая рабочая директория %s" % head_path)

                    f = open('index.html', 'tw', encoding='utf-8') # создаем html файл
                    f.write('<!DOCTYPE html> \n')
                    f.write('<html lang="en"> \n')
                    f.write('<head> \n')
                    f.write('  <meta charset="UTF-8"> \n')
                    f.write('  <title>Title</title> \n')
                    f.write('  <link rel="stylesheet" href="css/style.css"/> \n')
                    f.write('</head> \n')
                    f.write('<body> \n')
                    f.write('  <div class="content"> \n')
                    f.write('   <h1>Hello! I am ready for edit! :)</h1> \n')
                    f.write('  </div> \n')
                    f.write('  <script src="js/app.js"></script> \n')
                    f.write('</body> \n')
                    f.write('</html> \n')
                    f.close()

                    os.mkdir('js')                             # создаем каталог js и файл js-скрипта в нем
                    now_path = os.getcwd()
                    final_path = now_path + "\\" + 'js' + "\\"  # создаем строку с адресом для перехода
                    os.chdir(final_path)
                    f = open('script.js', 'tw', encoding='utf-8')
                    f.write('/* this source generate automatically */')
                    f.close()

                    os.chdir(head_path)
                    os.mkdir('css')                            # создаем каталог css и файл стиля в нем
                    now_path = os.getcwd()
                    final_path = now_path + "\\" + 'css' + "\\"  # создаем строку с адресом для перехода
                    os.chdir(final_path)
                    f = open('style.css', 'tw', encoding='utf-8')
                    f.write('/* this source generate automatically */ \n \n')
                    f.write('html { \n \n')
                    f.write('} \n \n')
                    f.write('body { \n \n')
                    f.write('} \n \n')
                    f.write('.content { \n \n')
                    f.write('} \n \n')
                    f.write('.content h1 { \n \n')
                    f.write('}')
                    f.close()

                    print('Проект успешно создан! Можно приступать к работе.')

                    break

        elif key == 2:

            while 1:
                try:
                    newDir = input('Введите адрес новой директории, где вы хотите создать проект:')
                    os.chdir(newDir)
                except FileNotFoundError:
                    print('Путь указан неверно, либо не существует')

                else:
                    path = os.getcwd()
                    print("Текущая рабочая директория %s" % path)

                    while 1:
                        try:
                            path = input('Введите имя проекта: ')
                            os.mkdir(path)
                        except OSError:
                            print("Создать директорию %s не удалось, такое имя уже существует." % path)

                        else:
                            print("Успешно создана директория %s " % path)
                            now_path = os.getcwd()
                            final_path = now_path + "\\" + path + "\\"  # создаем строку с адресом для перехода
                            os.chdir(final_path)
                            head_path = os.getcwd()  # запоминаем путь к папке проекта
                            print("Текущая рабочая директория %s" % head_path)

                            f = open('index.html', 'tw', encoding='utf-8')  # создаем html файл
                            f.write('<!DOCTYPE html> \n')
                            f.write('<html lang="en"> \n')
                            f.write('<head> \n')
                            f.write('  <meta charset="UTF-8"> \n')
                            f.write('  <title>Title</title> \n')
                            f.write('  <link rel="stylesheet" href="css/style.css"/> \n')
                            f.write('</head> \n')
                            f.write('<body> \n')
                            f.write('  <div class="content"> \n')
                            f.write('   <h1>Hello! I am ready for edit! :)</h1> \n')
                            f.write('  </div> \n')
                            f.write('  <script src="js/app.js"></script> \n')
                            f.write('</body> \n')
                            f.write('</html> \n')
                            f.close()

                            os.mkdir('js')  # создаем каталог js и файл js-скрипта в нем
                            now_path = os.getcwd()
                            final_path = now_path + "\\" + 'js' + "\\"  # создаем строку с адресом для перехода
                            os.chdir(final_path)
                            f = open('script.js', 'tw', encoding='utf-8')
                            f.write('/* this source generate automatically */')
                            f.close()

                            os.chdir(head_path)
                            os.mkdir('css')  # создаем каталог css и файл стиля в нем
                            now_path = os.getcwd()
                            final_path = now_path + "\\" + 'css' + "\\"  # создаем строку с адресом для перехода
                            os.chdir(final_path)
                            f = open('style.css', 'tw', encoding='utf-8')
                            f.write('/* this source generate automatically */ \n \n')
                            f.write('html { \n \n')
                            f.write('} \n \n')
                            f.write('body { \n \n')
                            f.write('} \n \n')
                            f.write('.content { \n \n')
                            f.write('} \n \n')
                            f.write('.content h1 { \n \n')
                            f.write('}')
                            f.close()

                            print('Проект успешно создан! Можно приступать к работе.')

                            break

                    break

        elif key ==3:
            print('Пока!')
            break

        else:
            continue

        break
    except ValueError:
        print("Ошибка! Введите 1 или 2")

hold=input("Press Enter to exit")