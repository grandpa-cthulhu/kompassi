import logging

from django.db import models
from django.utils.translation import gettext_lazy as _

from core.csv_export import CsvExportMixin

from ..utils import format_price
from .order import Order
from .product import Product


logger = logging.getLogger("kompassi")


class OrderProduct(models.Model, CsvExportMixin):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="order_product_set")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="order_product_set")
    count = models.IntegerField(default=0)

    @property
    def target(self):
        return self.product

    @property
    def price_cents(self):
        return self.count * self.product.price_cents

    @property
    def formatted_price(self):
        return format_price(self.price_cents)

    @property
    def description(self):
        return "%dx %s" % (self.count, self.product.name if self.product is not None else None)

    @classmethod
    def get_csv_fields(cls, event):
        return [
            (Order, "payment_date"),
            (Order, "formatted_order_number"),
            (Product, "name"),
            (Product, "price_cents"),
            (cls, "count"),
            (cls, "price_cents"),
        ]

    @classmethod
    def get_csv_header(cls, event, fields, m2m_mode):
        return [
            "payment_date",
            "order_number",
            "product_name",
            "product_price_cents",
            "count",
            "row_price_cents",
        ]

    def get_csv_related(self):
        return {
            Order: self.order,
            Product: self.product,
        }

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = "tilausrivi"
        verbose_name_plural = "tilausrivit"
        unique_together = [("order", "product")]
