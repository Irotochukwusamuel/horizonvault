from application.models import Country, State


class CountryModel:

    @staticmethod
    def CountryList():
        _country = Country.query.all()
        return [x.to_dict(add_filter=False) for x in _country]

    @staticmethod
    def get_states_by_country(country_id):
        _states = State.query.filter(State.country_id == country_id).all()
        return [x.to_dict(add_filter=False) for x in _states]
