from flask_restplus import Namespace, fields


class VesselDto:
    api = Namespace('vessel', description='vessel related operations')
    vessel = api.model('vessel', {
        'name': fields.String(required=False, description='Vessel name'),
        'imo' : fields.String(required=False, description='Vessel IMO Number'),
        'vtype' : fields.String(required=False, description='', default='Dirty Oil Tankers'),
        'flag' : fields.String(required=False, description='Flag'),
        'yearbuilt' : fields.Integer(required=False, description='Year Built'),
        'shipyard' : fields.String(required=False, description='Shipyard'),
        'owner' : fields.String(required=False, description='Owner'),
        'operator': fields.String(required=False, description='Operator'),
        'vclass' : fields.String(required=False, description='Vessel Class'),
        'atex' : fields.String(required=False, description='Atex', default='Atex1'),
        'ais' : fields.String(required=False, description='AIS'),
        'mmsi' : fields.String(required=False, description='MMSI'),
        'grt' : fields.Integer(required=False, description='GRT'),
        'dwt' : fields.Integer(required=False, description='DWT'),
        'capacity' : fields.Integer(required=False, description='Capacity'),
        'length' : fields.Integer(required=False, description='Length'),
        'beam': fields.Integer(required=False, description='Beam'),
        'draft' : fields.Integer(required=False, description='Draft'),
        'DraftUnit' : fields.Integer(required=False, description='Draft Unit'),
        'LengthUnit': fields.Integer(required=False, description='Length Unit'),
        'BeamUnit' : fields.Integer(required=False, description='Beam Unit'),
        'techDetailsFileName' : fields.String(required=False, description='Technical Details'),
        'linearityFileName' : fields.String(required=False, description='ShipLinearityyard'),
        'q88FileName' : fields.String(required=False, description='Q88'),
        'sireReportFileName': fields.String(required=False, description='SIRE Report')

    })