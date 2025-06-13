import {createContext, useContext} from "react";

const HomeContext = createContext(null);
const Home = () => {

    return (
    <HomeContext.Provider value={{}}>

    </HomeContext.Provider>);
};

export const useHome = () => useContext(HomeContext);

export default Home;