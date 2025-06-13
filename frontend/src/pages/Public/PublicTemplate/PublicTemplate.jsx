import {Outlet} from "react-router-dom";
import NavBar from "./NavBar/NavBar.jsx";

const PublicTemplate = () => {
    return (
    <>
        <NavBar/>
        <Outlet />
    </>);
};

export default PublicTemplate;
