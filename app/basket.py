from app.models import Product, Offer

class Basket(object):

    @staticmethod
    def price_of(sku_array):
        basket = {}

        # SKUs and total quantities of each, into basket
        for item in sku_array:
            if item not in basket:
                basket[item] = 1
            else:
                basket[item] = basket[item] + 1

        # and now, empty the basket applying offers
        total_price = 0.0
        for sku in basket:
            prod = Product.query.filter_by(sku=sku).first()
            # see README.md - only one active offer per product, offers are per single product
# quantity <= qty in basket

            offs = Offer.query.filter_by(product_id=prod.id, enabled=True).first()

            print(prod)
            if offs != None:
                print(offs)
                #print(basket[sku]) # qty left


        return total_price
