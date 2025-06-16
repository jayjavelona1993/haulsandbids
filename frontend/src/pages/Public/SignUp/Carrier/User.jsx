import {Input} from "@/components/ui/input.jsx";
import {Button} from "@/components/ui/button.jsx";
import {useCarrier} from "@/pages/Public/SignUp/Carrier/Carrier.jsx";
import {useApolloClient, useMutation, gql} from "@apollo/client";
import {toast, Toaster} from "sonner";

const User = () => {

    const {carrier, step, user} = useCarrier();

    const client = useApolloClient();

    const go_back = () => step.setter('carrier_name');

    const save = async () => {
        //create the user
        const CREATE_USER = gql(`
        mutation {
            create_user(
                email: "${user.value.email}",
                first_name: "${user.value.first_name}",
                last_name: "${user.value.last_name}",
                phone: "${user.value.phone}"
            ) {
                user { id }
            }
        } `);

        const user_response = await client.mutate({mutation: CREATE_USER});
        const user_id = user_response.data.create_user.user.id;

        const CREATE_CARRIER = gql(`
        mutation {
          create_carrier(name: "${carrier.value.name}") {
            carrier { id }
          }
        } `);

        const carrier_response = await client.mutate({mutation: CREATE_CARRIER});
        const carrier_id = carrier_response.data.create_carrier.carrier.id;

        const CREATE_CONTACT = gql(`
        mutation {
          create_carriercontact(
            carrier_id: "${carrier_id}"
            name: "${user.value.first_name} ${user.value.last_name}"
            email: "${user.value.email}"
            phone: "${user.value.phone}"
            user_id: "${user_id}"
          ) {
            carrierContact {
              id
            }
          }
        }`);


        console.log('CREATE_CONTACT',CREATE_CONTACT);

        await client.mutate({mutation: CREATE_CONTACT});
        alert("User created successfully.");

    };

    const check_requirements = async () => {

        const blanks = [
            user.value.first_name, user.value.last_name, user.value.email, user.value.phone
        ].filter(e => e.trim().length == 0);

        if(blanks.length > 0) {
            toast("Please fill out all required fields.")
            return;
        }

        const CHECK_EXISTING_USER = gql(`
        query MyQuery {
          users(email: "${user.value.email}") { id }
        }`);

        const response = await client.query({query: CHECK_EXISTING_USER});
        if(response.data.users.length > 0) {
            toast("This email is already in use.")
            return;
        }

        save();

    };

    return (
    <div>
        <Toaster/>
        <div>
            <a className={'text-blue-500 cursor-pointer'} onClick={go_back}>
                <small>
                    <i className="fa-solid fa-arrow-left me-2"></i> Back
                </small>
            </a>
        </div>
        <div>
            <small>Carrier Name:</small>
            <div>{carrier.value.name}</div>
        </div>
        <div className={'mt-5'}>
            <div className={'text-lg'}>User Information:</div>
            <div className={'mt-3'}>
                <div>Your Name:</div>
                <div className={'flex'}>
                    <Input
                        className={'rounded-r-none'}
                        placeholder={'First Name*'}
                        value={user.value.first_name}
                        onChange={e => user.setter(prev => ({...prev, first_name: e.target.value}))}
                    />
                    <Input
                        className={'rounded-l-none'}
                        placeholder={'Last Name*'}
                        value={user.value.last_name}
                        onChange={e => user.setter(prev => ({...prev, last_name: e.target.value}))}
                    />
                </div>
                <div className={'my-1'}>
                    <div>Email:</div>
                    <Input
                        placeholder={'Email*'}
                        value={user.value.email}
                        onChange={e => user.setter(prev => ({...prev, email: e.target.value}))}
                    />
                </div>
                <div className={'my-1'}>
                    <div>Phone:</div>
                    <Input
                        placeholder={'Phone*'}
                        value={user.value.phone}
                        onChange={e => user.setter(prev => ({...prev, phone: e.target.value}))}
                    />
                </div>
            </div>
            <div className={'mt-7'}>
                <Button
                    className={'w-full'} onClick={check_requirements}
                >
                    Complete Sign Up
                </Button>
            </div>
        </div>
    </div>);
};

/*
carrier_contact(id: "") {
    name
    email
    phone
    user {
      email
      first_name
      last_name
      phone
    }
  }
 */

export default User;