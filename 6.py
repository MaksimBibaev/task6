try:
    kol=int(input("Сколько значений вы хотите ввести?"))
except ValueError:
    print("Ошибка")
else:
    if kol>0:
        array=[]
        c=0
        count=0
        while c!=kol:
            a=int(input("Введите значение"))
            array.append(a)
            c+=1
        delta=int(input("Введите дэльту"))
        minValue=min(array)
        for i in array:
            if i-minValue==delta:
                count+=1
        print("Количество элементов с заданным условием:",count)
    else:
        print("Ошибка")
