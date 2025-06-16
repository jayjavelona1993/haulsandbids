import PublicRouter from "@/routers/PublicRouter.jsx";
import {BrowserRouter as Router} from "react-router-dom";
import CarrierRouter from "@/routers/CarrierRouter.jsx";

const App = () =>  {
    return (
    <Router>
        <PublicRouter/>
    </Router>);
};

export default App
