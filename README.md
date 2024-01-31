Технические требования
● Django 2.1+ / Flask 1.0+
● PostgreSQL 10+
● Python 3.7+


При выполнении тестового задания Вы можете дополнительно использовать любые
сторонние Python и/или Javascript/CSS библиотеки, без всяких ограничений. Все 3rd
party Python/Javascript/CSS библиотеки должны быть добавлены в проект через
pip/bower/npm/yarn если библиотека поддерживает такой способ установки. У нас
нет никаких требований к оформлению фронтенд части, но аккуратный вид
приветствуется и добавим вам бонусных пунктов.

Часть No1 (обязательная)

Создайте веб страницу, которая будет выводить список заявок на оплату.
● Информация о каждой заявке должна храниться в базе данных и
содержать следующие данные:
○ ID заявки;
○ Сумма;
Реквизиты;
Статус (Ожидает оплаты, Оплачена, Отменена)
● Реквизиты должны быть отдельной таблицей, содержащей следующую информацию: тип платежа (карта, платежный счет), тип карты/счета, ФИО владельца, номер телефона, лимит
● База данных должна содержать не менее 5000 заявок и 100 реквизитов.


Часть No2 (опциональная)
1. Создайте базу данных используя миграции Django.
2. Используйте DB seeder для Django ORM для заполнения
базы данных.
3. Используйте Twitter Bootstrap для создания базовых стилей Вашей страницы.
4. Создайте еще одну страницу и выведите на ней список реквизитов со всей
имеющейся о них информацией из базы данных и возможностью
сортировать по любому полю.
5. Добавьте возможность поиска реквизитов по любому полю для страницы
созданной в задаче 4.
6. Добавьте возможность сортировать (и искать если Вы выполнили задачу No5)
по любому полю без перезагрузки страницы, например используя ajax.
7. Используя стандартные функции Django, осуществите аутентификацию
пользователя для раздела веб сайта доступного только для
зарегистрированных пользователей (создайте таблицу пользователей содержащую роли - пользователь/администратор).
8. Перенесите функционал разработанный в задачах 4, 5 и 6 (используя ajax
запросы) в раздел доступный только для зарегистрированных пользователей. Обычные пользователи видят только список реквизитов, администраторы все таблицы
9. Реализуйте с помощью FlaskAPI/Django REST framework API методы:
	create_invoice (на входе тип реквизитов и сумма, на выходе id заявки и реквизиты)
	get_ivoice_status (на входе id заявки, на выходе статус заявки)
10. С помощью Swagger или Django REST framework создайте описание методов из задачи 9
