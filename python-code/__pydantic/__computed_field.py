from pydantic import BaseModel, computed_field,Field;

class Product(BaseModel):
    price:float
    quantity:int

    @computed_field
    @property
    def service_price(self)->float:
        return self.price*self.quantity;

product=Product(
    price=10,
    quantity=2
);

print(f"Number of Product got services {product.service_price}");

class Booking(BaseModel):
    user_id:int
    room_id:int
    nights:int
    rate_per_nights:int

    @computed_field
    @property
    def total_amount_booking(self)->int:
        return self.nights*self.rate_per_nights;

booking=Booking(
    user_id=1,
    room_id=102,
    nights=10,
    rate_per_nights=2
);

print(f"No of Booking Nights : {booking.total_amount_booking}");


        