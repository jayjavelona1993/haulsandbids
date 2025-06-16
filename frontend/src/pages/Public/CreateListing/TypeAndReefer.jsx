import {useCreateListing} from "@/pages/Public/CreateListing/CreateListing.jsx";
import {Button} from "@/components/ui/button.jsx";
import {useMemo} from "react";

const TypeAndReefer = () => {

    const {haul, step} = useCreateListing();
    const ok_to_continue = useMemo(() => {
        return haul.value.type_id != null && haul.value.requires_refrigeration != null;
    }, [haul.value]);

    return (
    <div>
        <div>
            <PickupType/>
            <Reefer/>
        </div>
        {ok_to_continue &&
            (<div className={'mt-7'}>
                <Button>
                    Continue
                    <i className="fa-solid fa-arrow-right ms-2"></i>
                </Button>
            </div>)}

    </div>);

};

const Reefer = () => {

    const {haul} = useCreateListing();

    /*
    provide options for min and max temp, ex
     */

    return (
    <div className={'mt-5'}>
        <div>Does your pickup need refrigeration?</div>
        <div className={'my-1'}>
            <Button
                className={'rounded-r-none bg-gray-100 hover:bg-gray-200 text-black cursor-pointer w-100'}
                onClick={() => haul.setter(prev => ({...prev, requires_refrigeration: true}))}
            >
                <i className="fa-solid fa-snowflake me-2 text-blue-400"></i> Requires Refrigeration
                {haul.value.requires_refrigeration != null && haul.value.requires_refrigeration && <i className="fa-solid fa-check text-green-700 ms-2"></i>}
            </Button>
        </div>
        <div className={'my-1'}>
            <Button
                className={'rounded-l-none bg-gray-100 hover:bg-gray-200 text-black cursor-pointer w-100'}
                onClick={() => haul.setter(prev => ({...prev, requires_refrigeration: false}))}
            >
                <i className="fa-solid fa-leaf text-green-700 me-2"></i> Dry Shipping OK
                {haul.value.requires_refrigeration != null && !haul.value.requires_refrigeration && <i className="fa-solid fa-check text-green-700 ms-2"></i>}
            </Button>
        </div>
    </div>);
};

const PickupType = () => {
    const {haul, haul_types} = useCreateListing();

    const TypeButton = ({index, type}) => {

        const selected = useMemo(() => {
            if(haul.value.type_id == null) return false;

            return haul.value.type_id == type.id;
        }, [haul.value, type]);

        const className = useMemo(() => {
            const classes = ['border-black outline-1 hover:bg-blue-500 hover:text-white cursor-pointer'];

            if(index == 0) classes.push('rounded-r-none');
            if(index == 1) classes.push('rounded-none');
            if(index == 2) classes.push('rounded-l-none');
            if(!selected) classes.push('bg-gray-100 text-black');
            if(selected) classes.push('bg-blue-500 text-white');

            return classes.join(' ');
        }, [type, index, haul.value, selected]);

        return (
        <Button className={className} onClick={() => haul.setter(prev => ({...prev, type_id: type.id}))}>
            {type.name}
        </Button>);
    };

    return (
    <div>
        <div>
            <div>What kind of Pickup?</div>
            <div className={'flex'}>
                {haul_types.map((type, index) => <TypeButton key={index} index={index} type={type}/>)}
            </div>

        </div>
    </div>);
};

export default TypeAndReefer;