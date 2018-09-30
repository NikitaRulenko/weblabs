import os
import sys

sys.getfilesystemencoding()
'UTF-8'

print('Wellcome to project auto-creation program.')
print('This program will create basic structure of a web-project: project named folder, index.html, css and js script folders.')

path = os.getcwd()
print("Current directory is %s" % path)

while 1:
    try:
        key = int(input("Input 1 to create here, input 2 to change directory or 3 to exit: \n"))
        if key != 1 and key != 2 and key !=3:
            key = int(input("Wrong value. Input again:"))

        if key == 1:

            while 1:
                try:
                    path = input('Input project name: ')
                    os.mkdir(path)
                except OSError:
                    print("Failure %s creation, this already exists." % path)

                else:
                    print("Succesfully created %s " % path)
                    now_path = os.getcwd()
                    final_path = now_path + "\\" + path + "\\" #string with adress
                    os.chdir(final_path)
                    head_path = os.getcwd()                         # mind a way to parent-folder
                    print("Current directory is %s" % head_path)

                    f = open('index.html', 'tw', encoding='utf-8') #  html creation
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

                    os.mkdir('js')                             # js folder and js-script creation
                    now_path = os.getcwd()
                    final_path = now_path + "\\" + 'js' + "\\"  # string with adress
                    os.chdir(final_path)
                    f = open('script.js', 'tw', encoding='utf-8')
                    f.write('/* this source generate automatically */')
                    f.close()

                    os.chdir(head_path)
                    os.mkdir('css')                            # css folder and css script inside
                    now_path = os.getcwd()
                    final_path = now_path + "\\" + 'css' + "\\"  # string with adress
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

                    print('Project has been succesfully created! It is ready for work.')

                    break

        elif key == 2:

            while 1:
                try:
                    newDir = input('Input directory for project creation:')
                    os.chdir(newDir)
                except FileNotFoundError:
                    print('Wrong way or doesn not exist!')

                else:
                    path = os.getcwd()
                    print("Current directory is %s" % path)

                    while 1:
                        try:
                            path = input('Input project name: ')
                            os.mkdir(path)
                        except OSError:
                            print("Failure %s creation, already exists." % path)

                        else:
                            print("Directory succesfully created %s " % path)
                            now_path = os.getcwd()
                            final_path = now_path + "\\" + path + "\\"  # string with adress
                            os.chdir(final_path)
                            head_path = os.getcwd()  # parent folder adress
                            print("Current directory is %s" % head_path)

                            f = open('index.html', 'tw', encoding='utf-8')  # html creation
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

                            os.mkdir('js')  # js folder with js-script inside
                            now_path = os.getcwd()
                            final_path = now_path + "\\" + 'js' + "\\"  # adress string generation
                            os.chdir(final_path)
                            f = open('script.js', 'tw', encoding='utf-8')
                            f.write('/* this source generate automatically */')
                            f.close()

                            os.chdir(head_path)
                            os.mkdir('css')  # css folder with css script inside
                            now_path = os.getcwd()
                            final_path = now_path + "\\" + 'css' + "\\"  # adress string
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

                            print('Project has been succesfully created! It is ready for work..')

                            break

                    break

        elif key ==3:
            print('GOOD BUY!')
            break

        else:
            continue

        break
    except ValueError:
        print("Error! Input 1,2 or 3")

hold=input("Press Enter to exit")