from sqlalchemy.ext.declarative import DeclarativeMeta
import json, logging, datetime

'''Uses to convert objects returned by Alchemy to json'''
class AlchemyEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            # an SQLAlchemy class
            fields = {}
            for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                data = obj.__getattribute__(field)
                # Manages the dates
                if isinstance(data, datetime.date):
                    data = data.strftime("%d/%m/%Y")
                try:
                    json.dumps(data) # this will fail on non-encodable values, like other classes
                    fields[field] = data
                except TypeError:
                    logging.warning(field + " can't be json encoded")
            # a json-encodable dict
            return fields

        return json.JSONEncoder.default(self, obj)