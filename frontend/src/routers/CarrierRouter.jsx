import {Routes, Route} from "react-router-dom";
import CarrierTemplate from "@/pages/CarrierPortal/CarrierPortalTemplate/CarrierPortalTemplate.jsx";

const CarrierRouter = () => {
    return (
    <Routes>
        <Route path="/carrier/" element={<CarrierTemplate/>}>

        </Route>
    </Routes>);
};

export default CarrierRouter;