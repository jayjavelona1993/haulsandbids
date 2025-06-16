from graphene_django import DjangoObjectType
from webapp.models import *

class UserTYPE(DjangoObjectType):
    class Meta:
        model = User
        fields = '__all__'

class ProfileTYPE(DjangoObjectType):
    class Meta:
        model = Profile
        fields = '__all__'

class UnitOfMeasureTYPE(DjangoObjectType):
    class Meta:
        model = UnitOfMeasure
        fields = '__all__'

class StateTYPE(DjangoObjectType):
    class Meta:
        model = State
        fields = '__all__'

class AddressTYPE(DjangoObjectType):
    class Meta:
        model = Address
        fields = '__all__'

class ClientTYPE(DjangoObjectType):
    class Meta:
        model = Client
        fields = '__all__'

class CarrierTYPE(DjangoObjectType):
    class Meta:
        model = Carrier
        fields = '__all__'

class DayOfWeekTYPE(DjangoObjectType):
    class Meta:
        model = DayOfWeek
        fields = '__all__'

class ContactTypeTYPE(DjangoObjectType):
    class Meta:
        model = ContactType
        fields = '__all__'

class ContactTYPE(DjangoObjectType):
    class Meta:
        model = Contact
        fields = '__all__'

class ContactClientTYPE(DjangoObjectType):
    class Meta:
        model = ContactClient
        fields = '__all__'

class CarrierContactTYPE(DjangoObjectType):
    class Meta:
        model = CarrierContact
        fields = '__all__'

class DockDayTYPE(DjangoObjectType):
    class Meta:
        model = DockDay
        fields = '__all__'

class SiteTYPE(DjangoObjectType):
    class Meta:
        model = Site
        fields = '__all__'

class HaulTypeTYPE(DjangoObjectType):
    class Meta:
        model = HaulType
        fields = '__all__'

class HaulStatusTYPE(DjangoObjectType):
    class Meta:
        model = HaulStatus
        fields = '__all__'

class HaulTYPE(DjangoObjectType):
    class Meta:
        model = Haul
        fields = '__all__'

class HaulDestinationTYPE(DjangoObjectType):
    class Meta:
        model = HaulDestination
        fields = '__all__'

class SkuTYPE(DjangoObjectType):
    class Meta:
        model = Sku
        fields = '__all__'

class HaulItemTYPE(DjangoObjectType):
    class Meta:
        model = HaulItem
        fields = '__all__'

class BidTYPE(DjangoObjectType):
    class Meta:
        model = Bid
        fields = '__all__'

class BidItemTYPE(DjangoObjectType):
    class Meta:
        model = BidItem
        fields = '__all__'
