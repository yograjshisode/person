from app import api
from app.views.person import PersonView

# Common Utility API's
api.add_resource(PersonView, '/api/person/<int:person_id>', '/api/person')
