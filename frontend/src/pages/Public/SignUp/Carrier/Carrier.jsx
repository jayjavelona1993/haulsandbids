import {createContext, useContext} from "react";
import {Card} from "@/components/ui/card.jsx";
import useSimpleState from "@/custom_js/useSimpleState.js";
import CarrierNameStep from "./CarrierNameStep.jsx";
import User from "./User.jsx";

const CarrierContext = createContext(null);

const STEPS = ['carrier_name', 'user'];
const Carrier = () => {

    const carrier = useSimpleState({name: ''});
    const user = useSimpleState({email: '', first_name: '', last_name: '', phone: ''});
    const step = useSimpleState('carrier_name');

    return (
    <CarrierContext.Provider value={{
        carrier, user, step
    }}>
        <div className={'container mx-auto h-full flex justify-center items-center mt-20'}>
            <Card className={'my-auto'}>
                 <div className={'flex flex-col m-5'}>
                     <div className={'text-center mb-3 text-lg font-bold'}>Carrier Sign Up</div>
                     {step.value == 'carrier_name' && <CarrierNameStep/>}
                     {step.value == 'user' && <User/>}
                 </div>
            </Card>
        </div>
    </CarrierContext.Provider>);
};

export const useCarrier = () => useContext(CarrierContext);

/*
query MyQuery {
  carrier(id: "") {
    name
  }
  carrier_contact(id: "") {
    name
    email
    phone
    user {
      email
      first_name
      last_name
      phone
    }
  }
}
 */

export default Carrier;