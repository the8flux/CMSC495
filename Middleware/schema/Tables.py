from dataclasses import dataclass


@dataclass
class Address:
    address_id: int
    street_address: str
    city: str
    state: str
    country: str
    postal_code: str


@dataclass
class CatalogItems:
    catalog_item_id: int
    manufacturer_id: int
    catalog_item_name: str
    item_category_id: int
    buy_cost: float


@dataclass
class Customers:
    customer_id: int
    address_id: int
    customer_name: str


@dataclass
class InventoryItems:
    inventory_item_id: int
    catalog_item_id: int
    stock_quantity: int
    item_serial_number: str
    sell_price: float


@dataclass
class Invoices:
    invoice_id: int
    customer_id: int
    cost_adjustment_id: int
    date_invoiced: str
    date_invoice_due: str
    invoice_subtotal: float
    tax_percent: int
    tax_amount: float
    invoice_total_due: float


@dataclass
class ItemCategories:
    item_category_id: int
    item_category_title: str
    item_category_description: str


@dataclass
class LineItems:
    line_item_id: int
    invoice_id: int
    inventory_item_id: int
    cost_adjustment_id: int
    sell_price: float
    quantity: int


@dataclass
class Manufacturers:
    manufacturer_id: int
    manufacturer_name: str
    manufacturer_description: str
    address_id: int


@dataclass
class PriceAdjustment:
    price_adjustment_id: int
    title: str
    reason_description: str
    is_fixed: bool
    fixed_amount: float
    is_percent: bool
    percent: int


@dataclass
class UserType:
    user_type_id: int
    description: str