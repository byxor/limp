GET_ATTRIBUTE = "get-attribute"


def symbols():
    return {
        GET_ATTRIBUTE: lambda object_, attribute: object_.resolve(attribute)
    }
