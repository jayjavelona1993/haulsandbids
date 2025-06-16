import {lazy} from "react";
import {BrowserRouter as Router, Route, Routes} from "react-router-dom";
import PublicTemplate from "@/pages/Public/PublicTemplate/PublicTemplate.jsx";
const Home = lazy(() => import("@/pages/Public/Home/Home.jsx"));
const SignUp = lazy(() => import("@/pages/Public/SignUp/SignUp.jsx"));
const SignUpCarrier = lazy(() => import("@/pages/Public/SignUp/Carrier/Carrier.jsx"));
const CreateListing = lazy(() => import("@/pages/Public/CreateListing/CreateListing.jsx"));


const PublicRouter = () => {
    return (
    <Routes>
        <Route path="/" element={<PublicTemplate/>}>
            <Route path="" element={<Home/>}/>
            <Route path="sign_up" element={<SignUp/>}/>
            <Route path="sign_up/carrier" element={<SignUpCarrier/>}/>
            <Route path="create_listing" element={<CreateListing/>}/>
        </Route>
    </Routes>);
};

export default PublicRouter;