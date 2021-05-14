from scripts.database import db
from typing import Callable


class BaseModel(db.Model):
    __abstract__ = True

    @staticmethod
    def create_commit(new_entry):
        try:
            db.session.add(new_entry)
            db.session.commit()
            return new_entry.id
        except Exception as e:
            print("create commit", e)
            return False

    @staticmethod
    def create(new_entry):
        try:
            db.session.add(new_entry)
            return new_entry.id
        except Exception as e:
            print("create", e)
            return False

    @classmethod
    def read(cls, id_) -> Callable[..., "BaseModel"]:
        return BaseModel.query.get(id_)

    def update(self):
        try:
            db.session.commit()
            return self.id
        except Exception as e:
            print("update", e)
            return False

    def delete(self):
        try:
            db.session.delete(self)
            return self.id
        except Exception as e:
            print("delete", e)
            return False

    def commit(self):
        try:
            db.session.commit()
            return True
        except Exception as e:
            print("commit", e)
            return False

    def delete_commit(self):
        try:
            db.session.delete(self)
            db.session.commit()
            return self.id
        except Exception as e:
            print("delete commit", e)
            return False

    @staticmethod
    def object_dump(obj_name, obj_inst):
        def dig_deep(prop_value):
            dd_str = prop_value
            if (
                    type(prop_value).__str__ is object.__str__
                    and not isinstance(prop_value, str)
                    and not isinstance(prop_value, dict)
            ):
                dd_str = BaseModel.object_dump(
                    prop_value.__class__.__name__, prop_value
                )
            return str(dd_str)

        obj_vars = sorted(
            [
                x
                for x in tuple(set(obj_inst.__dict__))
                if not x.startswith("__") and not x.startswith("_sa_instance_state")
            ]
        )
        return "{}({})".format(
            obj_name,
            ", ".join(
                [
                    "{}={}".format(var, dig_deep(getattr(obj_inst, var)))
                    for var in obj_vars
                ]
            ),
        )

    def __repr__(self):
        obj_vars = sorted(
            [
                x
                for x in tuple(set(self.__dict__))
                if not x.startswith("__") and x != "_sa_instance_state"
            ]
        )
        return "{}({})".format(
            self.__class__.__name__,
            ", ".join(["{}={}".format(var, getattr(self, var)) for var in obj_vars]),
        )

    def serialize(self):
        fields = {}
        for key, value in self.__dict__.items():
            if not key.startswith("_") and key != "metadata":
                fields[key] = value
        return fields

class ChuckSteps(BaseModel):
    __tablename__ = 'chuck_steps'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    duration = db.Column(db.Integer)
    distance = db.Column(db.Integer)
    position_values = db.Column(db.JSON)
    start_lat = db.Column(db.Float, nullable=False)
    start_long = db.Column(db.Float, nullable=False)
    end_lat= db.Column(db.Float, nullable=False)
    end_long = db.Column(db.Float, nullable=False)
    median_lat = db.Column(db.Float, nullable=False)
    median_long = db.Column(db.Float, nullable=False)
    route_name_id = db.Column(db.Integer)
    file_name = db.Column(db.String(512))
    timestamp = db.Column(db.DateTime)
    shorty_values = db.Column(db.JSON)
    sv2 = db.Column(db.JSON)


    @classmethod
    def read(cls, id_) -> "ChuckSteps":
        return ChuckSteps.query.get(id_)

class RouteNames(BaseModel):
    __tablename__ = 'route_names'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    route_name = db.Column(db.String(256), nullable=False)
    example_id = db.Column(db.Integer)


    @classmethod
    def read(cls, id_) -> "RouteNames":
        return RouteNames.query.get(id_)