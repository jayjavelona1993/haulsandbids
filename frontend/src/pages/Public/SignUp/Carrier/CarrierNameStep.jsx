import {useMemo} from "react";
import {Button} from "@/components/ui/button.jsx";
import {Input} from "@/components/ui/input.jsx";
import {useCarrier} from "@/pages/Public/SignUp/Carrier/Carrier.jsx";

const CarrierNameStep = () => {

    const {carrier, step} = useCarrier();

    const disabled = useMemo(() => {
        return carrier.value.name.length < 3;
    }, [carrier.value]);

    const next_step = () => step.setter('user');

    return (
    <div>
        <div>Carrier/Business Name</div>
        <Input
            value={carrier.value.name}
            onChange={e => carrier.setter(prev => ({...prev, name: e.target.value}))}
        />
        <div className={'mt-7'}>
            <Button
                className={'w-full'} disabled={disabled} onClick={next_step}
            >
                Continue
                <i className="fa-solid fa-arrow-right ms-2"></i>
            </Button>
        </div>
    </div>);
};

export default CarrierNameStep;