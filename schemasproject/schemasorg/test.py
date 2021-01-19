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


    potentialAction: 'Action' = Field(None,
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


class Action(BaseModel):
    """
    Action
    """
    
    actionStatus: str = Field(None,
        description="Indicates the current disposition of the Action."
    )


    agent: Union[str] = Field(None,
        description="The direct performer or driver of the action (animate or inanimate). e.g. John wrote a book."
    )


    endTime: Union[str] = Field(None,
        description="The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the end of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    error: 'Thing' = Field(None,
        description="For failed actions, more information on the cause of the failure."
    )


    instrument: 'Thing' = Field(None,
        description="The object that helped the agent perform the action. e.g. John wrote a book with a pen."
    )


    location: Union[str] = Field(None,
        description="The location of for example where the event is happening, an organization is located, or where an action takes place."
    )


    object: 'Thing' = Field(None,
        description="The object upon which the action is carried out, whose state is kept intact or changed. Also known as the semantic roles patient, affected or undergoer (which change their state) or theme (which doesn't). e.g. John read a book."
    )


    participant: Union[str] = Field(None,
        description="Other co-agents that participated in the action indirectly. e.g. John wrote a book with Steve."
    )


    result: 'Thing' = Field(None,
        description="The result produced in the action. e.g. John wrote a book."
    )


    startTime: Union[str] = Field(None,
        description="The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    target: str = Field(None,
        description="Indicates a target EntryPoint for an Action."
    )


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


    potentialAction: 'Action' = Field(None,
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


class AchieveAction(BaseModel):
    """
    AchieveAction
    """
    
    actionStatus: str = Field(None,
        description="Indicates the current disposition of the Action."
    )


    agent: Union[str] = Field(None,
        description="The direct performer or driver of the action (animate or inanimate). e.g. John wrote a book."
    )


    endTime: Union[str] = Field(None,
        description="The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the end of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    error: 'Thing' = Field(None,
        description="For failed actions, more information on the cause of the failure."
    )


    instrument: 'Thing' = Field(None,
        description="The object that helped the agent perform the action. e.g. John wrote a book with a pen."
    )


    location: Union[str] = Field(None,
        description="The location of for example where the event is happening, an organization is located, or where an action takes place."
    )


    object: 'Thing' = Field(None,
        description="The object upon which the action is carried out, whose state is kept intact or changed. Also known as the semantic roles patient, affected or undergoer (which change their state) or theme (which doesn't). e.g. John read a book."
    )


    participant: Union[str] = Field(None,
        description="Other co-agents that participated in the action indirectly. e.g. John wrote a book with Steve."
    )


    result: 'Thing' = Field(None,
        description="The result produced in the action. e.g. John wrote a book."
    )


    startTime: Union[str] = Field(None,
        description="The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    target: str = Field(None,
        description="Indicates a target EntryPoint for an Action."
    )


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


    potentialAction: 'Action' = Field(None,
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


class LoseAction(BaseModel):
    """
    LoseAction
    """
    
    winner: str = Field(None,
        description="A sub property of participant. The winner of the action."
    )


    actionStatus: str = Field(None,
        description="Indicates the current disposition of the Action."
    )


    agent: Union[str] = Field(None,
        description="The direct performer or driver of the action (animate or inanimate). e.g. John wrote a book."
    )


    endTime: Union[str] = Field(None,
        description="The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the end of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    error: 'Thing' = Field(None,
        description="For failed actions, more information on the cause of the failure."
    )


    instrument: 'Thing' = Field(None,
        description="The object that helped the agent perform the action. e.g. John wrote a book with a pen."
    )


    location: Union[str] = Field(None,
        description="The location of for example where the event is happening, an organization is located, or where an action takes place."
    )


    object: 'Thing' = Field(None,
        description="The object upon which the action is carried out, whose state is kept intact or changed. Also known as the semantic roles patient, affected or undergoer (which change their state) or theme (which doesn't). e.g. John read a book."
    )


    participant: Union[str] = Field(None,
        description="Other co-agents that participated in the action indirectly. e.g. John wrote a book with Steve."
    )


    result: 'Thing' = Field(None,
        description="The result produced in the action. e.g. John wrote a book."
    )


    startTime: Union[str] = Field(None,
        description="The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    target: str = Field(None,
        description="Indicates a target EntryPoint for an Action."
    )


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


    potentialAction: 'Action' = Field(None,
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


class TieAction(BaseModel):
    """
    TieAction
    """
    
    actionStatus: str = Field(None,
        description="Indicates the current disposition of the Action."
    )


    agent: Union[str] = Field(None,
        description="The direct performer or driver of the action (animate or inanimate). e.g. John wrote a book."
    )


    endTime: Union[str] = Field(None,
        description="The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the end of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    error: 'Thing' = Field(None,
        description="For failed actions, more information on the cause of the failure."
    )


    instrument: 'Thing' = Field(None,
        description="The object that helped the agent perform the action. e.g. John wrote a book with a pen."
    )


    location: Union[str] = Field(None,
        description="The location of for example where the event is happening, an organization is located, or where an action takes place."
    )


    object: 'Thing' = Field(None,
        description="The object upon which the action is carried out, whose state is kept intact or changed. Also known as the semantic roles patient, affected or undergoer (which change their state) or theme (which doesn't). e.g. John read a book."
    )


    participant: Union[str] = Field(None,
        description="Other co-agents that participated in the action indirectly. e.g. John wrote a book with Steve."
    )


    result: 'Thing' = Field(None,
        description="The result produced in the action. e.g. John wrote a book."
    )


    startTime: Union[str] = Field(None,
        description="The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    target: str = Field(None,
        description="Indicates a target EntryPoint for an Action."
    )


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


    potentialAction: 'Action' = Field(None,
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


class WinAction(BaseModel):
    """
    WinAction
    """
    
    loser: str = Field(None,
        description="A sub property of participant. The loser of the action."
    )


    actionStatus: str = Field(None,
        description="Indicates the current disposition of the Action."
    )


    agent: Union[str] = Field(None,
        description="The direct performer or driver of the action (animate or inanimate). e.g. John wrote a book."
    )


    endTime: Union[str] = Field(None,
        description="The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the end of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    error: 'Thing' = Field(None,
        description="For failed actions, more information on the cause of the failure."
    )


    instrument: 'Thing' = Field(None,
        description="The object that helped the agent perform the action. e.g. John wrote a book with a pen."
    )


    location: Union[str] = Field(None,
        description="The location of for example where the event is happening, an organization is located, or where an action takes place."
    )


    object: 'Thing' = Field(None,
        description="The object upon which the action is carried out, whose state is kept intact or changed. Also known as the semantic roles patient, affected or undergoer (which change their state) or theme (which doesn't). e.g. John read a book."
    )


    participant: Union[str] = Field(None,
        description="Other co-agents that participated in the action indirectly. e.g. John wrote a book with Steve."
    )


    result: 'Thing' = Field(None,
        description="The result produced in the action. e.g. John wrote a book."
    )


    startTime: Union[str] = Field(None,
        description="The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    target: str = Field(None,
        description="Indicates a target EntryPoint for an Action."
    )


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


    potentialAction: 'Action' = Field(None,
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


class AssessAction(BaseModel):
    """
    AssessAction
    """
    
    actionStatus: str = Field(None,
        description="Indicates the current disposition of the Action."
    )


    agent: Union[str] = Field(None,
        description="The direct performer or driver of the action (animate or inanimate). e.g. John wrote a book."
    )


    endTime: Union[str] = Field(None,
        description="The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the end of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    error: 'Thing' = Field(None,
        description="For failed actions, more information on the cause of the failure."
    )


    instrument: 'Thing' = Field(None,
        description="The object that helped the agent perform the action. e.g. John wrote a book with a pen."
    )


    location: Union[str] = Field(None,
        description="The location of for example where the event is happening, an organization is located, or where an action takes place."
    )


    object: 'Thing' = Field(None,
        description="The object upon which the action is carried out, whose state is kept intact or changed. Also known as the semantic roles patient, affected or undergoer (which change their state) or theme (which doesn't). e.g. John read a book."
    )


    participant: Union[str] = Field(None,
        description="Other co-agents that participated in the action indirectly. e.g. John wrote a book with Steve."
    )


    result: 'Thing' = Field(None,
        description="The result produced in the action. e.g. John wrote a book."
    )


    startTime: Union[str] = Field(None,
        description="The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    target: str = Field(None,
        description="Indicates a target EntryPoint for an Action."
    )


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


    potentialAction: 'Action' = Field(None,
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


class ChooseAction(BaseModel):
    """
    ChooseAction
    """
    
    actionOption: Union[Thing,str] = Field(None,
        description="A sub property of object. The options subject to this action. Supersedes option."
    )


    actionStatus: str = Field(None,
        description="Indicates the current disposition of the Action."
    )


    agent: Union[str] = Field(None,
        description="The direct performer or driver of the action (animate or inanimate). e.g. John wrote a book."
    )


    endTime: Union[str] = Field(None,
        description="The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the end of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    error: 'Thing' = Field(None,
        description="For failed actions, more information on the cause of the failure."
    )


    instrument: 'Thing' = Field(None,
        description="The object that helped the agent perform the action. e.g. John wrote a book with a pen."
    )


    location: Union[str] = Field(None,
        description="The location of for example where the event is happening, an organization is located, or where an action takes place."
    )


    object: 'Thing' = Field(None,
        description="The object upon which the action is carried out, whose state is kept intact or changed. Also known as the semantic roles patient, affected or undergoer (which change their state) or theme (which doesn't). e.g. John read a book."
    )


    participant: Union[str] = Field(None,
        description="Other co-agents that participated in the action indirectly. e.g. John wrote a book with Steve."
    )


    result: 'Thing' = Field(None,
        description="The result produced in the action. e.g. John wrote a book."
    )


    startTime: Union[str] = Field(None,
        description="The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    target: str = Field(None,
        description="Indicates a target EntryPoint for an Action."
    )


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


    potentialAction: 'Action' = Field(None,
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


class VoteAction(BaseModel):
    """
    VoteAction
    """
    
    candidate: str = Field(None,
        description="A sub property of object. The candidate subject of this action."
    )


    actionOption: Union[Thing,str] = Field(None,
        description="A sub property of object. The options subject to this action. Supersedes option."
    )


    actionStatus: str = Field(None,
        description="Indicates the current disposition of the Action."
    )


    agent: Union[str] = Field(None,
        description="The direct performer or driver of the action (animate or inanimate). e.g. John wrote a book."
    )


    endTime: Union[str] = Field(None,
        description="The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the end of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    error: 'Thing' = Field(None,
        description="For failed actions, more information on the cause of the failure."
    )


    instrument: 'Thing' = Field(None,
        description="The object that helped the agent perform the action. e.g. John wrote a book with a pen."
    )


    location: Union[str] = Field(None,
        description="The location of for example where the event is happening, an organization is located, or where an action takes place."
    )


    object: 'Thing' = Field(None,
        description="The object upon which the action is carried out, whose state is kept intact or changed. Also known as the semantic roles patient, affected or undergoer (which change their state) or theme (which doesn't). e.g. John read a book."
    )


    participant: Union[str] = Field(None,
        description="Other co-agents that participated in the action indirectly. e.g. John wrote a book with Steve."
    )


    result: 'Thing' = Field(None,
        description="The result produced in the action. e.g. John wrote a book."
    )


    startTime: Union[str] = Field(None,
        description="The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    target: str = Field(None,
        description="Indicates a target EntryPoint for an Action."
    )


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


    potentialAction: 'Action' = Field(None,
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


class IgnoreAction(BaseModel):
    """
    IgnoreAction
    """
    
    actionStatus: str = Field(None,
        description="Indicates the current disposition of the Action."
    )


    agent: Union[str] = Field(None,
        description="The direct performer or driver of the action (animate or inanimate). e.g. John wrote a book."
    )


    endTime: Union[str] = Field(None,
        description="The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the end of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    error: 'Thing' = Field(None,
        description="For failed actions, more information on the cause of the failure."
    )


    instrument: 'Thing' = Field(None,
        description="The object that helped the agent perform the action. e.g. John wrote a book with a pen."
    )


    location: Union[str] = Field(None,
        description="The location of for example where the event is happening, an organization is located, or where an action takes place."
    )


    object: 'Thing' = Field(None,
        description="The object upon which the action is carried out, whose state is kept intact or changed. Also known as the semantic roles patient, affected or undergoer (which change their state) or theme (which doesn't). e.g. John read a book."
    )


    participant: Union[str] = Field(None,
        description="Other co-agents that participated in the action indirectly. e.g. John wrote a book with Steve."
    )


    result: 'Thing' = Field(None,
        description="The result produced in the action. e.g. John wrote a book."
    )


    startTime: Union[str] = Field(None,
        description="The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    target: str = Field(None,
        description="Indicates a target EntryPoint for an Action."
    )


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


    potentialAction: 'Action' = Field(None,
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


class ReactAction(BaseModel):
    """
    ReactAction
    """
    
    actionStatus: str = Field(None,
        description="Indicates the current disposition of the Action."
    )


    agent: Union[str] = Field(None,
        description="The direct performer or driver of the action (animate or inanimate). e.g. John wrote a book."
    )


    endTime: Union[str] = Field(None,
        description="The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the end of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    error: 'Thing' = Field(None,
        description="For failed actions, more information on the cause of the failure."
    )


    instrument: 'Thing' = Field(None,
        description="The object that helped the agent perform the action. e.g. John wrote a book with a pen."
    )


    location: Union[str] = Field(None,
        description="The location of for example where the event is happening, an organization is located, or where an action takes place."
    )


    object: 'Thing' = Field(None,
        description="The object upon which the action is carried out, whose state is kept intact or changed. Also known as the semantic roles patient, affected or undergoer (which change their state) or theme (which doesn't). e.g. John read a book."
    )


    participant: Union[str] = Field(None,
        description="Other co-agents that participated in the action indirectly. e.g. John wrote a book with Steve."
    )


    result: 'Thing' = Field(None,
        description="The result produced in the action. e.g. John wrote a book."
    )


    startTime: Union[str] = Field(None,
        description="The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    target: str = Field(None,
        description="Indicates a target EntryPoint for an Action."
    )


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


    potentialAction: 'Action' = Field(None,
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


class AgreeAction(BaseModel):
    """
    AgreeAction
    """
    
    actionStatus: str = Field(None,
        description="Indicates the current disposition of the Action."
    )


    agent: Union[str] = Field(None,
        description="The direct performer or driver of the action (animate or inanimate). e.g. John wrote a book."
    )


    endTime: Union[str] = Field(None,
        description="The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the end of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    error: 'Thing' = Field(None,
        description="For failed actions, more information on the cause of the failure."
    )


    instrument: 'Thing' = Field(None,
        description="The object that helped the agent perform the action. e.g. John wrote a book with a pen."
    )


    location: Union[str] = Field(None,
        description="The location of for example where the event is happening, an organization is located, or where an action takes place."
    )


    object: 'Thing' = Field(None,
        description="The object upon which the action is carried out, whose state is kept intact or changed. Also known as the semantic roles patient, affected or undergoer (which change their state) or theme (which doesn't). e.g. John read a book."
    )


    participant: Union[str] = Field(None,
        description="Other co-agents that participated in the action indirectly. e.g. John wrote a book with Steve."
    )


    result: 'Thing' = Field(None,
        description="The result produced in the action. e.g. John wrote a book."
    )


    startTime: Union[str] = Field(None,
        description="The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    target: str = Field(None,
        description="Indicates a target EntryPoint for an Action."
    )


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


    potentialAction: 'Action' = Field(None,
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


class DisagreeAction(BaseModel):
    """
    DisagreeAction
    """
    
    actionStatus: str = Field(None,
        description="Indicates the current disposition of the Action."
    )


    agent: Union[str] = Field(None,
        description="The direct performer or driver of the action (animate or inanimate). e.g. John wrote a book."
    )


    endTime: Union[str] = Field(None,
        description="The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the end of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    error: 'Thing' = Field(None,
        description="For failed actions, more information on the cause of the failure."
    )


    instrument: 'Thing' = Field(None,
        description="The object that helped the agent perform the action. e.g. John wrote a book with a pen."
    )


    location: Union[str] = Field(None,
        description="The location of for example where the event is happening, an organization is located, or where an action takes place."
    )


    object: 'Thing' = Field(None,
        description="The object upon which the action is carried out, whose state is kept intact or changed. Also known as the semantic roles patient, affected or undergoer (which change their state) or theme (which doesn't). e.g. John read a book."
    )


    participant: Union[str] = Field(None,
        description="Other co-agents that participated in the action indirectly. e.g. John wrote a book with Steve."
    )


    result: 'Thing' = Field(None,
        description="The result produced in the action. e.g. John wrote a book."
    )


    startTime: Union[str] = Field(None,
        description="The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    target: str = Field(None,
        description="Indicates a target EntryPoint for an Action."
    )


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


    potentialAction: 'Action' = Field(None,
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


class DislikeAction(BaseModel):
    """
    DislikeAction
    """
    
    actionStatus: str = Field(None,
        description="Indicates the current disposition of the Action."
    )


    agent: Union[str] = Field(None,
        description="The direct performer or driver of the action (animate or inanimate). e.g. John wrote a book."
    )


    endTime: Union[str] = Field(None,
        description="The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the end of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    error: 'Thing' = Field(None,
        description="For failed actions, more information on the cause of the failure."
    )


    instrument: 'Thing' = Field(None,
        description="The object that helped the agent perform the action. e.g. John wrote a book with a pen."
    )


    location: Union[str] = Field(None,
        description="The location of for example where the event is happening, an organization is located, or where an action takes place."
    )


    object: 'Thing' = Field(None,
        description="The object upon which the action is carried out, whose state is kept intact or changed. Also known as the semantic roles patient, affected or undergoer (which change their state) or theme (which doesn't). e.g. John read a book."
    )


    participant: Union[str] = Field(None,
        description="Other co-agents that participated in the action indirectly. e.g. John wrote a book with Steve."
    )


    result: 'Thing' = Field(None,
        description="The result produced in the action. e.g. John wrote a book."
    )


    startTime: Union[str] = Field(None,
        description="The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    target: str = Field(None,
        description="Indicates a target EntryPoint for an Action."
    )


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


    potentialAction: 'Action' = Field(None,
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


class EndorseAction(BaseModel):
    """
    EndorseAction
    """
    
    endorsee: Union[str] = Field(None,
        description="A sub property of participant. The person/organization being supported."
    )


    actionStatus: str = Field(None,
        description="Indicates the current disposition of the Action."
    )


    agent: Union[str] = Field(None,
        description="The direct performer or driver of the action (animate or inanimate). e.g. John wrote a book."
    )


    endTime: Union[str] = Field(None,
        description="The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the end of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    error: 'Thing' = Field(None,
        description="For failed actions, more information on the cause of the failure."
    )


    instrument: 'Thing' = Field(None,
        description="The object that helped the agent perform the action. e.g. John wrote a book with a pen."
    )


    location: Union[str] = Field(None,
        description="The location of for example where the event is happening, an organization is located, or where an action takes place."
    )


    object: 'Thing' = Field(None,
        description="The object upon which the action is carried out, whose state is kept intact or changed. Also known as the semantic roles patient, affected or undergoer (which change their state) or theme (which doesn't). e.g. John read a book."
    )


    participant: Union[str] = Field(None,
        description="Other co-agents that participated in the action indirectly. e.g. John wrote a book with Steve."
    )


    result: 'Thing' = Field(None,
        description="The result produced in the action. e.g. John wrote a book."
    )


    startTime: Union[str] = Field(None,
        description="The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    target: str = Field(None,
        description="Indicates a target EntryPoint for an Action."
    )


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


    potentialAction: 'Action' = Field(None,
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


class LikeAction(BaseModel):
    """
    LikeAction
    """
    
    actionStatus: str = Field(None,
        description="Indicates the current disposition of the Action."
    )


    agent: Union[str] = Field(None,
        description="The direct performer or driver of the action (animate or inanimate). e.g. John wrote a book."
    )


    endTime: Union[str] = Field(None,
        description="The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the end of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    error: 'Thing' = Field(None,
        description="For failed actions, more information on the cause of the failure."
    )


    instrument: 'Thing' = Field(None,
        description="The object that helped the agent perform the action. e.g. John wrote a book with a pen."
    )


    location: Union[str] = Field(None,
        description="The location of for example where the event is happening, an organization is located, or where an action takes place."
    )


    object: 'Thing' = Field(None,
        description="The object upon which the action is carried out, whose state is kept intact or changed. Also known as the semantic roles patient, affected or undergoer (which change their state) or theme (which doesn't). e.g. John read a book."
    )


    participant: Union[str] = Field(None,
        description="Other co-agents that participated in the action indirectly. e.g. John wrote a book with Steve."
    )


    result: 'Thing' = Field(None,
        description="The result produced in the action. e.g. John wrote a book."
    )


    startTime: Union[str] = Field(None,
        description="The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    target: str = Field(None,
        description="Indicates a target EntryPoint for an Action."
    )


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


    potentialAction: 'Action' = Field(None,
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


class WantAction(BaseModel):
    """
    WantAction
    """
    
    actionStatus: str = Field(None,
        description="Indicates the current disposition of the Action."
    )


    agent: Union[str] = Field(None,
        description="The direct performer or driver of the action (animate or inanimate). e.g. John wrote a book."
    )


    endTime: Union[str] = Field(None,
        description="The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the end of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    error: 'Thing' = Field(None,
        description="For failed actions, more information on the cause of the failure."
    )


    instrument: 'Thing' = Field(None,
        description="The object that helped the agent perform the action. e.g. John wrote a book with a pen."
    )


    location: Union[str] = Field(None,
        description="The location of for example where the event is happening, an organization is located, or where an action takes place."
    )


    object: 'Thing' = Field(None,
        description="The object upon which the action is carried out, whose state is kept intact or changed. Also known as the semantic roles patient, affected or undergoer (which change their state) or theme (which doesn't). e.g. John read a book."
    )


    participant: Union[str] = Field(None,
        description="Other co-agents that participated in the action indirectly. e.g. John wrote a book with Steve."
    )


    result: 'Thing' = Field(None,
        description="The result produced in the action. e.g. John wrote a book."
    )


    startTime: Union[str] = Field(None,
        description="The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    target: str = Field(None,
        description="Indicates a target EntryPoint for an Action."
    )


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


    potentialAction: 'Action' = Field(None,
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


class ReviewAction(BaseModel):
    """
    ReviewAction
    """
    
    resultReview: str = Field(None,
        description="A sub property of result. The review that resulted in the performing of the action."
    )


    actionStatus: str = Field(None,
        description="Indicates the current disposition of the Action."
    )


    agent: Union[str] = Field(None,
        description="The direct performer or driver of the action (animate or inanimate). e.g. John wrote a book."
    )


    endTime: Union[str] = Field(None,
        description="The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the end of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    error: 'Thing' = Field(None,
        description="For failed actions, more information on the cause of the failure."
    )


    instrument: 'Thing' = Field(None,
        description="The object that helped the agent perform the action. e.g. John wrote a book with a pen."
    )


    location: Union[str] = Field(None,
        description="The location of for example where the event is happening, an organization is located, or where an action takes place."
    )


    object: 'Thing' = Field(None,
        description="The object upon which the action is carried out, whose state is kept intact or changed. Also known as the semantic roles patient, affected or undergoer (which change their state) or theme (which doesn't). e.g. John read a book."
    )


    participant: Union[str] = Field(None,
        description="Other co-agents that participated in the action indirectly. e.g. John wrote a book with Steve."
    )


    result: 'Thing' = Field(None,
        description="The result produced in the action. e.g. John wrote a book."
    )


    startTime: Union[str] = Field(None,
        description="The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    target: str = Field(None,
        description="Indicates a target EntryPoint for an Action."
    )


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


    potentialAction: 'Action' = Field(None,
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


class ConsumeAction(BaseModel):
    """
    ConsumeAction
    """
    
    actionAccessibilityRequirement: str = Field(None,
        description="A set of requirements that a must be fulfilled in order to perform an Action. If more than one value is specied, fulfilling one set of requirements will allow the Action to be performed."
    )


    expectsAcceptanceOf: str = Field(None,
        description="An Offer which must be accepted before the user can perform the Action. For example, the user may need to buy a movie before being able to watch it."
    )


    actionStatus: str = Field(None,
        description="Indicates the current disposition of the Action."
    )


    agent: Union[str] = Field(None,
        description="The direct performer or driver of the action (animate or inanimate). e.g. John wrote a book."
    )


    endTime: Union[str] = Field(None,
        description="The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the end of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    error: 'Thing' = Field(None,
        description="For failed actions, more information on the cause of the failure."
    )


    instrument: 'Thing' = Field(None,
        description="The object that helped the agent perform the action. e.g. John wrote a book with a pen."
    )


    location: Union[str] = Field(None,
        description="The location of for example where the event is happening, an organization is located, or where an action takes place."
    )


    object: 'Thing' = Field(None,
        description="The object upon which the action is carried out, whose state is kept intact or changed. Also known as the semantic roles patient, affected or undergoer (which change their state) or theme (which doesn't). e.g. John read a book."
    )


    participant: Union[str] = Field(None,
        description="Other co-agents that participated in the action indirectly. e.g. John wrote a book with Steve."
    )


    result: 'Thing' = Field(None,
        description="The result produced in the action. e.g. John wrote a book."
    )


    startTime: Union[str] = Field(None,
        description="The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    target: str = Field(None,
        description="Indicates a target EntryPoint for an Action."
    )


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


    potentialAction: 'Action' = Field(None,
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


class DrinkAction(BaseModel):
    """
    DrinkAction
    """
    
    actionAccessibilityRequirement: str = Field(None,
        description="A set of requirements that a must be fulfilled in order to perform an Action. If more than one value is specied, fulfilling one set of requirements will allow the Action to be performed."
    )


    expectsAcceptanceOf: str = Field(None,
        description="An Offer which must be accepted before the user can perform the Action. For example, the user may need to buy a movie before being able to watch it."
    )


    actionStatus: str = Field(None,
        description="Indicates the current disposition of the Action."
    )


    agent: Union[str] = Field(None,
        description="The direct performer or driver of the action (animate or inanimate). e.g. John wrote a book."
    )


    endTime: Union[str] = Field(None,
        description="The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the end of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    error: 'Thing' = Field(None,
        description="For failed actions, more information on the cause of the failure."
    )


    instrument: 'Thing' = Field(None,
        description="The object that helped the agent perform the action. e.g. John wrote a book with a pen."
    )


    location: Union[str] = Field(None,
        description="The location of for example where the event is happening, an organization is located, or where an action takes place."
    )


    object: 'Thing' = Field(None,
        description="The object upon which the action is carried out, whose state is kept intact or changed. Also known as the semantic roles patient, affected or undergoer (which change their state) or theme (which doesn't). e.g. John read a book."
    )


    participant: Union[str] = Field(None,
        description="Other co-agents that participated in the action indirectly. e.g. John wrote a book with Steve."
    )


    result: 'Thing' = Field(None,
        description="The result produced in the action. e.g. John wrote a book."
    )


    startTime: Union[str] = Field(None,
        description="The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    target: str = Field(None,
        description="Indicates a target EntryPoint for an Action."
    )


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


    potentialAction: 'Action' = Field(None,
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


class EatAction(BaseModel):
    """
    EatAction
    """
    
    actionAccessibilityRequirement: str = Field(None,
        description="A set of requirements that a must be fulfilled in order to perform an Action. If more than one value is specied, fulfilling one set of requirements will allow the Action to be performed."
    )


    expectsAcceptanceOf: str = Field(None,
        description="An Offer which must be accepted before the user can perform the Action. For example, the user may need to buy a movie before being able to watch it."
    )


    actionStatus: str = Field(None,
        description="Indicates the current disposition of the Action."
    )


    agent: Union[str] = Field(None,
        description="The direct performer or driver of the action (animate or inanimate). e.g. John wrote a book."
    )


    endTime: Union[str] = Field(None,
        description="The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the end of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    error: 'Thing' = Field(None,
        description="For failed actions, more information on the cause of the failure."
    )


    instrument: 'Thing' = Field(None,
        description="The object that helped the agent perform the action. e.g. John wrote a book with a pen."
    )


    location: Union[str] = Field(None,
        description="The location of for example where the event is happening, an organization is located, or where an action takes place."
    )


    object: 'Thing' = Field(None,
        description="The object upon which the action is carried out, whose state is kept intact or changed. Also known as the semantic roles patient, affected or undergoer (which change their state) or theme (which doesn't). e.g. John read a book."
    )


    participant: Union[str] = Field(None,
        description="Other co-agents that participated in the action indirectly. e.g. John wrote a book with Steve."
    )


    result: 'Thing' = Field(None,
        description="The result produced in the action. e.g. John wrote a book."
    )


    startTime: Union[str] = Field(None,
        description="The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    target: str = Field(None,
        description="Indicates a target EntryPoint for an Action."
    )


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


    potentialAction: 'Action' = Field(None,
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


class InstallAction(BaseModel):
    """
    InstallAction
    """
    
    actionAccessibilityRequirement: str = Field(None,
        description="A set of requirements that a must be fulfilled in order to perform an Action. If more than one value is specied, fulfilling one set of requirements will allow the Action to be performed."
    )


    expectsAcceptanceOf: str = Field(None,
        description="An Offer which must be accepted before the user can perform the Action. For example, the user may need to buy a movie before being able to watch it."
    )


    actionStatus: str = Field(None,
        description="Indicates the current disposition of the Action."
    )


    agent: Union[str] = Field(None,
        description="The direct performer or driver of the action (animate or inanimate). e.g. John wrote a book."
    )


    endTime: Union[str] = Field(None,
        description="The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the end of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    error: 'Thing' = Field(None,
        description="For failed actions, more information on the cause of the failure."
    )


    instrument: 'Thing' = Field(None,
        description="The object that helped the agent perform the action. e.g. John wrote a book with a pen."
    )


    location: Union[str] = Field(None,
        description="The location of for example where the event is happening, an organization is located, or where an action takes place."
    )


    object: 'Thing' = Field(None,
        description="The object upon which the action is carried out, whose state is kept intact or changed. Also known as the semantic roles patient, affected or undergoer (which change their state) or theme (which doesn't). e.g. John read a book."
    )


    participant: Union[str] = Field(None,
        description="Other co-agents that participated in the action indirectly. e.g. John wrote a book with Steve."
    )


    result: 'Thing' = Field(None,
        description="The result produced in the action. e.g. John wrote a book."
    )


    startTime: Union[str] = Field(None,
        description="The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    target: str = Field(None,
        description="Indicates a target EntryPoint for an Action."
    )


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


    potentialAction: 'Action' = Field(None,
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


class ListenAction(BaseModel):
    """
    ListenAction
    """
    
    actionAccessibilityRequirement: str = Field(None,
        description="A set of requirements that a must be fulfilled in order to perform an Action. If more than one value is specied, fulfilling one set of requirements will allow the Action to be performed."
    )


    expectsAcceptanceOf: str = Field(None,
        description="An Offer which must be accepted before the user can perform the Action. For example, the user may need to buy a movie before being able to watch it."
    )


    actionStatus: str = Field(None,
        description="Indicates the current disposition of the Action."
    )


    agent: Union[str] = Field(None,
        description="The direct performer or driver of the action (animate or inanimate). e.g. John wrote a book."
    )


    endTime: Union[str] = Field(None,
        description="The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the end of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    error: 'Thing' = Field(None,
        description="For failed actions, more information on the cause of the failure."
    )


    instrument: 'Thing' = Field(None,
        description="The object that helped the agent perform the action. e.g. John wrote a book with a pen."
    )


    location: Union[str] = Field(None,
        description="The location of for example where the event is happening, an organization is located, or where an action takes place."
    )


    object: 'Thing' = Field(None,
        description="The object upon which the action is carried out, whose state is kept intact or changed. Also known as the semantic roles patient, affected or undergoer (which change their state) or theme (which doesn't). e.g. John read a book."
    )


    participant: Union[str] = Field(None,
        description="Other co-agents that participated in the action indirectly. e.g. John wrote a book with Steve."
    )


    result: 'Thing' = Field(None,
        description="The result produced in the action. e.g. John wrote a book."
    )


    startTime: Union[str] = Field(None,
        description="The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    target: str = Field(None,
        description="Indicates a target EntryPoint for an Action."
    )


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


    potentialAction: 'Action' = Field(None,
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


class ReadAction(BaseModel):
    """
    ReadAction
    """
    
    actionAccessibilityRequirement: str = Field(None,
        description="A set of requirements that a must be fulfilled in order to perform an Action. If more than one value is specied, fulfilling one set of requirements will allow the Action to be performed."
    )


    expectsAcceptanceOf: str = Field(None,
        description="An Offer which must be accepted before the user can perform the Action. For example, the user may need to buy a movie before being able to watch it."
    )


    actionStatus: str = Field(None,
        description="Indicates the current disposition of the Action."
    )


    agent: Union[str] = Field(None,
        description="The direct performer or driver of the action (animate or inanimate). e.g. John wrote a book."
    )


    endTime: Union[str] = Field(None,
        description="The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the end of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    error: 'Thing' = Field(None,
        description="For failed actions, more information on the cause of the failure."
    )


    instrument: 'Thing' = Field(None,
        description="The object that helped the agent perform the action. e.g. John wrote a book with a pen."
    )


    location: Union[str] = Field(None,
        description="The location of for example where the event is happening, an organization is located, or where an action takes place."
    )


    object: 'Thing' = Field(None,
        description="The object upon which the action is carried out, whose state is kept intact or changed. Also known as the semantic roles patient, affected or undergoer (which change their state) or theme (which doesn't). e.g. John read a book."
    )


    participant: Union[str] = Field(None,
        description="Other co-agents that participated in the action indirectly. e.g. John wrote a book with Steve."
    )


    result: 'Thing' = Field(None,
        description="The result produced in the action. e.g. John wrote a book."
    )


    startTime: Union[str] = Field(None,
        description="The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    target: str = Field(None,
        description="Indicates a target EntryPoint for an Action."
    )


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


    potentialAction: 'Action' = Field(None,
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


class UseAction(BaseModel):
    """
    UseAction
    """
    
    actionAccessibilityRequirement: str = Field(None,
        description="A set of requirements that a must be fulfilled in order to perform an Action. If more than one value is specied, fulfilling one set of requirements will allow the Action to be performed."
    )


    expectsAcceptanceOf: str = Field(None,
        description="An Offer which must be accepted before the user can perform the Action. For example, the user may need to buy a movie before being able to watch it."
    )


    actionStatus: str = Field(None,
        description="Indicates the current disposition of the Action."
    )


    agent: Union[str] = Field(None,
        description="The direct performer or driver of the action (animate or inanimate). e.g. John wrote a book."
    )


    endTime: Union[str] = Field(None,
        description="The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the end of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    error: 'Thing' = Field(None,
        description="For failed actions, more information on the cause of the failure."
    )


    instrument: 'Thing' = Field(None,
        description="The object that helped the agent perform the action. e.g. John wrote a book with a pen."
    )


    location: Union[str] = Field(None,
        description="The location of for example where the event is happening, an organization is located, or where an action takes place."
    )


    object: 'Thing' = Field(None,
        description="The object upon which the action is carried out, whose state is kept intact or changed. Also known as the semantic roles patient, affected or undergoer (which change their state) or theme (which doesn't). e.g. John read a book."
    )


    participant: Union[str] = Field(None,
        description="Other co-agents that participated in the action indirectly. e.g. John wrote a book with Steve."
    )


    result: 'Thing' = Field(None,
        description="The result produced in the action. e.g. John wrote a book."
    )


    startTime: Union[str] = Field(None,
        description="The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    target: str = Field(None,
        description="Indicates a target EntryPoint for an Action."
    )


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


    potentialAction: 'Action' = Field(None,
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


class WearAction(BaseModel):
    """
    WearAction
    """
    
    actionAccessibilityRequirement: str = Field(None,
        description="A set of requirements that a must be fulfilled in order to perform an Action. If more than one value is specied, fulfilling one set of requirements will allow the Action to be performed."
    )


    expectsAcceptanceOf: str = Field(None,
        description="An Offer which must be accepted before the user can perform the Action. For example, the user may need to buy a movie before being able to watch it."
    )


    actionStatus: str = Field(None,
        description="Indicates the current disposition of the Action."
    )


    agent: Union[str] = Field(None,
        description="The direct performer or driver of the action (animate or inanimate). e.g. John wrote a book."
    )


    endTime: Union[str] = Field(None,
        description="The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the end of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    error: 'Thing' = Field(None,
        description="For failed actions, more information on the cause of the failure."
    )


    instrument: 'Thing' = Field(None,
        description="The object that helped the agent perform the action. e.g. John wrote a book with a pen."
    )


    location: Union[str] = Field(None,
        description="The location of for example where the event is happening, an organization is located, or where an action takes place."
    )


    object: 'Thing' = Field(None,
        description="The object upon which the action is carried out, whose state is kept intact or changed. Also known as the semantic roles patient, affected or undergoer (which change their state) or theme (which doesn't). e.g. John read a book."
    )


    participant: Union[str] = Field(None,
        description="Other co-agents that participated in the action indirectly. e.g. John wrote a book with Steve."
    )


    result: 'Thing' = Field(None,
        description="The result produced in the action. e.g. John wrote a book."
    )


    startTime: Union[str] = Field(None,
        description="The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    target: str = Field(None,
        description="Indicates a target EntryPoint for an Action."
    )


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


    potentialAction: 'Action' = Field(None,
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


class ViewAction(BaseModel):
    """
    ViewAction
    """
    
    actionAccessibilityRequirement: str = Field(None,
        description="A set of requirements that a must be fulfilled in order to perform an Action. If more than one value is specied, fulfilling one set of requirements will allow the Action to be performed."
    )


    expectsAcceptanceOf: str = Field(None,
        description="An Offer which must be accepted before the user can perform the Action. For example, the user may need to buy a movie before being able to watch it."
    )


    actionStatus: str = Field(None,
        description="Indicates the current disposition of the Action."
    )


    agent: Union[str] = Field(None,
        description="The direct performer or driver of the action (animate or inanimate). e.g. John wrote a book."
    )


    endTime: Union[str] = Field(None,
        description="The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the end of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    error: 'Thing' = Field(None,
        description="For failed actions, more information on the cause of the failure."
    )


    instrument: 'Thing' = Field(None,
        description="The object that helped the agent perform the action. e.g. John wrote a book with a pen."
    )


    location: Union[str] = Field(None,
        description="The location of for example where the event is happening, an organization is located, or where an action takes place."
    )


    object: 'Thing' = Field(None,
        description="The object upon which the action is carried out, whose state is kept intact or changed. Also known as the semantic roles patient, affected or undergoer (which change their state) or theme (which doesn't). e.g. John read a book."
    )


    participant: Union[str] = Field(None,
        description="Other co-agents that participated in the action indirectly. e.g. John wrote a book with Steve."
    )


    result: 'Thing' = Field(None,
        description="The result produced in the action. e.g. John wrote a book."
    )


    startTime: Union[str] = Field(None,
        description="The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    target: str = Field(None,
        description="Indicates a target EntryPoint for an Action."
    )


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


    potentialAction: 'Action' = Field(None,
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


class WatchAction(BaseModel):
    """
    WatchAction
    """
    
    actionAccessibilityRequirement: str = Field(None,
        description="A set of requirements that a must be fulfilled in order to perform an Action. If more than one value is specied, fulfilling one set of requirements will allow the Action to be performed."
    )


    expectsAcceptanceOf: str = Field(None,
        description="An Offer which must be accepted before the user can perform the Action. For example, the user may need to buy a movie before being able to watch it."
    )


    actionStatus: str = Field(None,
        description="Indicates the current disposition of the Action."
    )


    agent: Union[str] = Field(None,
        description="The direct performer or driver of the action (animate or inanimate). e.g. John wrote a book."
    )


    endTime: Union[str] = Field(None,
        description="The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the end of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    error: 'Thing' = Field(None,
        description="For failed actions, more information on the cause of the failure."
    )


    instrument: 'Thing' = Field(None,
        description="The object that helped the agent perform the action. e.g. John wrote a book with a pen."
    )


    location: Union[str] = Field(None,
        description="The location of for example where the event is happening, an organization is located, or where an action takes place."
    )


    object: 'Thing' = Field(None,
        description="The object upon which the action is carried out, whose state is kept intact or changed. Also known as the semantic roles patient, affected or undergoer (which change their state) or theme (which doesn't). e.g. John read a book."
    )


    participant: Union[str] = Field(None,
        description="Other co-agents that participated in the action indirectly. e.g. John wrote a book with Steve."
    )


    result: 'Thing' = Field(None,
        description="The result produced in the action. e.g. John wrote a book."
    )


    startTime: Union[str] = Field(None,
        description="The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    target: str = Field(None,
        description="Indicates a target EntryPoint for an Action."
    )


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


    potentialAction: 'Action' = Field(None,
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


class ControlAction(BaseModel):
    """
    ControlAction
    """
    
    actionStatus: str = Field(None,
        description="Indicates the current disposition of the Action."
    )


    agent: Union[str] = Field(None,
        description="The direct performer or driver of the action (animate or inanimate). e.g. John wrote a book."
    )


    endTime: Union[str] = Field(None,
        description="The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the end of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    error: 'Thing' = Field(None,
        description="For failed actions, more information on the cause of the failure."
    )


    instrument: 'Thing' = Field(None,
        description="The object that helped the agent perform the action. e.g. John wrote a book with a pen."
    )


    location: Union[str] = Field(None,
        description="The location of for example where the event is happening, an organization is located, or where an action takes place."
    )


    object: 'Thing' = Field(None,
        description="The object upon which the action is carried out, whose state is kept intact or changed. Also known as the semantic roles patient, affected or undergoer (which change their state) or theme (which doesn't). e.g. John read a book."
    )


    participant: Union[str] = Field(None,
        description="Other co-agents that participated in the action indirectly. e.g. John wrote a book with Steve."
    )


    result: 'Thing' = Field(None,
        description="The result produced in the action. e.g. John wrote a book."
    )


    startTime: Union[str] = Field(None,
        description="The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    target: str = Field(None,
        description="Indicates a target EntryPoint for an Action."
    )


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


    potentialAction: 'Action' = Field(None,
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


class ActivateAction(BaseModel):
    """
    ActivateAction
    """
    
    actionStatus: str = Field(None,
        description="Indicates the current disposition of the Action."
    )


    agent: Union[str] = Field(None,
        description="The direct performer or driver of the action (animate or inanimate). e.g. John wrote a book."
    )


    endTime: Union[str] = Field(None,
        description="The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the end of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    error: 'Thing' = Field(None,
        description="For failed actions, more information on the cause of the failure."
    )


    instrument: 'Thing' = Field(None,
        description="The object that helped the agent perform the action. e.g. John wrote a book with a pen."
    )


    location: Union[str] = Field(None,
        description="The location of for example where the event is happening, an organization is located, or where an action takes place."
    )


    object: 'Thing' = Field(None,
        description="The object upon which the action is carried out, whose state is kept intact or changed. Also known as the semantic roles patient, affected or undergoer (which change their state) or theme (which doesn't). e.g. John read a book."
    )


    participant: Union[str] = Field(None,
        description="Other co-agents that participated in the action indirectly. e.g. John wrote a book with Steve."
    )


    result: 'Thing' = Field(None,
        description="The result produced in the action. e.g. John wrote a book."
    )


    startTime: Union[str] = Field(None,
        description="The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    target: str = Field(None,
        description="Indicates a target EntryPoint for an Action."
    )


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


    potentialAction: 'Action' = Field(None,
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


class DeactivateAction(BaseModel):
    """
    DeactivateAction
    """
    
    actionStatus: str = Field(None,
        description="Indicates the current disposition of the Action."
    )


    agent: Union[str] = Field(None,
        description="The direct performer or driver of the action (animate or inanimate). e.g. John wrote a book."
    )


    endTime: Union[str] = Field(None,
        description="The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the end of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    error: 'Thing' = Field(None,
        description="For failed actions, more information on the cause of the failure."
    )


    instrument: 'Thing' = Field(None,
        description="The object that helped the agent perform the action. e.g. John wrote a book with a pen."
    )


    location: Union[str] = Field(None,
        description="The location of for example where the event is happening, an organization is located, or where an action takes place."
    )


    object: 'Thing' = Field(None,
        description="The object upon which the action is carried out, whose state is kept intact or changed. Also known as the semantic roles patient, affected or undergoer (which change their state) or theme (which doesn't). e.g. John read a book."
    )


    participant: Union[str] = Field(None,
        description="Other co-agents that participated in the action indirectly. e.g. John wrote a book with Steve."
    )


    result: 'Thing' = Field(None,
        description="The result produced in the action. e.g. John wrote a book."
    )


    startTime: Union[str] = Field(None,
        description="The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    target: str = Field(None,
        description="Indicates a target EntryPoint for an Action."
    )


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


    potentialAction: 'Action' = Field(None,
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


class ResumeAction(BaseModel):
    """
    ResumeAction
    """
    
    actionStatus: str = Field(None,
        description="Indicates the current disposition of the Action."
    )


    agent: Union[str] = Field(None,
        description="The direct performer or driver of the action (animate or inanimate). e.g. John wrote a book."
    )


    endTime: Union[str] = Field(None,
        description="The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the end of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    error: 'Thing' = Field(None,
        description="For failed actions, more information on the cause of the failure."
    )


    instrument: 'Thing' = Field(None,
        description="The object that helped the agent perform the action. e.g. John wrote a book with a pen."
    )


    location: Union[str] = Field(None,
        description="The location of for example where the event is happening, an organization is located, or where an action takes place."
    )


    object: 'Thing' = Field(None,
        description="The object upon which the action is carried out, whose state is kept intact or changed. Also known as the semantic roles patient, affected or undergoer (which change their state) or theme (which doesn't). e.g. John read a book."
    )


    participant: Union[str] = Field(None,
        description="Other co-agents that participated in the action indirectly. e.g. John wrote a book with Steve."
    )


    result: 'Thing' = Field(None,
        description="The result produced in the action. e.g. John wrote a book."
    )


    startTime: Union[str] = Field(None,
        description="The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    target: str = Field(None,
        description="Indicates a target EntryPoint for an Action."
    )


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


    potentialAction: 'Action' = Field(None,
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


class SuspendAction(BaseModel):
    """
    SuspendAction
    """
    
    actionStatus: str = Field(None,
        description="Indicates the current disposition of the Action."
    )


    agent: Union[str] = Field(None,
        description="The direct performer or driver of the action (animate or inanimate). e.g. John wrote a book."
    )


    endTime: Union[str] = Field(None,
        description="The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the end of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    error: 'Thing' = Field(None,
        description="For failed actions, more information on the cause of the failure."
    )


    instrument: 'Thing' = Field(None,
        description="The object that helped the agent perform the action. e.g. John wrote a book with a pen."
    )


    location: Union[str] = Field(None,
        description="The location of for example where the event is happening, an organization is located, or where an action takes place."
    )


    object: 'Thing' = Field(None,
        description="The object upon which the action is carried out, whose state is kept intact or changed. Also known as the semantic roles patient, affected or undergoer (which change their state) or theme (which doesn't). e.g. John read a book."
    )


    participant: Union[str] = Field(None,
        description="Other co-agents that participated in the action indirectly. e.g. John wrote a book with Steve."
    )


    result: 'Thing' = Field(None,
        description="The result produced in the action. e.g. John wrote a book."
    )


    startTime: Union[str] = Field(None,
        description="The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    target: str = Field(None,
        description="Indicates a target EntryPoint for an Action."
    )


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


    potentialAction: 'Action' = Field(None,
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


class CreateAction(BaseModel):
    """
    CreateAction
    """
    
    actionStatus: str = Field(None,
        description="Indicates the current disposition of the Action."
    )


    agent: Union[str] = Field(None,
        description="The direct performer or driver of the action (animate or inanimate). e.g. John wrote a book."
    )


    endTime: Union[str] = Field(None,
        description="The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the end of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    error: 'Thing' = Field(None,
        description="For failed actions, more information on the cause of the failure."
    )


    instrument: 'Thing' = Field(None,
        description="The object that helped the agent perform the action. e.g. John wrote a book with a pen."
    )


    location: Union[str] = Field(None,
        description="The location of for example where the event is happening, an organization is located, or where an action takes place."
    )


    object: 'Thing' = Field(None,
        description="The object upon which the action is carried out, whose state is kept intact or changed. Also known as the semantic roles patient, affected or undergoer (which change their state) or theme (which doesn't). e.g. John read a book."
    )


    participant: Union[str] = Field(None,
        description="Other co-agents that participated in the action indirectly. e.g. John wrote a book with Steve."
    )


    result: 'Thing' = Field(None,
        description="The result produced in the action. e.g. John wrote a book."
    )


    startTime: Union[str] = Field(None,
        description="The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    target: str = Field(None,
        description="Indicates a target EntryPoint for an Action."
    )


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


    potentialAction: 'Action' = Field(None,
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


class CookAction(BaseModel):
    """
    CookAction
    """
    
    foodEstablishment: Union[str] = Field(None,
        description="A sub property of location. The specific food establishment where the action occurred."
    )


    foodEvent: str = Field(None,
        description="A sub property of location. The specific food event where the action occurred."
    )


    recipe: str = Field(None,
        description="A sub property of instrument. The recipe/instructions used to perform the action."
    )


    actionStatus: str = Field(None,
        description="Indicates the current disposition of the Action."
    )


    agent: Union[str] = Field(None,
        description="The direct performer or driver of the action (animate or inanimate). e.g. John wrote a book."
    )


    endTime: Union[str] = Field(None,
        description="The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the end of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    error: 'Thing' = Field(None,
        description="For failed actions, more information on the cause of the failure."
    )


    instrument: 'Thing' = Field(None,
        description="The object that helped the agent perform the action. e.g. John wrote a book with a pen."
    )


    location: Union[str] = Field(None,
        description="The location of for example where the event is happening, an organization is located, or where an action takes place."
    )


    object: 'Thing' = Field(None,
        description="The object upon which the action is carried out, whose state is kept intact or changed. Also known as the semantic roles patient, affected or undergoer (which change their state) or theme (which doesn't). e.g. John read a book."
    )


    participant: Union[str] = Field(None,
        description="Other co-agents that participated in the action indirectly. e.g. John wrote a book with Steve."
    )


    result: 'Thing' = Field(None,
        description="The result produced in the action. e.g. John wrote a book."
    )


    startTime: Union[str] = Field(None,
        description="The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    target: str = Field(None,
        description="Indicates a target EntryPoint for an Action."
    )


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


    potentialAction: 'Action' = Field(None,
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


class DrawAction(BaseModel):
    """
    DrawAction
    """
    
    actionStatus: str = Field(None,
        description="Indicates the current disposition of the Action."
    )


    agent: Union[str] = Field(None,
        description="The direct performer or driver of the action (animate or inanimate). e.g. John wrote a book."
    )


    endTime: Union[str] = Field(None,
        description="The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the end of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    error: 'Thing' = Field(None,
        description="For failed actions, more information on the cause of the failure."
    )


    instrument: 'Thing' = Field(None,
        description="The object that helped the agent perform the action. e.g. John wrote a book with a pen."
    )


    location: Union[str] = Field(None,
        description="The location of for example where the event is happening, an organization is located, or where an action takes place."
    )


    object: 'Thing' = Field(None,
        description="The object upon which the action is carried out, whose state is kept intact or changed. Also known as the semantic roles patient, affected or undergoer (which change their state) or theme (which doesn't). e.g. John read a book."
    )


    participant: Union[str] = Field(None,
        description="Other co-agents that participated in the action indirectly. e.g. John wrote a book with Steve."
    )


    result: 'Thing' = Field(None,
        description="The result produced in the action. e.g. John wrote a book."
    )


    startTime: Union[str] = Field(None,
        description="The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    target: str = Field(None,
        description="Indicates a target EntryPoint for an Action."
    )


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


    potentialAction: 'Action' = Field(None,
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


class FilmAction(BaseModel):
    """
    FilmAction
    """
    
    actionStatus: str = Field(None,
        description="Indicates the current disposition of the Action."
    )


    agent: Union[str] = Field(None,
        description="The direct performer or driver of the action (animate or inanimate). e.g. John wrote a book."
    )


    endTime: Union[str] = Field(None,
        description="The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the end of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    error: 'Thing' = Field(None,
        description="For failed actions, more information on the cause of the failure."
    )


    instrument: 'Thing' = Field(None,
        description="The object that helped the agent perform the action. e.g. John wrote a book with a pen."
    )


    location: Union[str] = Field(None,
        description="The location of for example where the event is happening, an organization is located, or where an action takes place."
    )


    object: 'Thing' = Field(None,
        description="The object upon which the action is carried out, whose state is kept intact or changed. Also known as the semantic roles patient, affected or undergoer (which change their state) or theme (which doesn't). e.g. John read a book."
    )


    participant: Union[str] = Field(None,
        description="Other co-agents that participated in the action indirectly. e.g. John wrote a book with Steve."
    )


    result: 'Thing' = Field(None,
        description="The result produced in the action. e.g. John wrote a book."
    )


    startTime: Union[str] = Field(None,
        description="The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    target: str = Field(None,
        description="Indicates a target EntryPoint for an Action."
    )


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


    potentialAction: 'Action' = Field(None,
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


class PaintAction(BaseModel):
    """
    PaintAction
    """
    
    actionStatus: str = Field(None,
        description="Indicates the current disposition of the Action."
    )


    agent: Union[str] = Field(None,
        description="The direct performer or driver of the action (animate or inanimate). e.g. John wrote a book."
    )


    endTime: Union[str] = Field(None,
        description="The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the end of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    error: 'Thing' = Field(None,
        description="For failed actions, more information on the cause of the failure."
    )


    instrument: 'Thing' = Field(None,
        description="The object that helped the agent perform the action. e.g. John wrote a book with a pen."
    )


    location: Union[str] = Field(None,
        description="The location of for example where the event is happening, an organization is located, or where an action takes place."
    )


    object: 'Thing' = Field(None,
        description="The object upon which the action is carried out, whose state is kept intact or changed. Also known as the semantic roles patient, affected or undergoer (which change their state) or theme (which doesn't). e.g. John read a book."
    )


    participant: Union[str] = Field(None,
        description="Other co-agents that participated in the action indirectly. e.g. John wrote a book with Steve."
    )


    result: 'Thing' = Field(None,
        description="The result produced in the action. e.g. John wrote a book."
    )


    startTime: Union[str] = Field(None,
        description="The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    target: str = Field(None,
        description="Indicates a target EntryPoint for an Action."
    )


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


    potentialAction: 'Action' = Field(None,
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


class PhotographAction(BaseModel):
    """
    PhotographAction
    """
    
    actionStatus: str = Field(None,
        description="Indicates the current disposition of the Action."
    )


    agent: Union[str] = Field(None,
        description="The direct performer or driver of the action (animate or inanimate). e.g. John wrote a book."
    )


    endTime: Union[str] = Field(None,
        description="The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the end of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    error: 'Thing' = Field(None,
        description="For failed actions, more information on the cause of the failure."
    )


    instrument: 'Thing' = Field(None,
        description="The object that helped the agent perform the action. e.g. John wrote a book with a pen."
    )


    location: Union[str] = Field(None,
        description="The location of for example where the event is happening, an organization is located, or where an action takes place."
    )


    object: 'Thing' = Field(None,
        description="The object upon which the action is carried out, whose state is kept intact or changed. Also known as the semantic roles patient, affected or undergoer (which change their state) or theme (which doesn't). e.g. John read a book."
    )


    participant: Union[str] = Field(None,
        description="Other co-agents that participated in the action indirectly. e.g. John wrote a book with Steve."
    )


    result: 'Thing' = Field(None,
        description="The result produced in the action. e.g. John wrote a book."
    )


    startTime: Union[str] = Field(None,
        description="The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    target: str = Field(None,
        description="Indicates a target EntryPoint for an Action."
    )


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


    potentialAction: 'Action' = Field(None,
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


class WriteAction(BaseModel):
    """
    WriteAction
    """
    
    inLanguage: Union[str] = Field(None,
        description="The language of the content or performance or used in an action. Please use one of the language codes from the IETF BCP 47 standard. See also availableLanguage. Supersedes language."
    )


    actionStatus: str = Field(None,
        description="Indicates the current disposition of the Action."
    )


    agent: Union[str] = Field(None,
        description="The direct performer or driver of the action (animate or inanimate). e.g. John wrote a book."
    )


    endTime: Union[str] = Field(None,
        description="The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the end of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    error: 'Thing' = Field(None,
        description="For failed actions, more information on the cause of the failure."
    )


    instrument: 'Thing' = Field(None,
        description="The object that helped the agent perform the action. e.g. John wrote a book with a pen."
    )


    location: Union[str] = Field(None,
        description="The location of for example where the event is happening, an organization is located, or where an action takes place."
    )


    object: 'Thing' = Field(None,
        description="The object upon which the action is carried out, whose state is kept intact or changed. Also known as the semantic roles patient, affected or undergoer (which change their state) or theme (which doesn't). e.g. John read a book."
    )


    participant: Union[str] = Field(None,
        description="Other co-agents that participated in the action indirectly. e.g. John wrote a book with Steve."
    )


    result: 'Thing' = Field(None,
        description="The result produced in the action. e.g. John wrote a book."
    )


    startTime: Union[str] = Field(None,
        description="The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    target: str = Field(None,
        description="Indicates a target EntryPoint for an Action."
    )


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


    potentialAction: 'Action' = Field(None,
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


class FindAction(BaseModel):
    """
    FindAction
    """
    
    actionStatus: str = Field(None,
        description="Indicates the current disposition of the Action."
    )


    agent: Union[str] = Field(None,
        description="The direct performer or driver of the action (animate or inanimate). e.g. John wrote a book."
    )


    endTime: Union[str] = Field(None,
        description="The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the end of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    error: 'Thing' = Field(None,
        description="For failed actions, more information on the cause of the failure."
    )


    instrument: 'Thing' = Field(None,
        description="The object that helped the agent perform the action. e.g. John wrote a book with a pen."
    )


    location: Union[str] = Field(None,
        description="The location of for example where the event is happening, an organization is located, or where an action takes place."
    )


    object: 'Thing' = Field(None,
        description="The object upon which the action is carried out, whose state is kept intact or changed. Also known as the semantic roles patient, affected or undergoer (which change their state) or theme (which doesn't). e.g. John read a book."
    )


    participant: Union[str] = Field(None,
        description="Other co-agents that participated in the action indirectly. e.g. John wrote a book with Steve."
    )


    result: 'Thing' = Field(None,
        description="The result produced in the action. e.g. John wrote a book."
    )


    startTime: Union[str] = Field(None,
        description="The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    target: str = Field(None,
        description="Indicates a target EntryPoint for an Action."
    )


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


    potentialAction: 'Action' = Field(None,
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


class CheckAction(BaseModel):
    """
    CheckAction
    """
    
    actionStatus: str = Field(None,
        description="Indicates the current disposition of the Action."
    )


    agent: Union[str] = Field(None,
        description="The direct performer or driver of the action (animate or inanimate). e.g. John wrote a book."
    )


    endTime: Union[str] = Field(None,
        description="The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the end of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    error: 'Thing' = Field(None,
        description="For failed actions, more information on the cause of the failure."
    )


    instrument: 'Thing' = Field(None,
        description="The object that helped the agent perform the action. e.g. John wrote a book with a pen."
    )


    location: Union[str] = Field(None,
        description="The location of for example where the event is happening, an organization is located, or where an action takes place."
    )


    object: 'Thing' = Field(None,
        description="The object upon which the action is carried out, whose state is kept intact or changed. Also known as the semantic roles patient, affected or undergoer (which change their state) or theme (which doesn't). e.g. John read a book."
    )


    participant: Union[str] = Field(None,
        description="Other co-agents that participated in the action indirectly. e.g. John wrote a book with Steve."
    )


    result: 'Thing' = Field(None,
        description="The result produced in the action. e.g. John wrote a book."
    )


    startTime: Union[str] = Field(None,
        description="The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    target: str = Field(None,
        description="Indicates a target EntryPoint for an Action."
    )


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


    potentialAction: 'Action' = Field(None,
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


class DiscoverAction(BaseModel):
    """
    DiscoverAction
    """
    
    actionStatus: str = Field(None,
        description="Indicates the current disposition of the Action."
    )


    agent: Union[str] = Field(None,
        description="The direct performer or driver of the action (animate or inanimate). e.g. John wrote a book."
    )


    endTime: Union[str] = Field(None,
        description="The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the end of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    error: 'Thing' = Field(None,
        description="For failed actions, more information on the cause of the failure."
    )


    instrument: 'Thing' = Field(None,
        description="The object that helped the agent perform the action. e.g. John wrote a book with a pen."
    )


    location: Union[str] = Field(None,
        description="The location of for example where the event is happening, an organization is located, or where an action takes place."
    )


    object: 'Thing' = Field(None,
        description="The object upon which the action is carried out, whose state is kept intact or changed. Also known as the semantic roles patient, affected or undergoer (which change their state) or theme (which doesn't). e.g. John read a book."
    )


    participant: Union[str] = Field(None,
        description="Other co-agents that participated in the action indirectly. e.g. John wrote a book with Steve."
    )


    result: 'Thing' = Field(None,
        description="The result produced in the action. e.g. John wrote a book."
    )


    startTime: Union[str] = Field(None,
        description="The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    target: str = Field(None,
        description="Indicates a target EntryPoint for an Action."
    )


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


    potentialAction: 'Action' = Field(None,
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


class TrackAction(BaseModel):
    """
    TrackAction
    """
    
    deliveryMethod: str = Field(None,
        description="A sub property of instrument. The method of delivery."
    )


    actionStatus: str = Field(None,
        description="Indicates the current disposition of the Action."
    )


    agent: Union[str] = Field(None,
        description="The direct performer or driver of the action (animate or inanimate). e.g. John wrote a book."
    )


    endTime: Union[str] = Field(None,
        description="The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the end of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    error: 'Thing' = Field(None,
        description="For failed actions, more information on the cause of the failure."
    )


    instrument: 'Thing' = Field(None,
        description="The object that helped the agent perform the action. e.g. John wrote a book with a pen."
    )


    location: Union[str] = Field(None,
        description="The location of for example where the event is happening, an organization is located, or where an action takes place."
    )


    object: 'Thing' = Field(None,
        description="The object upon which the action is carried out, whose state is kept intact or changed. Also known as the semantic roles patient, affected or undergoer (which change their state) or theme (which doesn't). e.g. John read a book."
    )


    participant: Union[str] = Field(None,
        description="Other co-agents that participated in the action indirectly. e.g. John wrote a book with Steve."
    )


    result: 'Thing' = Field(None,
        description="The result produced in the action. e.g. John wrote a book."
    )


    startTime: Union[str] = Field(None,
        description="The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    target: str = Field(None,
        description="Indicates a target EntryPoint for an Action."
    )


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


    potentialAction: 'Action' = Field(None,
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


class InteractAction(BaseModel):
    """
    InteractAction
    """
    
    actionStatus: str = Field(None,
        description="Indicates the current disposition of the Action."
    )


    agent: Union[str] = Field(None,
        description="The direct performer or driver of the action (animate or inanimate). e.g. John wrote a book."
    )


    endTime: Union[str] = Field(None,
        description="The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the end of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    error: 'Thing' = Field(None,
        description="For failed actions, more information on the cause of the failure."
    )


    instrument: 'Thing' = Field(None,
        description="The object that helped the agent perform the action. e.g. John wrote a book with a pen."
    )


    location: Union[str] = Field(None,
        description="The location of for example where the event is happening, an organization is located, or where an action takes place."
    )


    object: 'Thing' = Field(None,
        description="The object upon which the action is carried out, whose state is kept intact or changed. Also known as the semantic roles patient, affected or undergoer (which change their state) or theme (which doesn't). e.g. John read a book."
    )


    participant: Union[str] = Field(None,
        description="Other co-agents that participated in the action indirectly. e.g. John wrote a book with Steve."
    )


    result: 'Thing' = Field(None,
        description="The result produced in the action. e.g. John wrote a book."
    )


    startTime: Union[str] = Field(None,
        description="The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    target: str = Field(None,
        description="Indicates a target EntryPoint for an Action."
    )


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


    potentialAction: 'Action' = Field(None,
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


class BefriendAction(BaseModel):
    """
    BefriendAction
    """
    
    actionStatus: str = Field(None,
        description="Indicates the current disposition of the Action."
    )


    agent: Union[str] = Field(None,
        description="The direct performer or driver of the action (animate or inanimate). e.g. John wrote a book."
    )


    endTime: Union[str] = Field(None,
        description="The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the end of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    error: 'Thing' = Field(None,
        description="For failed actions, more information on the cause of the failure."
    )


    instrument: 'Thing' = Field(None,
        description="The object that helped the agent perform the action. e.g. John wrote a book with a pen."
    )


    location: Union[str] = Field(None,
        description="The location of for example where the event is happening, an organization is located, or where an action takes place."
    )


    object: 'Thing' = Field(None,
        description="The object upon which the action is carried out, whose state is kept intact or changed. Also known as the semantic roles patient, affected or undergoer (which change their state) or theme (which doesn't). e.g. John read a book."
    )


    participant: Union[str] = Field(None,
        description="Other co-agents that participated in the action indirectly. e.g. John wrote a book with Steve."
    )


    result: 'Thing' = Field(None,
        description="The result produced in the action. e.g. John wrote a book."
    )


    startTime: Union[str] = Field(None,
        description="The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    target: str = Field(None,
        description="Indicates a target EntryPoint for an Action."
    )


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


    potentialAction: 'Action' = Field(None,
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


class CommunicateAction(BaseModel):
    """
    CommunicateAction
    """
    
    about: 'Thing' = Field(None,
        description="The subject matter of the content. Inverse property: subjectOf."
    )


    inLanguage: Union[str] = Field(None,
        description="The language of the content or performance or used in an action. Please use one of the language codes from the IETF BCP 47 standard. See also availableLanguage. Supersedes language."
    )


    recipient: Union[str] = Field(None,
        description="A sub property of participant. The participant who is at the receiving end of the action."
    )


    actionStatus: str = Field(None,
        description="Indicates the current disposition of the Action."
    )


    agent: Union[str] = Field(None,
        description="The direct performer or driver of the action (animate or inanimate). e.g. John wrote a book."
    )


    endTime: Union[str] = Field(None,
        description="The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the end of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    error: 'Thing' = Field(None,
        description="For failed actions, more information on the cause of the failure."
    )


    instrument: 'Thing' = Field(None,
        description="The object that helped the agent perform the action. e.g. John wrote a book with a pen."
    )


    location: Union[str] = Field(None,
        description="The location of for example where the event is happening, an organization is located, or where an action takes place."
    )


    object: 'Thing' = Field(None,
        description="The object upon which the action is carried out, whose state is kept intact or changed. Also known as the semantic roles patient, affected or undergoer (which change their state) or theme (which doesn't). e.g. John read a book."
    )


    participant: Union[str] = Field(None,
        description="Other co-agents that participated in the action indirectly. e.g. John wrote a book with Steve."
    )


    result: 'Thing' = Field(None,
        description="The result produced in the action. e.g. John wrote a book."
    )


    startTime: Union[str] = Field(None,
        description="The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    target: str = Field(None,
        description="Indicates a target EntryPoint for an Action."
    )


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


    potentialAction: 'Action' = Field(None,
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


class AskAction(BaseModel):
    """
    AskAction
    """
    
    question: str = Field(None,
        description="A sub property of object. A question."
    )


    about: 'Thing' = Field(None,
        description="The subject matter of the content. Inverse property: subjectOf."
    )


    inLanguage: Union[str] = Field(None,
        description="The language of the content or performance or used in an action. Please use one of the language codes from the IETF BCP 47 standard. See also availableLanguage. Supersedes language."
    )


    recipient: Union[str] = Field(None,
        description="A sub property of participant. The participant who is at the receiving end of the action."
    )


    actionStatus: str = Field(None,
        description="Indicates the current disposition of the Action."
    )


    agent: Union[str] = Field(None,
        description="The direct performer or driver of the action (animate or inanimate). e.g. John wrote a book."
    )


    endTime: Union[str] = Field(None,
        description="The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the end of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    error: 'Thing' = Field(None,
        description="For failed actions, more information on the cause of the failure."
    )


    instrument: 'Thing' = Field(None,
        description="The object that helped the agent perform the action. e.g. John wrote a book with a pen."
    )


    location: Union[str] = Field(None,
        description="The location of for example where the event is happening, an organization is located, or where an action takes place."
    )


    object: 'Thing' = Field(None,
        description="The object upon which the action is carried out, whose state is kept intact or changed. Also known as the semantic roles patient, affected or undergoer (which change their state) or theme (which doesn't). e.g. John read a book."
    )


    participant: Union[str] = Field(None,
        description="Other co-agents that participated in the action indirectly. e.g. John wrote a book with Steve."
    )


    result: 'Thing' = Field(None,
        description="The result produced in the action. e.g. John wrote a book."
    )


    startTime: Union[str] = Field(None,
        description="The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    target: str = Field(None,
        description="Indicates a target EntryPoint for an Action."
    )


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


    potentialAction: 'Action' = Field(None,
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


class CheckInAction(BaseModel):
    """
    CheckInAction
    """
    
    about: 'Thing' = Field(None,
        description="The subject matter of the content. Inverse property: subjectOf."
    )


    inLanguage: Union[str] = Field(None,
        description="The language of the content or performance or used in an action. Please use one of the language codes from the IETF BCP 47 standard. See also availableLanguage. Supersedes language."
    )


    recipient: Union[str] = Field(None,
        description="A sub property of participant. The participant who is at the receiving end of the action."
    )


    actionStatus: str = Field(None,
        description="Indicates the current disposition of the Action."
    )


    agent: Union[str] = Field(None,
        description="The direct performer or driver of the action (animate or inanimate). e.g. John wrote a book."
    )


    endTime: Union[str] = Field(None,
        description="The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the end of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    error: 'Thing' = Field(None,
        description="For failed actions, more information on the cause of the failure."
    )


    instrument: 'Thing' = Field(None,
        description="The object that helped the agent perform the action. e.g. John wrote a book with a pen."
    )


    location: Union[str] = Field(None,
        description="The location of for example where the event is happening, an organization is located, or where an action takes place."
    )


    object: 'Thing' = Field(None,
        description="The object upon which the action is carried out, whose state is kept intact or changed. Also known as the semantic roles patient, affected or undergoer (which change their state) or theme (which doesn't). e.g. John read a book."
    )


    participant: Union[str] = Field(None,
        description="Other co-agents that participated in the action indirectly. e.g. John wrote a book with Steve."
    )


    result: 'Thing' = Field(None,
        description="The result produced in the action. e.g. John wrote a book."
    )


    startTime: Union[str] = Field(None,
        description="The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    target: str = Field(None,
        description="Indicates a target EntryPoint for an Action."
    )


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


    potentialAction: 'Action' = Field(None,
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


class CheckOutAction(BaseModel):
    """
    CheckOutAction
    """
    
    about: 'Thing' = Field(None,
        description="The subject matter of the content. Inverse property: subjectOf."
    )


    inLanguage: Union[str] = Field(None,
        description="The language of the content or performance or used in an action. Please use one of the language codes from the IETF BCP 47 standard. See also availableLanguage. Supersedes language."
    )


    recipient: Union[str] = Field(None,
        description="A sub property of participant. The participant who is at the receiving end of the action."
    )


    actionStatus: str = Field(None,
        description="Indicates the current disposition of the Action."
    )


    agent: Union[str] = Field(None,
        description="The direct performer or driver of the action (animate or inanimate). e.g. John wrote a book."
    )


    endTime: Union[str] = Field(None,
        description="The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the end of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    error: 'Thing' = Field(None,
        description="For failed actions, more information on the cause of the failure."
    )


    instrument: 'Thing' = Field(None,
        description="The object that helped the agent perform the action. e.g. John wrote a book with a pen."
    )


    location: Union[str] = Field(None,
        description="The location of for example where the event is happening, an organization is located, or where an action takes place."
    )


    object: 'Thing' = Field(None,
        description="The object upon which the action is carried out, whose state is kept intact or changed. Also known as the semantic roles patient, affected or undergoer (which change their state) or theme (which doesn't). e.g. John read a book."
    )


    participant: Union[str] = Field(None,
        description="Other co-agents that participated in the action indirectly. e.g. John wrote a book with Steve."
    )


    result: 'Thing' = Field(None,
        description="The result produced in the action. e.g. John wrote a book."
    )


    startTime: Union[str] = Field(None,
        description="The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    target: str = Field(None,
        description="Indicates a target EntryPoint for an Action."
    )


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


    potentialAction: 'Action' = Field(None,
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


class CommentAction(BaseModel):
    """
    CommentAction
    """
    
    resultComment: str = Field(None,
        description="A sub property of result. The Comment created or sent as a result of this action."
    )


    about: 'Thing' = Field(None,
        description="The subject matter of the content. Inverse property: subjectOf."
    )


    inLanguage: Union[str] = Field(None,
        description="The language of the content or performance or used in an action. Please use one of the language codes from the IETF BCP 47 standard. See also availableLanguage. Supersedes language."
    )


    recipient: Union[str] = Field(None,
        description="A sub property of participant. The participant who is at the receiving end of the action."
    )


    actionStatus: str = Field(None,
        description="Indicates the current disposition of the Action."
    )


    agent: Union[str] = Field(None,
        description="The direct performer or driver of the action (animate or inanimate). e.g. John wrote a book."
    )


    endTime: Union[str] = Field(None,
        description="The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the end of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    error: 'Thing' = Field(None,
        description="For failed actions, more information on the cause of the failure."
    )


    instrument: 'Thing' = Field(None,
        description="The object that helped the agent perform the action. e.g. John wrote a book with a pen."
    )


    location: Union[str] = Field(None,
        description="The location of for example where the event is happening, an organization is located, or where an action takes place."
    )


    object: 'Thing' = Field(None,
        description="The object upon which the action is carried out, whose state is kept intact or changed. Also known as the semantic roles patient, affected or undergoer (which change their state) or theme (which doesn't). e.g. John read a book."
    )


    participant: Union[str] = Field(None,
        description="Other co-agents that participated in the action indirectly. e.g. John wrote a book with Steve."
    )


    result: 'Thing' = Field(None,
        description="The result produced in the action. e.g. John wrote a book."
    )


    startTime: Union[str] = Field(None,
        description="The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    target: str = Field(None,
        description="Indicates a target EntryPoint for an Action."
    )


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


    potentialAction: 'Action' = Field(None,
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


class InformAction(BaseModel):
    """
    InformAction
    """
    
    event: str = Field(None,
        description="Upcoming or past event associated with this place, organization, or action. Supersedes events."
    )


    about: 'Thing' = Field(None,
        description="The subject matter of the content. Inverse property: subjectOf."
    )


    inLanguage: Union[str] = Field(None,
        description="The language of the content or performance or used in an action. Please use one of the language codes from the IETF BCP 47 standard. See also availableLanguage. Supersedes language."
    )


    recipient: Union[str] = Field(None,
        description="A sub property of participant. The participant who is at the receiving end of the action."
    )


    actionStatus: str = Field(None,
        description="Indicates the current disposition of the Action."
    )


    agent: Union[str] = Field(None,
        description="The direct performer or driver of the action (animate or inanimate). e.g. John wrote a book."
    )


    endTime: Union[str] = Field(None,
        description="The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the end of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    error: 'Thing' = Field(None,
        description="For failed actions, more information on the cause of the failure."
    )


    instrument: 'Thing' = Field(None,
        description="The object that helped the agent perform the action. e.g. John wrote a book with a pen."
    )


    location: Union[str] = Field(None,
        description="The location of for example where the event is happening, an organization is located, or where an action takes place."
    )


    object: 'Thing' = Field(None,
        description="The object upon which the action is carried out, whose state is kept intact or changed. Also known as the semantic roles patient, affected or undergoer (which change their state) or theme (which doesn't). e.g. John read a book."
    )


    participant: Union[str] = Field(None,
        description="Other co-agents that participated in the action indirectly. e.g. John wrote a book with Steve."
    )


    result: 'Thing' = Field(None,
        description="The result produced in the action. e.g. John wrote a book."
    )


    startTime: Union[str] = Field(None,
        description="The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    target: str = Field(None,
        description="Indicates a target EntryPoint for an Action."
    )


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


    potentialAction: 'Action' = Field(None,
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


class ConfirmAction(BaseModel):
    """
    ConfirmAction
    """
    
    event: str = Field(None,
        description="Upcoming or past event associated with this place, organization, or action. Supersedes events."
    )


    about: 'Thing' = Field(None,
        description="The subject matter of the content. Inverse property: subjectOf."
    )


    inLanguage: Union[str] = Field(None,
        description="The language of the content or performance or used in an action. Please use one of the language codes from the IETF BCP 47 standard. See also availableLanguage. Supersedes language."
    )


    recipient: Union[str] = Field(None,
        description="A sub property of participant. The participant who is at the receiving end of the action."
    )


    actionStatus: str = Field(None,
        description="Indicates the current disposition of the Action."
    )


    agent: Union[str] = Field(None,
        description="The direct performer or driver of the action (animate or inanimate). e.g. John wrote a book."
    )


    endTime: Union[str] = Field(None,
        description="The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the end of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    error: 'Thing' = Field(None,
        description="For failed actions, more information on the cause of the failure."
    )


    instrument: 'Thing' = Field(None,
        description="The object that helped the agent perform the action. e.g. John wrote a book with a pen."
    )


    location: Union[str] = Field(None,
        description="The location of for example where the event is happening, an organization is located, or where an action takes place."
    )


    object: 'Thing' = Field(None,
        description="The object upon which the action is carried out, whose state is kept intact or changed. Also known as the semantic roles patient, affected or undergoer (which change their state) or theme (which doesn't). e.g. John read a book."
    )


    participant: Union[str] = Field(None,
        description="Other co-agents that participated in the action indirectly. e.g. John wrote a book with Steve."
    )


    result: 'Thing' = Field(None,
        description="The result produced in the action. e.g. John wrote a book."
    )


    startTime: Union[str] = Field(None,
        description="The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    target: str = Field(None,
        description="Indicates a target EntryPoint for an Action."
    )


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


    potentialAction: 'Action' = Field(None,
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


class RsvpAction(BaseModel):
    """
    RsvpAction
    """
    
    additionalNumberOfGuests: str = Field(None,
        description="If responding yes, the number of guests who will attend in addition to the invitee."
    )


    comment: str = Field(None,
        description="Comments, typically from users."
    )


    rsvpResponse: str = Field(None,
        description="The response (yes, no, maybe) to the RSVP."
    )


    event: str = Field(None,
        description="Upcoming or past event associated with this place, organization, or action. Supersedes events."
    )


    about: 'Thing' = Field(None,
        description="The subject matter of the content. Inverse property: subjectOf."
    )


    inLanguage: Union[str] = Field(None,
        description="The language of the content or performance or used in an action. Please use one of the language codes from the IETF BCP 47 standard. See also availableLanguage. Supersedes language."
    )


    recipient: Union[str] = Field(None,
        description="A sub property of participant. The participant who is at the receiving end of the action."
    )


    actionStatus: str = Field(None,
        description="Indicates the current disposition of the Action."
    )


    agent: Union[str] = Field(None,
        description="The direct performer or driver of the action (animate or inanimate). e.g. John wrote a book."
    )


    endTime: Union[str] = Field(None,
        description="The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the end of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    error: 'Thing' = Field(None,
        description="For failed actions, more information on the cause of the failure."
    )


    instrument: 'Thing' = Field(None,
        description="The object that helped the agent perform the action. e.g. John wrote a book with a pen."
    )


    location: Union[str] = Field(None,
        description="The location of for example where the event is happening, an organization is located, or where an action takes place."
    )


    object: 'Thing' = Field(None,
        description="The object upon which the action is carried out, whose state is kept intact or changed. Also known as the semantic roles patient, affected or undergoer (which change their state) or theme (which doesn't). e.g. John read a book."
    )


    participant: Union[str] = Field(None,
        description="Other co-agents that participated in the action indirectly. e.g. John wrote a book with Steve."
    )


    result: 'Thing' = Field(None,
        description="The result produced in the action. e.g. John wrote a book."
    )


    startTime: Union[str] = Field(None,
        description="The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    target: str = Field(None,
        description="Indicates a target EntryPoint for an Action."
    )


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


    potentialAction: 'Action' = Field(None,
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


class InviteAction(BaseModel):
    """
    InviteAction
    """
    
    event: str = Field(None,
        description="Upcoming or past event associated with this place, organization, or action. Supersedes events."
    )


    about: 'Thing' = Field(None,
        description="The subject matter of the content. Inverse property: subjectOf."
    )


    inLanguage: Union[str] = Field(None,
        description="The language of the content or performance or used in an action. Please use one of the language codes from the IETF BCP 47 standard. See also availableLanguage. Supersedes language."
    )


    recipient: Union[str] = Field(None,
        description="A sub property of participant. The participant who is at the receiving end of the action."
    )


    actionStatus: str = Field(None,
        description="Indicates the current disposition of the Action."
    )


    agent: Union[str] = Field(None,
        description="The direct performer or driver of the action (animate or inanimate). e.g. John wrote a book."
    )


    endTime: Union[str] = Field(None,
        description="The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the end of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    error: 'Thing' = Field(None,
        description="For failed actions, more information on the cause of the failure."
    )


    instrument: 'Thing' = Field(None,
        description="The object that helped the agent perform the action. e.g. John wrote a book with a pen."
    )


    location: Union[str] = Field(None,
        description="The location of for example where the event is happening, an organization is located, or where an action takes place."
    )


    object: 'Thing' = Field(None,
        description="The object upon which the action is carried out, whose state is kept intact or changed. Also known as the semantic roles patient, affected or undergoer (which change their state) or theme (which doesn't). e.g. John read a book."
    )


    participant: Union[str] = Field(None,
        description="Other co-agents that participated in the action indirectly. e.g. John wrote a book with Steve."
    )


    result: 'Thing' = Field(None,
        description="The result produced in the action. e.g. John wrote a book."
    )


    startTime: Union[str] = Field(None,
        description="The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    target: str = Field(None,
        description="Indicates a target EntryPoint for an Action."
    )


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


    potentialAction: 'Action' = Field(None,
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


class ReplyAction(BaseModel):
    """
    ReplyAction
    """
    
    resultComment: str = Field(None,
        description="A sub property of result. The Comment created or sent as a result of this action."
    )


    about: 'Thing' = Field(None,
        description="The subject matter of the content. Inverse property: subjectOf."
    )


    inLanguage: Union[str] = Field(None,
        description="The language of the content or performance or used in an action. Please use one of the language codes from the IETF BCP 47 standard. See also availableLanguage. Supersedes language."
    )


    recipient: Union[str] = Field(None,
        description="A sub property of participant. The participant who is at the receiving end of the action."
    )


    actionStatus: str = Field(None,
        description="Indicates the current disposition of the Action."
    )


    agent: Union[str] = Field(None,
        description="The direct performer or driver of the action (animate or inanimate). e.g. John wrote a book."
    )


    endTime: Union[str] = Field(None,
        description="The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the end of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    error: 'Thing' = Field(None,
        description="For failed actions, more information on the cause of the failure."
    )


    instrument: 'Thing' = Field(None,
        description="The object that helped the agent perform the action. e.g. John wrote a book with a pen."
    )


    location: Union[str] = Field(None,
        description="The location of for example where the event is happening, an organization is located, or where an action takes place."
    )


    object: 'Thing' = Field(None,
        description="The object upon which the action is carried out, whose state is kept intact or changed. Also known as the semantic roles patient, affected or undergoer (which change their state) or theme (which doesn't). e.g. John read a book."
    )


    participant: Union[str] = Field(None,
        description="Other co-agents that participated in the action indirectly. e.g. John wrote a book with Steve."
    )


    result: 'Thing' = Field(None,
        description="The result produced in the action. e.g. John wrote a book."
    )


    startTime: Union[str] = Field(None,
        description="The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    target: str = Field(None,
        description="Indicates a target EntryPoint for an Action."
    )


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


    potentialAction: 'Action' = Field(None,
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


class ShareAction(BaseModel):
    """
    ShareAction
    """
    
    about: 'Thing' = Field(None,
        description="The subject matter of the content. Inverse property: subjectOf."
    )


    inLanguage: Union[str] = Field(None,
        description="The language of the content or performance or used in an action. Please use one of the language codes from the IETF BCP 47 standard. See also availableLanguage. Supersedes language."
    )


    recipient: Union[str] = Field(None,
        description="A sub property of participant. The participant who is at the receiving end of the action."
    )


    actionStatus: str = Field(None,
        description="Indicates the current disposition of the Action."
    )


    agent: Union[str] = Field(None,
        description="The direct performer or driver of the action (animate or inanimate). e.g. John wrote a book."
    )


    endTime: Union[str] = Field(None,
        description="The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the end of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    error: 'Thing' = Field(None,
        description="For failed actions, more information on the cause of the failure."
    )


    instrument: 'Thing' = Field(None,
        description="The object that helped the agent perform the action. e.g. John wrote a book with a pen."
    )


    location: Union[str] = Field(None,
        description="The location of for example where the event is happening, an organization is located, or where an action takes place."
    )


    object: 'Thing' = Field(None,
        description="The object upon which the action is carried out, whose state is kept intact or changed. Also known as the semantic roles patient, affected or undergoer (which change their state) or theme (which doesn't). e.g. John read a book."
    )


    participant: Union[str] = Field(None,
        description="Other co-agents that participated in the action indirectly. e.g. John wrote a book with Steve."
    )


    result: 'Thing' = Field(None,
        description="The result produced in the action. e.g. John wrote a book."
    )


    startTime: Union[str] = Field(None,
        description="The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    target: str = Field(None,
        description="Indicates a target EntryPoint for an Action."
    )


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


    potentialAction: 'Action' = Field(None,
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


class FollowAction(BaseModel):
    """
    FollowAction
    """
    
    followee: Union[str] = Field(None,
        description="A sub property of object. The person or organization being followed."
    )


    actionStatus: str = Field(None,
        description="Indicates the current disposition of the Action."
    )


    agent: Union[str] = Field(None,
        description="The direct performer or driver of the action (animate or inanimate). e.g. John wrote a book."
    )


    endTime: Union[str] = Field(None,
        description="The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the end of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    error: 'Thing' = Field(None,
        description="For failed actions, more information on the cause of the failure."
    )


    instrument: 'Thing' = Field(None,
        description="The object that helped the agent perform the action. e.g. John wrote a book with a pen."
    )


    location: Union[str] = Field(None,
        description="The location of for example where the event is happening, an organization is located, or where an action takes place."
    )


    object: 'Thing' = Field(None,
        description="The object upon which the action is carried out, whose state is kept intact or changed. Also known as the semantic roles patient, affected or undergoer (which change their state) or theme (which doesn't). e.g. John read a book."
    )


    participant: Union[str] = Field(None,
        description="Other co-agents that participated in the action indirectly. e.g. John wrote a book with Steve."
    )


    result: 'Thing' = Field(None,
        description="The result produced in the action. e.g. John wrote a book."
    )


    startTime: Union[str] = Field(None,
        description="The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    target: str = Field(None,
        description="Indicates a target EntryPoint for an Action."
    )


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


    potentialAction: 'Action' = Field(None,
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


class JoinAction(BaseModel):
    """
    JoinAction
    """
    
    event: str = Field(None,
        description="Upcoming or past event associated with this place, organization, or action. Supersedes events."
    )


    actionStatus: str = Field(None,
        description="Indicates the current disposition of the Action."
    )


    agent: Union[str] = Field(None,
        description="The direct performer or driver of the action (animate or inanimate). e.g. John wrote a book."
    )


    endTime: Union[str] = Field(None,
        description="The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the end of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    error: 'Thing' = Field(None,
        description="For failed actions, more information on the cause of the failure."
    )


    instrument: 'Thing' = Field(None,
        description="The object that helped the agent perform the action. e.g. John wrote a book with a pen."
    )


    location: Union[str] = Field(None,
        description="The location of for example where the event is happening, an organization is located, or where an action takes place."
    )


    object: 'Thing' = Field(None,
        description="The object upon which the action is carried out, whose state is kept intact or changed. Also known as the semantic roles patient, affected or undergoer (which change their state) or theme (which doesn't). e.g. John read a book."
    )


    participant: Union[str] = Field(None,
        description="Other co-agents that participated in the action indirectly. e.g. John wrote a book with Steve."
    )


    result: 'Thing' = Field(None,
        description="The result produced in the action. e.g. John wrote a book."
    )


    startTime: Union[str] = Field(None,
        description="The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    target: str = Field(None,
        description="Indicates a target EntryPoint for an Action."
    )


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


    potentialAction: 'Action' = Field(None,
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


class LeaveAction(BaseModel):
    """
    LeaveAction
    """
    
    event: str = Field(None,
        description="Upcoming or past event associated with this place, organization, or action. Supersedes events."
    )


    actionStatus: str = Field(None,
        description="Indicates the current disposition of the Action."
    )


    agent: Union[str] = Field(None,
        description="The direct performer or driver of the action (animate or inanimate). e.g. John wrote a book."
    )


    endTime: Union[str] = Field(None,
        description="The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the end of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    error: 'Thing' = Field(None,
        description="For failed actions, more information on the cause of the failure."
    )


    instrument: 'Thing' = Field(None,
        description="The object that helped the agent perform the action. e.g. John wrote a book with a pen."
    )


    location: Union[str] = Field(None,
        description="The location of for example where the event is happening, an organization is located, or where an action takes place."
    )


    object: 'Thing' = Field(None,
        description="The object upon which the action is carried out, whose state is kept intact or changed. Also known as the semantic roles patient, affected or undergoer (which change their state) or theme (which doesn't). e.g. John read a book."
    )


    participant: Union[str] = Field(None,
        description="Other co-agents that participated in the action indirectly. e.g. John wrote a book with Steve."
    )


    result: 'Thing' = Field(None,
        description="The result produced in the action. e.g. John wrote a book."
    )


    startTime: Union[str] = Field(None,
        description="The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    target: str = Field(None,
        description="Indicates a target EntryPoint for an Action."
    )


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


    potentialAction: 'Action' = Field(None,
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


class MarryAction(BaseModel):
    """
    MarryAction
    """
    
    actionStatus: str = Field(None,
        description="Indicates the current disposition of the Action."
    )


    agent: Union[str] = Field(None,
        description="The direct performer or driver of the action (animate or inanimate). e.g. John wrote a book."
    )


    endTime: Union[str] = Field(None,
        description="The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the end of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    error: 'Thing' = Field(None,
        description="For failed actions, more information on the cause of the failure."
    )


    instrument: 'Thing' = Field(None,
        description="The object that helped the agent perform the action. e.g. John wrote a book with a pen."
    )


    location: Union[str] = Field(None,
        description="The location of for example where the event is happening, an organization is located, or where an action takes place."
    )


    object: 'Thing' = Field(None,
        description="The object upon which the action is carried out, whose state is kept intact or changed. Also known as the semantic roles patient, affected or undergoer (which change their state) or theme (which doesn't). e.g. John read a book."
    )


    participant: Union[str] = Field(None,
        description="Other co-agents that participated in the action indirectly. e.g. John wrote a book with Steve."
    )


    result: 'Thing' = Field(None,
        description="The result produced in the action. e.g. John wrote a book."
    )


    startTime: Union[str] = Field(None,
        description="The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    target: str = Field(None,
        description="Indicates a target EntryPoint for an Action."
    )


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


    potentialAction: 'Action' = Field(None,
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


class RegisterAction(BaseModel):
    """
    RegisterAction
    """
    
    actionStatus: str = Field(None,
        description="Indicates the current disposition of the Action."
    )


    agent: Union[str] = Field(None,
        description="The direct performer or driver of the action (animate or inanimate). e.g. John wrote a book."
    )


    endTime: Union[str] = Field(None,
        description="The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the end of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    error: 'Thing' = Field(None,
        description="For failed actions, more information on the cause of the failure."
    )


    instrument: 'Thing' = Field(None,
        description="The object that helped the agent perform the action. e.g. John wrote a book with a pen."
    )


    location: Union[str] = Field(None,
        description="The location of for example where the event is happening, an organization is located, or where an action takes place."
    )


    object: 'Thing' = Field(None,
        description="The object upon which the action is carried out, whose state is kept intact or changed. Also known as the semantic roles patient, affected or undergoer (which change their state) or theme (which doesn't). e.g. John read a book."
    )


    participant: Union[str] = Field(None,
        description="Other co-agents that participated in the action indirectly. e.g. John wrote a book with Steve."
    )


    result: 'Thing' = Field(None,
        description="The result produced in the action. e.g. John wrote a book."
    )


    startTime: Union[str] = Field(None,
        description="The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    target: str = Field(None,
        description="Indicates a target EntryPoint for an Action."
    )


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


    potentialAction: 'Action' = Field(None,
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


class SubscribeAction(BaseModel):
    """
    SubscribeAction
    """
    
    actionStatus: str = Field(None,
        description="Indicates the current disposition of the Action."
    )


    agent: Union[str] = Field(None,
        description="The direct performer or driver of the action (animate or inanimate). e.g. John wrote a book."
    )


    endTime: Union[str] = Field(None,
        description="The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the end of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    error: 'Thing' = Field(None,
        description="For failed actions, more information on the cause of the failure."
    )


    instrument: 'Thing' = Field(None,
        description="The object that helped the agent perform the action. e.g. John wrote a book with a pen."
    )


    location: Union[str] = Field(None,
        description="The location of for example where the event is happening, an organization is located, or where an action takes place."
    )


    object: 'Thing' = Field(None,
        description="The object upon which the action is carried out, whose state is kept intact or changed. Also known as the semantic roles patient, affected or undergoer (which change their state) or theme (which doesn't). e.g. John read a book."
    )


    participant: Union[str] = Field(None,
        description="Other co-agents that participated in the action indirectly. e.g. John wrote a book with Steve."
    )


    result: 'Thing' = Field(None,
        description="The result produced in the action. e.g. John wrote a book."
    )


    startTime: Union[str] = Field(None,
        description="The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    target: str = Field(None,
        description="Indicates a target EntryPoint for an Action."
    )


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


    potentialAction: 'Action' = Field(None,
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


class UnRegisterAction(BaseModel):
    """
    UnRegisterAction
    """
    
    actionStatus: str = Field(None,
        description="Indicates the current disposition of the Action."
    )


    agent: Union[str] = Field(None,
        description="The direct performer or driver of the action (animate or inanimate). e.g. John wrote a book."
    )


    endTime: Union[str] = Field(None,
        description="The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the end of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    error: 'Thing' = Field(None,
        description="For failed actions, more information on the cause of the failure."
    )


    instrument: 'Thing' = Field(None,
        description="The object that helped the agent perform the action. e.g. John wrote a book with a pen."
    )


    location: Union[str] = Field(None,
        description="The location of for example where the event is happening, an organization is located, or where an action takes place."
    )


    object: 'Thing' = Field(None,
        description="The object upon which the action is carried out, whose state is kept intact or changed. Also known as the semantic roles patient, affected or undergoer (which change their state) or theme (which doesn't). e.g. John read a book."
    )


    participant: Union[str] = Field(None,
        description="Other co-agents that participated in the action indirectly. e.g. John wrote a book with Steve."
    )


    result: 'Thing' = Field(None,
        description="The result produced in the action. e.g. John wrote a book."
    )


    startTime: Union[str] = Field(None,
        description="The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    target: str = Field(None,
        description="Indicates a target EntryPoint for an Action."
    )


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


    potentialAction: 'Action' = Field(None,
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


class MoveAction(BaseModel):
    """
    MoveAction
    """
    
    fromLocation: str = Field(None,
        description="A sub property of location. The original location of the object or the agent before the action."
    )


    toLocation: str = Field(None,
        description="A sub property of location. The final location of the object or the agent after the action."
    )


    actionStatus: str = Field(None,
        description="Indicates the current disposition of the Action."
    )


    agent: Union[str] = Field(None,
        description="The direct performer or driver of the action (animate or inanimate). e.g. John wrote a book."
    )


    endTime: Union[str] = Field(None,
        description="The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the end of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    error: 'Thing' = Field(None,
        description="For failed actions, more information on the cause of the failure."
    )


    instrument: 'Thing' = Field(None,
        description="The object that helped the agent perform the action. e.g. John wrote a book with a pen."
    )


    location: Union[str] = Field(None,
        description="The location of for example where the event is happening, an organization is located, or where an action takes place."
    )


    object: 'Thing' = Field(None,
        description="The object upon which the action is carried out, whose state is kept intact or changed. Also known as the semantic roles patient, affected or undergoer (which change their state) or theme (which doesn't). e.g. John read a book."
    )


    participant: Union[str] = Field(None,
        description="Other co-agents that participated in the action indirectly. e.g. John wrote a book with Steve."
    )


    result: 'Thing' = Field(None,
        description="The result produced in the action. e.g. John wrote a book."
    )


    startTime: Union[str] = Field(None,
        description="The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    target: str = Field(None,
        description="Indicates a target EntryPoint for an Action."
    )


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


    potentialAction: 'Action' = Field(None,
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


class ArriveAction(BaseModel):
    """
    ArriveAction
    """
    
    fromLocation: str = Field(None,
        description="A sub property of location. The original location of the object or the agent before the action."
    )


    toLocation: str = Field(None,
        description="A sub property of location. The final location of the object or the agent after the action."
    )


    actionStatus: str = Field(None,
        description="Indicates the current disposition of the Action."
    )


    agent: Union[str] = Field(None,
        description="The direct performer or driver of the action (animate or inanimate). e.g. John wrote a book."
    )


    endTime: Union[str] = Field(None,
        description="The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the end of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    error: 'Thing' = Field(None,
        description="For failed actions, more information on the cause of the failure."
    )


    instrument: 'Thing' = Field(None,
        description="The object that helped the agent perform the action. e.g. John wrote a book with a pen."
    )


    location: Union[str] = Field(None,
        description="The location of for example where the event is happening, an organization is located, or where an action takes place."
    )


    object: 'Thing' = Field(None,
        description="The object upon which the action is carried out, whose state is kept intact or changed. Also known as the semantic roles patient, affected or undergoer (which change their state) or theme (which doesn't). e.g. John read a book."
    )


    participant: Union[str] = Field(None,
        description="Other co-agents that participated in the action indirectly. e.g. John wrote a book with Steve."
    )


    result: 'Thing' = Field(None,
        description="The result produced in the action. e.g. John wrote a book."
    )


    startTime: Union[str] = Field(None,
        description="The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    target: str = Field(None,
        description="Indicates a target EntryPoint for an Action."
    )


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


    potentialAction: 'Action' = Field(None,
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


class DepartAction(BaseModel):
    """
    DepartAction
    """
    
    fromLocation: str = Field(None,
        description="A sub property of location. The original location of the object or the agent before the action."
    )


    toLocation: str = Field(None,
        description="A sub property of location. The final location of the object or the agent after the action."
    )


    actionStatus: str = Field(None,
        description="Indicates the current disposition of the Action."
    )


    agent: Union[str] = Field(None,
        description="The direct performer or driver of the action (animate or inanimate). e.g. John wrote a book."
    )


    endTime: Union[str] = Field(None,
        description="The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the end of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    error: 'Thing' = Field(None,
        description="For failed actions, more information on the cause of the failure."
    )


    instrument: 'Thing' = Field(None,
        description="The object that helped the agent perform the action. e.g. John wrote a book with a pen."
    )


    location: Union[str] = Field(None,
        description="The location of for example where the event is happening, an organization is located, or where an action takes place."
    )


    object: 'Thing' = Field(None,
        description="The object upon which the action is carried out, whose state is kept intact or changed. Also known as the semantic roles patient, affected or undergoer (which change their state) or theme (which doesn't). e.g. John read a book."
    )


    participant: Union[str] = Field(None,
        description="Other co-agents that participated in the action indirectly. e.g. John wrote a book with Steve."
    )


    result: 'Thing' = Field(None,
        description="The result produced in the action. e.g. John wrote a book."
    )


    startTime: Union[str] = Field(None,
        description="The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    target: str = Field(None,
        description="Indicates a target EntryPoint for an Action."
    )


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


    potentialAction: 'Action' = Field(None,
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


class TravelAction(BaseModel):
    """
    TravelAction
    """
    
    distance: str = Field(None,
        description="The distance travelled, e.g. exercising or travelling."
    )


    fromLocation: str = Field(None,
        description="A sub property of location. The original location of the object or the agent before the action."
    )


    toLocation: str = Field(None,
        description="A sub property of location. The final location of the object or the agent after the action."
    )


    actionStatus: str = Field(None,
        description="Indicates the current disposition of the Action."
    )


    agent: Union[str] = Field(None,
        description="The direct performer or driver of the action (animate or inanimate). e.g. John wrote a book."
    )


    endTime: Union[str] = Field(None,
        description="The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the end of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    error: 'Thing' = Field(None,
        description="For failed actions, more information on the cause of the failure."
    )


    instrument: 'Thing' = Field(None,
        description="The object that helped the agent perform the action. e.g. John wrote a book with a pen."
    )


    location: Union[str] = Field(None,
        description="The location of for example where the event is happening, an organization is located, or where an action takes place."
    )


    object: 'Thing' = Field(None,
        description="The object upon which the action is carried out, whose state is kept intact or changed. Also known as the semantic roles patient, affected or undergoer (which change their state) or theme (which doesn't). e.g. John read a book."
    )


    participant: Union[str] = Field(None,
        description="Other co-agents that participated in the action indirectly. e.g. John wrote a book with Steve."
    )


    result: 'Thing' = Field(None,
        description="The result produced in the action. e.g. John wrote a book."
    )


    startTime: Union[str] = Field(None,
        description="The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    target: str = Field(None,
        description="Indicates a target EntryPoint for an Action."
    )


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


    potentialAction: 'Action' = Field(None,
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


class OrganizeAction(BaseModel):
    """
    OrganizeAction
    """
    
    actionStatus: str = Field(None,
        description="Indicates the current disposition of the Action."
    )


    agent: Union[str] = Field(None,
        description="The direct performer or driver of the action (animate or inanimate). e.g. John wrote a book."
    )


    endTime: Union[str] = Field(None,
        description="The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the end of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    error: 'Thing' = Field(None,
        description="For failed actions, more information on the cause of the failure."
    )


    instrument: 'Thing' = Field(None,
        description="The object that helped the agent perform the action. e.g. John wrote a book with a pen."
    )


    location: Union[str] = Field(None,
        description="The location of for example where the event is happening, an organization is located, or where an action takes place."
    )


    object: 'Thing' = Field(None,
        description="The object upon which the action is carried out, whose state is kept intact or changed. Also known as the semantic roles patient, affected or undergoer (which change their state) or theme (which doesn't). e.g. John read a book."
    )


    participant: Union[str] = Field(None,
        description="Other co-agents that participated in the action indirectly. e.g. John wrote a book with Steve."
    )


    result: 'Thing' = Field(None,
        description="The result produced in the action. e.g. John wrote a book."
    )


    startTime: Union[str] = Field(None,
        description="The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    target: str = Field(None,
        description="Indicates a target EntryPoint for an Action."
    )


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


    potentialAction: 'Action' = Field(None,
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


class AllocateAction(BaseModel):
    """
    AllocateAction
    """
    
    actionStatus: str = Field(None,
        description="Indicates the current disposition of the Action."
    )


    agent: Union[str] = Field(None,
        description="The direct performer or driver of the action (animate or inanimate). e.g. John wrote a book."
    )


    endTime: Union[str] = Field(None,
        description="The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the end of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    error: 'Thing' = Field(None,
        description="For failed actions, more information on the cause of the failure."
    )


    instrument: 'Thing' = Field(None,
        description="The object that helped the agent perform the action. e.g. John wrote a book with a pen."
    )


    location: Union[str] = Field(None,
        description="The location of for example where the event is happening, an organization is located, or where an action takes place."
    )


    object: 'Thing' = Field(None,
        description="The object upon which the action is carried out, whose state is kept intact or changed. Also known as the semantic roles patient, affected or undergoer (which change their state) or theme (which doesn't). e.g. John read a book."
    )


    participant: Union[str] = Field(None,
        description="Other co-agents that participated in the action indirectly. e.g. John wrote a book with Steve."
    )


    result: 'Thing' = Field(None,
        description="The result produced in the action. e.g. John wrote a book."
    )


    startTime: Union[str] = Field(None,
        description="The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    target: str = Field(None,
        description="Indicates a target EntryPoint for an Action."
    )


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


    potentialAction: 'Action' = Field(None,
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


class AcceptAction(BaseModel):
    """
    AcceptAction
    """
    
    actionStatus: str = Field(None,
        description="Indicates the current disposition of the Action."
    )


    agent: Union[str] = Field(None,
        description="The direct performer or driver of the action (animate or inanimate). e.g. John wrote a book."
    )


    endTime: Union[str] = Field(None,
        description="The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the end of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    error: 'Thing' = Field(None,
        description="For failed actions, more information on the cause of the failure."
    )


    instrument: 'Thing' = Field(None,
        description="The object that helped the agent perform the action. e.g. John wrote a book with a pen."
    )


    location: Union[str] = Field(None,
        description="The location of for example where the event is happening, an organization is located, or where an action takes place."
    )


    object: 'Thing' = Field(None,
        description="The object upon which the action is carried out, whose state is kept intact or changed. Also known as the semantic roles patient, affected or undergoer (which change their state) or theme (which doesn't). e.g. John read a book."
    )


    participant: Union[str] = Field(None,
        description="Other co-agents that participated in the action indirectly. e.g. John wrote a book with Steve."
    )


    result: 'Thing' = Field(None,
        description="The result produced in the action. e.g. John wrote a book."
    )


    startTime: Union[str] = Field(None,
        description="The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    target: str = Field(None,
        description="Indicates a target EntryPoint for an Action."
    )


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


    potentialAction: 'Action' = Field(None,
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


class AssignAction(BaseModel):
    """
    AssignAction
    """
    
    actionStatus: str = Field(None,
        description="Indicates the current disposition of the Action."
    )


    agent: Union[str] = Field(None,
        description="The direct performer or driver of the action (animate or inanimate). e.g. John wrote a book."
    )


    endTime: Union[str] = Field(None,
        description="The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the end of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    error: 'Thing' = Field(None,
        description="For failed actions, more information on the cause of the failure."
    )


    instrument: 'Thing' = Field(None,
        description="The object that helped the agent perform the action. e.g. John wrote a book with a pen."
    )


    location: Union[str] = Field(None,
        description="The location of for example where the event is happening, an organization is located, or where an action takes place."
    )


    object: 'Thing' = Field(None,
        description="The object upon which the action is carried out, whose state is kept intact or changed. Also known as the semantic roles patient, affected or undergoer (which change their state) or theme (which doesn't). e.g. John read a book."
    )


    participant: Union[str] = Field(None,
        description="Other co-agents that participated in the action indirectly. e.g. John wrote a book with Steve."
    )


    result: 'Thing' = Field(None,
        description="The result produced in the action. e.g. John wrote a book."
    )


    startTime: Union[str] = Field(None,
        description="The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    target: str = Field(None,
        description="Indicates a target EntryPoint for an Action."
    )


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


    potentialAction: 'Action' = Field(None,
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


class AuthorizeAction(BaseModel):
    """
    AuthorizeAction
    """
    
    recipient: Union[str] = Field(None,
        description="A sub property of participant. The participant who is at the receiving end of the action."
    )


    actionStatus: str = Field(None,
        description="Indicates the current disposition of the Action."
    )


    agent: Union[str] = Field(None,
        description="The direct performer or driver of the action (animate or inanimate). e.g. John wrote a book."
    )


    endTime: Union[str] = Field(None,
        description="The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the end of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    error: 'Thing' = Field(None,
        description="For failed actions, more information on the cause of the failure."
    )


    instrument: 'Thing' = Field(None,
        description="The object that helped the agent perform the action. e.g. John wrote a book with a pen."
    )


    location: Union[str] = Field(None,
        description="The location of for example where the event is happening, an organization is located, or where an action takes place."
    )


    object: 'Thing' = Field(None,
        description="The object upon which the action is carried out, whose state is kept intact or changed. Also known as the semantic roles patient, affected or undergoer (which change their state) or theme (which doesn't). e.g. John read a book."
    )


    participant: Union[str] = Field(None,
        description="Other co-agents that participated in the action indirectly. e.g. John wrote a book with Steve."
    )


    result: 'Thing' = Field(None,
        description="The result produced in the action. e.g. John wrote a book."
    )


    startTime: Union[str] = Field(None,
        description="The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    target: str = Field(None,
        description="Indicates a target EntryPoint for an Action."
    )


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


    potentialAction: 'Action' = Field(None,
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


class RejectAction(BaseModel):
    """
    RejectAction
    """
    
    actionStatus: str = Field(None,
        description="Indicates the current disposition of the Action."
    )


    agent: Union[str] = Field(None,
        description="The direct performer or driver of the action (animate or inanimate). e.g. John wrote a book."
    )


    endTime: Union[str] = Field(None,
        description="The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the end of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    error: 'Thing' = Field(None,
        description="For failed actions, more information on the cause of the failure."
    )


    instrument: 'Thing' = Field(None,
        description="The object that helped the agent perform the action. e.g. John wrote a book with a pen."
    )


    location: Union[str] = Field(None,
        description="The location of for example where the event is happening, an organization is located, or where an action takes place."
    )


    object: 'Thing' = Field(None,
        description="The object upon which the action is carried out, whose state is kept intact or changed. Also known as the semantic roles patient, affected or undergoer (which change their state) or theme (which doesn't). e.g. John read a book."
    )


    participant: Union[str] = Field(None,
        description="Other co-agents that participated in the action indirectly. e.g. John wrote a book with Steve."
    )


    result: 'Thing' = Field(None,
        description="The result produced in the action. e.g. John wrote a book."
    )


    startTime: Union[str] = Field(None,
        description="The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    target: str = Field(None,
        description="Indicates a target EntryPoint for an Action."
    )


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


    potentialAction: 'Action' = Field(None,
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


class ApplyAction(BaseModel):
    """
    ApplyAction
    """
    
    actionStatus: str = Field(None,
        description="Indicates the current disposition of the Action."
    )


    agent: Union[str] = Field(None,
        description="The direct performer or driver of the action (animate or inanimate). e.g. John wrote a book."
    )


    endTime: Union[str] = Field(None,
        description="The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the end of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    error: 'Thing' = Field(None,
        description="For failed actions, more information on the cause of the failure."
    )


    instrument: 'Thing' = Field(None,
        description="The object that helped the agent perform the action. e.g. John wrote a book with a pen."
    )


    location: Union[str] = Field(None,
        description="The location of for example where the event is happening, an organization is located, or where an action takes place."
    )


    object: 'Thing' = Field(None,
        description="The object upon which the action is carried out, whose state is kept intact or changed. Also known as the semantic roles patient, affected or undergoer (which change their state) or theme (which doesn't). e.g. John read a book."
    )


    participant: Union[str] = Field(None,
        description="Other co-agents that participated in the action indirectly. e.g. John wrote a book with Steve."
    )


    result: 'Thing' = Field(None,
        description="The result produced in the action. e.g. John wrote a book."
    )


    startTime: Union[str] = Field(None,
        description="The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    target: str = Field(None,
        description="Indicates a target EntryPoint for an Action."
    )


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


    potentialAction: 'Action' = Field(None,
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


class BookmarkAction(BaseModel):
    """
    BookmarkAction
    """
    
    actionStatus: str = Field(None,
        description="Indicates the current disposition of the Action."
    )


    agent: Union[str] = Field(None,
        description="The direct performer or driver of the action (animate or inanimate). e.g. John wrote a book."
    )


    endTime: Union[str] = Field(None,
        description="The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the end of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    error: 'Thing' = Field(None,
        description="For failed actions, more information on the cause of the failure."
    )


    instrument: 'Thing' = Field(None,
        description="The object that helped the agent perform the action. e.g. John wrote a book with a pen."
    )


    location: Union[str] = Field(None,
        description="The location of for example where the event is happening, an organization is located, or where an action takes place."
    )


    object: 'Thing' = Field(None,
        description="The object upon which the action is carried out, whose state is kept intact or changed. Also known as the semantic roles patient, affected or undergoer (which change their state) or theme (which doesn't). e.g. John read a book."
    )


    participant: Union[str] = Field(None,
        description="Other co-agents that participated in the action indirectly. e.g. John wrote a book with Steve."
    )


    result: 'Thing' = Field(None,
        description="The result produced in the action. e.g. John wrote a book."
    )


    startTime: Union[str] = Field(None,
        description="The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    target: str = Field(None,
        description="Indicates a target EntryPoint for an Action."
    )


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


    potentialAction: 'Action' = Field(None,
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


class PlanAction(BaseModel):
    """
    PlanAction
    """
    
    scheduledTime: str = Field(None,
        description="The time the object is scheduled to."
    )


    actionStatus: str = Field(None,
        description="Indicates the current disposition of the Action."
    )


    agent: Union[str] = Field(None,
        description="The direct performer or driver of the action (animate or inanimate). e.g. John wrote a book."
    )


    endTime: Union[str] = Field(None,
        description="The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the end of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    error: 'Thing' = Field(None,
        description="For failed actions, more information on the cause of the failure."
    )


    instrument: 'Thing' = Field(None,
        description="The object that helped the agent perform the action. e.g. John wrote a book with a pen."
    )


    location: Union[str] = Field(None,
        description="The location of for example where the event is happening, an organization is located, or where an action takes place."
    )


    object: 'Thing' = Field(None,
        description="The object upon which the action is carried out, whose state is kept intact or changed. Also known as the semantic roles patient, affected or undergoer (which change their state) or theme (which doesn't). e.g. John read a book."
    )


    participant: Union[str] = Field(None,
        description="Other co-agents that participated in the action indirectly. e.g. John wrote a book with Steve."
    )


    result: 'Thing' = Field(None,
        description="The result produced in the action. e.g. John wrote a book."
    )


    startTime: Union[str] = Field(None,
        description="The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    target: str = Field(None,
        description="Indicates a target EntryPoint for an Action."
    )


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


    potentialAction: 'Action' = Field(None,
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


class CancelAction(BaseModel):
    """
    CancelAction
    """
    
    scheduledTime: str = Field(None,
        description="The time the object is scheduled to."
    )


    actionStatus: str = Field(None,
        description="Indicates the current disposition of the Action."
    )


    agent: Union[str] = Field(None,
        description="The direct performer or driver of the action (animate or inanimate). e.g. John wrote a book."
    )


    endTime: Union[str] = Field(None,
        description="The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the end of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    error: 'Thing' = Field(None,
        description="For failed actions, more information on the cause of the failure."
    )


    instrument: 'Thing' = Field(None,
        description="The object that helped the agent perform the action. e.g. John wrote a book with a pen."
    )


    location: Union[str] = Field(None,
        description="The location of for example where the event is happening, an organization is located, or where an action takes place."
    )


    object: 'Thing' = Field(None,
        description="The object upon which the action is carried out, whose state is kept intact or changed. Also known as the semantic roles patient, affected or undergoer (which change their state) or theme (which doesn't). e.g. John read a book."
    )


    participant: Union[str] = Field(None,
        description="Other co-agents that participated in the action indirectly. e.g. John wrote a book with Steve."
    )


    result: 'Thing' = Field(None,
        description="The result produced in the action. e.g. John wrote a book."
    )


    startTime: Union[str] = Field(None,
        description="The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    target: str = Field(None,
        description="Indicates a target EntryPoint for an Action."
    )


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


    potentialAction: 'Action' = Field(None,
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


class ReserveAction(BaseModel):
    """
    ReserveAction
    """
    
    scheduledTime: str = Field(None,
        description="The time the object is scheduled to."
    )


    actionStatus: str = Field(None,
        description="Indicates the current disposition of the Action."
    )


    agent: Union[str] = Field(None,
        description="The direct performer or driver of the action (animate or inanimate). e.g. John wrote a book."
    )


    endTime: Union[str] = Field(None,
        description="The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the end of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    error: 'Thing' = Field(None,
        description="For failed actions, more information on the cause of the failure."
    )


    instrument: 'Thing' = Field(None,
        description="The object that helped the agent perform the action. e.g. John wrote a book with a pen."
    )


    location: Union[str] = Field(None,
        description="The location of for example where the event is happening, an organization is located, or where an action takes place."
    )


    object: 'Thing' = Field(None,
        description="The object upon which the action is carried out, whose state is kept intact or changed. Also known as the semantic roles patient, affected or undergoer (which change their state) or theme (which doesn't). e.g. John read a book."
    )


    participant: Union[str] = Field(None,
        description="Other co-agents that participated in the action indirectly. e.g. John wrote a book with Steve."
    )


    result: 'Thing' = Field(None,
        description="The result produced in the action. e.g. John wrote a book."
    )


    startTime: Union[str] = Field(None,
        description="The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    target: str = Field(None,
        description="Indicates a target EntryPoint for an Action."
    )


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


    potentialAction: 'Action' = Field(None,
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


class ScheduleAction(BaseModel):
    """
    ScheduleAction
    """
    
    scheduledTime: str = Field(None,
        description="The time the object is scheduled to."
    )


    actionStatus: str = Field(None,
        description="Indicates the current disposition of the Action."
    )


    agent: Union[str] = Field(None,
        description="The direct performer or driver of the action (animate or inanimate). e.g. John wrote a book."
    )


    endTime: Union[str] = Field(None,
        description="The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the end of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    error: 'Thing' = Field(None,
        description="For failed actions, more information on the cause of the failure."
    )


    instrument: 'Thing' = Field(None,
        description="The object that helped the agent perform the action. e.g. John wrote a book with a pen."
    )


    location: Union[str] = Field(None,
        description="The location of for example where the event is happening, an organization is located, or where an action takes place."
    )


    object: 'Thing' = Field(None,
        description="The object upon which the action is carried out, whose state is kept intact or changed. Also known as the semantic roles patient, affected or undergoer (which change their state) or theme (which doesn't). e.g. John read a book."
    )


    participant: Union[str] = Field(None,
        description="Other co-agents that participated in the action indirectly. e.g. John wrote a book with Steve."
    )


    result: 'Thing' = Field(None,
        description="The result produced in the action. e.g. John wrote a book."
    )


    startTime: Union[str] = Field(None,
        description="The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    target: str = Field(None,
        description="Indicates a target EntryPoint for an Action."
    )


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


    potentialAction: 'Action' = Field(None,
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


class PlayAction(BaseModel):
    """
    PlayAction
    """
    
    audience: str = Field(None,
        description="An intended audience, i.e. a group for whom something was created. Supersedes serviceAudience."
    )


    event: str = Field(None,
        description="Upcoming or past event associated with this place, organization, or action. Supersedes events."
    )


    actionStatus: str = Field(None,
        description="Indicates the current disposition of the Action."
    )


    agent: Union[str] = Field(None,
        description="The direct performer or driver of the action (animate or inanimate). e.g. John wrote a book."
    )


    endTime: Union[str] = Field(None,
        description="The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the end of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    error: 'Thing' = Field(None,
        description="For failed actions, more information on the cause of the failure."
    )


    instrument: 'Thing' = Field(None,
        description="The object that helped the agent perform the action. e.g. John wrote a book with a pen."
    )


    location: Union[str] = Field(None,
        description="The location of for example where the event is happening, an organization is located, or where an action takes place."
    )


    object: 'Thing' = Field(None,
        description="The object upon which the action is carried out, whose state is kept intact or changed. Also known as the semantic roles patient, affected or undergoer (which change their state) or theme (which doesn't). e.g. John read a book."
    )


    participant: Union[str] = Field(None,
        description="Other co-agents that participated in the action indirectly. e.g. John wrote a book with Steve."
    )


    result: 'Thing' = Field(None,
        description="The result produced in the action. e.g. John wrote a book."
    )


    startTime: Union[str] = Field(None,
        description="The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    target: str = Field(None,
        description="Indicates a target EntryPoint for an Action."
    )


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


    potentialAction: 'Action' = Field(None,
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


class ExerciseAction(BaseModel):
    """
    ExerciseAction
    """
    
    diet: str = Field(None,
        description="A sub property of instrument. The diet used in this action."
    )


    distance: str = Field(None,
        description="The distance travelled, e.g. exercising or travelling."
    )


    exerciseCourse: str = Field(None,
        description="A sub property of location. The course where this action was taken. Supersedes course."
    )


    exercisePlan: str = Field(None,
        description="A sub property of instrument. The exercise plan used on this action."
    )


    exerciseRelatedDiet: str = Field(None,
        description="A sub property of instrument. The diet used in this action."
    )


    exerciseType: str = Field(None,
        description="Type(s) of exercise or activity, such as strength training, flexibility training, aerobics, cardiac rehabilitation, etc."
    )


    fromLocation: str = Field(None,
        description="A sub property of location. The original location of the object or the agent before the action."
    )


    opponent: str = Field(None,
        description="A sub property of participant. The opponent on this action."
    )


    sportsActivityLocation: Union[str] = Field(None,
        description="A sub property of location. The sports activity location where this action occurred."
    )


    sportsEvent: Union[str] = Field(None,
        description="A sub property of location. The sports event where this action occurred."
    )


    sportsTeam: Union[str] = Field(None,
        description="A sub property of participant. The sports team that participated on this action."
    )


    toLocation: str = Field(None,
        description="A sub property of location. The final location of the object or the agent after the action."
    )


    audience: str = Field(None,
        description="An intended audience, i.e. a group for whom something was created. Supersedes serviceAudience."
    )


    event: str = Field(None,
        description="Upcoming or past event associated with this place, organization, or action. Supersedes events."
    )


    actionStatus: str = Field(None,
        description="Indicates the current disposition of the Action."
    )


    agent: Union[str] = Field(None,
        description="The direct performer or driver of the action (animate or inanimate). e.g. John wrote a book."
    )


    endTime: Union[str] = Field(None,
        description="The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the end of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    error: 'Thing' = Field(None,
        description="For failed actions, more information on the cause of the failure."
    )


    instrument: 'Thing' = Field(None,
        description="The object that helped the agent perform the action. e.g. John wrote a book with a pen."
    )


    location: Union[str] = Field(None,
        description="The location of for example where the event is happening, an organization is located, or where an action takes place."
    )


    object: 'Thing' = Field(None,
        description="The object upon which the action is carried out, whose state is kept intact or changed. Also known as the semantic roles patient, affected or undergoer (which change their state) or theme (which doesn't). e.g. John read a book."
    )


    participant: Union[str] = Field(None,
        description="Other co-agents that participated in the action indirectly. e.g. John wrote a book with Steve."
    )


    result: 'Thing' = Field(None,
        description="The result produced in the action. e.g. John wrote a book."
    )


    startTime: Union[str] = Field(None,
        description="The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    target: str = Field(None,
        description="Indicates a target EntryPoint for an Action."
    )


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


    potentialAction: 'Action' = Field(None,
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


class PerformAction(BaseModel):
    """
    PerformAction
    """
    
    entertainmentBusiness: str = Field(None,
        description="A sub property of location. The entertainment business where the action occurred."
    )


    audience: str = Field(None,
        description="An intended audience, i.e. a group for whom something was created. Supersedes serviceAudience."
    )


    event: str = Field(None,
        description="Upcoming or past event associated with this place, organization, or action. Supersedes events."
    )


    actionStatus: str = Field(None,
        description="Indicates the current disposition of the Action."
    )


    agent: Union[str] = Field(None,
        description="The direct performer or driver of the action (animate or inanimate). e.g. John wrote a book."
    )


    endTime: Union[str] = Field(None,
        description="The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the end of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    error: 'Thing' = Field(None,
        description="For failed actions, more information on the cause of the failure."
    )


    instrument: 'Thing' = Field(None,
        description="The object that helped the agent perform the action. e.g. John wrote a book with a pen."
    )


    location: Union[str] = Field(None,
        description="The location of for example where the event is happening, an organization is located, or where an action takes place."
    )


    object: 'Thing' = Field(None,
        description="The object upon which the action is carried out, whose state is kept intact or changed. Also known as the semantic roles patient, affected or undergoer (which change their state) or theme (which doesn't). e.g. John read a book."
    )


    participant: Union[str] = Field(None,
        description="Other co-agents that participated in the action indirectly. e.g. John wrote a book with Steve."
    )


    result: 'Thing' = Field(None,
        description="The result produced in the action. e.g. John wrote a book."
    )


    startTime: Union[str] = Field(None,
        description="The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    target: str = Field(None,
        description="Indicates a target EntryPoint for an Action."
    )


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


    potentialAction: 'Action' = Field(None,
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


class SearchAction(BaseModel):
    """
    SearchAction
    """
    
    query: str = Field(None,
        description="A sub property of instrument. The query used on this action."
    )


    actionStatus: str = Field(None,
        description="Indicates the current disposition of the Action."
    )


    agent: Union[str] = Field(None,
        description="The direct performer or driver of the action (animate or inanimate). e.g. John wrote a book."
    )


    endTime: Union[str] = Field(None,
        description="The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the end of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    error: 'Thing' = Field(None,
        description="For failed actions, more information on the cause of the failure."
    )


    instrument: 'Thing' = Field(None,
        description="The object that helped the agent perform the action. e.g. John wrote a book with a pen."
    )


    location: Union[str] = Field(None,
        description="The location of for example where the event is happening, an organization is located, or where an action takes place."
    )


    object: 'Thing' = Field(None,
        description="The object upon which the action is carried out, whose state is kept intact or changed. Also known as the semantic roles patient, affected or undergoer (which change their state) or theme (which doesn't). e.g. John read a book."
    )


    participant: Union[str] = Field(None,
        description="Other co-agents that participated in the action indirectly. e.g. John wrote a book with Steve."
    )


    result: 'Thing' = Field(None,
        description="The result produced in the action. e.g. John wrote a book."
    )


    startTime: Union[str] = Field(None,
        description="The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    target: str = Field(None,
        description="Indicates a target EntryPoint for an Action."
    )


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


    potentialAction: 'Action' = Field(None,
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


class TradeAction(BaseModel):
    """
    TradeAction
    """
    
    price: Union[str] = Field(None,
        description="The offer price of a product, or of a price component when attached to PriceSpecification and its subtypes.Usage guidelines:Use the priceCurrency property (with standard formats: ISO 4217 currency format e.g. \"USD\"; Ticker symbol for cryptocurrencies e.g. \"BTC\"; well known names for Local Exchange Tradings Systems (LETS) and other currency types e.g. \"Ithaca HOUR\") instead of including ambiguous symbols such as '$' in the value.Use '.' (Unicode 'FULL STOP' (U+002E)) rather than ',' to indicate a decimal point. Avoid using these symbols as a readability separator.Note that both RDFa and Microdata syntax allow the use of a \"content=\" attribute for publishing simple machine-readable values alongside more human-friendly formatting.Use values from 0123456789 (Unicode 'DIGIT ZERO' (U+0030) to 'DIGIT NINE' (U+0039)) rather than superficially similiar Unicode symbols."
    )


    priceCurrency: str = Field(None,
        description="The currency of the price, or a price component when attached to PriceSpecification and its subtypes.Use standard formats: ISO 4217 currency format e.g. \"USD\"; Ticker symbol for cryptocurrencies e.g. \"BTC\"; well known names for Local Exchange Tradings Systems (LETS) and other currency types e.g. \"Ithaca HOUR\"."
    )


    priceSpecification: str = Field(None,
        description="One or more detailed price specifications, indicating the unit price and delivery or payment charges."
    )


    actionStatus: str = Field(None,
        description="Indicates the current disposition of the Action."
    )


    agent: Union[str] = Field(None,
        description="The direct performer or driver of the action (animate or inanimate). e.g. John wrote a book."
    )


    endTime: Union[str] = Field(None,
        description="The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the end of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    error: 'Thing' = Field(None,
        description="For failed actions, more information on the cause of the failure."
    )


    instrument: 'Thing' = Field(None,
        description="The object that helped the agent perform the action. e.g. John wrote a book with a pen."
    )


    location: Union[str] = Field(None,
        description="The location of for example where the event is happening, an organization is located, or where an action takes place."
    )


    object: 'Thing' = Field(None,
        description="The object upon which the action is carried out, whose state is kept intact or changed. Also known as the semantic roles patient, affected or undergoer (which change their state) or theme (which doesn't). e.g. John read a book."
    )


    participant: Union[str] = Field(None,
        description="Other co-agents that participated in the action indirectly. e.g. John wrote a book with Steve."
    )


    result: 'Thing' = Field(None,
        description="The result produced in the action. e.g. John wrote a book."
    )


    startTime: Union[str] = Field(None,
        description="The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    target: str = Field(None,
        description="Indicates a target EntryPoint for an Action."
    )


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


    potentialAction: 'Action' = Field(None,
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


class BuyAction(BaseModel):
    """
    BuyAction
    """
    
    seller: Union[str] = Field(None,
        description="An entity which offers (sells / leases / lends / loans) the services / goods.  A seller may also be a provider. Supersedes merchant, vendor."
    )


    price: Union[str] = Field(None,
        description="The offer price of a product, or of a price component when attached to PriceSpecification and its subtypes.Usage guidelines:Use the priceCurrency property (with standard formats: ISO 4217 currency format e.g. \"USD\"; Ticker symbol for cryptocurrencies e.g. \"BTC\"; well known names for Local Exchange Tradings Systems (LETS) and other currency types e.g. \"Ithaca HOUR\") instead of including ambiguous symbols such as '$' in the value.Use '.' (Unicode 'FULL STOP' (U+002E)) rather than ',' to indicate a decimal point. Avoid using these symbols as a readability separator.Note that both RDFa and Microdata syntax allow the use of a \"content=\" attribute for publishing simple machine-readable values alongside more human-friendly formatting.Use values from 0123456789 (Unicode 'DIGIT ZERO' (U+0030) to 'DIGIT NINE' (U+0039)) rather than superficially similiar Unicode symbols."
    )


    priceCurrency: str = Field(None,
        description="The currency of the price, or a price component when attached to PriceSpecification and its subtypes.Use standard formats: ISO 4217 currency format e.g. \"USD\"; Ticker symbol for cryptocurrencies e.g. \"BTC\"; well known names for Local Exchange Tradings Systems (LETS) and other currency types e.g. \"Ithaca HOUR\"."
    )


    priceSpecification: str = Field(None,
        description="One or more detailed price specifications, indicating the unit price and delivery or payment charges."
    )


    actionStatus: str = Field(None,
        description="Indicates the current disposition of the Action."
    )


    agent: Union[str] = Field(None,
        description="The direct performer or driver of the action (animate or inanimate). e.g. John wrote a book."
    )


    endTime: Union[str] = Field(None,
        description="The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the end of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    error: 'Thing' = Field(None,
        description="For failed actions, more information on the cause of the failure."
    )


    instrument: 'Thing' = Field(None,
        description="The object that helped the agent perform the action. e.g. John wrote a book with a pen."
    )


    location: Union[str] = Field(None,
        description="The location of for example where the event is happening, an organization is located, or where an action takes place."
    )


    object: 'Thing' = Field(None,
        description="The object upon which the action is carried out, whose state is kept intact or changed. Also known as the semantic roles patient, affected or undergoer (which change their state) or theme (which doesn't). e.g. John read a book."
    )


    participant: Union[str] = Field(None,
        description="Other co-agents that participated in the action indirectly. e.g. John wrote a book with Steve."
    )


    result: 'Thing' = Field(None,
        description="The result produced in the action. e.g. John wrote a book."
    )


    startTime: Union[str] = Field(None,
        description="The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    target: str = Field(None,
        description="Indicates a target EntryPoint for an Action."
    )


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


    potentialAction: 'Action' = Field(None,
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


class DonateAction(BaseModel):
    """
    DonateAction
    """
    
    recipient: Union[str] = Field(None,
        description="A sub property of participant. The participant who is at the receiving end of the action."
    )


    price: Union[str] = Field(None,
        description="The offer price of a product, or of a price component when attached to PriceSpecification and its subtypes.Usage guidelines:Use the priceCurrency property (with standard formats: ISO 4217 currency format e.g. \"USD\"; Ticker symbol for cryptocurrencies e.g. \"BTC\"; well known names for Local Exchange Tradings Systems (LETS) and other currency types e.g. \"Ithaca HOUR\") instead of including ambiguous symbols such as '$' in the value.Use '.' (Unicode 'FULL STOP' (U+002E)) rather than ',' to indicate a decimal point. Avoid using these symbols as a readability separator.Note that both RDFa and Microdata syntax allow the use of a \"content=\" attribute for publishing simple machine-readable values alongside more human-friendly formatting.Use values from 0123456789 (Unicode 'DIGIT ZERO' (U+0030) to 'DIGIT NINE' (U+0039)) rather than superficially similiar Unicode symbols."
    )


    priceCurrency: str = Field(None,
        description="The currency of the price, or a price component when attached to PriceSpecification and its subtypes.Use standard formats: ISO 4217 currency format e.g. \"USD\"; Ticker symbol for cryptocurrencies e.g. \"BTC\"; well known names for Local Exchange Tradings Systems (LETS) and other currency types e.g. \"Ithaca HOUR\"."
    )


    priceSpecification: str = Field(None,
        description="One or more detailed price specifications, indicating the unit price and delivery or payment charges."
    )


    actionStatus: str = Field(None,
        description="Indicates the current disposition of the Action."
    )


    agent: Union[str] = Field(None,
        description="The direct performer or driver of the action (animate or inanimate). e.g. John wrote a book."
    )


    endTime: Union[str] = Field(None,
        description="The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the end of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    error: 'Thing' = Field(None,
        description="For failed actions, more information on the cause of the failure."
    )


    instrument: 'Thing' = Field(None,
        description="The object that helped the agent perform the action. e.g. John wrote a book with a pen."
    )


    location: Union[str] = Field(None,
        description="The location of for example where the event is happening, an organization is located, or where an action takes place."
    )


    object: 'Thing' = Field(None,
        description="The object upon which the action is carried out, whose state is kept intact or changed. Also known as the semantic roles patient, affected or undergoer (which change their state) or theme (which doesn't). e.g. John read a book."
    )


    participant: Union[str] = Field(None,
        description="Other co-agents that participated in the action indirectly. e.g. John wrote a book with Steve."
    )


    result: 'Thing' = Field(None,
        description="The result produced in the action. e.g. John wrote a book."
    )


    startTime: Union[str] = Field(None,
        description="The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    target: str = Field(None,
        description="Indicates a target EntryPoint for an Action."
    )


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


    potentialAction: 'Action' = Field(None,
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


class OrderAction(BaseModel):
    """
    OrderAction
    """
    
    deliveryMethod: str = Field(None,
        description="A sub property of instrument. The method of delivery."
    )


    price: Union[str] = Field(None,
        description="The offer price of a product, or of a price component when attached to PriceSpecification and its subtypes.Usage guidelines:Use the priceCurrency property (with standard formats: ISO 4217 currency format e.g. \"USD\"; Ticker symbol for cryptocurrencies e.g. \"BTC\"; well known names for Local Exchange Tradings Systems (LETS) and other currency types e.g. \"Ithaca HOUR\") instead of including ambiguous symbols such as '$' in the value.Use '.' (Unicode 'FULL STOP' (U+002E)) rather than ',' to indicate a decimal point. Avoid using these symbols as a readability separator.Note that both RDFa and Microdata syntax allow the use of a \"content=\" attribute for publishing simple machine-readable values alongside more human-friendly formatting.Use values from 0123456789 (Unicode 'DIGIT ZERO' (U+0030) to 'DIGIT NINE' (U+0039)) rather than superficially similiar Unicode symbols."
    )


    priceCurrency: str = Field(None,
        description="The currency of the price, or a price component when attached to PriceSpecification and its subtypes.Use standard formats: ISO 4217 currency format e.g. \"USD\"; Ticker symbol for cryptocurrencies e.g. \"BTC\"; well known names for Local Exchange Tradings Systems (LETS) and other currency types e.g. \"Ithaca HOUR\"."
    )


    priceSpecification: str = Field(None,
        description="One or more detailed price specifications, indicating the unit price and delivery or payment charges."
    )


    actionStatus: str = Field(None,
        description="Indicates the current disposition of the Action."
    )


    agent: Union[str] = Field(None,
        description="The direct performer or driver of the action (animate or inanimate). e.g. John wrote a book."
    )


    endTime: Union[str] = Field(None,
        description="The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the end of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    error: 'Thing' = Field(None,
        description="For failed actions, more information on the cause of the failure."
    )


    instrument: 'Thing' = Field(None,
        description="The object that helped the agent perform the action. e.g. John wrote a book with a pen."
    )


    location: Union[str] = Field(None,
        description="The location of for example where the event is happening, an organization is located, or where an action takes place."
    )


    object: 'Thing' = Field(None,
        description="The object upon which the action is carried out, whose state is kept intact or changed. Also known as the semantic roles patient, affected or undergoer (which change their state) or theme (which doesn't). e.g. John read a book."
    )


    participant: Union[str] = Field(None,
        description="Other co-agents that participated in the action indirectly. e.g. John wrote a book with Steve."
    )


    result: 'Thing' = Field(None,
        description="The result produced in the action. e.g. John wrote a book."
    )


    startTime: Union[str] = Field(None,
        description="The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    target: str = Field(None,
        description="Indicates a target EntryPoint for an Action."
    )


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


    potentialAction: 'Action' = Field(None,
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


class PayAction(BaseModel):
    """
    PayAction
    """
    
    recipient: Union[str] = Field(None,
        description="A sub property of participant. The participant who is at the receiving end of the action."
    )


    price: Union[str] = Field(None,
        description="The offer price of a product, or of a price component when attached to PriceSpecification and its subtypes.Usage guidelines:Use the priceCurrency property (with standard formats: ISO 4217 currency format e.g. \"USD\"; Ticker symbol for cryptocurrencies e.g. \"BTC\"; well known names for Local Exchange Tradings Systems (LETS) and other currency types e.g. \"Ithaca HOUR\") instead of including ambiguous symbols such as '$' in the value.Use '.' (Unicode 'FULL STOP' (U+002E)) rather than ',' to indicate a decimal point. Avoid using these symbols as a readability separator.Note that both RDFa and Microdata syntax allow the use of a \"content=\" attribute for publishing simple machine-readable values alongside more human-friendly formatting.Use values from 0123456789 (Unicode 'DIGIT ZERO' (U+0030) to 'DIGIT NINE' (U+0039)) rather than superficially similiar Unicode symbols."
    )


    priceCurrency: str = Field(None,
        description="The currency of the price, or a price component when attached to PriceSpecification and its subtypes.Use standard formats: ISO 4217 currency format e.g. \"USD\"; Ticker symbol for cryptocurrencies e.g. \"BTC\"; well known names for Local Exchange Tradings Systems (LETS) and other currency types e.g. \"Ithaca HOUR\"."
    )


    priceSpecification: str = Field(None,
        description="One or more detailed price specifications, indicating the unit price and delivery or payment charges."
    )


    actionStatus: str = Field(None,
        description="Indicates the current disposition of the Action."
    )


    agent: Union[str] = Field(None,
        description="The direct performer or driver of the action (animate or inanimate). e.g. John wrote a book."
    )


    endTime: Union[str] = Field(None,
        description="The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the end of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    error: 'Thing' = Field(None,
        description="For failed actions, more information on the cause of the failure."
    )


    instrument: 'Thing' = Field(None,
        description="The object that helped the agent perform the action. e.g. John wrote a book with a pen."
    )


    location: Union[str] = Field(None,
        description="The location of for example where the event is happening, an organization is located, or where an action takes place."
    )


    object: 'Thing' = Field(None,
        description="The object upon which the action is carried out, whose state is kept intact or changed. Also known as the semantic roles patient, affected or undergoer (which change their state) or theme (which doesn't). e.g. John read a book."
    )


    participant: Union[str] = Field(None,
        description="Other co-agents that participated in the action indirectly. e.g. John wrote a book with Steve."
    )


    result: 'Thing' = Field(None,
        description="The result produced in the action. e.g. John wrote a book."
    )


    startTime: Union[str] = Field(None,
        description="The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    target: str = Field(None,
        description="Indicates a target EntryPoint for an Action."
    )


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


    potentialAction: 'Action' = Field(None,
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


class PreOrderAction(BaseModel):
    """
    PreOrderAction
    """
    
    price: Union[str] = Field(None,
        description="The offer price of a product, or of a price component when attached to PriceSpecification and its subtypes.Usage guidelines:Use the priceCurrency property (with standard formats: ISO 4217 currency format e.g. \"USD\"; Ticker symbol for cryptocurrencies e.g. \"BTC\"; well known names for Local Exchange Tradings Systems (LETS) and other currency types e.g. \"Ithaca HOUR\") instead of including ambiguous symbols such as '$' in the value.Use '.' (Unicode 'FULL STOP' (U+002E)) rather than ',' to indicate a decimal point. Avoid using these symbols as a readability separator.Note that both RDFa and Microdata syntax allow the use of a \"content=\" attribute for publishing simple machine-readable values alongside more human-friendly formatting.Use values from 0123456789 (Unicode 'DIGIT ZERO' (U+0030) to 'DIGIT NINE' (U+0039)) rather than superficially similiar Unicode symbols."
    )


    priceCurrency: str = Field(None,
        description="The currency of the price, or a price component when attached to PriceSpecification and its subtypes.Use standard formats: ISO 4217 currency format e.g. \"USD\"; Ticker symbol for cryptocurrencies e.g. \"BTC\"; well known names for Local Exchange Tradings Systems (LETS) and other currency types e.g. \"Ithaca HOUR\"."
    )


    priceSpecification: str = Field(None,
        description="One or more detailed price specifications, indicating the unit price and delivery or payment charges."
    )


    actionStatus: str = Field(None,
        description="Indicates the current disposition of the Action."
    )


    agent: Union[str] = Field(None,
        description="The direct performer or driver of the action (animate or inanimate). e.g. John wrote a book."
    )


    endTime: Union[str] = Field(None,
        description="The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the end of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    error: 'Thing' = Field(None,
        description="For failed actions, more information on the cause of the failure."
    )


    instrument: 'Thing' = Field(None,
        description="The object that helped the agent perform the action. e.g. John wrote a book with a pen."
    )


    location: Union[str] = Field(None,
        description="The location of for example where the event is happening, an organization is located, or where an action takes place."
    )


    object: 'Thing' = Field(None,
        description="The object upon which the action is carried out, whose state is kept intact or changed. Also known as the semantic roles patient, affected or undergoer (which change their state) or theme (which doesn't). e.g. John read a book."
    )


    participant: Union[str] = Field(None,
        description="Other co-agents that participated in the action indirectly. e.g. John wrote a book with Steve."
    )


    result: 'Thing' = Field(None,
        description="The result produced in the action. e.g. John wrote a book."
    )


    startTime: Union[str] = Field(None,
        description="The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    target: str = Field(None,
        description="Indicates a target EntryPoint for an Action."
    )


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


    potentialAction: 'Action' = Field(None,
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


class QuoteAction(BaseModel):
    """
    QuoteAction
    """
    
    price: Union[str] = Field(None,
        description="The offer price of a product, or of a price component when attached to PriceSpecification and its subtypes.Usage guidelines:Use the priceCurrency property (with standard formats: ISO 4217 currency format e.g. \"USD\"; Ticker symbol for cryptocurrencies e.g. \"BTC\"; well known names for Local Exchange Tradings Systems (LETS) and other currency types e.g. \"Ithaca HOUR\") instead of including ambiguous symbols such as '$' in the value.Use '.' (Unicode 'FULL STOP' (U+002E)) rather than ',' to indicate a decimal point. Avoid using these symbols as a readability separator.Note that both RDFa and Microdata syntax allow the use of a \"content=\" attribute for publishing simple machine-readable values alongside more human-friendly formatting.Use values from 0123456789 (Unicode 'DIGIT ZERO' (U+0030) to 'DIGIT NINE' (U+0039)) rather than superficially similiar Unicode symbols."
    )


    priceCurrency: str = Field(None,
        description="The currency of the price, or a price component when attached to PriceSpecification and its subtypes.Use standard formats: ISO 4217 currency format e.g. \"USD\"; Ticker symbol for cryptocurrencies e.g. \"BTC\"; well known names for Local Exchange Tradings Systems (LETS) and other currency types e.g. \"Ithaca HOUR\"."
    )


    priceSpecification: str = Field(None,
        description="One or more detailed price specifications, indicating the unit price and delivery or payment charges."
    )


    actionStatus: str = Field(None,
        description="Indicates the current disposition of the Action."
    )


    agent: Union[str] = Field(None,
        description="The direct performer or driver of the action (animate or inanimate). e.g. John wrote a book."
    )


    endTime: Union[str] = Field(None,
        description="The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the end of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    error: 'Thing' = Field(None,
        description="For failed actions, more information on the cause of the failure."
    )


    instrument: 'Thing' = Field(None,
        description="The object that helped the agent perform the action. e.g. John wrote a book with a pen."
    )


    location: Union[str] = Field(None,
        description="The location of for example where the event is happening, an organization is located, or where an action takes place."
    )


    object: 'Thing' = Field(None,
        description="The object upon which the action is carried out, whose state is kept intact or changed. Also known as the semantic roles patient, affected or undergoer (which change their state) or theme (which doesn't). e.g. John read a book."
    )


    participant: Union[str] = Field(None,
        description="Other co-agents that participated in the action indirectly. e.g. John wrote a book with Steve."
    )


    result: 'Thing' = Field(None,
        description="The result produced in the action. e.g. John wrote a book."
    )


    startTime: Union[str] = Field(None,
        description="The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    target: str = Field(None,
        description="Indicates a target EntryPoint for an Action."
    )


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


    potentialAction: 'Action' = Field(None,
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


class RentAction(BaseModel):
    """
    RentAction
    """
    
    landlord: Union[str] = Field(None,
        description="A sub property of participant. The owner of the real estate property."
    )


    realEstateAgent: str = Field(None,
        description="A sub property of participant. The real estate agent involved in the action."
    )


    price: Union[str] = Field(None,
        description="The offer price of a product, or of a price component when attached to PriceSpecification and its subtypes.Usage guidelines:Use the priceCurrency property (with standard formats: ISO 4217 currency format e.g. \"USD\"; Ticker symbol for cryptocurrencies e.g. \"BTC\"; well known names for Local Exchange Tradings Systems (LETS) and other currency types e.g. \"Ithaca HOUR\") instead of including ambiguous symbols such as '$' in the value.Use '.' (Unicode 'FULL STOP' (U+002E)) rather than ',' to indicate a decimal point. Avoid using these symbols as a readability separator.Note that both RDFa and Microdata syntax allow the use of a \"content=\" attribute for publishing simple machine-readable values alongside more human-friendly formatting.Use values from 0123456789 (Unicode 'DIGIT ZERO' (U+0030) to 'DIGIT NINE' (U+0039)) rather than superficially similiar Unicode symbols."
    )


    priceCurrency: str = Field(None,
        description="The currency of the price, or a price component when attached to PriceSpecification and its subtypes.Use standard formats: ISO 4217 currency format e.g. \"USD\"; Ticker symbol for cryptocurrencies e.g. \"BTC\"; well known names for Local Exchange Tradings Systems (LETS) and other currency types e.g. \"Ithaca HOUR\"."
    )


    priceSpecification: str = Field(None,
        description="One or more detailed price specifications, indicating the unit price and delivery or payment charges."
    )


    actionStatus: str = Field(None,
        description="Indicates the current disposition of the Action."
    )


    agent: Union[str] = Field(None,
        description="The direct performer or driver of the action (animate or inanimate). e.g. John wrote a book."
    )


    endTime: Union[str] = Field(None,
        description="The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the end of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    error: 'Thing' = Field(None,
        description="For failed actions, more information on the cause of the failure."
    )


    instrument: 'Thing' = Field(None,
        description="The object that helped the agent perform the action. e.g. John wrote a book with a pen."
    )


    location: Union[str] = Field(None,
        description="The location of for example where the event is happening, an organization is located, or where an action takes place."
    )


    object: 'Thing' = Field(None,
        description="The object upon which the action is carried out, whose state is kept intact or changed. Also known as the semantic roles patient, affected or undergoer (which change their state) or theme (which doesn't). e.g. John read a book."
    )


    participant: Union[str] = Field(None,
        description="Other co-agents that participated in the action indirectly. e.g. John wrote a book with Steve."
    )


    result: 'Thing' = Field(None,
        description="The result produced in the action. e.g. John wrote a book."
    )


    startTime: Union[str] = Field(None,
        description="The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    target: str = Field(None,
        description="Indicates a target EntryPoint for an Action."
    )


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


    potentialAction: 'Action' = Field(None,
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


class SellAction(BaseModel):
    """
    SellAction
    """
    
    buyer: str = Field(None,
        description="A sub property of participant. The participant/person/organization that bought the object."
    )


    price: Union[str] = Field(None,
        description="The offer price of a product, or of a price component when attached to PriceSpecification and its subtypes.Usage guidelines:Use the priceCurrency property (with standard formats: ISO 4217 currency format e.g. \"USD\"; Ticker symbol for cryptocurrencies e.g. \"BTC\"; well known names for Local Exchange Tradings Systems (LETS) and other currency types e.g. \"Ithaca HOUR\") instead of including ambiguous symbols such as '$' in the value.Use '.' (Unicode 'FULL STOP' (U+002E)) rather than ',' to indicate a decimal point. Avoid using these symbols as a readability separator.Note that both RDFa and Microdata syntax allow the use of a \"content=\" attribute for publishing simple machine-readable values alongside more human-friendly formatting.Use values from 0123456789 (Unicode 'DIGIT ZERO' (U+0030) to 'DIGIT NINE' (U+0039)) rather than superficially similiar Unicode symbols."
    )


    priceCurrency: str = Field(None,
        description="The currency of the price, or a price component when attached to PriceSpecification and its subtypes.Use standard formats: ISO 4217 currency format e.g. \"USD\"; Ticker symbol for cryptocurrencies e.g. \"BTC\"; well known names for Local Exchange Tradings Systems (LETS) and other currency types e.g. \"Ithaca HOUR\"."
    )


    priceSpecification: str = Field(None,
        description="One or more detailed price specifications, indicating the unit price and delivery or payment charges."
    )


    actionStatus: str = Field(None,
        description="Indicates the current disposition of the Action."
    )


    agent: Union[str] = Field(None,
        description="The direct performer or driver of the action (animate or inanimate). e.g. John wrote a book."
    )


    endTime: Union[str] = Field(None,
        description="The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the end of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    error: 'Thing' = Field(None,
        description="For failed actions, more information on the cause of the failure."
    )


    instrument: 'Thing' = Field(None,
        description="The object that helped the agent perform the action. e.g. John wrote a book with a pen."
    )


    location: Union[str] = Field(None,
        description="The location of for example where the event is happening, an organization is located, or where an action takes place."
    )


    object: 'Thing' = Field(None,
        description="The object upon which the action is carried out, whose state is kept intact or changed. Also known as the semantic roles patient, affected or undergoer (which change their state) or theme (which doesn't). e.g. John read a book."
    )


    participant: Union[str] = Field(None,
        description="Other co-agents that participated in the action indirectly. e.g. John wrote a book with Steve."
    )


    result: 'Thing' = Field(None,
        description="The result produced in the action. e.g. John wrote a book."
    )


    startTime: Union[str] = Field(None,
        description="The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    target: str = Field(None,
        description="Indicates a target EntryPoint for an Action."
    )


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


    potentialAction: 'Action' = Field(None,
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


class TipAction(BaseModel):
    """
    TipAction
    """
    
    recipient: Union[str] = Field(None,
        description="A sub property of participant. The participant who is at the receiving end of the action."
    )


    price: Union[str] = Field(None,
        description="The offer price of a product, or of a price component when attached to PriceSpecification and its subtypes.Usage guidelines:Use the priceCurrency property (with standard formats: ISO 4217 currency format e.g. \"USD\"; Ticker symbol for cryptocurrencies e.g. \"BTC\"; well known names for Local Exchange Tradings Systems (LETS) and other currency types e.g. \"Ithaca HOUR\") instead of including ambiguous symbols such as '$' in the value.Use '.' (Unicode 'FULL STOP' (U+002E)) rather than ',' to indicate a decimal point. Avoid using these symbols as a readability separator.Note that both RDFa and Microdata syntax allow the use of a \"content=\" attribute for publishing simple machine-readable values alongside more human-friendly formatting.Use values from 0123456789 (Unicode 'DIGIT ZERO' (U+0030) to 'DIGIT NINE' (U+0039)) rather than superficially similiar Unicode symbols."
    )


    priceCurrency: str = Field(None,
        description="The currency of the price, or a price component when attached to PriceSpecification and its subtypes.Use standard formats: ISO 4217 currency format e.g. \"USD\"; Ticker symbol for cryptocurrencies e.g. \"BTC\"; well known names for Local Exchange Tradings Systems (LETS) and other currency types e.g. \"Ithaca HOUR\"."
    )


    priceSpecification: str = Field(None,
        description="One or more detailed price specifications, indicating the unit price and delivery or payment charges."
    )


    actionStatus: str = Field(None,
        description="Indicates the current disposition of the Action."
    )


    agent: Union[str] = Field(None,
        description="The direct performer or driver of the action (animate or inanimate). e.g. John wrote a book."
    )


    endTime: Union[str] = Field(None,
        description="The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the end of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    error: 'Thing' = Field(None,
        description="For failed actions, more information on the cause of the failure."
    )


    instrument: 'Thing' = Field(None,
        description="The object that helped the agent perform the action. e.g. John wrote a book with a pen."
    )


    location: Union[str] = Field(None,
        description="The location of for example where the event is happening, an organization is located, or where an action takes place."
    )


    object: 'Thing' = Field(None,
        description="The object upon which the action is carried out, whose state is kept intact or changed. Also known as the semantic roles patient, affected or undergoer (which change their state) or theme (which doesn't). e.g. John read a book."
    )


    participant: Union[str] = Field(None,
        description="Other co-agents that participated in the action indirectly. e.g. John wrote a book with Steve."
    )


    result: 'Thing' = Field(None,
        description="The result produced in the action. e.g. John wrote a book."
    )


    startTime: Union[str] = Field(None,
        description="The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    target: str = Field(None,
        description="Indicates a target EntryPoint for an Action."
    )


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


    potentialAction: 'Action' = Field(None,
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


class TransferAction(BaseModel):
    """
    TransferAction
    """
    
    fromLocation: str = Field(None,
        description="A sub property of location. The original location of the object or the agent before the action."
    )


    toLocation: str = Field(None,
        description="A sub property of location. The final location of the object or the agent after the action."
    )


    actionStatus: str = Field(None,
        description="Indicates the current disposition of the Action."
    )


    agent: Union[str] = Field(None,
        description="The direct performer or driver of the action (animate or inanimate). e.g. John wrote a book."
    )


    endTime: Union[str] = Field(None,
        description="The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the end of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    error: 'Thing' = Field(None,
        description="For failed actions, more information on the cause of the failure."
    )


    instrument: 'Thing' = Field(None,
        description="The object that helped the agent perform the action. e.g. John wrote a book with a pen."
    )


    location: Union[str] = Field(None,
        description="The location of for example where the event is happening, an organization is located, or where an action takes place."
    )


    object: 'Thing' = Field(None,
        description="The object upon which the action is carried out, whose state is kept intact or changed. Also known as the semantic roles patient, affected or undergoer (which change their state) or theme (which doesn't). e.g. John read a book."
    )


    participant: Union[str] = Field(None,
        description="Other co-agents that participated in the action indirectly. e.g. John wrote a book with Steve."
    )


    result: 'Thing' = Field(None,
        description="The result produced in the action. e.g. John wrote a book."
    )


    startTime: Union[str] = Field(None,
        description="The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    target: str = Field(None,
        description="Indicates a target EntryPoint for an Action."
    )


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


    potentialAction: 'Action' = Field(None,
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


class BorrowAction(BaseModel):
    """
    BorrowAction
    """
    
    lender: Union[str] = Field(None,
        description="A sub property of participant. The person that lends the object being borrowed."
    )


    fromLocation: str = Field(None,
        description="A sub property of location. The original location of the object or the agent before the action."
    )


    toLocation: str = Field(None,
        description="A sub property of location. The final location of the object or the agent after the action."
    )


    actionStatus: str = Field(None,
        description="Indicates the current disposition of the Action."
    )


    agent: Union[str] = Field(None,
        description="The direct performer or driver of the action (animate or inanimate). e.g. John wrote a book."
    )


    endTime: Union[str] = Field(None,
        description="The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the end of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    error: 'Thing' = Field(None,
        description="For failed actions, more information on the cause of the failure."
    )


    instrument: 'Thing' = Field(None,
        description="The object that helped the agent perform the action. e.g. John wrote a book with a pen."
    )


    location: Union[str] = Field(None,
        description="The location of for example where the event is happening, an organization is located, or where an action takes place."
    )


    object: 'Thing' = Field(None,
        description="The object upon which the action is carried out, whose state is kept intact or changed. Also known as the semantic roles patient, affected or undergoer (which change their state) or theme (which doesn't). e.g. John read a book."
    )


    participant: Union[str] = Field(None,
        description="Other co-agents that participated in the action indirectly. e.g. John wrote a book with Steve."
    )


    result: 'Thing' = Field(None,
        description="The result produced in the action. e.g. John wrote a book."
    )


    startTime: Union[str] = Field(None,
        description="The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    target: str = Field(None,
        description="Indicates a target EntryPoint for an Action."
    )


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


    potentialAction: 'Action' = Field(None,
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


class DownloadAction(BaseModel):
    """
    DownloadAction
    """
    
    fromLocation: str = Field(None,
        description="A sub property of location. The original location of the object or the agent before the action."
    )


    toLocation: str = Field(None,
        description="A sub property of location. The final location of the object or the agent after the action."
    )


    actionStatus: str = Field(None,
        description="Indicates the current disposition of the Action."
    )


    agent: Union[str] = Field(None,
        description="The direct performer or driver of the action (animate or inanimate). e.g. John wrote a book."
    )


    endTime: Union[str] = Field(None,
        description="The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the end of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    error: 'Thing' = Field(None,
        description="For failed actions, more information on the cause of the failure."
    )


    instrument: 'Thing' = Field(None,
        description="The object that helped the agent perform the action. e.g. John wrote a book with a pen."
    )


    location: Union[str] = Field(None,
        description="The location of for example where the event is happening, an organization is located, or where an action takes place."
    )


    object: 'Thing' = Field(None,
        description="The object upon which the action is carried out, whose state is kept intact or changed. Also known as the semantic roles patient, affected or undergoer (which change their state) or theme (which doesn't). e.g. John read a book."
    )


    participant: Union[str] = Field(None,
        description="Other co-agents that participated in the action indirectly. e.g. John wrote a book with Steve."
    )


    result: 'Thing' = Field(None,
        description="The result produced in the action. e.g. John wrote a book."
    )


    startTime: Union[str] = Field(None,
        description="The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    target: str = Field(None,
        description="Indicates a target EntryPoint for an Action."
    )


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


    potentialAction: 'Action' = Field(None,
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


class GiveAction(BaseModel):
    """
    GiveAction
    """
    
    recipient: Union[str] = Field(None,
        description="A sub property of participant. The participant who is at the receiving end of the action."
    )


    fromLocation: str = Field(None,
        description="A sub property of location. The original location of the object or the agent before the action."
    )


    toLocation: str = Field(None,
        description="A sub property of location. The final location of the object or the agent after the action."
    )


    actionStatus: str = Field(None,
        description="Indicates the current disposition of the Action."
    )


    agent: Union[str] = Field(None,
        description="The direct performer or driver of the action (animate or inanimate). e.g. John wrote a book."
    )


    endTime: Union[str] = Field(None,
        description="The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the end of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    error: 'Thing' = Field(None,
        description="For failed actions, more information on the cause of the failure."
    )


    instrument: 'Thing' = Field(None,
        description="The object that helped the agent perform the action. e.g. John wrote a book with a pen."
    )


    location: Union[str] = Field(None,
        description="The location of for example where the event is happening, an organization is located, or where an action takes place."
    )


    object: 'Thing' = Field(None,
        description="The object upon which the action is carried out, whose state is kept intact or changed. Also known as the semantic roles patient, affected or undergoer (which change their state) or theme (which doesn't). e.g. John read a book."
    )


    participant: Union[str] = Field(None,
        description="Other co-agents that participated in the action indirectly. e.g. John wrote a book with Steve."
    )


    result: 'Thing' = Field(None,
        description="The result produced in the action. e.g. John wrote a book."
    )


    startTime: Union[str] = Field(None,
        description="The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    target: str = Field(None,
        description="Indicates a target EntryPoint for an Action."
    )


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


    potentialAction: 'Action' = Field(None,
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


class LendAction(BaseModel):
    """
    LendAction
    """
    
    borrower: str = Field(None,
        description="A sub property of participant. The person that borrows the object being lent."
    )


    fromLocation: str = Field(None,
        description="A sub property of location. The original location of the object or the agent before the action."
    )


    toLocation: str = Field(None,
        description="A sub property of location. The final location of the object or the agent after the action."
    )


    actionStatus: str = Field(None,
        description="Indicates the current disposition of the Action."
    )


    agent: Union[str] = Field(None,
        description="The direct performer or driver of the action (animate or inanimate). e.g. John wrote a book."
    )


    endTime: Union[str] = Field(None,
        description="The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the end of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    error: 'Thing' = Field(None,
        description="For failed actions, more information on the cause of the failure."
    )


    instrument: 'Thing' = Field(None,
        description="The object that helped the agent perform the action. e.g. John wrote a book with a pen."
    )


    location: Union[str] = Field(None,
        description="The location of for example where the event is happening, an organization is located, or where an action takes place."
    )


    object: 'Thing' = Field(None,
        description="The object upon which the action is carried out, whose state is kept intact or changed. Also known as the semantic roles patient, affected or undergoer (which change their state) or theme (which doesn't). e.g. John read a book."
    )


    participant: Union[str] = Field(None,
        description="Other co-agents that participated in the action indirectly. e.g. John wrote a book with Steve."
    )


    result: 'Thing' = Field(None,
        description="The result produced in the action. e.g. John wrote a book."
    )


    startTime: Union[str] = Field(None,
        description="The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    target: str = Field(None,
        description="Indicates a target EntryPoint for an Action."
    )


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


    potentialAction: 'Action' = Field(None,
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


class MoneyTransfer(BaseModel):
    """
    MoneyTransfer
    """
    
    amount: Union[str] = Field(None,
        description="The amount of money."
    )


    beneficiaryBank: Union[str] = Field(None,
        description="A bank or bankâs branch, financial institution or international financial institution operating the beneficiaryâs bank account or releasing funds for the beneficiary"
    )


    fromLocation: str = Field(None,
        description="A sub property of location. The original location of the object or the agent before the action."
    )


    toLocation: str = Field(None,
        description="A sub property of location. The final location of the object or the agent after the action."
    )


    actionStatus: str = Field(None,
        description="Indicates the current disposition of the Action."
    )


    agent: Union[str] = Field(None,
        description="The direct performer or driver of the action (animate or inanimate). e.g. John wrote a book."
    )


    endTime: Union[str] = Field(None,
        description="The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the end of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    error: 'Thing' = Field(None,
        description="For failed actions, more information on the cause of the failure."
    )


    instrument: 'Thing' = Field(None,
        description="The object that helped the agent perform the action. e.g. John wrote a book with a pen."
    )


    location: Union[str] = Field(None,
        description="The location of for example where the event is happening, an organization is located, or where an action takes place."
    )


    object: 'Thing' = Field(None,
        description="The object upon which the action is carried out, whose state is kept intact or changed. Also known as the semantic roles patient, affected or undergoer (which change their state) or theme (which doesn't). e.g. John read a book."
    )


    participant: Union[str] = Field(None,
        description="Other co-agents that participated in the action indirectly. e.g. John wrote a book with Steve."
    )


    result: 'Thing' = Field(None,
        description="The result produced in the action. e.g. John wrote a book."
    )


    startTime: Union[str] = Field(None,
        description="The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    target: str = Field(None,
        description="Indicates a target EntryPoint for an Action."
    )


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


    potentialAction: 'Action' = Field(None,
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


class ReceiveAction(BaseModel):
    """
    ReceiveAction
    """
    
    deliveryMethod: str = Field(None,
        description="A sub property of instrument. The method of delivery."
    )


    sender: Union[str] = Field(None,
        description="A sub property of participant. The participant who is at the sending end of the action."
    )


    fromLocation: str = Field(None,
        description="A sub property of location. The original location of the object or the agent before the action."
    )


    toLocation: str = Field(None,
        description="A sub property of location. The final location of the object or the agent after the action."
    )


    actionStatus: str = Field(None,
        description="Indicates the current disposition of the Action."
    )


    agent: Union[str] = Field(None,
        description="The direct performer or driver of the action (animate or inanimate). e.g. John wrote a book."
    )


    endTime: Union[str] = Field(None,
        description="The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the end of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    error: 'Thing' = Field(None,
        description="For failed actions, more information on the cause of the failure."
    )


    instrument: 'Thing' = Field(None,
        description="The object that helped the agent perform the action. e.g. John wrote a book with a pen."
    )


    location: Union[str] = Field(None,
        description="The location of for example where the event is happening, an organization is located, or where an action takes place."
    )


    object: 'Thing' = Field(None,
        description="The object upon which the action is carried out, whose state is kept intact or changed. Also known as the semantic roles patient, affected or undergoer (which change their state) or theme (which doesn't). e.g. John read a book."
    )


    participant: Union[str] = Field(None,
        description="Other co-agents that participated in the action indirectly. e.g. John wrote a book with Steve."
    )


    result: 'Thing' = Field(None,
        description="The result produced in the action. e.g. John wrote a book."
    )


    startTime: Union[str] = Field(None,
        description="The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions."
    )


    target: str = Field(None,
        description="Indicates a target EntryPoint for an Action."
    )


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


    potentialAction: 'Action' = Field(None,
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

