import pytest
from tests.invoices.test_generate_invoice_number import test_generate_invoice_number


def create_draft_invoice(invoice_number):
    data = {
        "detail": {
            "invoice_number": invoice_number,
            "invoice_date": "2022-02-04",
            "payment_term": {
                "term_type": "NET_10",
                "due_date": "2022-02-14"
            },
            "currency_code": "USD",
            "reference": "<The reference data. Includes a post office (PO) number.>",
            "note": "<A note to the invoice recipient. Also appears on the invoice notification email.>",
            "terms_and_conditions": "<The general terms of the invoice. Can include return or cancellation policy and other terms and conditions.>",
            "memo": "<A private bookkeeping note for merchant.>"
        },
        "invoicer": {
            "name": {
                "given_name": "David",
                "surname": "Larusso"
            },
            "address": {
                "address_line_1": "123 Townsend St",
                "address_line_2": "Floor 6",
                "admin_area_2": "San Francisco",
                "admin_area_1": "CA",
                "postal_code": "94107",
                "country_code": "US"
            },
            "phones": [
                {
                    "country_code": "001",
                    "national_number": "4085551234",
                    "phone_type": "MOBILE"
                }
            ],
            "website": "www.example.com",
            "tax_id": "XX-XXXXXXX",
            "logo_url": "https://example.com/logo.png",
            "additional_notes": "<Any additional information. Includes business hours.>"
        },
        "primary_recipients": [
            {
                "billing_info": {
                    "name": {
                        "given_name": "Stephanie",
                        "surname": "Meyers"
                    },
                    "address": {
                        "address_line_1": "1234 Main Street",
                        "admin_area_2": "Anytown",
                        "admin_area_1": "CA",
                        "postal_code": "98765",
                        "country_code": "US"
                    },
                    "email_address": "foobuyer@example.com",
                    "phones": [
                        {
                            "country_code": "001",
                            "national_number": "4884551234",
                            "phone_type": "HOME"
                        }
                    ],
                    "additional_info_value": "add-info"
                },
                "shipping_info": {
                    "name": {
                        "given_name": "Stephanie",
                        "surname": "Meyers"
                    },
                    "address": {
                        "address_line_1": "1234 Main Street",
                        "admin_area_2": "Anytown",
                        "admin_area_1": "CA",
                        "postal_code": "98765",
                        "country_code": "US"
                    }
                }
            }
        ],
        "items": [
            {
                "name": "Yoga Mat",
                "description": "Elastic mat to practice yoga.",
                "quantity": "1",
                "unit_amount": {
                    "currency_code": "USD",
                    "value": "50.00"
                },
                "tax": {
                    "name": "Sales Tax",
                    "percent": "7.25"
                },
                "discount": {
                    "percent": "5"
                },
                "unit_of_measure": "QUANTITY"
            },
            {
                "name": "Yoga t-shirt",
                "quantity": "1",
                "unit_amount": {
                    "currency_code": "USD",
                    "value": "10.00"
                },
                "tax": {
                    "name": "Sales Tax",
                    "percent": "7.25"
                },
                "discount": {
                    "amount": {
                        "currency_code": "USD",
                        "value": "5.00"
                    }
                },
                "unit_of_measure": "QUANTITY"
            }
        ],
        "configuration": {
            "partial_payment": {
                "allow_partial_payment": True,
                "minimum_amount_due": {
                    "currency_code": "USD",
                    "value": "20.00"
                }
            },
            "allow_tip": True,
            "tax_calculated_after_discount": True,
            "tax_inclusive": False
        },
        "amount": {
            "breakdown": {
                "custom": {
                    "label": "Packing Charges",
                    "amount": {
                        "currency_code": "USD",
                        "value": "10.00"
                    }
                },
                "shipping": {
                    "amount": {
                        "currency_code": "USD",
                        "value": "10.00"
                    },
                    "tax": {
                        "name": "Sales Tax",
                        "percent": "7.25"
                    }
                },
                "discount": {
                    "invoice_discount": {
                        "percent": "5"
                    }
                }
            }
        }
    }
    return data
