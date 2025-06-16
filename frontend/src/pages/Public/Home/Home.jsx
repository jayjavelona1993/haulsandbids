import {createContext, useContext, useMemo} from "react";

const HomeContext = createContext(null);
const Home = () => {

    return (
    <HomeContext.Provider value={{}}>

    </HomeContext.Provider>);
};

const useFeaturedHaul = () => {

};

const useHauls = () => {

};

export const useHome = () => useContext(HomeContext);

export default Home;