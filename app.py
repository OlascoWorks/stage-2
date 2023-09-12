from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
import os

db = SQLAlchemy()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')

db.init_app(app=app)

# Person object table
class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)

# create database only when it hasn't been created
with app.app_context():
    db.create_all()

def update_person(id, new_name):
    person = Person.query.filter_by(id=id).first()
    person.name = new_name
    db.session.commit()
def delete_person(id):
    person = Person.query.filter_by(id=id).first()
    db.session.delete(person)
    db.session.commit()

# route for creating new person
@app.route('/api', methods=['GET', 'POST', 'PATCH', 'DELETE'])
def person_endpoint():
    if request.is_json:
        if request.method == 'GET':
            try:
                name = request.json["name"]
                person = Person.query.filter_by(name=name).first()
                res = {
                    "name": person.name,
                    "id": person.id
                }

                return jsonify(res), 200
            except AttributeError:
                return jsonify({ "message": f"There was an error processing the request. Person with name '{name}' does not exist."}), 400
            except Exception as e:
                return jsonify({ "message": f"There was an unexpected error processing the request. Error - {e}"}), 400
            
        elif request.method == 'POST':
            try:
                name = request.json["name"]
                person = Person.query.filter_by(name=name).first()
                if person:
                    return jsonify({ "message": f"There was an error creating person. Person with name '{name}' already exists."}), 400
                else:
                    new_person = Person(name=name)
                    db.session.add(new_person)
                    db.session.commit()
                    return jsonify({ "message": "Succesfully created new person"}), 201
            except IntegrityError:
                return jsonify({ "message": "'name' should be a unique value"}), 400
            except KeyError:
                return jsonify({ "message": "please provide a 'name' key"}), 400
            except ValueError:
                return jsonify({ "message": "'name' should be a string value"}), 400
            except Exception as e:
                return jsonify({ "message": f"There was an unexpected error processing the request. Error - {e}"}), 400
            
        elif request.method == 'PATCH':
            try:
                id = request.json['id']
                new_name = request.json['new_name']
                person = Person.query.filter_by(id=id).first()
                old_name = person.name
                if new_name != old_name:
                    update_person(person.id, new_name)
                    res = {
                        "message": "Successfully updated person",
                        "old_name": f"{old_name}",
                        "new_name": f"{person.name}",
                        "id": f"{person.id}"
                    }
                    return jsonify(res), 200
                else:
                    return jsonify({ "message": "Error! New name cannot be the same with old name" }), 400
            except KeyError:
                return jsonify({ "message": "please provide a 'new_name' key and an 'id' key"}), 400
            except ValueError:
                return jsonify({ "message": "'new_name' should be a string value"}), 400
            except AttributeError:
                return jsonify({ "message": f"could not find person with id - {id}"}), 400
            except Exception as e:
                return jsonify({ "message": f"There was an unexpected error processing the request. Error - {e}"}), 400
            
        elif request.method == 'DELETE':
                try:
                    id = request.json['id']
                    person = Person.query.filter_by(id=id).first()
                    delete_person(person.id)
                    return jsonify({ "message": f"successfully deleted person with id '{id}'" })
                except KeyError:
                    return jsonify({ "message": "please provide an 'id' key"}), 400
                except ValueError:
                    return jsonify({ "message": "'new_name' should be a string value"}), 400
                except AttributeError:
                    return jsonify({ "message": f"could not find person with id - {id}"}), 400
                except Exception as e:
                    return jsonify({ "message": f"There was an unexpected error processing the request. Error - {e}"}), 400
    else:
        return jsonify({ "message": 'The request is not in the right format. Please provide a json request' })


if __name__ == '__main__':
    app.run(debug=True)