# section3__Q.py

import sqlite3


conn = sqlite3.connect(':memory:')
c = conn.cursor()


c.execute("CREATE TABLE StudentScores (name TEXT, subject TEXT, marks INTEGER)")


c.execute("INSERT INTO StudentScores VALUES ('Alice', 'Math', 75)")
c.execute("INSERT INTO StudentScores VALUES ('Bob', 'Science', 55)")
c.execute("INSERT INTO StudentScores VALUES ('Charlie', 'Math', 35)")
c.execute("INSERT INTO StudentScores VALUES ('Daisy', 'English', 82)")
c.execute("INSERT INTO StudentScores VALUES ('Ethan', 'Science', 29)")
c.execute("INSERT INTO StudentScores VALUES ('Fiona', 'Math', 91)")


print("All Students:")
for row in c.execute("SELECT * FROM StudentScores"):
    print(row)


c.execute("SELECT AVG(marks) FROM StudentScores")
avg = c.fetchone()[0]
print("\nAverage Marks:", round(avg, 2))


print("\nStudents scoring below 40:")
for row in c.execute("SELECT * FROM StudentScores WHERE marks < 40"):
    print(row)


conn.close()