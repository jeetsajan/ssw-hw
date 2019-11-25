"""

@author: Jeet Sajan

    Flask Python application to flood the data from database into a table on a webpage

"""

from flask import Flask, render_template
import sqlite3

app = Flask(__name__)


@app.route('/instructors')
def instructors_summary():
    db_path = '/Users/jeetsajan/PycharmProjects/SSW810 Assignments/810_startup.db'

    try:
        db = sqlite3.connect(db_path)
    except sqlite3.OperationalError:
        return f"Error! Unable to open the database at {db_path}"
    else:
        query = "select i.CWID, i.Name, i.Dept, g.Course, count(*) as count from instructors i " \
                "join grades g on i.CWID = g.InstructorCWID group by g.Course, i.Name, i.Dept, i.CWID"

        data = [{'cwid': CWID, 'name': Name, 'dept': Dept, 'course': Course, 'students': count}
                for CWID, Name, Dept, Course, count in db.execute(query)]

        db.close()

    return render_template(
        'instructor.html',
        title='Stevens Repository',
        table_title='Instructors Summary',
        instructors=data
    )


app.run(debug=True)
