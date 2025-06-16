import GOOGLE_MAPS_API_KEY from "@/GOOGLE_MAPS_API_KEY.js";
import {APIProvider} from "@vis.gl/react-google-maps";

const GoogleMapsProvider = ({children}) => {
    return (
    <APIProvider googleMapsApiKey={GOOGLE_MAPS_API_KEY}>
        {children}
    </APIProvider>);
};

export default GoogleMapsProvider;