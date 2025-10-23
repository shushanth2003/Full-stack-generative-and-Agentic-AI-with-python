users=[
    {"id":1,"total":150,"coupon":"po1x"},
    {"id":2,"total":200,"coupon":"po2x"},
    {"id":3,"total":300,"coupon":"po3x"}
];
discount={
    "po1x":(0.5,0),
    "po2x":(0.7,0),
    "po3x":(0,10)
};
for user in users:
    percent,fixed=discount.get(user["coupon"],(0,0));
    discounts=user["total"]*percent+fixed;
    print(f"{user["id"]} platform calculated my {user["total"]} in fixed discount {discounts}");