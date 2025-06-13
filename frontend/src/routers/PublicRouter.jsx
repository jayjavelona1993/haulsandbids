import {BrowserRouter as Router, Route, Routes} from "react-router-dom";
import PublicTemplate from "@/pages/Public/PublicTemplate/PublicTemplate.jsx";

const PublicRouter = () => {
    return (
    <Router>
        <Routes>
            <Route path="/" element={<PublicTemplate/>}>

            </Route>
        </Routes>
    </Router>);
};

export default PublicRouter;