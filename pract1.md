# Практическое занятие №1. Введение, основы работы в командной строке

Е.Н. Коршак , РТУ МИРЭА

Научиться выполнять простые действия с файлами и каталогами в Linux из командной строки. Сравнить работу в командной строке Windows и Linux.

## Задача 1

Вывести отсортированный в алфавитном порядке список имен пользователей в файле passwd (вам понадобится grep).
grep '.*' /etc/passwd | cut -d: -f1 | sort
![photo_5470137324361866858_y](https://github.com/user-attachments/assets/fe5ac1f2-13de-4a0e-9d97-6c5de419fcbb)


## Задача 2

Вывести данные /etc/protocols в отформатированном и отсортированном порядке для 5 наибольших портов, как показано в примере ниже:

```
awk '{print $2, $1}' /etc/protocols | sort -nr | head -n 5
```
![photo_5470137324361866866_y](https://github.com/user-attachments/assets/669a376d-e4c1-4e7d-a2df-84bd8857d50b)


## Задача 3

Написать программу banner средствами bash для вывода текстов, как в следующем примере (размер баннера должен меняться!):

```
#!/bin/bash

text=$*
length=${#text}

for i in $(seq 1 $((length + 2))); do
    line+="-"
done

echo "+${line}+"
echo "| ${text} |"
echo "+${line}+"
```
![photo_5474466960633881470_x](https://github.com/user-attachments/assets/e8c0deea-8a62-4128-be80-934366adb59d)
Перед отправкой решения проверьте его в ShellCheck на предупреждения.

## Задача 4

Написать программу для вывода всех идентификаторов (по правилам C/C++ или Java) в файле (без повторений).

Пример для hello.c:

```
#!/bin/bash

file="$1"

id=$(grep -o -E '\b[a-zA-Z]*\b' "$file" | sort -u)
_________________________________

grep -oE '\b[a-zA-Z_][a-zA-Z0-9_]*\b' hello.c | grep -vE '\b(int|void|return|if|else|for|while|include|stdio)\b' | sort | uniq

```

![photo_5470137324361866980_y](https://github.com/user-attachments/assets/4c2963ef-da8e-47f1-ab3c-208575c63bf7)

## Задача 5

Написать программу для регистрации пользовательской команды (правильные права доступа и копирование в /usr/local/bin).

Например, пусть программа называется reg:

```
#!/bin/bash

file=$1

chmod 755 "./$file"

sudo cp "$file" /usr/local/bin/
```

В результате для banner задаются правильные права доступа и сам banner копируется в /usr/local/bin.
![photo_5469919913117344618_y](https://github.com/user-attachments/assets/ca910a8c-889d-409c-bcb1-6019b1be6cf9)


Общие сведения

https://ru.wikipedia.org/wiki/Интерфейс_командной_строки
https://nullprogram.com/blog/2020/08/01/
https://habr.com/ru/post/150950/

Стандарты

https://www.gnu.org/prep/standards/standards.html#Command_002dLine-Interfaces
https://www.gnu.org/software/libc/manual/html_node/Argument-Syntax.html
https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap12.html

Реализация разбора опций

Питон

https://docs.python.org/3/library/argparse.html#module-argparse
https://click.palletsprojects.com/en/7.x/
