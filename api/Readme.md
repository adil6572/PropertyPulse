# Realtor Endpoint API

The Realtor Endpoint API provides access to real estate data from multiple sources, including realtor.com. This API allows users to retrieve detailed information about real estate properties, including their status, pricing, location, and more.

## Attributes Provided

The Realtor endpoint API provides the following attributes for each property:

1. `property_id`: Unique identifier for the property.
2. `list_price`: Price of the property.
3. `status`: Status of the property (e.g., "for_sale", "sold").
4. `permalink`: URL of the property listing on realtor.com.
5. `primary_photo`: URL of the primary photo of the property.
6. `description`: Object containing details about the property description.
   - `beds`: Number of bedrooms.
   - `baths`: Number of bathrooms.
   - `sqft`: Total square footage of the property.
   - `lot_sqft`: Square footage of the lot.
   - `type`: Type of property (e.g., single_family).
7. `location`: Object containing address and coordinate details of the property.
   - `address`:
     - `line`: Street address.
     - `postal_code`: Postal code.
     - `state`: State.
     - `city`: City.
   - `coordinate`:
     - `lat`: Latitude coordinate.
     - `lon`: Longitude coordinate.
8. `flags`: Object containing flags indicating various attributes of the property.
   - `is_coming_soon`: Indicates if the property is coming soon.
   - `is_new_listing`: Indicates if the property is a new listing.
9. `list_date`: Date and time when the property was listed.

These attributes provide comprehensive information about each property available through the Realtor endpoint API.
