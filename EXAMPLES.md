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
```

#### Request POST to /fast/v1/update (Bill To Info)
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

#### Request POST to /fast/v1/update (Shipment Contact Info)
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

#### Request POST to /fast/v1/update (Shipping Option Selection)
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
#### Request POST to /fast/v1/update (convert cart to order)
```
{
  "order": {
    "convert_cart_to_order": true,
    "convert_mode": "CART_TO_ORDER_CONVERT_UPDATE_AND_CONVERT",
    "is_cart": true,
    "order_id": {
      "value": "eb3b8e18-930d-4213-92a0-4993f9e536a8"
    }
  },
  "request_id": {
    "value": "6514b4d9-a41a-4e24-a3ff-75266e29492c"
  },
  "type": "ENTITY_TYPE_ORDER"
}
```
#### Response
```
{
  "order": {
    "order": {
      "bill_to": {
        "address_1": "9000 Over St.",
        "address_2": "#1",
        "city_locality": "San Francisco",
        "country": "US",
        "country_code": "US",
        "email": "pdp_simple_new_user-tester+lxbikihkrj-z7dnnxck3ta@fast.invalid",
        "first_name": "Guest",
        "last_name": "offastco",
        "phone": "555-555-5555",
        "postal_code": "94107",
        "state_province_code": "CA"
      },
      "currency_code": "USD",
      "external_id": "a98a387e-02ec-41a8-a38e-e3ca5fb0548d",
      "id": {
        "value": "eb3b8e18-930d-4213-92a0-4993f9e536a8"
      },
      "lines": [
        {
          "customizations": [],
          "description": "",
          "discounted_unit_price": "32.99",
          "discounts": [],
          "external_id": "ee121991-2d0d-443b-a2c4-651666cac754",
          "external_options": [],
          "external_product_id": "123",
          "external_variant_id": "",
          "fulfillment_mode": 1,
          "id": {
            "value": "7260da2d-d6c2-44b4-a071-7bdf819f5a2a"
          },
          "image_url": "",
          "line_discount_amount": "0.0",
          "name": "Blue Hoodie",
          "quantity": 1,
          "quantity_fulfilled": 0,
          "subtotal_amount": "32.99",
          "tax_amount": "0.00",
          "total_amount": "32.99",
          "unit_price": "32.99"
        }
      ],
      "order_type": "ORDER_TYPE_CART",
      "shipment_plans": [
        {
          "available_options": [
            {
              "cost": "0.00",
              "external_id": "3e22e6e0-b52d-4c98-94e9-febb66299679",
              "name": "Free Shipping",
              "shipment_type": 99,
              "tax": "0.00",
              "total": "0.00"
            }
          ],
          "external_id": "73498753-d0e2-4f92-accc-7c4fcb94f424",
          "id": {
            "value": "bdb5967c-3894-4ac4-8dea-5fcc1915c132"
          },
          "selected_option": {
            "cost": "0.00",
            "external_id": "3e22e6e0-b52d-4c98-94e9-febb66299679",
            "shipment_type": 99,
            "tax": "0.00",
            "total": "0.00"
          },
          "ship_to": {
            "address_1": "9000 Over St.",
            "address_2": "#1",
            "city_locality": "San Francisco",
            "country": "US",
            "country_code": "US",
            "email": "pdp_simple_new_user-tester+lxbikihkrj-z7dnnxck3ta@fast.invalid",
            "first_name": "Guest",
            "last_name": "offastco",
            "phone": "555-555-5555",
            "postal_code": "94107",
            "state_province_code": "CA"
          }
        }
      ],
      "status": "ORDER_STATUS_CART",
      "sub_total": "32.99",
      "total_amount": "32.99",
      "total_discounts": "0.0",
      "total_tax": "0.0"
    }
  },
  "request_id": {
    "value": "abc684fe-55e1-4c87-b707-3b611877691c"
  },
  "type": "ENTITY_TYPE_ORDER"
}
```


#### Request POST to /fast/v1/read
```
{
  "order": {
    "external_order_id": "c826f409-fd6f-42f9-ae8b-d5a862ddcf27"
  },
  "type": "ENTITY_TYPE_ORDER"
}
```
#### Response
```
{
  "order": {
    "order": {
      "bill_to": {
        "address_1": "9000 Over St.",
        "address_2": "#1",
        "city_locality": "San Francisco",
        "country": "US",
        "country_code": "US",
        "email": "pdp_simple_new_user-tester+lxbikihkrj-z7dnnxck3ta@fast.invalid",
        "first_name": "Guest",
        "last_name": "offastco",
        "phone": "555-555-5555",
        "postal_code": "94107",
        "state_province_code": "CA"
      },
      "currency_code": "USD",
      "external_id": "c826f409-fd6f-42f9-ae8b-d5a862ddcf27",
      "id": {
        "value": "5d6b3b40-a9c8-469a-9da6-d35408fadc2a"
      },
      "lines": [
        {
          "customizations": [],
          "description": "",
          "discounted_unit_price": "32.99",
          "discounts": [],
          "external_id": "ee121991-2d0d-443b-a2c4-651666cac754",
          "external_options": [],
          "external_product_id": "123",
          "external_variant_id": "",
          "fulfillment_mode": 1,
          "id": {
            "value": "7260da2d-d6c2-44b4-a071-7bdf819f5a2a"
          },
          "image_url": "",
          "line_discount_amount": "0.0",
          "name": "Blue Hoodie",
          "quantity": 1,
          "quantity_fulfilled": 0,
          "subtotal_amount": "32.99",
          "tax_amount": "0.00",
          "total_amount": "32.99",
          "unit_price": "32.99"
        }
      ],
      "order_type": "ORDER_TYPE_CART",
      "shipment_plans": [
        {
          "available_options": [
            {
              "cost": "0.00",
              "external_id": "3e22e6e0-b52d-4c98-94e9-febb66299679",
              "name": "Free Shipping",
              "shipment_type": 99,
              "tax": "0.00",
              "total": "0.00"
            }
          ],
          "external_id": "73498753-d0e2-4f92-accc-7c4fcb94f424",
          "id": {
            "value": "bdb5967c-3894-4ac4-8dea-5fcc1915c132"
          },
          "selected_option": {
            "cost": "0.00",
            "external_id": "3e22e6e0-b52d-4c98-94e9-febb66299679",
            "shipment_type": 99,
            "tax": "0.00",
            "total": "0.00"
          },
          "ship_to": {
            "address_1": "9000 Over St.",
            "address_2": "#1",
            "city_locality": "San Francisco",
            "country": "US",
            "country_code": "US",
            "email": "pdp_simple_new_user-tester+lxbikihkrj-z7dnnxck3ta@fast.invalid",
            "first_name": "Guest",
            "last_name": "offastco",
            "phone": "555-555-5555",
            "postal_code": "94107",
            "state_province_code": "CA"
          }
        }
      ],
      "status": "ORDER_STATUS_CART",
      "sub_total": "32.99",
      "total_amount": "32.99",
      "total_discounts": "0.0",
      "total_tax": "0.0"
    }
  },
  "request_id": {
    "value": "abc684fe-55e1-4c87-b707-3b611877691c"
  },
  "type": "ENTITY_TYPE_ORDER"
}
```
