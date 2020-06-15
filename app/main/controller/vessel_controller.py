from flask import request, Flask, render_template
from flask_restplus import Resource
from flask_cors import cross_origin
from werkzeug import secure_filename
from ..util.dto import VesselDto
from ..service.vessel_service import save_new_vessel, get_all_vessels, get_a_vessel

api = VesselDto.api
_vessel = VesselDto.vessel


@api.route('/')
class VesselList(Resource):
    @api.doc('list_of_registered_vessels')
    @api.marshal_list_with(_vessel, envelope='data')
    def get(self):
        """List all registered vessels"""
        return get_all_vessels()


@api.route('/<id>')
@api.param('id', 'The Vessel identifier')
@api.response(404, 'Vessel not found.')
class GetVessel(Resource):
    @api.doc('get a vessel')
    @api.marshal_with(_vessel)
    def get(self, id):
        return get_a_vessel(id)


@api.route('/newVessel')
class NewVessel(Resource):
    @api.response(201, 'Vessel successfully created.')
    @api.doc('create a new vessel')
    @api.expect(_vessel, validate=False)
    @cross_origin()
    def post(self):
        data = request.json
        return save_new_vessel(data=data)
