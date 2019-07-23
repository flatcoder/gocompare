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
            offs = Offer.query.filter_by(product_id=prod.id, enabled=True).first()

            if offs != None:
                while basket[sku] > 0:
                    if offs.quantity <= basket[sku]:
                        # print("GOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO COMPARE")
                        total_price = total_price + offs.price
                        basket[sku] = basket[sku] - offs.quantity
                    else:
                        total_price = total_price + (prod.price*basket[sku])
                        basket[sku] = 0
            else:
                total_price = total_price + (prod.price*basket[sku])

        return total_price
