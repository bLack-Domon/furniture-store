from decimal import Decimal
from django.conf import settings  # Memanggil Setting
from website.models import Produk  # Memanggil table produk


class Cart(object):
    def __init__(self, request):  # menginisialisasi objek
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1, update_quantity=False):  # Menyimpan data session
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0,
                                     'price': int(product.setelah_diskon)}
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):  # Mengedit data session
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, product):  # Menghapus data session
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):  # iterator data session
        product_ids = self.cart.keys()
        products = Produk.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product
        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):  # Menghitung quantity
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):  # Menghitung total Harga
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):  # Membersikan Session
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
