
from app.models.vaccine_model import Vaccine
from flask import request, jsonify, current_app
from http import HTTPStatus
from datetime import datetime, timedelta
from sqlalchemy.exc import IntegrityError

    

def insert_vaccine():
    try:
        data = request.get_json()
        
        for d in data.values():
            if type(d) != str:
                return jsonify({"error": "Todos os campos precisam ser tipo String"}), HTTPStatus.BAD_REQUEST
        for k in data.keys():
            if k != 'name' and k != 'cpf' and k != 'vaccine_name' and k != 'health_unit_name':
                ...
                # return jsonify({"error": "Foram informados mais campos que o permitido"}), HTTPStatus.BAD_REQUEST
        data_dict = {
            "name" : data['name'].upper(),
            "cpf" : data['cpf'],
            "first_shot_date" : datetime.now(),
            "second_shot_date" : datetime.now() + timedelta(days=90),
            "vaccine_name" : data['vaccine_name'].upper(),
            "health_unit_name" : data['health_unit_name'].upper()
        }
        if len(data["cpf"]) == 11 and data["cpf"].isnumeric():
            data_dict["cpf"] = data["cpf"]
        else:
            return jsonify({"msg": "CPF precisa conter 11 dígitos numéricos"}), HTTPStatus.BAD_REQUEST

        vaccine = Vaccine(**data_dict)

        current_app.db.session.add(vaccine)
        current_app.db.session.commit()

        return jsonify(vaccine), HTTPStatus.CREATED
    except KeyError:
        return jsonify({"error": "Todos os campos são obrigatórios: name, cpf, vaccine_name, health_unit_name"}), HTTPStatus.BAD_REQUEST
    except IntegrityError:
        return jsonify({"error": "CPF já cadastrado no banco de dados"}),HTTPStatus.CONFLICT    
def show_list_vaccinations():
    vacinas = (
      Vaccine
      .query
      .all()
    )
    return jsonify(vacinas)
