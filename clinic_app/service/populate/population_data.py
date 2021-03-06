"""
This module stores sample population data
"""
DOCTORS_SRC = (
    {
        "id": 1,
        "uuid": "1",
        "full_name": "Семендяева Лариса Дмитриевна",
        "speciality": "Врач-терапевт, гастроэнтеролог высшей категории",
        "info":
            "Комплексная терапия хронических и неотложных патологических "
            "состояний в гастроэнтерологии, кардиологии и пульмонологии. "
            "Предоставляет индивидуальные рекомендации по здоровому "
            "образу жизни, назначение ЛФК, диетотерапии.",
        "experience_years": 38
    },
    {
        "id": 2,
        "uuid": "2",
        "full_name": "Аблялимова Альбина Шевкетовна",
        "speciality": "Врач - акушер-гинеколог, врач УЗД",
        "info":
            "Альбина Шевкетовна владеет всеми современными методами "
            "диагностики и лечения гинекологических заболеваний: расширенная "
            "видеокольпоскопия, прицельная биопсия шейки матки радиоволновым "
            "методом, техникой радиоволновой и лазерной деструкции "
            "патологий шейки матки (эрозия, дисплазия).",
        "experience_years": 13
    },
    {
        "id": 3,
        "uuid": "3",
        "full_name": "Бонюк Ирина Владимировна",
        "speciality": "Врач - акушер-гинеколог высшей категории, "
                      "врач УЗД, гинеколог-эндокринолог",
        "info":
            "Ирина Владимировна занимается вопросами диагностики и лечения "
            "патологий шейки матки, атрофии слизистой влагалища, проводит "
            "операции в сфере эстетической гинекологии. Консультирует по "
            "вопросам планирования беременности и занимается ее ведением до родов.",
        "experience_years": 15
    },
    {
        "id": 4,
        "uuid": "4",
        "full_name": "Держановская Людмила Николаевна",
        "speciality": "Врач - акушер-гинеколог, первой категории",
        "info":
            "Людмила Николаевна — врач первой категории — владеет "
            "современными методиками диагностики и лечения заболеваний "
            "патологии шейки матки (эрозии, дисплазии, полипы). Ведение "
            "беременности с момента беременности и до родов",
        "experience_years": 14
    },
    {
        "id": 5,
        "uuid": "5",
        "full_name": "Серветник Лариса Сергеевна",
        "speciality": "Врач - акушер - гинеколог высшей категории, "
                      "гинеколог-эндокринолог, врач УЗД",
        "info":
            "Специализируется на диагностике и лечении в области "
            "эндокринной гинекологии: аномально маточного кровотечения; "
            "эндокринного бесплодия; метаболического, предменструального, "
            "климактерического синдромов у женщин. Занимается вопросами "
            "диагностики и лечения патологии шейки матки.",
        "experience_years": 27
    },
    {
        "id": 6,
        "uuid": "6",
        "full_name": "Шалюта Алла Григорьевна",
        "speciality": "Врач - акушер-гинеколог первой категории",
        "info":
            "Алла Григорьевна в своей работе использует современные и доступные "
            "методы диагностики патологии шейки матки, эрозии и дисплазии шейки "
            "матки, миомы матки, эндометриоза, нарушений менструального цикла, "
            "гиперплазии эндометрия, проводит расширенную видеокольпоскопию.",
        "experience_years": 28
    },
    {
        "id": 7,
        "uuid": "7",
        "full_name": "Шкута Анатолий Николаевич",
        "speciality": "Врач - гинеколог высшей категории",
        "info":
            "Врач специализируется на проведении операций эндоскопического "
            "профиля-лапароскопии, гистероскопии. Осуществляет реконструктивно-"
            "пластические операции влагалища и шейки матки. Осуществляет лечение "
            "воспалительных заболеваний придатков матки, "
            "аномальных кровотечений, гормональных нарушений.",
        "experience_years": 27
    },
    {
        "id": 8,
        "uuid": "8",
        "full_name": "Голубец Наталья Валентиновна",
        "speciality": "Врач-дерматокосметолог",
        "info":
            "Специализируется на лазерной и классической инъекционной косметологии. "
            "Для решения эстетических проблем, Наталья Валентиновна использует "
            "такие методы как химический пилинг, мезотерапия, биоревитализация, "
            "объемно-контурная коррекция, имплантация нитей, ботулинотерапия. "
            "Владеет современными лазерными методиками омоложения лица и тела.",
        "experience_years": 18
    },
    {
        "id": 9,
        "uuid": "9",
        "full_name": "Науменко Андрей Аркадьевич",
        "speciality": "Врач - дерматовенеролог высшей категории, "
                      "детский дерматолог, дерматокосметолог",
        "info":
            "Диагностика и лечение различных кожных заболеваний (аллергической, "
            "бактериальной, вирусной, грибковой, не уточненной этиологии) у "
            "взрослых и детей с грудного возраста, а также "
            "заболеваний передающихся половым путем.",
        "experience_years": 25
    },
    {
        "id": 10,
        "uuid": "10",
        "full_name": "Семенова Анжела Дмитриевна",
        "speciality": "Главный врач, дерматокосметолог",
        "info":
            "Основным направлением в работе Анжелы Дмитриевны является "
            "дерматокосметология.Успешно проводит диагностику и лечение "
            "различных кожных заболеваний: аллергической, бактериальной, "
            "вирусной, грибковой и неуточненной этиологии у взрослых.Доктор "
            "специализируется на инновационной лечебно-омолаживающей процедуре "
            "плазмолифтинга. Имеет большой опыт в лечении паразитарных "
            "заболеваний кожи и волосистой части головы. Совместно с акушерами"
            "-гинекологами ведет пациентов с андрогенным поражением кожи.",
        "experience_years": 25
    },
    {
        "id": 11,
        "uuid": "11",
        "full_name": "Гай Ольга Ивановна",
        "speciality": "Врач-кардиолог, кандидат медицинских наук",
        "info":
            "Ольга Ивановна специализируется в области диагностики, лечения "
            "и профилактики сердечно-сосудистых заболеваний. Имеет "
            "успешную практику лечения пациентов, страдающих аритмии сердца.",
        "experience_years": 7
    },
    {
        "id": 12,
        "uuid": "12",
        "full_name": "Кудашова Елена Петровна",
        "speciality": "Врач-лаборант",
        "info":
            "Елена Петровна в совершенстве владеет цитологическими, "
            "биохимическими, иммунологическими и общеклиническими "
            "методами лабораторного исследования.",
        "experience_years": 33
    },
    {
        "id": 13,
        "uuid": "13",
        "full_name": "Тарасюк Геннадий Филиппович",
        "speciality": "Врач-хирург, хирург-проктолог высшей категории",
        "info":
            "Геннадий Филиппович является специалистом малоинвазивной "
            "и эстетической проктологии. В совершенстве владеет современным "
            "методом безоперационного лечения внутреннего "
            "геморроя – методом латексного лигирования.",
        "experience_years": 24
    },
    {
        "id": 14,
        "uuid": "14",
        "full_name": "Сторожев Евгений Евгеньевич",
        "speciality": "Врач - уролог-андролог, врач УЗД",
        "info":
            "Евгений Евгеньевич владеет всеми техниками консервативной и "
            "оперативной урологии: диагностика и лечение заболеваний "
            "передающихся половым путем, удаление остроконечных кондилом с "
            "помощью лазерной хирургии, обладает навыками комплексного "
            "лечения простатита с применением магнитно-лазерной методики.",
        "experience_years": 27
    },
    {
        "id": 15,
        "uuid": "15",
        "full_name": "Петрусь Игорь Васильевич",
        "speciality": "Врач - анестезиолог",
        "info":
            "Игорь Васильевич владеет современными методами "
            "анестезиологического обеспечения – внутривенная, ингаляционная, "
            "регионарная и комбинированная анестезии, а "
            "также навыками проведения интенсивной терапии.",
        "experience_years": 27
    },
    {
        "id": 16,
        "uuid": "16",
        "full_name": "Семёнов Антон Вадимович",
        "speciality": "Врач-хирург, сосудистый хирург, флеболог, врач УЗД",
        "info":
            "Семёнов Антон Вадимович владеет современными методами диагностики "
            "и лечения заболеваний сосудов, варикозной болезни вен "
            "нижних конечностей, грыж передней брюшной стенки, "
            "заболеваний подкожной жировой клетчатки.",
        "experience_years": 5
    },
    {
        "id": 17,
        "uuid": "17",
        "full_name": "Добровинская Елена Вячеславовна",
        "speciality": "Врач - эндокринолог, кандидат медицинских наук",
        "info":
            "Доктор успешно занимается вопросами эндокринологии: проводит "
            "диагностику и лечение пациентов с нарушением углеводного обмена "
            "(сахарный диабет), заболеваниями щитовидной железы (тиреотоксикоз, "
            "гипотиреоз, аутоиммунный тиреоидит, узловой зоб, рак щитовидной "
            "железы), ожирением и метаболическим синдромом, патологией "
            "надпочечников (хроническая почечная недостаточность). Ведет беременных.",
        "experience_years": 13
    }
)

ROOT_PASSWORD = 'root1234'
DOCTORS_PASSWORD = 'doctor1234'

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
