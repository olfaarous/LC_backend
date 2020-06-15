from flask_restplus import Namespace, fields


class VesselDto:
    api = Namespace('vessel', description='vessel related operations')
    vessel = api.model('vessel', {
        'name': fields.String(required=True, description='Vessel name'),
        'imo' : fields.String(required=True, description='Vessel IMO Number'),
        'vtype' : fields.String(required=True, description='', default='Dirty Oil Tankers'),
        'flag' : fields.String(required=True, description='Flag'),
        'yearbuilt' : fields.Integer(required=False, description='Year Built'),
        'shipyard' : fields.String(required=True, description='Shipyard'),
        'owner' : fields.String(required=True, description='Owner'),
        'operator': fields.String(required=True, description='Operator'),
        'vclass' : fields.String(required=True, description='Vessel Class'),
        'atex' : fields.String(required=True, description='Atex', default='Atex1'),
        'ais' : fields.String(required=True, description='AIS'),
        'mmsi' : fields.String(required=True, description='MMSI'),
        'grt' : fields.Integer(required=False, description='GRT'),
        'dwt' : fields.Integer(required=False, description='DWT'),
        'capacity' : fields.Integer(required=False, description='Capacity'),
        'length' : fields.Integer(required=False, description='Length'),
        'beam': fields.Integer(required=False, description='Beam'),
        'draft' : fields.Integer(required=False, description='Draft'),
    })