from django.shortcuts import render
from django.contrib.auth.decorators import login_required

import random

from authapp.models import AppUser

# Create your views here.
NAME_ORGANIZATION = 'СБТ'

QUESTIONS_A = {'1': ['Сокращенная продолжительность рабочего времени для работников в возрасте от 16 до 18 лет составляет:', 'не более 35 часов в неделю', 'не более 35 часов в неделю', 'не более 24 часов в неделю', 'не более 36 часов в неделю'],
               '2': ['Можно ли беременных женщин привлекать к работам, выполняемым вахтовым методом?', 'Нет', 'Нет', 'Да', 'Не имеет значения'],
               '3': ['Финансирование мероприятий по улучшению условий и охраны труда работодателями осуществляется в размере:', 'не менее 0,2 процента суммы затрат на производство продукции (работ, услуг)', 'не менее 0,2 процента суммы затрат на производство продукции (работ, услуг)', 'не менее 0,1 процента суммы затрат на производство продукции (работ, услуг)', 'не менее 0,5 процента суммы затрат на производство продукции (работ, услуг)'],
               '4': ['В течение какого срока с момента получения требования об устранении выявленных нарушений работодатели обязаны сообщить в профсоюзный орган о результатах рассмотрения требования и принятых мерах:', '7 дней', '3 дней', '7 дней', '14 дней'],
               '5': ['Обязан ли работник проходить обязательные предварительные и периодические медицинские осмотры?', 'Да', 'Нет', 'Да', 'Не имеет значения'],
               '6': ['Основными принципами обеспечения безопасности труда являются:', 'предупреждение и профилактика опасностей, а также минимизация повреждения здоровья работников', 'минимизация повреждения здоровья работников', 'предупреждение и профилактика опасностей', 'предупреждение и профилактика опасностей, а также минимизация повреждения здоровья работников'],
               '7': ['Продолжительность рабочего времени при работе по совместительству не должна превышать:', '4 часов в день', '5 часов в день', '3 часов в день', '4 часов в день'],
               '8': ['При какой численности работников в организации создается служба охраны труда?', 'более 50 человек', 'более 100 человек', 'более 30 человек', 'более 50 человек'],
               '9': ['Как часто проводится периодическая оценка эффективности системы управления охраной труда?', 'ежегодно во время планирования бюджета на СУОТ', '1 раз в 3 года', '1 раз в 5 лет', 'ежегодно во время планирования бюджета на СУОТ'],
               '10': ['Обязан ли работодатель обеспечить соответствие каждого рабочего места государственным нормативным требованиям охраны труда?', 'Да', 'Нет', 'Да', 'Не имеет значения'],
               '11': ['Специальная оценка условий труда НЕ проводится в отношении условий труда:', 'все перечисленное', 'все перечисленное', 'дистанционных работников', 'работников, вступивших в трудовые отношения с работодателями-физическими лицами, не являющимися индивидуальными предпринимателями'],
               '12': ['Какие средства НЕ используют для защиты от вредного воздействия пыли?', 'Ионизаторы и увлажнители воздуха', 'Изоляция технологического процесса, в котором образуется пыль от рабочей зоны в пространстве', 'Ионизаторы и увлажнители воздуха', 'Индивидуальные средства защиты (респираторы, маски, полумаски)'],
               '13': ['Обязан ли работодатель в соответствии с требованиями Трудового кодекса РФ осуществлять обязательное социальное страхование работников?', 'Да', 'Нет', 'Да', 'Не имеет значения'],
               '14': ['Количество членов комиссии по расследованию несчастных случаев должно быть:', 'нечетным, не менее 3 человек', 'нечетным, не менее 5 человек', 'нечетным, не менее 3 человек', 'нечетным, не менее 7 человек'],
               '15': ['Сколько лет хранятся вторые экземпляры актов о несчастном случае и его расследовании вместе с материалами дела?', '45 лет', '75 лет', '60 лет', '45 лет'],
               '16': ['Обязан ли работодатель расследовать все случаи выявленных профессиональных заболеваний с работниками?', 'Да', 'Нет', 'Да', 'Не имеет значения'],
               '17': ['Обязаны ли юридические лица и граждане, деятельность которых связана с повышенной опасностью для окружающих, возместить вред, причиненный источником повышенной опасности?', 'Да, если не докажут, что вред возник вследствие непреодолимой силы или умысла потерпевшего', 'Да, если не докажут, что вред возник вследствие непреодолимой силы или умысла потерпевшего', 'Нет', 'Не имеет значения'],
               '18': ['Какой вид вреда связан с лишением или повреждением имущества, иных материальных благ и выражается в денежной сумме?', 'Материальный вред', 'Материальный вред', 'Моральный вред', 'Физический вред'],
               '19': ['Когда на предприятии должны регистрировать микротравму в журнале и рассматривать ее обстоятельства и причины?', 'когда от пострадавшего поступило обращение', 'сразу после возникновения микроповреждений', 'когда от пострадавшего поступило обращение', 'через месяц после возникновения повреждения'],
               '20': ['Установленный срок действия сертификата безопасности по охране труда составляет:', '5 лет', '1 год', '3 года', '5 лет'],
               '21': ['Какой срок расследования несчастных случаев при тяжелых повреждениях здоровья?', '15 дней', '3 дня', '15 дней', 'месяц'],
               '22': ['Входят ли в состав аптечек для оказания первой помощи работникам лекарственные средства?', 'Нет', 'Нет', 'Да', 'Не имеет значения'],
               '23': ['В какой срок с момента извещения о заключительном диагнозе профзаболевания работодатель уведомляем ФСС о страховом случае по установленной форме?', 'сутки', 'сутки', '48 часов', '72 часа'],
               '24': ['В каком стандарте прописаны основные требования к безопасности технологических процессов?', 'ГОСТ 12.3.002-2014', 'ГОСТ 12.3.002-15', 'ГОСТ 12.3.002-2014', 'ГОСТ 12.3.002-75'],
               '25': ['Как часто проводится специальная оценка условий труда на рабочем месте?', 'не реже чем 1 раз в 5 лет', 'не реже чем 1 раз в год', 'не реже чем 1 раз в 3 года', 'не реже чем 1 раз в 5 лет'],
               '26': ['Работникам, занятым на работах с вредными или опасными условиями труда, предоставляется оплата труда в повышенном размере, не менее:', '0,04', '0,03', '0,04', '0,05'],
               '27': ['К какой группе знаков безопасности относится знак «Проход здесь»?', 'Предписывающие', 'Указательные', 'Предупреждающие', 'Предписывающие'],
               '28': ['Для какого класса условий труда характерно сохранение не только здоровья работников, но и создание предпосылок для поддержания высокого уровня работоспособности?', '1 класс-оптимальные', '1 класс-оптимальные', '2 класс-допустимые', '3 класс-вредные']
               }

QUESTIONS_B = {'1': ['Защита по разбросу проявляется в:', 'Увеличение обращения от источника до работников', 'Увеличение обращения от источника до работников', 'Уменьшение мощности источников до минимальных величин', 'Производство материалов'],
               '2': ['Процесс эмоциональной реакции и разумное проявление выраженности, снижение частоты проявлений от проявления утомления?', 'Синдром эмоционального выгорания', 'Синдром эмоционального выгорания', 'Депрессия', 'Уныние'],
               '3': ['Какие опасные биологические факторы вызывают появление у человека инфекций, вирусов, грибов или спор?', 'инфицирующие', 'аллергенные', 'токсичные', 'инфицирующие'],
               '4': ['Что относится к показателю тяжести трудового процесса?', 'Масса поднимаемого и перемещаемого груза вручную', 'Мощная внешняя работа', 'Масса поднимаемого и перемещаемого груза вручную', 'Монотонность задержки'],
               '5': ['Что означает под идентификацией опасности вредных и (или) опасных производственных факторов?', 'Сопоставление и установление совпадения условий для рабочих условий производственной среды и трудового процесса с факторами производственной среды и трудового процесса, предусмотренными классификатором вредных и (или) опасных производственных факторов', 'Предварительная оценка условий труда', 'Выявление вредных и вредных факторов производственной среды', 'Сопоставление и установление совпадения условий для рабочих условий производственной среды и трудового процесса с факторами производственной среды и трудового процесса, предусмотренными классификатором вредных и (или) опасных производственных факторов'],
               '6': ['К каким мероприятиям относится обеспечение работников мылом, смывающими и обезвреживающими средствами в соответствии с установленными нормами?', 'К мероприятиям по выявлению индивидуальной защиты', 'К лечебно-профилактическим и санитарно-бытовым мероприятиям', 'К организационным видам защиты', 'К мероприятиям по выявлению индивидуальной защиты'],
               '7': ['Оценка и учет профессиональных рисков – это:', 'Функция системы управления охраной труда', 'Метод управления охраной труда', 'Функция системы управления охраной труда', 'Принцип управления охраной труда'],
               '8': ['Какие опасные биологические факторы вызывают аллергические реакции в очагах?', 'аллергенные', 'инфицирующие', 'токсичные', 'аллергенные'],
               '9': ['Вредный производственный фактор – это:', 'Производственный фактор, возникновение которого на работника может привести к его заболеванию', 'Производственный фактор, возникновение которого на работника может привести к травме', 'Производственный фактор, возникновение которого на работника может привести к его заболеванию', 'Производственный фактор, возникновение которого на работника может привести к проявлению его трудоспособности'],
               '10': ['Заболевание считается профессиональным, если оно:', 'Вызвано профессиональными вредностями и его диагнозом встречается списку профзаболеваний', 'Соответствует списку профзаболеваний, не зависимо от того, где и как оно было получено', 'Вызвано профессиональными вредностями и его диагнозом встречается списку профзаболеваний', 'Вызвано абсолютно любыми вредными производственными факторами'],
               '11': ['Какая группа показателей не оценивается при тяжести трудового процесса?', 'Монотонность задержки', 'Рабочая поза', 'Монотонность задержки', 'Масса поднимаемого и перемещаемого груза вручную'],
               '12': ['Учитывается ли при обнаружении результатов, ранее проводившихся на данных рабочих исследований (испытаний) и измерений вредных и (или) опасных факторов производства?', 'Учитываются', 'Учитываются', 'Не учитываются', 'Учитываются требования территориального органа Федеральной службы по труду и занятости'],
               '13': ['Как проявляются классы окружающей среды по воздействию химических веществ?', 'Допустимый, вредный, опасный', 'Допустимый, вредный, опасный', 'Оптимальный, допустимый, вредный', 'Оптимальный, допустимый, вредный, опасный'],
               '14': ['От чего зависит достаточность искусственного освещения у детей?', 'Мощность лампы', 'Мощность лампы', 'Чистота стекол', 'Ориентация окон помещения по стороне света'],
               '15': ['Каковы условия условий труда, при которых на работника воздействуют вредные и (или) опасные производственные факторы, затрагивающие факторы, охватывающие весь рабочий день (смены) или его части, создают проблемы в жизни работников?', 'Опасные', 'Недопустимые', 'Вредные', 'Опасные'],
               '16': ['Какие опасные биологические факторы вызывают пристрастие к токсинам?', 'токсичные', 'инфицирующие', 'аллергенные', 'токсичные'],
               '17': ['Какой из факторов не имеет отношения к воздействию производственной среды?', 'Солнечная радиация', 'Шум', 'Солнечная радиация', 'Вибрация'],
               '18': ['Укажите предупредительные и контролирующие меры по показателю риска', 'Все ответы верны', 'Все ответы верны', 'СИЗ', 'Устранение опасности/риска'],
               '19': ['Каким термином называется раздражение сухожилий, соединяющих мышцы предплечья и локтевой сустав?', 'Травматический эпикондилит', 'Тендинит', 'Синдром канала запястья', 'Травматический эпикондилит'],
               '20': ['Что такое острота трудового процесса?', 'Характеристика трудового процесса, характеризующаяся производительностью центральной нервной системы и органов органов работника.', 'Характеристика трудового процесса, характеризующаяся производительностью центральной нервной системы и органов органов работника.', 'Характеристика трудового процесса, которая приносит пользу на опорно-двигательный аппарат и функциональную систему организма, благотворное влияние на его деятельность (сердечнососудистую, дыхательную и др.)', 'Характеристика трудового процесса, которая приносит пользу на опорно-двигательный аппарат и функциональную систему организма, улучшение его деятельности (сердечно-сосудистую, дыхательную и др.), а также характеристику трудового процесса, которая нагружает.'],
               '21': ['Что такое естественное освещение?', 'Освещение помещений светом неба (прямым или отражающим), проникающим через световые проемы в наружных ограждающих конструкциях', 'Освещение помещений светом неба (прямым или отражающим), проникающим через световые проемы в наружных ограждающих конструкциях', 'Освещение, поглощающее осветительную установку, компенсирующую недостаточность солнечного света', 'Рабочее освещение'],
               '22': ['Чем характерны вредные условия труда?', 'Наличие вредных производственных факторов, вызывающих неблагоприятное воздействие на организм', 'Наличие вредных производственных факторов, вызывающих нежелательное воздействие на организм', 'Наличие вредных производственных факторов, вызывающих неблагоприятное воздействие на организм', 'Уровнем производственных факторов, вызывающих повышенное напряжение'],
               '23': ['Вредные химические вещества - это вещества, которые при контакте с организмом работника в случае нарушения безопасности могут быть опасными:', 'Производственные заболевания, профессиональные заболевания или случаи исчезновения в состоянии здоровья, обнаруживаемые в редких случаях, как в работе, так и в отдаленных периодах жизни настоящего и выявления случаев', 'Производственные заболевания, профессиональные заболевания или случаи исчезновения в состоянии здоровья, обнаруживаемые в редких случаях, как в работе, так и в отдаленных периодах жизни настоящего и выявления случаев', 'Профессиональные заболевания', 'Отклонения в состоянии здоровья, обнаруживаемые отдельными методами, как в процессе работы, так и в отдаленных периодах жизни настоящего и выявленных случаев'],
               '24': ['Что из перечисленного не относится к опасным производственным объектам?', 'Стационарно установленные лифты', 'Объекты по добыче нефти', 'Эскалаторы в метрополитенах', 'Стационарно установленные лифты'],
               }

QUESTIONS_C = {'1': ['На производстве каких работ на объектах теплоснабжения и теплопотрябляющих установках должен выдаваться наряд-допуск?', 'Все перечисленные', 'Ремонт вращающихся механизмов', 'Нанесение антикоррозионных покрытий', 'Все перечисленные'],
               '2': ['Каким документом оформляется допуск к самостоятельной работе по эксплуатации тепловых энергоустановок?', 'Организационно-распорядительным документом', 'Протоколом', 'Организационно-распорядительным документом', 'Актом'],
               '3': ['Когда могут быть допущены работники к самостоятельному выполнению работ по эксплуатации объектов теплоснабжения и теплопотребляющих установок?', 'После проверки знаний', 'После проверки знаний', 'Все перечисленное верно', 'После проведения обучения'],
               '4': ['Какова минимальная продолжительность стажировки для работников 1 и 2 группы после завершения обучения безопасным методом и приемом выполнения работ в ограниченных и замкнутых пространствах и получением удостоверения?', 'Не менее 2 рабочих дней (смен)', 'Не менее 2 рабочих дней (смен)', 'Не менее 10 рабочих дней (смен)', 'Не менее 15 рабочих дней (смен)'],
               '5': ['На какой срок разрешается продлевать наряд-допуск для производства работ в крупных электроустановках?', 'Не более чем на 15 календарных дней', 'Не более чем на 10 календарных дней', 'Не более чем на 15 календарных дней', 'Не более чем на 30 рабочих дней со дня начала работы'],
               '6': ['Какие съемные грузозахватные приспособления (стропы, кольца, петли)не доходят до эксплуатации?', 'Все перечисленное верно', 'При отсутствии бирки (клеймо)', 'Все перечисленное верно', 'В присутствии деформированных коуши'],
               '7': ['Погрузка и разгрузка грузов какой массы должна производиться с использованием грузоподъемных машин?', 'Массой более 500 кг', 'Массой более 300 кг', 'Массой более 200 кг', 'Массой более 500 кг'],
               '8': ['Какой плакат должен быть вывешен при выполнении работ под напряжением, на приводах ручного и дистанционного управления коммутационными аппаратами?', '«Работа под напряжением. Повторно не встречается!»', '«Осторожно работай!»', '«Не записано! Работают люди»', '«Работа под напряжением. Повторно не встречается!»'],
               '9': ['При транспортировке грузов на какой-то скорости при сборке навесных конвейеров под сборку должны быть установлены градационные устройства, обеспечение безопасности работников при случайном падении загрузки?', 'На высоте свыше 2 м', 'На высоте свыше 2,5 м', 'На высоте свыше 2 м', 'На высоте свыше 1 м'],
               '10': ['Что необходимо выполнить перед началом ремонта на теплопотребляющей установке и трубопроводе?', 'Все перечисленное верно', 'Электроприводы отключающей арматуры должны быть обесточены', 'Все перечисленное верно', 'нужно снять давление'],
              }

QUESTIONS_D = {'1': ['Фильтрующие-поглощающие коробки, предназначенные для использования с полными лицевыми масками с байонетным креплением, должны:', 'Обладает малым весом, плоской формой, высокой эффективностью, комфортом и безопасностью при длительных и трудоемких работах', 'твердый корпус, допускающий возможность контакта с загрязняющим фильтрующим оборудованием', 'Обладает малым весом, плоской формой, высокой эффективностью, комфортом и безопасностью при длительных и трудоемких работах', 'Не имеет возможности содержать газовые фильтры с противоаэрозольными предфильтрами'],
               '2': ['Полумаски и маски со сменными патронами, фильтрами и предфильтрам и не рассчитаны на использование в атмосфере, содержащей менее __% кислорода.', '18%', '25%', '20%', '18%'],
               '3': ['Что не относится к видам респираторов?', 'противоаэрозольные респираторы с расширенной защитой от сварочных аэрозолей', 'противоаэрозольные респираторы, снабженные клапаном выдоха', 'противоаэрозольные респираторы с расширенной защитой от сварочных аэрозолей', 'противоаэрозольные респираторы без дыхательного выдоха'],
               '4': ['Какие из перечисленных определений, согласно ТК РФ, соответствуют понятию «охрана труда»?', 'система учета жизни и здоровья сотрудников в процессе трудовой деятельности, включающая в себя правовые, социальноэкономические, организационно-технические, санитарногигиенические, лечебно-профилактические, реабилитационные и иные мероприятия', 'система учета жизни и здоровья сотрудников в процессе трудовой деятельности, включающая в себя правовые, социальноэкономические, организационно-технические, санитарногигиенические, лечебно-профилактические, реабилитационные и иные мероприятия', 'условия труда, при возникновении которых возникают вредные и (или) опасные производственные факторы, могут быть исключены уровни воздействия таких факторов, которые не превышают сочетания нормативов', 'совокупность факторов производственной среды и трудового процесса, оказывающих влияние на работоспособность и здоровье работника'],
               '5': ['Правила снятия респираторов:', 'cнимайте респираторы, используя ремешки', 'после этого использованный респиратор можно использовать повторно', 'перенос респиратора за переднюю часть', 'cнимайте респираторы, используя ремешки'],
               '6': ['Первое место среди профессионального окружения:', 'респираторные заболевания', 'заболевания суставов', 'респираторные заболевания', 'сердечно-сосудистые заболевания'],
               '7': ['Что не является средством индивидуальной защиты работника?', 'сезонная одежда', 'сезонная одежда', 'специальная обувь', 'обезвреживающие средства'],
               '8': ['Полумаска из изолирующего материала должна:', 'всё вышеперечисленное', 'хорошо сбалансирована', 'изготовлена из термопластика, выдерживающего высокую температуру или из силикона', 'всё вышеперечисленное'],
               '9': ['Как выбрать нормальный респиратор?', 'все вышеперечисленное', 'универсального респиратора не существует', 'все вышеперечисленное', 'респиратор должен плотно прилегать к лицу'],
               '10': ['Что не относится к всеобъемлющим средствам органов защиты дыхания:', 'респираторы', 'респираторы', 'противопылевые тканевые маски', 'ватно-марлевые повязки'],
               '11': ['Системы обеспечения безопасности должны выполняться в срок:', 'все перечисленное', 'все перечисленное', 'соблюдать эргономические требования и состояние здоровья работника', 'после закрытия подгонки соответствует полу, росту и размеру работника'],
               '12': ['Для чего выдаются средства индивидуальной защиты?', 'для защиты от обнаружения вредных и (или) опасных объектов производственной среды и (или) обнаружения, а также на работах, применяемых в определенных температурных условиях', 'для защиты занятых, занятых на работах с вредными и (или) опасными условиями труда', 'для защиты от захватов, задержанных на работах, подверженных заражению', 'для защиты от обнаружения вредных и (или) опасных объектов производственной среды и (или) обнаружения, а также на работах, применяемых в определенных температурных условиях'],
               '13': ['На основании чего возникают потребности индивидуальной защиты?', 'на основании оценки условий труда', 'на основании оценки условий труда', 'на основании жалобы работника на условия труда', 'на основании желания работодателя'],
               '14': ['Что не относится к классификации СИЗОД', 'перчатки', 'полумаски', 'самоспасатели', 'перчатки'],
               '15': ['Средства индивидуальной защиты не бывают:', 'поглощающий', 'изолирующими', 'поглощающий', 'фильтрующий'],
               '16': ['Стропы для остановки падения (страховочные) не должны быть повышены', '2 метра', '3 метра', '2 метра', '5 метров'],
               '17': ['Как выбрать нормальный респиратор?', 'всё вышеперечисленное', 'необходимо правильно оценить риски', 'всё вышеперечисленное', 'при повышенных и первоначальных температурах необходимо применять респираторы с клапаном выдоха'],
               '18': ['Дыхательные аппараты со сжатым воздухом', 'всё вышеперечисленное', 'подвесная система (ложемент)', 'баллон со сжатым воздухом', 'всё вышеперечисленное'],
               }


@login_required
def test_a(request, questions=[], unanswered_questions_answer=[]):
    # print(request.headers)

    # global questions
    # global unanswered_questions_answer
    # global answered
    # print(questions)
    student = AppUser.objects.filter(username=request.user).first()
    if student.result_score == 0:
        # Обнуляем значение ранее проходимых тестов

        student.result_general = 0
        student.read_general = 0
        student.save()
        unanswered_questions_answer = []

        # Набираем список вопросов с ответами из общего словаря
        while len(questions) < 28:
            question_1 = QUESTIONS_A[random.choice(list(QUESTIONS_A))]
            if question_1 not in questions:
                questions.append(question_1)
    student.result_score = student.result_general + student.read_general
    print(student.max_general)

    question = questions.pop()
    # print(question)

    if request.method == 'POST':
        if not student.result_score:
            question = questions.pop()
        student.result_score += 1
        student.save()
        check_answer = request.POST['answer'].split(';')
        # print(check_answer)
        # print(question[1])
        if check_answer[0] == check_answer[1]:
            student.result_general += 1
            student.save()
        else:
            list_unanswered = [check_answer[2], check_answer[0], check_answer[1]]
            unanswered_questions_answer.append(list_unanswered)
            student.read_general += 1
            student.save()

    context = {
        'title': f'СДО {NAME_ORGANIZATION}',
        'name': NAME_ORGANIZATION,
        'questions': question,
        'questions_list': questions,
        'student': student,
        'answered': student.result_score,
        'unanswered_questions_answer': unanswered_questions_answer
    }
    print(student.result_general)
    print(student.read_general)
    print(questions)
    print(student.result_score)
    student.save()
    if student.result_score < 27:
        return render(request, 'tests/test_a.html', context=context)
    else:
        # answered = 0
        context = {
            'title': f'СДО {NAME_ORGANIZATION}',
            'name': NAME_ORGANIZATION,
            'questions': question,
            'questions_list': questions,
            'student': student,
            'answered': student.result_score,
            'answered_right': student.result_general,
            'unanswered_questions_answer': unanswered_questions_answer
        }
        student.result_general = 0
        student.read_general = 0
        student.result_score = 0
        student.save()
        return render(request, 'tests/result_test_a.html', context=context)


@login_required
def test_b(request, questions=[], unanswered_questions_answer=[]):
    # print(request.headers)

    # global questions
    # global unanswered_questions_answer
    # global answered
    # print(questions)
    student = AppUser.objects.filter(username=request.user).first()
    if student.result_score == 0:
        # Обнуляем значение ранее проходимых тестов

        student.result_safe = 0
        student.read_safe = 0
        student.save()
        unanswered_questions_answer = []

        # Набираем список вопросов с ответами из общего словаря
        while len(questions) < 24:
            question_1 = QUESTIONS_B[random.choice(list(QUESTIONS_B))]
            if question_1 not in questions:
                questions.append(question_1)
    student.result_score = student.result_safe + student.read_safe
    print(student.max_safe)

    question = questions.pop()
    # print(question)

    if request.method == 'POST':
        if not student.result_score:
            question = questions.pop()
        student.result_score += 1
        student.save()
        check_answer = request.POST['answer'].split(';')
        # print(check_answer)
        # print(question[1])
        if check_answer[0] == check_answer[1]:
            student.result_safe += 1
            student.save()
        else:
            list_unanswered = [check_answer[2], check_answer[0], check_answer[1]]
            unanswered_questions_answer.append(list_unanswered)
            student.read_safe += 1
            student.save()

    context = {
        'title': f'СДО {NAME_ORGANIZATION}',
        'name': NAME_ORGANIZATION,
        'questions': question,
        'questions_list': questions,
        'student': student,
        'answered': student.result_score,
        'unanswered_questions_answer': unanswered_questions_answer
    }
    # print(student.result_general)
    # print(student.read_general)
    # print(questions)
    # print(student.result_score)
    student.save()
    if student.result_score < 23:
        return render(request, 'tests/test_b.html', context=context)
    else:
        # answered = 0
        context = {
            'title': f'СДО {NAME_ORGANIZATION}',
            'name': NAME_ORGANIZATION,
            'questions': question,
            'questions_list': questions,
            'student': student,
            'answered': student.result_score,
            'answered_right': student.result_safe,
            'unanswered_questions_answer': unanswered_questions_answer
        }
        student.result_safe = 0
        student.read_safe = 0
        student.result_score = 0
        student.save()
        return render(request, 'tests/result_test_b.html', context=context)


@login_required
def test_c(request, questions=[], unanswered_questions_answer=[]):

    student = AppUser.objects.filter(username=request.user).first()
    if student.result_score == 0:
        # Обнуляем значение ранее проходимых тестов
        student.result_danger = 0
        student.read_danger = 0
        student.save()
        unanswered_questions_answer = []

        # Набираем список вопросов с ответами из общего словаря
        while len(questions) < 10:
            question_1 = QUESTIONS_C[random.choice(list(QUESTIONS_C))]
            if question_1 not in questions:
                questions.append(question_1)
    student.result_score = student.result_danger + student.read_danger

    question = questions.pop()

    if request.method == 'POST':
        if not student.result_score:
            question = questions.pop()
        student.result_score += 1
        student.save()
        check_answer = request.POST['answer'].split(';')

        if check_answer[0] == check_answer[1]:
            student.result_danger += 1
            student.save()
        else:
            list_unanswered = [check_answer[2], check_answer[0], check_answer[1]]
            unanswered_questions_answer.append(list_unanswered)
            student.read_danger += 1
            student.save()

    context = {
        'title': f'СДО {NAME_ORGANIZATION}',
        'name': NAME_ORGANIZATION,
        'questions': question,
        'questions_list': questions,
        'student': student,
        'answered': student.result_score,
        'unanswered_questions_answer': unanswered_questions_answer
    }

    student.save()
    if student.result_score < 9:
        return render(request, 'tests/test_c.html', context=context)
    else:
        # answered = 0
        context = {
            'title': f'СДО {NAME_ORGANIZATION}',
            'name': NAME_ORGANIZATION,
            'questions': question,
            'questions_list': questions,
            'student': student,
            'answered': student.result_score,
            'answered_right': student.result_danger,
            'unanswered_questions_answer': unanswered_questions_answer
        }
        student.result_danger = 0
        student.read_danger = 0
        student.result_score = 0
        student.save()
        return render(request, 'tests/result_test_c.html', context=context)


@login_required
def test_d(request, questions=[], unanswered_questions_answer=[]):

    student = AppUser.objects.filter(username=request.user).first()
    if student.result_score == 0:
        # Обнуляем значение ранее проходимых тестов
        student.result_personal = 0
        student.read_personal = 0
        student.save()
        unanswered_questions_answer = []

        # Набираем список вопросов с ответами из общего словаря
        while len(questions) < 18:
            question_1 = QUESTIONS_D[random.choice(list(QUESTIONS_D))]
            if question_1 not in questions:
                questions.append(question_1)
    student.result_score = student.result_personal + student.read_personal

    question = questions.pop()

    if request.method == 'POST':
        if not student.result_score:
            question = questions.pop()
        student.result_score += 1
        student.save()
        check_answer = request.POST['answer'].split(';')

        if check_answer[0] == check_answer[1]:
            student.result_personal += 1
            student.save()
        else:
            list_unanswered = [check_answer[2], check_answer[0], check_answer[1]]
            unanswered_questions_answer.append(list_unanswered)
            student.read_personal += 1
            student.save()

    context = {
        'title': f'СДО {NAME_ORGANIZATION}',
        'name': NAME_ORGANIZATION,
        'questions': question,
        'questions_list': questions,
        'student': student,
        'answered': student.result_score,
        'unanswered_questions_answer': unanswered_questions_answer
    }

    student.save()
    if student.result_score < 17:
        return render(request, 'tests/test_d.html', context=context)
    else:
        # answered = 0
        context = {
            'title': f'СДО {NAME_ORGANIZATION}',
            'name': NAME_ORGANIZATION,
            'questions': question,
            'questions_list': questions,
            'student': student,
            'answered': student.result_score,
            'answered_right': student.result_personal,
            'unanswered_questions_answer': unanswered_questions_answer
        }
        student.result_personal = 0
        student.read_personal = 0
        student.result_score = 0
        student.save()
        return render(request, 'tests/result_test_d.html', context=context)


@login_required
def exit_test_a(request):

    student = AppUser.objects.filter(username=request.user).first()

    student.result_general = 0
    student.read_general = 0
    student.result_score = 0
    student.save()

    context = {
        'title': f'СДО {NAME_ORGANIZATION}',
        'name': NAME_ORGANIZATION,
    }
    return render(request, 'info/index.html', context=context)


@login_required
def exit_test_b(request):

    student = AppUser.objects.filter(username=request.user).first()

    student.result_safe = 0
    student.read_safe = 0
    student.result_score = 0
    student.save()

    context = {
        'title': f'СДО {NAME_ORGANIZATION}',
        'name': NAME_ORGANIZATION,
    }
    return render(request, 'info/index.html', context=context)


@login_required
def exit_test_c(request):

    student = AppUser.objects.filter(username=request.user).first()

    student.result_danger = 0
    student.read_danger = 0
    student.result_score = 0
    student.save()

    context = {
        'title': f'СДО {NAME_ORGANIZATION}',
        'name': NAME_ORGANIZATION,
    }
    return render(request, 'info/index.html', context=context)


@login_required
def exit_test_d(request):

    student = AppUser.objects.filter(username=request.user).first()

    student.result_personal = 0
    student.read_personal = 0
    student.result_score = 0
    student.save()

    context = {
        'title': f'СДО {NAME_ORGANIZATION}',
        'name': NAME_ORGANIZATION,
    }
    return render(request, 'info/index.html', context=context)
