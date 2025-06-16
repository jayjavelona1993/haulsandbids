import {useState} from "react";

const useSimpleState = init_value => {
    const [value, setter] = useState(init_value);
    return {value, setter};
};

export default useSimpleState;