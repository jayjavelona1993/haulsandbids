import graphene
from api.graphql.queries.common import *
from api.graphql.mutations.common import Mutation

class Query(
    UserQuery,
    ProfileQuery,
    UnitOfMeasureQuery,
    StateQuery,
    AddressQuery,
    ClientQuery,
    CarrierQuery,
    DayOfWeekQuery,
    ContactTypeQuery,
    ContactQuery,
    ContactClientQuery,
    CarrierContactQuery,
    DockDayQuery,
    SiteQuery,
    HaulTypeQuery,
    HaulStatusQuery,
    HaulQuery,
    HaulDestinationQuery,
    SkuQuery,
    HaulItemQuery,
    BidQuery,
    BidItemQuery,
    graphene.ObjectType
):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation, auto_camelcase=False)
