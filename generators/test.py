from pydantic import BaseModel, Field, AnyHttpUrl
from uuid import UUID
from typing import Union
class Thing(BaseModel):
    """
    Thing
    """
    
    additionalType: AnyHttpUrl = Field(None,
        description="An additional type for the item, typically used for adding more specific types from external vocabularies in microdata syntax. This is a relationship between something and a class that the thing is in. In RDFa syntax, it is better to use the native RDFa syntax - the 'typeof' attribute - for multiple types. Schema.org tools may have only weaker understanding of extra types, in particular those defined externally."
    )


    alternateName: str = Field(None,
        description="An alias for the item."
    )


    description: str = Field(None,
        description="A description of the item."
    )


    disambiguatingDescription: str = Field(None,
        description="A sub property of description. A short description of the item used to disambiguate from other, similar items. Information from other properties (in particular, name) may be necessary for the description to be useful for disambiguation."
    )


    identifier: Union[AnyHttpUrl,str] = Field(None,
        description="The identifier property represents any kind of identifier for any kind of Thing, such as ISBNs, GTIN codes, UUIDs etc. Schema.org provides dedicated properties for representing many of these, either as textual strings or as URL (URI) links. See background notes for more details."
    )


    image: Union[AnyHttpUrl,str] = Field(None,
        description="An image of the item. This can be a URL or a fully described ImageObject."
    )


    mainEntityOfPage: Union[AnyHttpUrl,str] = Field(None,
        description="Indicates a page (or other CreativeWork) for which this thing is the main entity being described. See background notes for details. Inverse property: mainEntity."
    )


    name: str = Field(
        description="The name of the item."
    )


    potentialAction: str = Field(None,
        description="Indicates a potential Action, which describes an idealized action in which this thing would play an 'object' role."
    )


    sameAs: AnyHttpUrl = Field(None,
        description="URL of a reference Web page that unambiguously indicates the item's identity. E.g. the URL of the item's Wikipedia page, Wikidata entry, or official website."
    )


    subjectOf: Union[str] = Field(None,
        description="A CreativeWork or Event about this Thing. Inverse property: about."
    )


    url: AnyHttpUrl = Field(None,
        description="URL of the item."
    )

