import {useEffect, useRef, useCallback} from "react";
import useSimpleState from "@/custom_js/useSimpleState.js";
import {Input} from "@/components/ui/input.jsx";
import {Button} from "@/components/ui/button.jsx";
import axios from "axios";
import GOOGLE_MAPS_API_KEY from "@/GOOGLE_MAPS_API_KEY.js";
import {Card} from "@/components/ui/card.jsx";
import {useCreateListing} from "@/pages/Public/CreateListing/CreateListing.jsx";

const Where = () => {

    const search_string = useSimpleState('');

    const [results, search, search_term] = useSearch(search_string.value);

    const input_ref = useRef(null);

    useKeyEnter(input_ref, search);
    useFocusOnInput(input_ref);

    return (
    <div className={'text-center mt-7 px-20'}>
        <div className={'font-bold text-lg'}>Where are we picking up from?</div>
        <div className={'mt-5 flex justify-center'}>
            <div className={'w-md flex'}>
                <Input
                    value={search_string.value} placeholder={'Enter Zipcode (ex. 22201)'}
                    onChange={e => search_string.setter(e.target.value)}
                    className={'rounded-r-none h-10'} ref={input_ref}
                />
                <Button className={'rounded-l-none h-10'} onClick={search}>
                    <i className="fa-solid fa-magnifying-glass me-2"></i> Search
                </Button>
            </div>
        </div>
        <div className={'flex justify-center'}>
            {results && results.length == 0 && <NoResults search_string_value={search_term} />}
            {results && results.length > 0 && <Results results={results} search_string_value={search_term} />}
        </div>
    </div>);
};

const useFocusOnInput = (input_ref) => {
    useEffect(() => {
        if(!input_ref.current) return;
        input_ref.current.focus();
    }, [input_ref]);
};

const useKeyEnter = (input_ref, search) => {
    useEffect(() => {

        if(!input_ref.current) return;
        const listener = e => {
            if(e.key == 'Enter') search();
        };
        input_ref.current.addEventListener('keydown', listener);
        return () => {
            if(!input_ref.current) return;
            input_ref.current.removeEventListener('keydown', listener);
        };
    }, [input_ref, search]);
};

const Results = ({results, search_string_value}) => {

    return (
    <div className={'mt-5 w-md'}>
        <div>
            We found {results.length} {results.length == 1 ? 'result' : 'results'} for your "{search_string_value}".
        </div>
        <div className={'mt-3'}>
            {results.map((result, i) => <Result key={i} result={result}/>)}
        </div>
    </div>);
};

const Result = ({result}) => {

    const {haul, step} = useCreateListing();

    const confirm_address = () => {
        haul.setter(prev => ({...prev, geocoded_address: result}));
        step.setter('type_and_reefer');
    };

    return (
    <div className={'my-1'}>
        <Card>
            <div className={'flex px-5'}>
                <div className={'my-auto'}>{result.formatted_address}</div>
                <div className={'ms-auto'}>
                    <Button onClick={confirm_address}>
                        Confirm
                        <i className="fa-solid fa-arrow-right ms-2"></i>
                    </Button>
                </div>
            </div>
        </Card>
    </div>);
}

const NoResults = ({search_string_value}) => {
    return (
    <div className={'text-center mt-5'}>
        <div className={'text-lg'}>
            No results found for "{search_string_value}".
        </div>
    </div>);
};

const useSearch = (search_string_value) => {

    const results = useSimpleState(null);
    const search_term = useSimpleState(null);


    const search = useCallback(async () => {
        const response = await axios.get(`https://maps.googleapis.com/maps/api/geocode/json?address=${search_string_value}&key=${GOOGLE_MAPS_API_KEY}`);
        results.setter(response.data.results);
        search_term.setter(search_string_value);
    }, [search_string_value]);

    return [results.value, search, search_term.value];
};

export default Where;