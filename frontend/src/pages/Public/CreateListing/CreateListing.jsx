import {createContext, useContext} from "react";
import {Card} from "@/components/ui/card.jsx";
import useSimpleState from "@/custom_js/useSimpleState.js";
import {gql, useQuery} from "@apollo/client";
import Where from "./Where.jsx";
import SidePanelAndStep from "@/pages/Public/CreateListing/SidePanelAndStep.jsx";

const CreateListingContext = createContext(null);
const CreateListing = () => {

    const haul = useSimpleState(default_haul);
    const step = useSimpleState('where');
    const haul_types = useHaulTypes();

    return (
    <CreateListingContext.Provider value={{
        haul, haul_types, step
    }}>

        <div className={'container mx-auto h-full mt-20'}>
            <Card>
                <div className={'flex flex-col justify-center items-center m-5'}>
                    <div className={'text-center text-xl font-bold'}>Tell us about your pickup</div>
                    {step.value == 'where' && <Where/>}
                    {step.value != 'where' && <SidePanelAndStep/>}
                </div>
            </Card>
        </div>

    </CreateListingContext.Provider>);
};

const useHaulTypes = () => {
    const GET_HAUL_TYPES = gql(`
    query MyQuery {
      haul_types{id, name}
    }`);

    const {loading, data} = useQuery(GET_HAUL_TYPES);
    if(loading) return [];
    return data.haul_types;

};

const default_haul = {
    pickup_zipcode: '', listing_pickup_name: '',
    blind_bidding: true, type_id: null, requires_refrigeration: null,
};

export const useCreateListing = () => useContext(CreateListingContext);

export default CreateListing;