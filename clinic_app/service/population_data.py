"""
This module stores sample population data
"""
AREAS_SRC = (
    (
        'Гастроэнтерология',
        'Гастроэнтерология — это раздел внутренних болезней, который '
        'покрывает диагностику и лечение органов желудочно-кишечного '
        'тракта: пищевода, желудка, тонкого и толстого кишечника, '
        'печени, поджелудочной железы, желчного пузыря.'
    ),
    (
        'Гинекология',
        'Женский организм – идеальное творение природы. Женщина '
        'одновременно сильная и выносливая, уязвимая и хрупкая. Каждой '
        'женщине для сохранения здоровья важно найти «своего» гинеколога.'
    ),
    (
        'Дерматокосметология',
        'Дерматокосметология – это область медицины, которая сочетает '
        'в себе дерматологию и косметологию. Болезни кожи выявляет, '
        'диагностирует и лечит врач дерматолог.Основной задачей '
        'дерматокосметологии, является возвращение здоровья и красоты кожи.'
    ),
    (
        'Кардиология',
        'Кардиология — это раздел внутренней медицины, который включает '
        'в себя диагностику и лечение органов сердечно-сосудистой системы: '
        'сердца, коронарных и периферических сосудов. Консультации в этой '
        'области проводит узкопрофильный специалист - врач-кардиолог.'
    ),
    (
        'Лабораторная диагностика',
        'Каждый доктор честно скажет, что верный диагноз без '
        'лабораторной диагностики невозможен.'
    ),
    (
        'Проктология',
        'Главные жалобы, с которыми обращаются к врачу проктологу - это '
        'болезненные ощущения и дискомфорт в заднем проходе, ноющая боль, '
        'болезненный акт дефекации, появление крови из заднего прохода.'
    ),
    (
        'Урология',
        'Мужчина – это олицетворение силы, мужества и надежности. Он, как '
        'защитник, всегда готов принять любой вызов судьбы. Стрессы, '
        'нагрузки, напряженные ситуации являются его постоянными '
        'попутчиками. Все это приводит к нарушению мужского здоровья.'
    ),
    (
        'Хирургия',
        'Хирургия в наше время это огромный веер подразделений. '
        'Абдоминальная хирургия, амбулаторная хирургия, лазерная хирургия, '
        'сосудистая хирургия, онкохирургия, оперативная хирургия, '
        'эстетическая хирургия, пластическая хирургия.'
    ),
    (
        'Эндокринология',
        'Эндокринология – это сегмент медицины, который подробно '
        'изучает строение, функцию каждой эндокринной железы, '
        'вырабатываемые ею гормоны и их сферу влияния на другие '
        'органы и системы человеческого организма.'
    )
)

DOCTORS_SRC = (
    {
        'area_index': 0,
        'data': (
            'Семендяева Лариса Дмитриевна',
            'Врач-терапевт, гастроэнтеролог высшей категории',
            'Комплексная терапия хронических и неотложных патологических '
            'состояний в гастроэнтерологии, кардиологии и пульмонологии. '
            'Предоставляет индивидуальные рекомендации по здоровому '
            'образу жизни, назначение ЛФК, диетотерапии.',
            38)
    },
    {
        'area_index': 1,
        'data': (
            'Аблялимова Альбина Шевкетовна',
            'Врач - акушер-гинеколог, врач УЗД',
            'Альбина Шевкетовна владеет всеми современными методами '
            'диагностики и лечения гинекологических заболеваний: расширенная '
            'видеокольпоскопия, прицельная биопсия шейки матки '
            'радиоволновым методом, техникой радиоволновой и лазерной '
            'деструкции патологий шейки матки (эрозия, дисплазия).',
            13)
    },
    {
        'area_index': 1,
        'data': (
            'Бонюк Ирина Владимировна',
            'Врач - акушер-гинеколог высшей категории, '
            'врач УЗД, гинеколог-эндокринолог',
            'Ирина Владимировна занимается вопросами диагностики и '
            'лечения патологий шейки матки, атрофии слизистой '
            'влагалища, проводит операции в сфере эстетической '
            'гинекологии. Консультирует по вопросам планирования '
            'беременности и занимается ее ведением до родов.',
            15)
    },
    {
        'area_index': 1,
        'data': (
            'Держановская Людмила Николаевна',
            'Врач - акушер-гинеколог, первой категории',
            'Людмила Николаевна — врач первой категории — владеет '
            'современными методиками диагностики и лечения заболеваний '
            'патологии шейки матки (эрозии, дисплазии, полипы). '
            'Ведение беременности с момента беременности и до родов',
            14)
    },
    {
        'area_index': 1,
        'data': (
            'Серветник Лариса Сергеевна',
            'Врач - акушер - гинеколог высшей категории, '
            'гинеколог-эндокринолог, врач УЗД',
            'Специализируется на диагностике и лечении в области '
            'эндокринной гинекологии: аномально маточного кровотечения; '
            'эндокринного бесплодия; метаболического, предменструального, '
            'климактерического синдромов у женщин. Занимается вопросами '
            'диагностики и лечения патологии шейки матки.',
            27)
    },
    {
        'area_index': 1,
        'data': (
            'Шалюта Алла Григорьевна',
            'Врач - акушер-гинеколог первой категории',
            'Алла Григорьевна в своей работе использует современные '
            'и доступные методы диагностики патологии шейки матки, '
            'эрозии и дисплазии шейки матки, миомы матки, эндометриоза, '
            'нарушений менструального цикла, гиперплазии эндометрия, '
            'проводит расширенную видеокольпоскопию.',
            28)
    },
    {
        'area_index': 1,
        'data': (
            'Шкута Анатолий Николаевич',
            'Врач - гинеколог высшей категории',
            'Врач специализируется на проведении операций эндоскопического '
            'профиля-лапароскопии, гистероскопии. Осуществляет '
            'реконструктивно-пластические операции влагалища и шейки матки. '
            'Осуществляет лечение воспалительных заболеваний придатков матки, '
            'аномальных кровотечений, гормональных нарушений.',
            27)
    },
    {
        'area_index': 2,
        'data': (
            'Голубец Наталья Валентиновна',
            'Врач-дерматокосметолог',
            'Специализируется на лазерной и классической инъекционной '
            'косметологии. Для решения эстетических проблем, Наталья '
            'Валентиновна использует такие методы как химический пилинг, '
            'мезотерапия, биоревитализация, объемно-контурная коррекция, '
            'имплантация нитей, ботулинотерапия. Владеет современными '
            'лазерными методиками омоложения лица и тела.',
            18)
    },
    {
        'area_index': 2,
        'data': (
            'Науменко Андрей Аркадьевич',
            'Врач - дерматовенеролог высшей категории, '
            'детский дерматолог, дерматокосметолог',
            'Диагностика и лечение различных кожных заболеваний '
            '(аллергической, бактериальной, вирусной, грибковой, '
            'не уточненной этиологии) у взрослых и детей с грудного '
            'возраста, а также заболеваний передающихся половым путем.',
            25)
    },
    {
        'area_index': 2,
        'data': (
            'Семенова Анжела Дмитриевна',
            'Главный врач, дерматокосметолог',
            'Основным направлением в работе Анжелы Дмитриевны является '
            'дерматокосметология.Успешно проводит диагностику и лечение '
            'различных кожных заболеваний: аллергической, бактериальной, '
            'вирусной, грибковой и неуточненной этиологии у взрослых.Доктор '
            'специализируется на инновационной лечебно-омолаживающей процедуре '
            'плазмолифтинга. Имеет большой опыт в лечении паразитарных '
            'заболеваний кожи и волосистой части головы. Совместно с акушерами-'
            'гинекологами ведет пациентов с андрогенным поражением кожи.',
            25)
    },
    {
        'area_index': 3,
        'data': (
            'Гай Ольга Ивановна',
            'Врач-кардиолог, кандидат медицинских наук',
            'Ольга Ивановна специализируется в области диагностики, '
            'лечения и профилактики сердечно-сосудистых заболеваний. Имеет '
            'успешную практику лечения пациентов, страдающих аритмии сердца.',
            7)
    },
    {
        'area_index': 4,
        'data': (
            'Кудашова Елена Петровна',
            'Врач-лаборант',
            'Елена Петровна в совершенстве владеет цитологическими, '
            'биохимическими, иммунологическими и общеклиническими '
            'методами лабораторного исследования.',
            33)
    },
    {
        'area_index': 5,
        'data': (
            'Тарасюк Геннадий Филиппович',
            'Врач-хирург, хирург-проктолог высшей категории',
            'Геннадий Филиппович является специалистом малоинвазивной '
            'и эстетической проктологии. В совершенстве владеет '
            'современным методом безоперационного лечения внутреннего '
            'геморроя – методом латексного лигирования.',
            24)
    },
    {
        'area_index': 6,
        'data': (
            'Сторожев Евгений Евгеньевич',
            'Врач - уролог-андролог, врач УЗД',
            'Евгений Евгеньевич владеет всеми техниками консервативной '
            'и оперативной урологии: диагностика и лечение заболеваний '
            'передающихся половым путем, удаление остроконечных кондилом '
            'с помощью лазерной хирургии, обладает навыками комплексного '
            'лечения простатита с применением магнитно-лазерной методики.',
            27)
    },
    {
        'area_index': 7,
        'data': (
            'Петрусь Игорь Васильевич',
            'Врач - анестезиолог',
            'Игорь Васильевич владеет современными методами '
            'анестезиологического обеспечения – внутривенная, ингаляционная, '
            'регионарная и комбинированная анестезии, а также '
            'навыками проведения интенсивной терапии.',
            27)
    },
    {
        'area_index': 7,
        'data': (
            'Семёнов Антон Вадимович',
            'Врач-хирург, сосудистый хирург, флеболог, врач УЗД',
            'Семёнов Антон Вадимович владеет современными методами '
            'диагностики и лечения заболеваний сосудов, варикозной '
            'болезни вен нижних конечностей, грыж передней брюшной '
            'стенки, заболеваний подкожной жировой клетчатки.',
            5)
    },
    {
        'area_index': 8,
        'data': (
            'Добровинская Елена Вячеславовна',
            'Врач - эндокринолог, кандидат медицинских наук',
            'Доктор успешно занимается вопросами эндокринологии: '
            'проводит диагностику и лечение пациентов с нарушением '
            'углеводного обмена (сахарный диабет), заболеваниями щитовидной '
            'железы (тиреотоксикоз, гипотиреоз, аутоиммунный тиреоидит, '
            'узловой зоб, рак щитовидной железы), ожирением и метаболическим '
            'синдромом, патологией надпочечников (хроническая почечная '
            'недостаточность). Ведет беременных.',
            13)
    }
)

NAMES_SRC = (
    ('Александр', 'Алексей', 'Андрей', 'Артем', 'Богдан',
     'Василий', 'Влад', 'Владимир', 'Владислав', 'Данил',
     'Денис', 'Дмитрий', 'Евгений', 'Егор', 'Иван',
     'Илья', 'Кирилл', 'Максим', 'Назар', 'Никита',
     'Павел', 'Роман', 'Станислав', 'Тарас', 'Ярослав'),
    ('Александра', 'Алена', 'Алина', 'Анастасия', 'Анна',
     'Антонина', 'Богдана', 'Валерия', 'Вероника', 'Виктория',
     'Дарина', 'Дарья', 'Ева', 'Екатерина', 'Елизавета',
     'Злата', 'Ирина', 'Кристина', 'Ксения', 'Маргарита',
     'Мария', 'Милана', 'Полина', 'Соломия', 'София')
)

SURNAMES_SRC = (
    'Бутко', 'Винниченко', 'Гончаренко', 'Григоренко', 'Гузенко',
    'Коваль', 'Ковальчук', 'Кравец', 'Кравченко', 'Кравчук',
    'Лещенко', 'Матвиенко', 'Онищенко', 'Панасенко', 'Плющенко',
    'Придиус', 'Романченко', 'Романюк', 'Скрипко', 'Собчак',
    'Степаненко', 'Тимошенко', 'Тищенко', 'Ткаченко', 'Шевченко'
)

PATRONYMICS_SRC = (
    (
        'Александрович', 'Алексеевич', 'Андреевич', 'Артемович', 'Богданович',
        'Вадимович', 'Василиевич', 'Владимирович', 'Владиславович', 'Данилович',
        'Денисович', 'Дмитриевич', 'Евгениевич', 'Егорович', 'Иванович',
        'Ильич', 'Кириллович', 'Максимович', 'Назарович', 'Никитич',
        'Павлович', 'Романович', 'Станиславович', 'Тарасович', 'Ярославович'
    ),
    (
        'Александровна', 'Алексеевна', 'Андреевна', 'Артемовна', 'Богдановна',
        'Вадимовна', 'Василиевна', 'Владимировна', 'Владиславовна', 'Даниловна',
        'Денисовна', 'Дмитриевна', 'Евгениевна', 'Егоровна', 'Ивановна',
        'Ильинична', 'Кирилловна', 'Максимовна', 'Назаровна', 'Никитовна',
        'Павловна', 'Романовна', 'Станиславовна', 'Тарасовна', 'Ярославовна'
    )
)
