from flask_script import Command, Option
from app.models import Product, Offer
from app.config import app_config
from app import create_app
from app.models import db
from app.seed_db import SeedDBCommand
from app.basket import Basket
from flask import Flask
from datetime import datetime, timedelta
from flask_sqlalchemy import SQLAlchemy
import unittest

class TestBase(unittest.TestCase):
    def setUp(self):
        print("\nCREATE DATABASE")
        db.create_all()
        print("SEED DATABASE")
        sc = SeedDBCommand()
        res = sc.run()

    def tearDown(self):
        print("TEAR DOWN DATABASE")
        db.session.remove()
        db.drop_all()

class CreateTestApp(TestBase):
    def test(self):
        print("Testing DB Ok")
        self.assertIsInstance(db, SQLAlchemy, "Failed  - Database access!")

class TestModels(TestBase):
    def test(self):
        print("Testing 'all' and 'filter' for...")

        print("Products")
        data = Product.query.filter().all()
        self.assertTrue( len(data) > 0, "No Products in database!")
        if len(data) > 0:
            self.assertIsInstance(data[0], Product, "Failed - Products model!")

        print("Offers")
        data = Offer.query.filter().all()
        self.assertTrue( len(data) > 0, "No Offers in database!")
        if len(data) > 0:
            self.assertIsInstance(data[0], Offer, "Failed - Offers model!")

class TestBasket(TestBase):
    def test(self):
        print("Testing basket functionality")

        print("PRODUCTS in basket, single, multiple.")
        self.assertEquals(50.0, Basket.price_of(["A",]))
        self.assertEquals(80.0, Basket.price_of(["A","B"]))
        self.assertEquals(115.0, Basket.price_of(["C","D","B","A"]))
        self.assertEquals(100.0, Basket.price_of(["A","A"]))

        print("PRODUCTS of same type in basket, no offers")
        self.assertEquals(100.0, Basket.price_of(["C","C","C","C","C"]))

        print("An OFFER is applicable.")
        self.assertEquals(130.0, Basket.price_of(["A","A","A"]))
        self.assertEquals(45.0, Basket.price_of(["B","B"]))

        print("More than 1 OFFER is applicable, cart is jumbled up.")
        self.assertEquals(175.0, Basket.price_of(["A","B","A","B","A"]))

        # Multiple Offers of same and different type
        print("Multiple OFFERS of the same and different type.")
        self.assertEquals(350.0, Basket.price_of(["A","A","A","B","B","A","A","A","B","B"]))

        # Left over items - i.e., offer then some left over at full price
        print("OFFERS where some left in basket get full price.")
        self.assertEquals(75.0, Basket.price_of(["B","B","B"]))

class TestDDCommand(Command):
    """TDD Management Command"""

    def run(self):
        # Create and seed the database
        self._integration_testing([TestModels,TestBasket])

    def _integration_testing(self, unittests):
        for ut in unittests:
            suite = unittest.TestLoader().loadTestsFromTestCase(ut)
            unittest.TextTestRunner(verbosity=2).run(suite)
