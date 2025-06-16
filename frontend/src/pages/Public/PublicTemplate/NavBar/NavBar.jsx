import {NavigationMenu, NavigationMenuContent, NavigationMenuLink, NavigationMenuList, NavigationMenuItem} from "@/components/ui/navigation-menu.jsx";
import {Link} from "react-router-dom";

const NavBar = () => {

    return (
    <NavigationMenu>
        <NavigationMenuList>
            <NavigationMenuItem>
                <NavigationMenuLink asChild>
                    <Link to={'/'}>
                        Hauls
                    </Link>
                </NavigationMenuLink>
            </NavigationMenuItem>
            <NavigationMenuItem>
                <NavigationMenuLink asChild>
                    <Link to={'/create_listing'}>
                        List Your Pickup
                    </Link>
                </NavigationMenuLink>
            </NavigationMenuItem>
            <NavigationMenuItem>
                <NavigationMenuLink>
                    Carrier Network
                </NavigationMenuLink>
            </NavigationMenuItem>
            <NavigationMenuItem>
                <NavigationMenuLink>
                    Leaderboard
                </NavigationMenuLink>
            </NavigationMenuItem>
            <NavigationMenuItem>
                <NavigationMenuLink asChild>
                    <Link to={'/sign_up'}>
                        Sign Up
                    </Link>
                </NavigationMenuLink>
            </NavigationMenuItem>
        </NavigationMenuList>
    </NavigationMenu>);
};

export default NavBar;