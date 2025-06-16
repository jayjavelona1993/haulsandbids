import graphene
from webapp.models import *
from api.graphql.types.common import *

class CreateUser(graphene.Mutation):
    class Arguments:
        email = graphene.String(required=True)
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)
        phone = graphene.String(required=False)
        #password = graphene.String(required=True)

    user = graphene.Field(UserTYPE)

    def mutate(self, info, email, first_name, last_name, phone):
        instance = User.objects.create(email=email, first_name=first_name, last_name=last_name, phone=phone)
        return CreateUser(user=instance)

class CreateProfile(graphene.Mutation):
    class Arguments:
        user_id = graphene.ID(required=True)

    profile = graphene.Field(ProfileTYPE)

    def mutate(self, info, user_id):
        instance = Profile.objects.create(user_id=user_id)
        return CreateProfile(profile=instance)

class CreateUnitOfMeasure(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        abbreviation = graphene.String(required=True)
        metric = graphene.Boolean(required=True)

    unitOfMeasure = graphene.Field(UnitOfMeasureTYPE)

    def mutate(self, info, name, abbreviation, metric):
        instance = UnitOfMeasure.objects.create(name=name, abbreviation=abbreviation, metric=metric)
        return CreateUnitOfMeasure(unitOfMeasure=instance)

class CreateState(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        abbreviation = graphene.String(required=True)

    state = graphene.Field(StateTYPE)

    def mutate(self, info, name, abbreviation):
        instance = State.objects.create(name=name, abbreviation=abbreviation)
        return CreateState(state=instance)

class CreateAddress(graphene.Mutation):
    class Arguments:
        line_1 = graphene.String(required=True)
        city = graphene.String(required=True)
        postal_code = graphene.String(required=True)
        state_id = graphene.ID(required=True)

    address = graphene.Field(AddressTYPE)

    def mutate(self, info, line_1, city, postal_code, state_id):
        instance = Address.objects.create(line_1=line_1, city=city, postal_code=postal_code, state_id=state_id)
        return CreateAddress(address=instance)

class CreateClient(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        address_id = graphene.ID(required=True)

    client = graphene.Field(ClientTYPE)

    def mutate(self, info, name, address_id):
        instance = Client.objects.create(name=name, address_id=address_id)
        return CreateClient(client=instance)

class CreateCarrier(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        address_id = graphene.ID(required=False)

    carrier = graphene.Field(CarrierTYPE)

    def mutate(self, info, name, address_id=None):
        instance = Carrier.objects.create(name=name, address_id=address_id)
        return CreateCarrier(carrier=instance)

class CreateDayOfWeek(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        abbreviation = graphene.String(required=True)
        python_day_of_week = graphene.Int(required=True)

    dayOfWeek = graphene.Field(DayOfWeekTYPE)

    def mutate(self, info, name, abbreviation, python_day_of_week):
        instance = DayOfWeek.objects.create(name=name, abbreviation=abbreviation, python_day_of_week=python_day_of_week)
        return CreateDayOfWeek(dayOfWeek=instance)

class CreateContactType(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)

    contactType = graphene.Field(ContactTypeTYPE)

    def mutate(self, info, name):
        instance = ContactType.objects.create(name=name)
        return CreateContactType(contactType=instance)

class CreateContact(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        phone = graphene.String(required=True)
        email = graphene.String(required=True)
        user_id = graphene.ID(required=True)

    contact = graphene.Field(ContactTYPE)

    def mutate(self, info, name, phone, email, user_id):
        instance = Contact.objects.create(name=name, phone=phone, email=email, user_id=user_id)
        return CreateContact(contact=instance)

class CreateContactClient(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        phone = graphene.String(required=True)
        email = graphene.String(required=True)
        user_id = graphene.ID(required=True)
        client_id = graphene.ID(required=True)
        contact_type_id = graphene.ID(required=True)

    contactClient = graphene.Field(ContactClientTYPE)

    def mutate(self, info, name, phone, email, user_id, client_id, contact_type_id):
        instance = ContactClient.objects.create(name=name, phone=phone, email=email, user_id=user_id, client_id=client_id, contact_type_id=contact_type_id)
        return CreateContactClient(contactClient=instance)

class CreateCarrierContact(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        phone = graphene.String(required=False)
        email = graphene.String(required=False)
        user_id = graphene.ID(required=False)
        carrier_id = graphene.ID(required=True)

    carrierContact = graphene.Field(CarrierContactTYPE)

    def mutate(self, info, name, phone, email, user_id, carrier_id):
        instance = CarrierContact.objects.create(name=name, phone=phone, email=email, user_id=user_id, carrier_id=carrier_id)
        return CreateCarrierContact(carrierContact=instance)

class CreateDockDay(graphene.Mutation):
    class Arguments:
        day_id = graphene.ID(required=True)
        start_time = graphene.Time(required=True)
        end_time = graphene.Time(required=True)
        note = graphene.String(required=False)

    dockDay = graphene.Field(DockDayTYPE)

    def mutate(self, info, day_id, start_time, end_time, note):
        instance = DockDay.objects.create(day_id=day_id, start_time=start_time, end_time=end_time, note=note)
        return CreateDockDay(dockDay=instance)

class CreateSite(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        address_id = graphene.ID(required=True)

    site = graphene.Field(SiteTYPE)

    def mutate(self, info, name, address_id):
        instance = Site.objects.create(name=name, address_id=address_id)
        return CreateSite(site=instance)

class CreateHaulType(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)

    haulType = graphene.Field(HaulTypeTYPE)

    def mutate(self, info, name):
        instance = HaulType.objects.create(name=name)
        return CreateHaulType(haulType=instance)

class CreateHaulStatus(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)

    haulStatus = graphene.Field(HaulStatusTYPE)

    def mutate(self, info, name):
        instance = HaulStatus.objects.create(name=name)
        return CreateHaulStatus(haulStatus=instance)

class CreateHaul(graphene.Mutation):
    class Arguments:
        type_id = graphene.ID(required=True)
        client_id = graphene.ID(required=True)
        pickup_id = graphene.ID(required=True)
        status_id = graphene.ID(required=True)

    haul = graphene.Field(HaulTYPE)

    def mutate(self, info, type_id, client_id, pickup_id, status_id):
        instance = Haul.objects.create(type_id=type_id, client_id=client_id, pickup_id=pickup_id, status_id=status_id)
        return CreateHaul(haul=instance)

class CreateHaulDestination(graphene.Mutation):
    class Arguments:
        haul_id = graphene.ID(required=True)
        destination_id = graphene.ID(required=True)
        price = graphene.Decimal(required=True)

    haulDestination = graphene.Field(HaulDestinationTYPE)

    def mutate(self, info, haul_id, destination_id, price):
        instance = HaulDestination.objects.create(haul_id=haul_id, destination_id=destination_id, price=price)
        return CreateHaulDestination(haulDestination=instance)

class CreateSku(graphene.Mutation):
    class Arguments:
        sku = graphene.String(required=True)
        description = graphene.String(required=True)

    sku = graphene.Field(SkuTYPE)

    def mutate(self, info, sku, description):
        instance = Sku.objects.create(sku=sku, description=description)
        return CreateSku(sku=instance)

class CreateHaulItem(graphene.Mutation):
    class Arguments:
        destination_id = graphene.ID(required=True)
        description = graphene.String(required=True)
        dimensions_uom_id = graphene.ID(required=True)
        mass_uom_id = graphene.ID(required=True)

    haulItem = graphene.Field(HaulItemTYPE)

    def mutate(self, info, destination_id, description, dimensions_uom_id, mass_uom_id):
        instance = HaulItem.objects.create(destination_id=destination_id, description=description, dimensions_uom_id=dimensions_uom_id, mass_uom_id=mass_uom_id)
        return CreateHaulItem(haulItem=instance)

class CreateBid(graphene.Mutation):
    class Arguments:
        haul_id = graphene.ID(required=True)
        contact_id = graphene.ID(required=True)
        total = graphene.Decimal(required=True)

    bid = graphene.Field(BidTYPE)

    def mutate(self, info, haul_id, contact_id, total):
        instance = Bid.objects.create(haul_id=haul_id, contact_id=contact_id, total=total)
        return CreateBid(bid=instance)

class CreateBidItem(graphene.Mutation):
    class Arguments:
        bid_id = graphene.ID(required=True)
        item_id = graphene.ID(required=True)
        amount = graphene.Decimal(required=True)

    bidItem = graphene.Field(BidItemTYPE)

    def mutate(self, info, bid_id, item_id, amount):
        instance = BidItem.objects.create(bid_id=bid_id, item_id=item_id, amount=amount)
        return CreateBidItem(bidItem=instance)

class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    create_profile = CreateProfile.Field()
    create_unitofmeasure = CreateUnitOfMeasure.Field()
    create_state = CreateState.Field()
    create_address = CreateAddress.Field()
    create_client = CreateClient.Field()
    create_carrier = CreateCarrier.Field()
    create_dayofweek = CreateDayOfWeek.Field()
    create_contacttype = CreateContactType.Field()
    create_contact = CreateContact.Field()
    create_contactclient = CreateContactClient.Field()
    create_carriercontact = CreateCarrierContact.Field()
    create_dockday = CreateDockDay.Field()
    create_site = CreateSite.Field()
    create_haultype = CreateHaulType.Field()
    create_haulstatus = CreateHaulStatus.Field()
    create_haul = CreateHaul.Field()
    create_hauldestination = CreateHaulDestination.Field()
    create_sku = CreateSku.Field()
    create_haulitem = CreateHaulItem.Field()
    create_bid = CreateBid.Field()
    create_biditem = CreateBidItem.Field()