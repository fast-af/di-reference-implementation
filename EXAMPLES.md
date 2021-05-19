## User clicks Fast Checkout Button 
#### Request POST to /fast/v1/create
```
{
  "type": "ENTITY_TYPE_ORDER",
  "order": {
    "is_cart": true,
    "order": {
      "id": {
        "value": "eb3b8e18-930d-4213-92a0-4993f9e536a8"
      },
      "order_type": "ORDER_TYPE_CART",
      "status": "ORDER_STATUS_CART",
      "bill_to": {},
      "lines": [
        {
          "id": {
            "value": "32dc17ee-ebff-40f8-87c5-b83f838d79d1"
          },
          "external_product_id": "112",
          "quantity": 1,
          "subtotal_amount": "0.00",
          "tax_amount": "0.00",
          "total_amount": "0.00"
        }
      ]
    }
  }
}
```
#### Response
```
{
  "order": {
    "order": {
      "id": {
        "value": "eb3b8e18-930d-4213-92a0-4993f9e536a8"
      },
      "external_id": "a98a387e-02ec-41a8-a38e-e3ca5fb0548d",
      "order_type": 1,
      "currency_code": "USD",
      "bill_to": {},
      "lines": [
        {
          "id": {
            "value": "32dc17ee-ebff-40f8-87c5-b83f838d79d1"
          },
          "external_id": "d3d6eca1-1697-4ad2-872b-6f369364f75b",
          "external_product_id": "112",
          "external_variant_id": "77",
          "quantity": 1,
          "subtotal_amount": "29.99",
          "total_amount": "29.99",
          "discounts": [
            {
              "origin": 3,
              "type": 2,
              "applied": true,
              "total_amount": "0.00"
            },
            {
              "origin": 3,
              "type": 2,
              "total_amount": "0.00"
            }
          ],
          "name": "Fast Hoodie",
          "image_url": "https://cdn11.bigcommerce.com/s-rbozo853xi/products/112/images/382/fast-hoodie-black__93230.1614697898.220.290.jpg?c=1",
          "fulfillment_mode": 1
        }
      ],
      "total_amount": "29.99",
      "sub_total": "29.99",
      "total_discounts": "0.00"
    }
  }
}
```

## New User completes the sign up form
### Checkout is initiated
#### Request POST to /fast/v1/read
```
{
  "type": "ENTITY_TYPE_ORDER",
  "order": {
    "is_cart": true,
    "external_order_id": "a98a387e-02ec-41a8-a38e-e3ca5fb0548d"
  }
}
```
#### Response
{
  "order": {
    "order": {
      "id": {
        "value": "eb3b8e18-930d-4213-92a0-4993f9e536a8"
      },
      "external_id": "a98a387e-02ec-41a8-a38e-e3ca5fb0548d",
      "order_type": 1,
      "currency_code": "USD",
      "status": 1,
      "bill_to": {},
      "lines": [
        {
          "id": {
            "value": "32dc17ee-ebff-40f8-87c5-b83f838d79d1"
          },
          "external_id": "d3d6eca1-1697-4ad2-872b-6f369364f75b",
          "external_product_id": "112",
          "external_variant_id": "77",
          "quantity": 1,
          "subtotal_amount": "29.99",
          "total_amount": "29.99",
          "discounts": [
            {
              "origin": 3,
              "type": 2,
              "applied": true,
              "total_amount": "0.00"
            },
            {
              "origin": 3,
              "type": 2,
              "total_amount": "0.00"
            }
          ],
          "name": "Fast Hoodie",
          "image_url": "https://cdn11.bigcommerce.com/s-rbozo853xi/products/112/images/382/fast-hoodie-black__93230.1614697898.220.290.jpg?c=1",
          "fulfillment_mode": 1
        }
      ],
      "total_amount": "29.99",
      "sub_total": "29.99",
      "total_discounts": "0.00",
      "total_tax": "0.00",
      "total_shipping": "0.00"
    }
  }
}

#### Request POST to /fast/v1/update
```
{
  "request_id": {
    "value": "e39fdccd-36ba-42ca-87e6-41ead8c39de9"
  },
  "type": "ENTITY_TYPE_ORDER",
  "order": {
    "order_id": {
      "value": "eb3b8e18-930d-4213-92a0-4993f9e536a8"
    },
    "is_cart": true,
    "bill_to": {
      "first_name": "John",
      "last_name": "Smith",
      "email": "John+23roujwn@fast.in",
      "phone": "+15555555555",
      "address_1": "349 9th Street",
      "city_locality": "San Francisco",
      "state_province_code": "CA",
      "country": "US",
      "country_code": "US",
      "postal_code": "94103"
    }
  }
}
```
#### Response
```
{
  "request_id": {
    "value": "e39fdccd-36ba-42ca-87e6-41ead8c39de9"
  },
  "order": {
    "order": {
      "id": {
        "value": "eb3b8e18-930d-4213-92a0-4993f9e536a8"
      },
      "external_id": "a98a387e-02ec-41a8-a38e-e3ca5fb0548d",
      "order_type": 1,
      "currency_code": "USD",
      "status": 1,
      "bill_to": {
        "first_name": "John",
        "last_name": "Smith",
        "address_1": "349 9th Street",
        "city_locality": "San Francisco",
        "state_province": "California",
        "state_province_code": "CA",
        "country": "United States",
        "country_code": "US",
        "postal_code": "94103"
      },
      "lines": [
        {
          "id": {
            "value": "32dc17ee-ebff-40f8-87c5-b83f838d79d1"
          },
          "external_id": "d3d6eca1-1697-4ad2-872b-6f369364f75b",
          "external_product_id": "112",
          "external_variant_id": "77",
          "quantity": 1,
          "subtotal_amount": "29.99",
          "total_amount": "29.99",
          "discounts": [
            {
              "origin": 3,
              "type": 2,
              "applied": true,
              "total_amount": "0.00"
            },
            {
              "origin": 3,
              "type": 2,
              "total_amount": "0.00"
            }
          ],
          "name": "Fast Hoodie",
          "image_url": "https://cdn11.bigcommerce.com/s-rbozo853xi/products/112/images/382/fast-hoodie-black__93230.1614697898.220.290.jpg?c=1",
          "fulfillment_mode": 1
        }
      ],
      "total_amount": "29.99",
      "sub_total": "29.99",
      "total_discounts": "0.00",
      "total_tax": "0.00",
      "total_shipping": "0.00"
    },
    "status": [
      {
        "updated": 3,
        "status": true,
        "message": "billing address added"
      }
    ]
  }
}
```

#### Request POST to /fast/v1/read
```
{
  "type": "ENTITY_TYPE_ORDER",
  "order": {
    "is_cart": true,
    "external_order_id": "a98a387e-02ec-41a8-a38e-e3ca5fb0548d"
  }
}
```
#### Response
```
{
  "order": {
    "order": {
      "id": {
        "value": "eb3b8e18-930d-4213-92a0-4993f9e536a8"
      },
      "external_id": "a98a387e-02ec-41a8-a38e-e3ca5fb0548d",
      "order_type": 1,
      "currency_code": "USD",
      "status": 1,
      "bill_to": {
        "first_name": "John",
        "last_name": "Smith",
        "address_1": "349 9th Street",
        "city_locality": "San Francisco",
        "state_province": "California",
        "state_province_code": "CA",
        "country": "United States",
        "country_code": "US",
        "postal_code": "94103"
      },
      "lines": [
        {
          "id": {
            "value": "32dc17ee-ebff-40f8-87c5-b83f838d79d1"
          },
          "external_id": "d3d6eca1-1697-4ad2-872b-6f369364f75b",
          "external_product_id": "112",
          "external_variant_id": "77",
          "quantity": 1,
          "subtotal_amount": "29.99",
          "total_amount": "29.99",
          "discounts": [
            {
              "origin": 3,
              "type": 2,
              "applied": true,
              "total_amount": "0.00"
            },
            {
              "origin": 3,
              "type": 2,
              "total_amount": "0.00"
            }
          ],
          "name": "Fast Hoodie",
          "image_url": "https://cdn11.bigcommerce.com/s-rbozo853xi/products/112/images/382/fast-hoodie-black__93230.1614697898.220.290.jpg?c=1",
          "fulfillment_mode": 1
        }
      ],
      "total_amount": "29.99",
      "sub_total": "29.99",
      "total_discounts": "0.00",
      "total_tax": "0.00",
      "total_shipping": "0.00"
    }
  }
}
```

#### Request POST to /fast/v1/update
```
{
  "request_id": {
    "value": "10bad9bf-0d12-434f-99fe-994185d97398"
  },
  "type": "ENTITY_TYPE_ORDER",
  "order": {
    "order_id": {
      "value": "eb3b8e18-930d-4213-92a0-4993f9e536a8"
    },
    "is_cart": true,
    "shipments": [
      {
        "ship_to": {
          "first_name": "John",
          "last_name": "Smith",
          "email": "John+23roujwn@fast.in",
          "phone": "+15555555555",
          "address_1": "349 9th Street",
          "city_locality": "San Francisco",
          "state_province_code": "CA",
          "country": "US",
          "country_code": "US",
          "postal_code": "94103"
        },
        "line_refs": [
          {
            "id": {
              "value": "32dc17ee-ebff-40f8-87c5-b83f838d79d1"
            },
            "quantity": 1
          }
        ]
      }
    ]
  }
}
```
#### Response
```
{
  "request_id": {
    "value": "10bad9bf-0d12-434f-99fe-994185d97398"
  },
  "order": {
    "order": {
      "id": {
        "value": "eb3b8e18-930d-4213-92a0-4993f9e536a8"
      },
      "external_id": "a98a387e-02ec-41a8-a38e-e3ca5fb0548d",
      "order_type": 1,
      "currency_code": "USD",
      "status": 1,
      "bill_to": {
        "first_name": "John",
        "last_name": "Smith",
        "address_1": "349 9th Street",
        "city_locality": "San Francisco",
        "state_province": "California",
        "state_province_code": "CA",
        "country": "United States",
        "country_code": "US",
        "postal_code": "94103"
      },
      "lines": [
        {
          "id": {
            "value": "32dc17ee-ebff-40f8-87c5-b83f838d79d1"
          },
          "external_id": "d3d6eca1-1697-4ad2-872b-6f369364f75b",
          "external_product_id": "112",
          "external_variant_id": "77",
          "quantity": 1,
          "subtotal_amount": "29.99",
          "total_amount": "29.99",
          "discounts": [
            {
              "origin": 3,
              "type": 2,
              "applied": true,
              "total_amount": "0.00"
            },
            {
              "origin": 3,
              "type": 2,
              "total_amount": "0.00"
            }
          ],
          "name": "Fast Hoodie",
          "image_url": "https://cdn11.bigcommerce.com/s-rbozo853xi/products/112/images/382/fast-hoodie-black__93230.1614697898.220.290.jpg?c=1",
          "fulfillment_mode": 1
        }
      ],
      "shipment_plans": [
        {
          "external_id": "60a4bbe63f601",
          "ship_to": {
            "first_name": "John",
            "last_name": "Smith",
            "address_1": "349 9th Street",
            "city_locality": "San Francisco",
            "state_province": "California",
            "state_province_code": "CA",
            "country": "United States",
            "country_code": "US",
            "postal_code": "94103"
          },
          "selected_option": {
            "shipment_type": 99,
            "cost": "0.00",
            "tax": "0.00",
            "total": "0.00"
          },
          "available_options": [
            {
              "external_id": "4dcbf24f457dd67d5f89bcf374e0bc9b",
              "name": "Free Shipping",
              "shipment_type": 99,
              "cost": "0.00",
              "tax": "0.00",
              "total": "0.00"
            }
          ]
        }
      ],
      "total_amount": "29.99",
      "sub_total": "29.99",
      "total_discounts": "0.00",
      "total_tax": "0.00",
      "total_shipping": "0.00"
    },
    "status": [
      {
        "updated": 2,
        "status": true,
        "message": "shipping added"
      }
    ]
  }
}
```

#### Request POST to /fast/v1/update
```
{
  "request_id": {
    "value": "fb077844-69be-471a-b1e8-cef2591747fa"
  },
  "type": "ENTITY_TYPE_ORDER",
  "order": {
    "order_id": {
      "value": "eb3b8e18-930d-4213-92a0-4993f9e536a8"
    },
    "is_cart": true,
    "shipping_option": {
      "plan_id": {
        "value": "60a4bbe63f601"
      },
      "option_id": {
        "value": "4dcbf24f457dd67d5f89bcf374e0bc9b"
      }
    }
  }
}
```
#### Response
```
{
  "request_id": {
    "value": "fb077844-69be-471a-b1e8-cef2591747fa"
  },
  "order": {
    "order": {
      "id": {
        "value": "eb3b8e18-930d-4213-92a0-4993f9e536a8"
      },
      "external_id": "a98a387e-02ec-41a8-a38e-e3ca5fb0548d",
      "order_type": 1,
      "currency_code": "USD",
      "status": 1,
      "bill_to": {
        "first_name": "John",
        "last_name": "Smith",
        "address_1": "349 9th Street",
        "city_locality": "San Francisco",
        "state_province": "California",
        "state_province_code": "CA",
        "country": "United States",
        "country_code": "US",
        "postal_code": "94103"
      },
      "lines": [
        {
          "id": {
            "value": "32dc17ee-ebff-40f8-87c5-b83f838d79d1"
          },
          "external_id": "d3d6eca1-1697-4ad2-872b-6f369364f75b",
          "external_product_id": "112",
          "external_variant_id": "77",
          "quantity": 1,
          "subtotal_amount": "29.99",
          "total_amount": "29.99",
          "discounts": [
            {
              "origin": 3,
              "type": 2,
              "applied": true,
              "total_amount": "0.00"
            },
            {
              "origin": 3,
              "type": 2,
              "total_amount": "0.00"
            }
          ],
          "name": "Fast Hoodie",
          "image_url": "https://cdn11.bigcommerce.com/s-rbozo853xi/products/112/images/382/fast-hoodie-black__93230.1614697898.220.290.jpg?c=1",
          "fulfillment_mode": 1
        }
      ],
      "shipment_plans": [
        {
          "external_id": "60a4bbe63f601",
          "ship_to": {
            "first_name": "John",
            "last_name": "Smith",
            "address_1": "349 9th Street",
            "city_locality": "San Francisco",
            "state_province": "California",
            "state_province_code": "CA",
            "country": "United States",
            "country_code": "US",
            "postal_code": "94103"
          },
          "selected_option": {
            "external_id": "4dcbf24f457dd67d5f89bcf374e0bc9b",
            "name": "Free Shipping",
            "shipment_type": 99,
            "cost": "0.00",
            "tax": "0.00",
            "total": "0.00"
          },
          "available_options": [
            {
              "external_id": "4dcbf24f457dd67d5f89bcf374e0bc9b",
              "name": "Free Shipping",
              "shipment_type": 99,
              "cost": "0.00",
              "tax": "0.00",
              "total": "0.00"
            }
          ]
        }
      ],
      "total_amount": "29.99",
      "sub_total": "29.99",
      "total_discounts": "0.00",
      "total_tax": "0.00",
      "total_shipping": "0.00"
    },
    "status": [
      {
        "updated": 5,
        "status": true,
        "message": "shipping options updated"
      }
    ]
  }
}
```

## Checkout Timer expires and order is set to capture payment
Coming soon