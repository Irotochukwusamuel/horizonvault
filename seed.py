import sys
from os.path import dirname, abspath

sys.path.append(dirname(abspath(__file__)))

from sqlalchemy.exc import IntegrityError
from config.countries import countries_data
from application import db, app
from application.models import *


class Seed:

    @staticmethod
    def populate_country():
        country_data = countries_data['data']

        for x in country_data:
            try:
                add_country = Country(country_name=x['name'], country_code=x['iso3'])
                add_country.save()
            except IntegrityError:
                db.session.rollback()
                continue

        print("Country DB has been populated")

    @staticmethod
    def populate_states():
        country_data = countries_data['data']
        state_length = len(country_data)
        print()
        count = 0
        for x in country_data:
            fetch_country = Country.query.filter_by(country_name=x['name']).first()
            for y in x['states']:
                count += 1
                try:
                    state_exist = State.query.filter_by(state_name=y['name']).first()
                    if not state_exist:
                        add_state = State(state_name=y['name'], country=fetch_country)
                        add_state.save(refresh=True)
                    print(f'{count} of {state_length} states have been added successfully')
                except IntegrityError:
                    db.session.rollback()
                    continue

        print("States DB has been populated")

    @staticmethod
    def add_coins():
        wallet_symbols = open('crypto_names_and_symbols.csv', 'r')
        for x in wallet_symbols:
            name, symbol = x.split(',')
            if name != "Name":
                try:
                    print(f"Adding {name} coin")
                    coin_exist = Coins.query.filter(Coins.name == name).first()
                    if not coin_exist:
                        coin = Coins(name=name, symbol=symbol.strip())
                        coin.save(refresh=True)
                except Exception as e:
                    db.session.rollback()
                    continue
        print(f"Completed coin population")

    def RunSeed(self):
        """
             Implementation scripts to automate the creation of the database and seeding with initial data.
             This ensures that all developers have the same initial data for testing and development.
        """
        # self.populate_country()
        # self.populate_states()
        self.add_coins()


with app.app_context():
    # Create and add records to the database
    Seed().RunSeed()
