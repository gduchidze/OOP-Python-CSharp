import sqlite3
import matplotlib.pyplot as plt
conn = sqlite3.connect("movies_ranking.sqlite")
cursor = conn.cursor()

# cursor.execute("SELECT * FROM movies")
#
# record = cursor.fetchone()
# print("Film = ", record[1])
#
# record = cursor.fetchone()
# print("Film = ", record[1])
#fetchone() მეთოდის გამოყენებისას შესაძლებელია გაშვებული SQL ბრძანების შედეგის თითო-თითოდ სტრიქონების დაბრუნება

# cursor.execute("SELECT * FROM movies WHERE year >= ?", (2005,))
# records = cursor.fetchmany(4)
# for record in records:
#     print(record)
#fetchmany(?) მეთოდში პარამეტრად გადაეცემა რიცხვი და აბრუნებს შესაბამისი რაოდენობის ჩანაწერს

# cursor.execute("SELECT * FROM movies WHERE year >= ?", (2000,))
# records = cursor.fetchall()
# for record in records:
#     print(record)
#fetchall() მეთოდით ხდება SQL ბრძანების შედეგის ერთიანად დაბრუნება და წარმოდგენილია სიის სახით, რომლის თითოეული ელემენტი არის ცხრილის სტრიქონი (ჩანაწერი) tuple ტიპის.

# Film = input("ფილმის სახელი: ")
# Year = input("გამოშვების წელი: ")
# Genre = input("ჟანრი: ")
# cursor.execute("INSERT INTO movies (Film, Year, Genre) VALUES (?, ?, ?)", (Film, Year, Genre))
# conn.commit()
#ცხრილში დაამატებს ახალ ჩანაწერ(ებ)ს, მომხარებლის მიერ (input-ით) შეყვანილი ინფორმაციის მიხედვით მე დავამატე ფილმი ბასიანი .

# old_genre = input("ჩაწერე ძველი ჟანრი: ")
# new_genre = input("ჩაწერე ახალი ჟანრი: ")
# cursor.execute("UPDATE movies SET Genre = ? WHERE Genre = ?", (new_genre, old_genre))
# conn.commit()
#UPDATE ბრძანების მეშვეობით შესაძლებელია ცხრილის მონაცემების შეცვლა. ამ შემთხვევაში მე Genre Animations მქონე ფილმებს Cartoon ჯანრი მივანიჭე

# Film = input("ჩაწერე ფილმის სახელი რომლის წაშლაც გსურს ბაზიდან: ")
# cursor.execute("DELETE FROM movies WHERE Film = ?", (Film,))
# conn.commit()
# DELETE  ბრძანების მეშვეობით შესაძლებელია ცხრილის მონაცემების წაშლა პირობის მიხედვით ,ამ ბრძანებით მე წავშალე ბაზიდან ფილმის მთლიანი მონაცემები ამ კონკრეტულ შემთხვევაში Inputs გადავეცი და ბაზიდან წავშალე ფილმი Tangled

# cursor.execute("SELECT Genre, COUNT(*) FROM movies GROUP BY Genre")
# rows = cursor.fetchall()
#
# labels = [row[0] for row in rows]
# values = [row[1] for row in rows]
#
# fig, ax = plt.subplots()
# ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
# ax.axis('equal')
#
# ax.set_title('Movies by Genre')
#
# plt.show()
#ჩემ დიაგრამაში წარმოდგენილია ბაზაში თითოეული ჟანრის პროცენტული რაოდენობა
conn.close()
