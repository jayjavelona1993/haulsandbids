import {useCreateListing} from "@/pages/Public/CreateListing/CreateListing.jsx";
import TypeAndReefer from "@/pages/Public/CreateListing/TypeAndReefer.jsx";
import {useMemo} from "react";

const SidePanelAndStep = () => {
    const {step, haul} = useCreateListing();

    return (
    <div className={'grid grid-cols-3 gap-3 w-xl mt-5'}>
        <div className={'col-span-1 border-r-2'}>
            <KnownFact description={'Pickup'} value={haul.value.geocoded_address.formatted_address}/>
            <PickupType/>
            <Reefer/>
        </div>
        <div className={'col-span-2'}>
            {step.value == 'type_and_reefer' && <TypeAndReefer/>}
        </div>
    </div>);
};

const Reefer = () => {
    const {haul} = useCreateListing();

    const value = useMemo(() => {
        if(haul.value.requires_refrigeration) return 'Requires Refrigeration';
        return 'Dry Shipping OK';
    }, [haul.value]);

    if(haul.value.requires_refrigeration == null) return;

    return <KnownFact description={'Requires Refrigeration?'} value={value} />
};

const PickupType = () => {
    const {haul, haul_types} = useCreateListing();

    const pickup_type = useMemo(() => {
        if(haul.value.type_id == null) return null;
        return haul_types.find(type => type.id == haul.value.type_id).name;
    }, [haul.value, haul_types]);

    if(haul.value.type_id == null) return;
    return <KnownFact description={'Pickup Type'} value={pickup_type}/>;
};

const KnownFact = ({description, value}) => {
    return (
    <div className={'text-gray-500 my-2'}>
        <small>{description}</small>
        <div>{value}</div>
    </div>);
};

export default SidePanelAndStep;