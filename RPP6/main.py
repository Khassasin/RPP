from peewee import *
import cherrypy

db = SqliteDatabase('people.db')


class Person(Model):
    number = IntegerField()
    reason = CharField()
    is_solved = BooleanField()

    class Meta:
        database = db  # модель будет использовать базу данных 'people.db'


class Root(object):

    @cherrypy.expose
    def index(self):
        db.connect()
        str_out = "<head>LAB6</head><body><table><tr><th>id</th><th>number</th><th>reason</th><th>is_solved</th></tr><tr>"
        for person in Person.select():
            str_out += '<th>' + str(person.id) + '</th><th>' + str(person.number) + '</th><th>' + person.reason \
                       + '</th><th>' + str(person.is_solved) + '</th></tr>'
        str_out += """</table><form method="get" action="add_row">
              <label for="number">Number </label>
              <input type="number" name="number" /><br>
              <label for="reason">Reason </label>
              <input type="text" name="reason" /><br>
              <label for="status">Is solved </label><br>
              True <input type="checkbox" name="status" value="true"/><br>
              False <input type="checkbox" name="status" value="false"/><br>
              <button type="submit">Submit</button>
            </form>
            <form method="get" action="update_row">
              <label for="id">ID </label>
              <input type="number" name="id" /><br>
              <label for="number">Number </label>
              <input type="number" name="number" /><br>
              <label for="reason">Reason </label>
              <input type="text" name="reason" /><br>
              <label for="status">Is solved </label><br>
              True <input type="checkbox" name="status" value="true"/><br>
              False <input type="checkbox" name="status" value="false"/><br>
              <button type="submit">Submit</button>"""
        db.close()
        return str_out

    @cherrypy.expose()
    def add_row(self, number, reason, status):
        db.connect()
        b_status = False
        if status == "true":
            b_status = True
        Person.create(number=number, reason=reason, is_solved=b_status)
        db.close()
        raise cherrypy.HTTPRedirect("/")

    @cherrypy.expose()
    def update_row(self, id, number, reason, status):
        db.connect()
        b_status = ''
        if status == "true":
            b_status = True
        elif status == "false":
            b_status = False
        row_count = Person.select().count()
        if 0 <= int(id) <= row_count:
            person = Person.get(Person.id == id)
            if number == '':
                number = person.number
            if reason == '':
                reason = person.reason
            if status == '':
                b_status = person.is_solved
            person.number = number
            person.reason = reason
            person.is_solved = b_status
            person.save()
            # person.update(number=number, reason=reason, is_solved=b_status).where(person.id == id).execute()
        else:
            return "NO SUCH ID"
        db.close()
        raise cherrypy.HTTPRedirect("/")


if __name__ == '__main__':
    cherrypy.quickstart(Root(), '/')
