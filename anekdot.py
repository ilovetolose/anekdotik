import random
print('Выберите категорию анекдотов:\n'
          '1.Анекдоты про тещу\n'
          '2.Анекдоты про евреев\n'
          '3.Анекдоты про вовочку\n'
          '4.Вернуть категории анекдотов\n')
tesha = ['\nДети - цветы жизни.Теща - кактус смерти.',
         '\nТеща решила переехать к своему зятю - генералу. Но по дороге ее мобилизовали в армию.',
         '\nМоя теща буквально исключение: за неделю до свадьбы выдала мне все приданое. '
         '\n- А моя так еще обязательнее была: за год до моей женитьбы умерла.',
         ]
evrei = ['\n— Почему евреям никогда не нравится полная, необрезанная версия фильма?',
         '\nВ чем разница между евреем и пиццой? \n -Пицца не кричит когда ее засовывают в духовку.',
         '\nКак уместить 10000 евреев в Daewoo Matiz? \n -Очень просто! - в пепельницу.']
vova = ['\nНа уроке Мария Ивановна спрашивает:\n- Дети, кто знает: почему аисты на зиму улетают в Африку?Вовочка тянет руку:\n- Чтобы и негры могли иметь детей.',
        '\nПреподаватель истории:\n— Представляете — у наших прадедов не было ни электричества, ни радио, ни телевидения…\nВовочка:\n— Вот поэтому они и умерли.',
        '\nВовочку, когда он простудился, мама заставила дышать под одеялом над горячей картошкой. Через две минуты он попросил котлет и вилку.']
while True:
    x = int(input('введите категорию анекдота: \n'
                  ''))
    if x == 1:
        print(tesha[random.randint(0,2)])
    elif x == 2:
        print(evrei[random.randint(0,2)])
    elif x == 3:
        print(vova[random.randint(0,2)])
    else:
        print('Выберите категорию анекдотов:\n'
         '1.Анекдоты про тещу\n'
         '2.Анекдоты про евреев\n'
         '3.Анекдоты про вовочку\n'
         '4.Вернуть категории анекдотов\n')

