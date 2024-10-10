# Практическое занятие №1. Введение, основы работы в командной строке

Е.Н. Коршак , РТУ МИРЭА

Научиться выполнять простые действия с файлами и каталогами в Linux из командной строки. Сравнить работу в командной строке Windows и Linux.

## Задача 1

Вывести отсортированный в алфавитном порядке список имен пользователей в файле passwd (вам понадобится grep).
grep '.*' /etc/passwd | cut -d: -f1 | sort
![Снимок экрана 2024-10-04 143910](https://github.com/user-attachments/assets/b4955197-010a-47d9-884e-cc40ebc91207)



## Задача 2

Вывести данные /etc/protocols в отформатированном и отсортированном порядке для 5 наибольших портов, как показано в примере ниже:

```
awk '{print $2, $1}' /etc/protocols | sort -nr | head -n 5
```
![Снимок экрана 2024-10-04 102928](https://github.com/user-attachments/assets/6db0e5e1-aad0-4d70-b807-ff8a4a808a7c)

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
![Снимок экрана 2024-10-04 144531](https://github.com/user-attachments/assets/c4fc9c4b-97ed-4c92-b99a-27790fb09a29)

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

Например, пусть программа называется pifitsa:

```
#!/bin/bash

file=$1

chmod 755 "./$file"

sudo cp "$file" /usr/local/bin/
```

В результате для banner задаются правильные права доступа и сам banner копируется в /usr/local/bin.
