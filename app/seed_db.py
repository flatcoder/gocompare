from flask_script import Command, Option
from app.models import Product, Offer

# Simple management command to populate initial database
class SeedDBCommand(Command):
    """ Seed the database """

    # SKU, price
    products = [ [ "A", 50.0 ],
                 [ "B", 30.0 ],
                 [ "C", 20.0 ],
                 [ "D", 15.0 ],
               ]

    def run(self):
        for atype in self.products:
            try:
                prod = Product.create(atype[0],"","",atype[1])
            except Exception as e:
                # already exists, but confirm so (will rethrow)
                prod = Product.query.filter_by(sku=atype[0]).first()

        prod_a = Product.query.filter_by(sku="A").first()
        prod_b = Product.query.filter_by(sku="B").first()

        try:
            offer_1 = Offer.create(prod_a.id, 130.0, 3, True)
            offer_2 = Offer.create(prod_b.id, 45.0, 2, True)
        except:
            # already exists, but confirm so (will rethrow)
            offer_1 = Offer.query.filter_by(product_id=prod_a.id).first()
            offer_2 = Offer.query.filter_by(product_id=prod_b.id).first()

        return True
