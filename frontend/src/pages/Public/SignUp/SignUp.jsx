import {Card} from "@/components/ui/card.jsx";
import {Button} from "@/components/ui/button.jsx";
import {Link} from "react-router-dom";

const SignUp = () => {
    return (
    <div className={'flex justify-center h-100'}>
        <Card className={'w-lg my-auto'}>
            <div className={'grid grid-cols-2 gap-6'}>
                <div className={'text-center border-r-2'}>
                    <div className={'my-2'}>
                        <Button>
                            <Link to={'/sign_up/carrier'}>
                                Carrier Sign Up
                            </Link>
                        </Button>
                    </div>
                    <div>
                        <Button>
                            Client Sign Up
                        </Button>
                    </div>

                </div>
                <div className={'text-center'}>
                    <div>
                        Already have an account?
                    </div>
                    <div>
                        <Button>
                            Sign In
                        </Button>
                    </div>
                </div>
            </div>
        </Card>
    </div>);
};

export default SignUp;