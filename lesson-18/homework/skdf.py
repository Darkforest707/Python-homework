StackOverflow Q&A Tasks
import pandas as pd

# Загрузка данных
df = pd.read_csv('task\\stackoverflow_qa.csv')

# 1️ Вопросы, созданные до 2014 года
questions_before_2014 = df[pd.to_datetime(df['creationdate']) < '2014-01-01']
print("Questions before 2014:\n", questions_before_2014)

# 2️ Вопросы с оценкой больше 50
questions_score_gt_50 = df[df['score'] > 50]
print("\nQuestions with score > 50:\n", questions_score_gt_50)

# 3️ Вопросы с оценкой между 50 и 100
questions_score_50_100 = df[df['score'].between(50, 100)]
print("\nQuestions with score between 50 and 100:\n", questions_score_50_100)

# 4️ Вопросы, на которые ответил Scott Boston
questions_answered_by_scott = df[df['ans_name'] == 'Scott Boston']
print("\nQuestions answered by Scott Boston:\n", questions_answered_by_scott)

# 5️ Вопросы, на которые ответили 5 указанных пользователей
users = ['User1', 'User2', 'User3', 'User4', 'User5']  # замените на настоящие имена
questions_by_users = df[df['ans_name'].isin(users)]
print("\nQuestions answered by 5 users:\n", questions_by_users)

# 6️ Вопросы между мартом и октябрем 2014, отвеченные Unutbu, score < 5
mask = (
    (pd.to_datetime(df['creationdate']) >= '2014-03-01') &
    (pd.to_datetime(df['creationdate']) <= '2014-10-31') &
    (df['ans_name'] == 'Unutbu') &
    (df['score'] < 5)
)
questions_mar_oct_2014 = df[mask]
print("\nQuestions Mar-Oct 2014 answered by Unutbu with score < 5:\n", questions_mar_oct_2014)

# 7️ Вопросы с score между 5 и 10 или viewcount > 10000
questions_score_or_views = df[(df['score'].between(5, 10)) | (df['viewcount'] > 10000)]
print("\nQuestions with score 5-10 or viewcount > 10000:\n", questions_score_or_views)

# 8️ Вопросы, не отвеченные Scott Boston
questions_not_scott = df[df['ans_name'] != 'Scott Boston']
print("\nQuestions not answered by Scott Boston:\n", questions_not_scott)

Titanic Dataset Tasks
# Загрузка данных Titanic
titanic_df = pd.read_csv("task\\titanic.csv")

# 1️ Женщины в классе 1, возраст 20-30
female_class1_20_30 = titanic_df[
    (titanic_df['Sex'] == 'female') &
    (titanic_df['Pclass'] == 1) &
    (titanic_df['Age'].between(20, 30))
]
print("Female passengers Class 1, Age 20-30:\n", female_class1_20_30)

# 2️ Пассажиры, оплатившие более $100
fare_gt_100 = titanic_df[titanic_df['Fare'] > 100]
print("\nPassengers paid more than $100:\n", fare_gt_100)

# 3️ Выжившие, путешествующие одни
survived_alone = titanic_df[
    (titanic_df['Survived'] == 1) &
    (titanic_df['SibSp'] == 0) &
    (titanic_df['Parch'] == 0)
]
print("\nPassengers survived and alone:\n", survived_alone)

# 4️ Пассажиры из порта 'C', платившие >$50
embarked_C_fare_gt50 = titanic_df[
    (titanic_df['Embarked'] == 'C') &
    (titanic_df['Fare'] > 50)
]
print("\nPassengers embarked from C and paid >50:\n", embarked_C_fare_gt50)

# 5️ Пассажиры с родственниками и детьми на борту
with_sibsp_parch = titanic_df[
    (titanic_df['SibSp'] > 0) &
    (titanic_df['Parch'] > 0)
]
print("\nPassengers with siblings/spouses and parents/children:\n", with_sibsp_parch)

# 6️ Пассажиры ≤15 лет, не выжившие
young_not_survived = titanic_df[
    (titanic_df['Age'] <= 15) &
    (titanic_df['Survived'] == 0)
]
print("\nPassengers aged <=15 who did not survive:\n", young_not_survived)

# 7️ Пассажиры с известными каютами и Fare >200
cabin_fare_gt200 = titanic_df[
    titanic_df['Cabin'].notna() &
    (titanic_df['Fare'] > 200)
]
print("\nPassengers with cabins and fare >200:\n", cabin_fare_gt200)

# 8️ Пассажиры с нечётными PassengerId
odd_passengerid = titanic_df[titanic_df['PassengerId'] % 2 == 1]
print("\nPassengers with odd PassengerId:\n", odd_passengerid)

# 9️ Пассажиры с уникальными Ticket
unique_tickets = titanic_df[titanic_df['Ticket'].duplicated(keep=False) == False]
print("\nPassengers with unique tickets:\n", unique_tickets)

# 10️ Женщины с 'Miss' в имени, Class 1
miss_class1 = titanic_df[
    (titanic_df['Name'].str.contains('Miss')) &
    (titanic_df['Pclass'] == 1)
]
print("\nFemale passengers with 'Miss' in Name, Class 1:\n", miss_class1)
