from singer_sdk import typing as th

schema = th.PropertiesList(
    th.Property("id", th.IntegerType),
    th.Property("customer",
                th.ObjectType(
                    th.Property("id_legacy", th.StringType),
                    th.Property("name", th.StringType),
                    th.Property("name_contract", th.StringType),
                )
                ),
    th.Property("is_active", th.BooleanType),
    th.Property("name", th.StringType),
    th.Property("email", th.EmailType),
    th.Property("custom_fields",
                th.ObjectType(
                    th.Property("comunicacoes_cm",
                                th.ObjectType(
                                    th.Property("value", th.StringType)
                                ),
                                ),
                    ),
                required=False,
                ),
).to_dict()
