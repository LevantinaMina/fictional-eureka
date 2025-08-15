#ФУНКЦИЯ, КОТОРАЯ ПРИНИМАЕТ НА ВХОД СПИСОК ВОПРОСОВ ОТ ПОЛЬЗОВАТЕЛЕЙ И ВОЗВРАЩАЕТ СПИСОК ОТВЕТОВ ПОДДЕРЖКИ
#ОТВЕТЫ НА ВОПРОСЫ ДОЛЖНЫ ГЕНЕРИРОВАТЬСЯ АВТОМАТИЧЕСКИ, НО В СООТВЕТСТВИИ С КЛЮЧЕВЫМИ СЛОВАМИ В ВОПРОСЕ
def customer_support_simulator(questions):
   responses = []
   for question in questions:
       question = question.lower()
       if 'ошибка' in question:
           responses.append("Мы извиняемся за причиненные неудобства. Наши специалисты уже работают над этой ошибкой.")
       elif 'заказ' in question:
           responses.append("Ваш заказ обрабатывается. Мы уведомим вас, как только он будет отправлен.")
       elif 'вернуть' in question:
           responses.append("Вы можете вернуть товар в течение 14 дней с момента получения.")
       else:
           responses.append("Благодарим вас за обращение. Ваш вопрос передан специалистам.")
   return responses



#ФУНКЦИЯ, КОТОРАЯ ВОЗВРАЩАЕТ СПИСОК ПОЛЬЗОВАТЕЛЕЙ, ОТСОРТИРОВАННЫХ ПО УРОВНЮ АКТИВНОСТИ В ПОРЯДКЕ УБЫВАНИЯ
def sort_users_by_activity(user_activity):
    return sorted(user_activity.keys(), key=lambda x: -user_activity[x])
#user_activity = {"user1": 10, "user2": 5, "user3": 20, "user4": 15, "user5": 10}
#print(sort_users_by_activity(user_activity))



#ФУНКЦИЯ, КОТОРАЯ ПРИНИМАЕТ СПИСОК СПИСКОВ, И КЛЮЧЕВЫЕ АРГУМЕНТЫ, КОТОРЫЕ ОПРЕДЕЛЯЮТ, КАКУЮ СТАТИСТИКУ НУЖНО ВЕРНУТЬ:
#ОБЩИЙ ДОХОД ИЛИ КОЛИЧЕСТВО ПРОДАННЫХ ЕДЕНИЦ КАЖДОГО ТОВАРА
def sales_stats(data, **kwargs):
   revenue = sum([item[1]*item[2] for item in data]) if kwargs.get('revenue') else None
   if kwargs.get('quantity'):
       quantity = {}
       for item in data:
           if item[0] in quantity:
               quantity[item[0]] += item[1]
           else:
               quantity[item[0]] = item[1]
   else:
       quantity = None
   return revenue, quantity

#sales_data = [["яблоки", 10, 20], ["груши", 5, 30], ["яблоки", 7, 20]]
#print(sales_stats(sales_data, revenue=True))
## (490, None)
#print(sales_stats(sales_data, quantity=True))
## (None, {'яблоки': 17, 'груши': 5})
#print(sales_stats(sales_data, customers=True))
## (None, None)



#ФУНКЦИЯ, КОТОРАЯ АВТОМАТИЧЕСКИ СОЗДАЕТ ОТЧЕТЫ О СРЕДНЕМ ДОХОДЕ И ОБЩЕМ КОЛИЧЕСТВЕ ПРОДАННЫХ ЕДЕНИЦ ТОВАРА
#ФУНКЦИЯ ПРИНИМАЕТ НА ВХОД ДАННЫЕ О ПРОДАЖАХ И ФУНКЦИЮ, КОТОРУЮ НУЖНО ИСПОЛЬЗОВАТЬ ДЛЯ ОБРАБОТКИ ЭТИХ ДАННЫХ
def create_report(data, func):
   revenue, quantity = func(data, revenue=True, quantity=True)
   report = f"Средний доход за данный период составил {revenue/len(data)}.\n"
   report += "Количество проданных единиц каждого товара:\n"
   for item, qty in quantity.items():
       report += f"{item}: {qty}\n"
   return report

def dummy_func(data, **kwargs):
    revenue = 100.0
    quantity = {"Apple": 10, "Orange": 5}
    return revenue, quantity
print(create_report([('Apple', 10, 0.5), ('Orange', 5, 0.6)], dummy_func))