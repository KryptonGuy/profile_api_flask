from datetime import datetime
from threading import active_count
from app import app, ma, db, api
from app.model import ProfileModel
from flask_restful import Resource
from flask_restful import reqparse
from flask_restful_swagger import swagger
from flask import abort
from marshmallow import fields
import markdown.extensions.fenced_code

# Profile Schema for serialization using marsahmallow

class ProfileSchema(ma.SQLAlchemySchema):
    class Meta:
        model = ProfileModel

    id = ma.auto_field()
    name = ma.auto_field()
    birthdate = ma.auto_field()
    status = ma.auto_field()

#Parser Arguments for Create
parser = reqparse.RequestParser()
parser.add_argument('name')
parser.add_argument('birthdate')
parser.add_argument('status')




resolve_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'birthdate': fields.DateTime,
    'status': fields.String,
}

profile_schema = ProfileSchema()

class Profile(Resource):

    #get request on "profiles"
    @swagger.operation()
    def get(self):
        profile_schema = ProfileSchema()
        all_profiles = ProfileModel.query.all() #querying all the existing profiles
        
        # Dictonary for response

        response = dict()
        response["created_at"] = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

        #if no database is empty
        if not all_profiles:
            response['data'] = "No profile exist in the databse"
            return response, 200

        total = len(all_profiles)
        data = []

        for profile in all_profiles:
            data.append(profile_schema.dump(profile)) #adding the profile object in Json

        response['data'] = data
        response['total'] = total

        return response, 200

    #POST request on 'profiles', Creates a new profile
    @swagger.operation()
    def post(self):
        profile_schema = ProfileSchema()
        args = parser.parse_args()

        #if None Arguments
        if args["name"]==None or args["birthdate"]==None:
            abort(400)

        #If Status not active or paused
        if args['status'] != None:
            if args['status'] not in ("ACTIVE", "PAUSED"):
                abort(400)

        profile = ProfileModel(name=args["name"], birthdate=args["birthdate"], status=args["status"])
        
        #Saving and Adding to Database
        db.session.add(profile)
        db.session.commit()

        #response
        response = dict()
        response["created_at"] = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        response["data"] = profile_schema.dump(profile)

        return response , 201

    def delete(self):
        abort(405)

    def put(self):
        abort(405)

#Parser Arguments for Update
update = reqparse.RequestParser() 
update.add_argument('name')
update.add_argument('birthdate')
update.add_argument('status')

class Edit(Resource):

    #GET request on 'profile/id', returns Profile
    @swagger.operation()
    def get(self, id):
        profile_schema = ProfileSchema()

        profile = ProfileModel.query.get(id) #querying to get profile with id

        response = dict()

        #if profiles does not exist
        if not profile:
            abort(404)
        
        #response
        response = dict()
        response["created_at"] = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        response["data"] = profile_schema.dump(profile)
        
        return response, 200

    @swagger.operation()
    def patch(self, id):
        args = update.parse_args()    
        profile_schema = ProfileSchema()

        profile = ProfileModel.query.get(id)

        #if the profile with given id does not exist
        if not profile:
            abort(404)
            
        # Updating given args
            
        if args['name']!= None:
            profile.name = args['name']

        if args['birthdate']!= None:
            profile.birthdate = args['birthdate']

        if args['status']!= None:
            profile.status = args['status']   

        db.session.commit()

        #response
        response = dict()
        response["created_at"] = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        response["message"] = "Profile Successfully added"
        response["data"] = profile_schema.dump(profile)

        return response, 200       

    def post(self, id):
        abort(405)

    def put(self, id):
        abort(405)

    @swagger.operation()
    def delete(self, id):
        profile = ProfileModel.query.get(id) #querying for profile

        #if profile does not exist
        if not profile:
            abort(404)

        db.session.delete(profile)
        db.session.commit()
        
        return {"message": "Profile deleted succesfully"}, 204


#For all ACTIVE Profiles
class Active(Resource):

    #GET request to get all ACTIVE profiles
    @swagger.operation()
    def get(self):
        status = "ACTIVE"

        profile_schema = ProfileSchema()
        all_profiles = ProfileModel.query.filter_by(status=status)
        
        # Dictonary for response

        response = dict()
        response["created_at"] = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

        #if no database is empty
        if not all_profiles:
            response['data'] = "No profile exist in the databse"
            return response, 200

        data = []

        for profile in all_profiles:
            data.append(profile_schema.dump(profile)) #adding the profile object in Json

        total = len(data)
        response['data'] = data
        response['total'] = total

        return response, 200


    def post(self):
        abort(405)   

    def delete(self):
        abort(405)


class Paused(Resource):

    #GET request to get all Paused profiles
    @swagger.operation()
    def get(self):
        status = "PAUSED"

        profile_schema = ProfileSchema()
        all_profiles = ProfileModel.query.filter_by(status=status)
        
        # Dictonary for response

        response = dict()
        response["created_at"] = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

        #if no database is empty
        if not all_profiles:
            response['data'] = "No profile exist in the databse"
            return response, 200

        data = []

        for profile in all_profiles:
            data.append(profile_schema.dump(profile)) #adding the profile object in Json

        total = len(data)
        response['data'] = data
        response['total'] = total

        return response, 200

    @swagger.operation()
    def POST(self):
        abort(405)   

    @swagger.operation()
    def DELETE(self):
        abort(405) 

#Documenting README file
@app.route("/doc")
def index():
    readme_file = open("README.md", "r")
    md_template_string = markdown.markdown(
        readme_file.read(), extensions=["fenced_code"]
    )

    return md_template_string


api.add_resource(Profile, '/profiles')
api.add_resource(Edit, '/profiles/<int:id>')
api.add_resource(Active, '/profiles/active')
api.add_resource(Paused, '/profiles/paused')