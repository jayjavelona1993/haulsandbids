import graphene
from webapp.models import *
from api.graphql.types.common import *

class UserQuery(graphene.ObjectType):
    users = graphene.List(UserTYPE,
      limit=graphene.Int(), email=graphene.String()
    )
    user = graphene.Field(UserTYPE, id=graphene.ID(required=True))

    def resolve_users(root, info, limit=100, email=None):
        queryset = User.objects.all()

        if email:
            queryset = queryset.filter(email=email)

        return queryset[:limit]

    def resolve_user(root, info, id):
        return User.objects.get(pk=id)

class ProfileQuery(graphene.ObjectType):
    profiles = graphene.List(ProfileTYPE, limit=graphene.Int())
    profile = graphene.Field(ProfileTYPE, id=graphene.ID(required=True))

    def resolve_profiles(root, info, limit=100):
        return Profile.objects.all()[:limit]

    def resolve_profile(root, info, id):
        return Profile.objects.get(pk=id)

class UnitOfMeasureQuery(graphene.ObjectType):
    unitofmeasures = graphene.List(UnitOfMeasureTYPE, limit=graphene.Int())
    unitofmeasure = graphene.Field(UnitOfMeasureTYPE, id=graphene.ID(required=True))

    def resolve_units(root, info, limit=100):
        return UnitOfMeasure.objects.all()[:limit]

    def resolve_unit(root, info, id):
        return UnitOfMeasure.objects.get(pk=id)

class StateQuery(graphene.ObjectType):
    states = graphene.List(StateTYPE, limit=graphene.Int())
    state = graphene.Field(StateTYPE, id=graphene.ID(required=True))

    def resolve_states(root, info, limit=100):
        return State.objects.all()[:limit]

    def resolve_state(root, info, id):
        return State.objects.get(pk=id)

class AddressQuery(graphene.ObjectType):
    addresses = graphene.List(AddressTYPE, limit=graphene.Int())
    address = graphene.Field(AddressTYPE, id=graphene.ID(required=True))

    def resolve_addresses(root, info, limit=100):
        return Address.objects.all()[:limit]

    def resolve_address(root, info, id):
        return Address.objects.get(pk=id)

class ClientQuery(graphene.ObjectType):
    clients = graphene.List(ClientTYPE, limit=graphene.Int())
    client = graphene.Field(ClientTYPE, id=graphene.ID(required=True))

    def resolve_clients(root, info, limit=100):
        return Client.objects.all()[:limit]

    def resolve_client(root, info, id):
        return Client.objects.get(pk=id)

class CarrierQuery(graphene.ObjectType):
    carriers = graphene.List(CarrierTYPE, limit=graphene.Int())
    carrier = graphene.Field(CarrierTYPE, id=graphene.ID(required=True))

    def resolve_carriers(root, info, limit=100):
        return Carrier.objects.all()[:limit]

    def resolve_carrier(root, info, id):
        return Carrier.objects.get(pk=id)

class DayOfWeekQuery(graphene.ObjectType):
    days = graphene.List(DayOfWeekTYPE, limit=graphene.Int())
    day = graphene.Field(DayOfWeekTYPE, id=graphene.ID(required=True))

    def resolve_days(root, info, limit=100):
        return DayOfWeek.objects.all()[:limit]

    def resolve_day(root, info, id):
        return DayOfWeek.objects.get(pk=id)

class ContactTypeQuery(graphene.ObjectType):
    contact_types = graphene.List(ContactTypeTYPE, limit=graphene.Int())
    contact_type = graphene.Field(ContactTypeTYPE, id=graphene.ID(required=True))

    def resolve_contact_types(root, info, limit=100):
        return ContactType.objects.all()[:limit]

    def resolve_contact_type(root, info, id):
        return ContactType.objects.get(pk=id)

class ContactQuery(graphene.ObjectType):
    contacts = graphene.List(ContactTYPE, limit=graphene.Int())
    contact = graphene.Field(ContactTYPE, id=graphene.ID(required=True))

    def resolve_contacts(root, info, limit=100):
        return Contact.objects.all()[:limit]

    def resolve_contact(root, info, id):
        return Contact.objects.get(pk=id)

class ContactClientQuery(graphene.ObjectType):
    contact_clients = graphene.List(ContactClientTYPE, limit=graphene.Int())
    contact_client = graphene.Field(ContactClientTYPE, id=graphene.ID(required=True))

    def resolve_contact_clients(root, info, limit=100):
        return ContactClient.objects.all()[:limit]

    def resolve_contact_client(root, info, id):
        return ContactClient.objects.get(pk=id)

class CarrierContactQuery(graphene.ObjectType):
    carrier_contacts = graphene.List(CarrierContactTYPE, limit=graphene.Int())
    carrier_contact = graphene.Field(CarrierContactTYPE, id=graphene.ID(required=True))

    def resolve_carrier_contacts(root, info, limit=100):
        return CarrierContact.objects.all()[:limit]

    def resolve_carrier_contact(root, info, id):
        return CarrierContact.objects.get(pk=id)

class DockDayQuery(graphene.ObjectType):
    dock_days = graphene.List(DockDayTYPE, limit=graphene.Int())
    dock_day = graphene.Field(DockDayTYPE, id=graphene.ID(required=True))

    def resolve_dock_days(root, info, limit=100):
        return DockDay.objects.all()[:limit]

    def resolve_dock_day(root, info, id):
        return DockDay.objects.get(pk=id)

class SiteQuery(graphene.ObjectType):
    sites = graphene.List(SiteTYPE, limit=graphene.Int())
    site = graphene.Field(SiteTYPE, id=graphene.ID(required=True))

    def resolve_sites(root, info, limit=100):
        return Site.objects.all()[:limit]

    def resolve_site(root, info, id):
        return Site.objects.get(pk=id)

class HaulTypeQuery(graphene.ObjectType):
    haul_types = graphene.List(HaulTypeTYPE, limit=graphene.Int())
    haul_type = graphene.Field(HaulTypeTYPE, id=graphene.ID(required=True))

    def resolve_haul_types(root, info, limit=100):
        return HaulType.objects.all()[:limit]

    def resolve_haul_type(root, info, id):
        return HaulType.objects.get(pk=id)

class HaulStatusQuery(graphene.ObjectType):
    haul_statuses = graphene.List(HaulStatusTYPE, limit=graphene.Int())
    haul_status = graphene.Field(HaulStatusTYPE, id=graphene.ID(required=True))

    def resolve_haul_statuses(root, info, limit=100):
        return HaulStatus.objects.all()[:limit]

    def resolve_haul_status(root, info, id):
        return HaulStatus.objects.get(pk=id)

class HaulQuery(graphene.ObjectType):
    hauls = graphene.List(HaulTYPE, limit=graphene.Int())
    haul = graphene.Field(HaulTYPE, id=graphene.ID(required=True))

    def resolve_hauls(root, info, limit=100):
        return Haul.objects.all()[:limit]

    def resolve_haul(root, info, id):
        return Haul.objects.get(pk=id)

class HaulDestinationQuery(graphene.ObjectType):
    haul_destinations = graphene.List(HaulDestinationTYPE, limit=graphene.Int())
    haul_destination = graphene.Field(HaulDestinationTYPE, id=graphene.ID(required=True))

    def resolve_haul_destinations(root, info, limit=100):
        return HaulDestination.objects.all()[:limit]

    def resolve_haul_destination(root, info, id):
        return HaulDestination.objects.get(pk=id)

class SkuQuery(graphene.ObjectType):
    skus = graphene.List(SkuTYPE, limit=graphene.Int())
    sku = graphene.Field(SkuTYPE, id=graphene.ID(required=True))

    def resolve_skus(root, info, limit=100):
        return Sku.objects.all()[:limit]

    def resolve_sku(root, info, id):
        return Sku.objects.get(pk=id)

class HaulItemQuery(graphene.ObjectType):
    haul_items = graphene.List(HaulItemTYPE, limit=graphene.Int())
    haul_item = graphene.Field(HaulItemTYPE, id=graphene.ID(required=True))

    def resolve_haul_items(root, info, limit=100):
        return HaulItem.objects.all()[:limit]

    def resolve_haul_item(root, info, id):
        return HaulItem.objects.get(pk=id)

class BidQuery(graphene.ObjectType):
    bids = graphene.List(BidTYPE, limit=graphene.Int())
    bid = graphene.Field(BidTYPE, id=graphene.ID(required=True))

    def resolve_bids(root, info, limit=100):
        return Bid.objects.all()[:limit]

    def resolve_bid(root, info, id):
        return Bid.objects.get(pk=id)

class BidItemQuery(graphene.ObjectType):
    bid_items = graphene.List(BidItemTYPE, limit=graphene.Int())
    bid_item = graphene.Field(BidItemTYPE, id=graphene.ID(required=True))

    def resolve_bid_items(root, info, limit=100):
        return BidItem.objects.all()[:limit]

    def resolve_bid_item(root, info, id):
        return BidItem.objects.get(pk=id)
