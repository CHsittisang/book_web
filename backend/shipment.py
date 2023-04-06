from dataclasses import dataclass 

@dataclass
class shipment:
    shipment_id: int
    shipment_status: str
    shipment_date: str
    shipment_detail: str
    shipment_price: int
    shipment_address: str