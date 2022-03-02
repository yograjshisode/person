from flask import request
from flask_restful import Resource
from flask_api import status
from app import db, logger
from app.models.person import Person
from app.utils.response_generator import ResponseGenerator


class PersonView(Resource):

    def get(self, person_id):
        """
        Get list persons
        """
        try:
            person_data = Person.query.get(person_id)
            if person_data:
                return ResponseGenerator(data=person_data.serialize,
                                         message="Successfully Returned Cloud Providers List",
                                         status_code=status.HTTP_200_OK).make_success_response()
            else:
                message = f'No person info found for id {person_id}'
                return ResponseGenerator(message={"message": message},
                                         status_code=status.HTTP_404_NOT_FOUND).make_error_response()
        except Exception as e:
            return ResponseGenerator(message={"message": str(e)},
                                     status_code=status.HTTP_400_BAD_REQUEST).make_error_response()



    def post(self):
        """
        Add person
        """
        try:
            # Read form data from request and convert it to json
            data = request.json

            # Insert application details in the database
            person_data = Person(name=data['name'], address=data['address'], email=data['email'],
                                 mobile_number=data['mobile_number'])
            db.session.add(person_data)
            db.session.flush()
            db.session.refresh(person_data)

            response = person_data.serialize
            db.session.commit()
            message = "Person added successfully"
            logger.debug(message)
            return ResponseGenerator(data=response,
                                     message=message,
                                     status_code=status.HTTP_201_CREATED). \
                make_success_response()
        except KeyError as e:
            db.session.rollback()
            error_message = f"Please provide {e} parameter "
            logger.error(error_message)
            return ResponseGenerator(message=error_message,
                                     status_code=status.HTTP_400_BAD_REQUEST).make_error_response()
        except Exception as e:
            db.session.rollback()
            logger.exception(e)
            return ResponseGenerator(message=str(e),
                                     status_code=status.HTTP_400_BAD_REQUEST).make_error_response()


    def put(self, person_id):
        """
        Add person
        """
        try:
            data = request.json
            person_data = Person.query.get(person_id)
            if person_data:
                person_data.name = data.get("name", person_data.name)
                person_data.address = data.get("address", person_data.address)
                person_data.email = data.get("email", person_data.email)
                person_data.mobile_number = data.get("mobile_number", person_data.mobile_number)

                db.session.commit()
                db.session.refresh(person_data)
                response = person_data.serialize
                db.session.commit()
                message = "Person updated successfully"
                logger.debug(message)
                return ResponseGenerator(data=response,
                                         message=message,
                                         status_code=status.HTTP_200_OK).make_success_response()
            else:
                message = f'No person info found for id {person_id}'
                return ResponseGenerator(message={"message": message},
                                         status_code=status.HTTP_404_NOT_FOUND).make_error_response()
        except KeyError as e:
            db.session.rollback()
            error_message = f"Please provide {e} parameter "
            logger.error(error_message)
            return ResponseGenerator(message=error_message,
                                     status_code=status.HTTP_400_BAD_REQUEST).make_error_response()
        except Exception as e:
            db.session.rollback()
            logger.exception(e)
            return ResponseGenerator(message=str(e),
                                     status_code=status.HTTP_400_BAD_REQUEST).make_error_response()



    def delete(self, person_id):
        """Delete person"""
        try:
            # Fetch existing details from database
            person_data = Person.query.get(person_id)
            if person_data:
                db.session.delete(person_data)
                db.session.commit()
                message = f"Person {person_id} Deleted Successfully"
                logger.debug(message)
                return ResponseGenerator(data={"message": message},
                                         status_code=status.HTTP_200_OK).make_success_response()
            else:
                message = f'No person info found for id {person_id}'
                return ResponseGenerator(message={"message": message},
                                         status_code=status.HTTP_404_NOT_FOUND).make_error_response()
        except Exception as e:
            return ResponseGenerator(message="Exception: {}".format(e),
                                     status_code=status.HTTP_400_BAD_REQUEST).make_error_response()
