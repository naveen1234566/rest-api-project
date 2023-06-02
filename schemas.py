from marshmallow import Schema, fields


class PlainItemSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    price = fields.Float(required=True)


class PlainStoreSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)


class PlainTagSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()


class ItemUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()
    store_id = fields.Int()


class ItemSchema(PlainItemSchema):
    store_id = fields.Int(required=True, load_only=True)
    store = fields.Nested(PlainStoreSchema(), dump_only=True)
    tags = fields.List(fields.Nested(PlainTagSchema()), dump_only=True)


class StoreSchema(PlainStoreSchema):
    items = fields.List(fields.Nested(PlainItemSchema()), dump_only=True)
    tags = fields.List(fields.Nested(PlainTagSchema()), dump_only=True)


class TagSchema(PlainTagSchema):
    store_id = fields.Int(load_only=True)
    store = fields.Nested(PlainStoreSchema(), dump_only=True)
    items = fields.List(fields.Nested(PlainItemSchema()), dump_only=True)


class TagAndItemSchema(Schema):
    message = fields.Str()
    item = fields.Nested(ItemSchema)
    tag = fields.Nested(TagSchema)


class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    password = fields.Str(required=True)


class UserRegisterSchema(UserSchema):
    email = fields.Str(required=True)
    
    
# "example": {
#             "name": "pni-1/2",
#             "admin": "true",
#             "description": "Ethernet-interface",
#             "nativeVlanId": 1,
#             "mtu": 80,
#             "bandwidth": {
#                 "uplink": 10,
#                 "downlink": 20
#             },
#             "subInterface": [
#                 {
#                 "unitId": 1,
#                 "description": "Sub-interface",
#                 "vlanId": 22,
#                 "networkType": "WAN",
#                 "networkName": "WAN networks",
#                 "mtu": 72,
#                 "bandwidth": {
#                     "uplink": 800,
#                     "downlink": 900
#                 },
#                 "ipv4": {
#                     "addressType": "Static",
#                     "staticAddress": {
#                     "ipAddressMask": [
#                         "1.2.3.4/24"
#                     ],
#                     "staticArp": [
#                         {
#                         "subnetAddressMask": "1.2.3.4/24",
#                         "macAddress": "aa:bb:cc:34:e5:44"
#                         }
#                     ]
#                     }
#                 },
#                 "dhcpAddress": {
#                     "routePreference": 3,
#                     "vendorClassIdentifier": "aaa 1212 bbbb",
#                     "reachabilityMonitor": {
#                     "icmp": "True",
#                     "interval": 1,
#                     "threshold": 2
#                     }
                    
#                 }
#                 }
#         ]
#         }
# }
        
    